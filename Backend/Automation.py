# macOS-Compatible Automation.py

import subprocess
import webbrowser
import os
import asyncio
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq

# Load environment variables from the .env file
env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")

useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

client = Groq(api_key=GroqAPIKey)

messages = []
SystemChatBot = [{
    "role": "system",
    "content": f"Hello, I am {os.environ.get('USER', 'NovaAI')}, You're a content writer. You have to write content like letters, codes, applications, essays, notes, songs, poems etc."
}]

website_mapping = {
    "facebook": "https://www.facebook.com",
    "twitter": "https://twitter.com",
    "x": "https://twitter.com",
    "instagram": "https://www.instagram.com",
    "linkedin": "https://www.linkedin.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "spotify": "https://open.spotify.com",
    "netflix": "https://www.netflix.com",
    "amazon": "https://www.amazon.com",
    "flipkart": "https://www.flipkart.com",
    "github": "https://github.com",
    "stackoverflow": "https://stackoverflow.com"
}

def GoogleSearch(topic):
    search(topic)
    return True

def Content(topic):
    def OpenTextEditor(file_path):
        subprocess.Popen(["open", file_path])  # macOS default opener

    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": prompt})
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=SystemChatBot + messages,
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )
        answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                answer += chunk.choices[0].delta.content
        messages.append({"role": "assistant", "content": answer})
        return answer

    topic = topic.replace("Content", "").strip()
    content_by_ai = ContentWriterAI(topic)
    file_name = f"{topic.lower().replace(' ', '')}.txt"
    file_path = os.path.join("Data", file_name)
    os.makedirs("Data", exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content_by_ai)
    OpenTextEditor(file_path)
    return True

def YouTubeSearch(topic):
    webbrowser.open(f"https://www.youtube.com/results?search_query={topic}")
    return True

def PlayYoutube(query):
    playonyt(query)
    return True

def OpenApp(app):
    app = app.strip().lower()
    if app in website_mapping:
        webbrowser.open(website_mapping[app])
        return True
    elif "." in app:
        webbrowser.open(f"https://{app}")
        return True
    else:
        try:
            subprocess.Popen(["open", "-a", app])
            return True
        except Exception as e:
            print(f"[bold red]Could not open app:[/bold red] {e}")
            webbrowser.open(f"https://www.google.com/search?q={app}")
            return False

def CloseApp(app):
    print("[bold yellow]CloseApp not implemented for macOS.[/bold yellow]")
    return False

def System(command):
    def run_osascript(script):
        subprocess.call(["osascript", "-e", script])
    
    if command == "mute":
        run_osascript("set volume output muted true")
    elif command == "unmute":
        run_osascript("set volume output muted false")
    elif command == "volume up":
        run_osascript("set volume output volume ((output volume of (get volume settings)) + 10)")
    elif command == "volume down":
        run_osascript("set volume output volume ((output volume of (get volume settings)) - 10)")
    return True

async def TranslateAndExecute(commands: list[str]):
    funcs = []
    for command in commands:
        if command.startswith("open "):
            funcs.append(asyncio.to_thread(OpenApp, command.removeprefix("open ").strip()))
        elif command.startswith("close "):
            funcs.append(asyncio.to_thread(CloseApp, command.removeprefix("close ").strip()))
        elif command.startswith("play "):
            funcs.append(asyncio.to_thread(PlayYoutube, command.removeprefix("play ").strip()))
        elif command.startswith("content "):
            funcs.append(asyncio.to_thread(Content, command.removeprefix("content ").strip()))
        elif command.startswith("google search "):
            funcs.append(asyncio.to_thread(GoogleSearch, command.removeprefix("google search ").strip()))
        elif command.startswith("youtube search "):
            funcs.append(asyncio.to_thread(YouTubeSearch, command.removeprefix("youtube search ").strip()))
        elif command.startswith("system "):
            funcs.append(asyncio.to_thread(System, command.removeprefix("system ").strip()))
        else:
            print(f"[bold red]No Function Found for: {command}[/bold red]")

    results = await asyncio.gather(*funcs)
    for result in results:
        yield result

async def Automation(commands: list[str]):
    async for _ in TranslateAndExecute(commands):
        pass
    return True