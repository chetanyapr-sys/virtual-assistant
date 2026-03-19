# 🤖 Virtual Assistant

A Python-based AI-powered desktop virtual assistant with voice recognition, text input, and smart responses using Google Gemini AI.

---

## ✨ Features

- 🎤 **Voice Input** — Speak to the assistant using your microphone
- ⌨️ **Text Input** — Type your query directly
- 🌤️ **Weather Updates** — Get real-time weather for any city
- 🌐 **Open Websites** — YouTube, Google, Gaana with voice/text commands
- 🕐 **Date & Time** — Ask current time and date
- 📸 **Screenshot** — Take screenshots with a voice command
- 🔋 **Battery Status** — Check battery percentage and charging status
- 🤖 **Gemini AI** — Powered by Google Gemini for general questions
- 🔊 **Text to Speech** — Assistant speaks back to you

---

## 🛠️ Tech Stack

- **Python** — Core language
- **Tkinter** — GUI (Graphical User Interface)
- **SpeechRecognition** — Voice input
- **pyttsx3** — Text to speech
- **Google Gemini AI** — AI responses
- **OpenWeatherMap API** — Weather data
- **Pillow** — Image handling

---

## 📁 Project Structure

```
virtual-assistant/
│
├── GUI.py              # Main GUI file
├── action.py           # Core logic & commands
├── speech_to_text.py   # Voice recognition
├── text_to_speech.py   # Text to speech
├── weather.py          # Weather API
├── ai2.png             # Assistant image
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/chetanyapr-sys/virtual-assistant.git
cd virtual-assistant
```

### 2. Install dependencies
```bash
pip install tkinter pillow speechrecognition pyttsx3 google-generativeai requests pyautogui psutil
```

### 3. Add API Keys
In `action.py`:
```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

In `weather.py`:
```python
api_key = "YOUR_OPENWEATHER_API_KEY"
```

### 4. Run the project
```bash
python GUI.py
```

---

## 🗣️ Commands You Can Use

| Command | Action |
|--------|--------|
| `hello` | Greet the assistant |
| `what is your name` | Assistant introduces itself |
| `time` | Get current time |
| `date` | Get current date |
| `weather in Delhi` | Get weather of any city |
| `open youtube` | Opens YouTube |
| `open google` | Opens Google |
| `play music` | Opens Gaana |
| `take a screenshot` | Takes a screenshot |
| `battery` | Check battery status |
| `shutdown` | Close the assistant |
| Any other query | Answered by Gemini AI |

---

## 🔑 API Keys Required

- **Gemini AI** — [aistudio.google.com](https://aistudio.google.com)
- **OpenWeatherMap** — [openweathermap.org](https://openweathermap.org/api)

---

## 👨‍💻 Developer

**Chetanya Prakash**  
B.Tech CSE — Shri Rammurti Smarak College of Engineering, Bareilly  
[![GitHub](https://img.shields.io/badge/GitHub-chetanyapr--sys-black?logo=github)](https://github.com/chetanyapr-sys)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
