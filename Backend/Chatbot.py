from groq import Groq  # Importing the Groq library to use its API.
from json import load, dump  # Importing functions to read and write JSON files.
import datetime  # Importing the datetime module for real-time date and time information.
from dotenv import dotenv_values  # Importing dotenv_values to read environment variables from a .env file.

# Load environment variables from the .env file.
env_vars = dotenv_values(".env")

# Retrieve specific environment variables for username, assistant name, and API key.
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")  

# Initialize the Groq client using the provided API key.
client = Groq(api_key=GroqAPIKey)

messages=[]

# System prompt for chatbot behavior.
System = f"""Hello, I am {Username}. You are a very accurate and advanced AI chatbot named {Assistantname} which also has real-time up-to-date information from the internet.
*** Do not tell time until I ask, do not talk too much, just answer the question. ***
*** Reply in only English, even if the question is in Hindi, reply in English. ***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""

SystemChatBot = [{"role": "system", "content": System}]

# Load chat history or create a new one.

try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
except FileNotFoundError:
    with open(r"Data\ChatLog.json", "w") as f:
        dump([], f)

# Function to get real-time date and time information.
def RealtimeInformation():
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date=current_date_time.strftime("%d")
    month=current_date_time.strftime("%B")
    year=current_date_time.strftime("%Y")
    hour=current_date_time.strftime("%H")
    minute=current_date_time.strftime("%M")
    second=current_date_time.strftime("%S")

    data = f"Please use this real-time information if needed, \n" 
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n" 
    data += f"Time: {hour} hours: {minute} minutes: {second} seconds.\n" 
    return data

# Function to format chatbot responses.
def AnswerModifier(Answer):
    lines=Answer.split('\n') # Split the response into lines. 
    non_empty_lines = [line for line in lines if line.strip()] 
    modified_answer='\n'.join(non_empty_lines)
    return modified_answer
# Main chatbot function to handle user queries.
def ChatBot(Query):
    """This function sends the user's query to the chatbot and returns the AI's response.""" 
    try:
        # Append user's query to messages.
        with open(r"Data\ChatLog.json","r") as f:
            messages = load(f)

        messages.append({"role": "user", "content": f"{Query}"})

        # Make a request to the Groq API for a response.
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,
            max_tokens=1024,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None    # Disable streaming for simpler handling.
        )

        Answer=""

        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content


        # Clean response
        Answer = Answer.replace("</s>", "")

        # Append assistant's response to messages.
        messages.append({"role": "assistant", "content": Answer})

        # Save the updated chat log.
        with open(r"Data\ChatLog.json", "w") as f:
            dump(messages, f, indent=4)

        return AnswerModifier(Answer=Answer)

    except Exception as e:
        print(f"Error: {e}")
        with open(r"Data\ChatLog.json", "w") as f:
            dump([], f, indent=4) 
        return ChatBot(Query) 
        

# Main program loop for testing.
if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question: ")
        print(ChatBot(user_input))