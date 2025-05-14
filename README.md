# NOVA - Virtual Desktop Assistant

NOVA is a highly capable virtual assistant built to run on macOS, leveraging **subprocess** and various integrated tools for system control, automation, speech-to-text, text-to-speech, image generation, and real-time search. This assistant provides a seamless interaction with your desktop environment through voice commands and natural language processing.

---
##Note: This is for now only comaptible for the macOS operating system, the working automation contribution of windows are welcomed by contributors.

## 🚀 Getting Started

### 1. **System Requirements**

* **macOS** (version 10.15 or higher)
* **Python 3.7+**
* Required Python libraries:

  * `pygame`
  * `random`
  * `asyncio`
  * `edge_tts`
  * `pywhatkit`
  * `python-dotenv`
  * `beautifulsoup4`
  * `rich`
  * `groq`
  * `subprocess`
  * `json`
  * `threading`

To install these dependencies, you can use the following command:

```bash
pip install pygame edge_tts pywhatkit python-dotenv beautifulsoup4 rich groq
```

### 2. **Setting up the `.env` File**

To configure your assistant, you'll need to create an `.env` file in the root of the project directory. This file will contain your API keys and other configuration values.

#### 2.1. **Create the `.env` File**

In the root directory of your NOVA project, create a file named `.env`.

#### 2.2. **Add the Required API Keys and Configuration**

Open the `.env` file and add the following lines:

```
Username=YourNameHere
Assistantname=NOVA
AssistantVoice=Microsoft David Desktop
GroqAPIKey=YourGroqAPIKeyHere
```

* **Username**: Your username (or name) to be used for interactions with NOVA.
* **Assistantname**: The name of your assistant (e.g., NOVA).
* **AssistantVoice**: Choose your preferred TTS (Text-To-Speech) voice (e.g., "Microsoft David Desktop").
* **GroqAPIKey**: Obtain your API key for Groq’s NLP model (replace with your actual API key).

> **Note**: For the **GroqAPIKey**, you’ll need to sign up for an account with Groq and retrieve the API key from their platform.

---

## 🖥️ Running NOVA on macOS

### 3. **Running the Application**

To start NOVA, follow these steps:

1. Open the terminal on your macOS system.
2. Navigate to your project directory using the `cd` command.
3. Run the following command to start the assistant:

```bash
python main.py
```

This will launch the assistant and start listening for commands.

### 4. **macOS Compatibility (Subprocess Integration)**

NOVA utilizes the `subprocess` module to interact with macOS applications and system commands. This allows NOVA to:

* Open and close applications.
* Adjust system settings like volume and mute.
* Trigger file-related tasks.

For example, NOVA can execute commands like:

* `open "Google Chrome"` - Opens Google Chrome.
* `system mute` - Mutes the system volume.

These tasks are macOS-compatible, and `subprocess` ensures seamless interaction between the assistant and macOS system commands.

> **Important**: Ensure you allow necessary permissions for NOVA to execute system-level commands on your macOS device. This might include giving terminal access to "Full Disk Access" or "Accessibility" in the system preferences.

---

## 🗣️ Speech Recognition & Text-to-Speech

### 5. **Speech-to-Text (STT) and Text-to-Speech (TTS)**

NOVA supports **speech-to-text** to capture voice commands and **text-to-speech** to respond audibly.

* **Speech Recognition**: The assistant listens for commands using the system’s microphone and processes them into actions.
* **Text-to-Speech**: NOVA will speak back to you, using the voice configured in the `.env` file.

---

## ⚙️ Task Automation

NOVA can automate a variety of system tasks using voice commands, such as:

* Opening and closing applications (e.g., `open Google Chrome`, `close Finder`).
* Adjusting system volume (`volume up`, `volume down`, `mute`).
* Running automation scripts (e.g., launching a Python script or opening a browser).

This functionality is designed to be extended and customized for various use cases.

---

## 🖼️ Image Generation

NOVA can generate images based on descriptive commands. This uses external services (such as DALL-E or any other image generation API) to create images based on natural language prompts.

For example, say:

* “Generate a futuristic cityscape.”
* “Create an image of a flying dragon.”

The generated images are saved and can be displayed in the GUI interface.

---

## 📚 FAQs

### 1. **How do I customize NOVA's responses?**

You can modify the responses and behavior by editing the **Backend** modules and adjusting the assistant's voice, personality, and actions in the `.env` file.

### 2. **How can I add more APIs to NOVA?**

To add more APIs, simply:

1. Install the necessary Python package.
2. Add the corresponding API key or credentials to the `.env` file.
3. Modify the relevant module in the `Backend` directory to incorporate the new API's functionality.

### 3. **Does NOVA support other operating systems?**

Currently, NOVA is optimized for macOS and uses macOS-specific features such as subprocess integration. To run NOVA on other operating systems like Windows or Linux, additional modifications are required, especially for system commands.

---

## 💡 Troubleshooting

1. **Issue with API key**: Ensure that the key is correctly copied into the `.env` file. Check the official documentation of the respective API provider for troubleshooting.
2. **Permission Issues**: On macOS, you might need to provide terminal or application permissions for NOVA to execute system commands. Go to **System Preferences > Security & Privacy** and enable required permissions.
3. **Missing Dependencies**: If a required module is not installed, run `pip install <module-name>` to install missing dependencies.

---

## 🤖 Conclusion

NOVA is an AI-powered assistant designed to provide you with a hands-free experience for managing tasks, retrieving information, and interacting with your system. With its integration of various APIs and system commands, NOVA is fully customizable and ready to automate your desktop experience.

Enjoy exploring NOVA and make your everyday tasks simpler and more efficient!

---

## Contributors

### 1.Mrunali Kodhe
### 2.Snehal Rakas
### 3.Musharrif Shaikh


**Contact Information:**
For any issues or feedback, please feel free to reach out to snehalgjrakas118@gmail.com raise an issue in the GitHub repository.

---

