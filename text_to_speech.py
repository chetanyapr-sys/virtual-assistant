import pyttsx3
import threading

def text_to_speech(text):
    def speak():
        try:
            engine = pyttsx3.init('sapi5')  # Windows ke liye
            rate = engine.getProperty("rate")
            engine.setProperty("rate", rate - 50)
            engine.say(text)
            engine.runAndWait()
            engine.stop()
            del engine
        except Exception as e:
            print("TTS Error:", e)
    
    thread = threading.Thread(target=speak)
    thread.daemon = True
    thread.start()
    thread.join()