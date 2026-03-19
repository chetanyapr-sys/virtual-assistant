import speech_recognition as sr

def speech_to_text():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            return ""

    try:
        voice_data = r.recognize_google(audio)
        print("You said:", voice_data)
        return voice_data.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return ""
