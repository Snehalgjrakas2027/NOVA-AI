import asyncio
from random import randint
from PIL import Image
import requests
from dotenv import load_dotenv
import os
from time import sleep

# Load environment variables from .env file
load_dotenv()

# Define constants
IMAGE_GEN_PATH = "/Users/snehalgjrakas/Downloads/Jarvis AI/Frontend/Files/ImageGeneration.data"
IMAGE_SAVE_FOLDER = "/Users/snehalgjrakas/Downloads/Jarvis AI/Data"

# API details
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
api_key = os.getenv("HuggingFaceAPIKey")
headers = {"Authorization": f"Bearer {api_key}"}

def open_images(prompt):
    """Opens generated image files based on prompt name"""
    prompt = prompt.replace(" ", "_")
    files = [f"{prompt}{i}.jpg" for i in range(1, 5)]

    for jpg_file in files:
        image_path = os.path.join(IMAGE_SAVE_FOLDER, jpg_file)
        try:
            img = Image.open(image_path)
            print(f"Opening image: {image_path}")
            img.show()
            sleep(1)
        except IOError:
            print(f"Unable to open {image_path}")

async def query(payload):
    """Sends a request to Hugging Face API asynchronously"""
    try:
        response = await asyncio.to_thread(requests.post, API_URL, headers=headers, json=payload)
        if response.status_code != 200:
            print(f"API error {response.status_code}: {response.text}")
        return response.content
    except Exception as e:
        print(f"Request failed: {e}")
        return b""

async def generate_images(prompt: str):
    """Generates images by sending multiple prompts to the API"""
    tasks = []
    for _ in range(4):
        payload = {
            "inputs": f"{prompt}, quality=4K, sharpness=maximum, Ultra High details, high resolution, seed={randint(0, 1000000)}",
        }
        task = asyncio.create_task(query(payload))
        tasks.append(task)

    image_bytes_list = await asyncio.gather(*tasks)

    for i, image_bytes in enumerate(image_bytes_list):
        filename = os.path.join(IMAGE_SAVE_FOLDER, f"{prompt.replace(' ', '_')}{i + 1}.jpg")
        try:
            with open(filename, "wb") as f:
                f.write(image_bytes)
            print(f"Saved image: {filename}")
        except Exception as e:
            print(f"Failed to save image {filename}: {e}")

def GenerateImages(prompt: str):
    """Wrapper to generate images and open them after generation"""
    asyncio.run(generate_images(prompt))
    open_images(prompt)

# Main loop to check for prompt input and trigger generation
while True:
    try:
        with open(IMAGE_GEN_PATH, "r") as f:
            data = f.read().strip()

        if not data:
            sleep(1)
            continue

        parts = data.split(",")
        if len(parts) >= 2:
            prompt = parts[0].strip()
            status = parts[1].strip().lower()
        else:
            sleep(1)
            continue

        if status == "true":
            print(f"Generating Images for prompt: '{prompt}'")
            GenerateImages(prompt=prompt)

            # Reset the status to False
            with open(IMAGE_GEN_PATH, "w") as f:
                f.write("False,False")

            break  # Exit after processing
        else:
            sleep(1)

    except Exception as e:
        print(f"Error in main loop: {e}")
        sleep(1)
