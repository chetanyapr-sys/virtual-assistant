import text_to_speech
import datetime
import webbrowser
import weather
import google.generativeai as genai
 
genai.configure(api_key="AIzaSyDFKuUBylWg9v_aBWLzpKEdyI-KxbwjhLg")
model = genai.GenerativeModel("gemini-2.0-flash")
 
 
def Action(data):
 
    user_data = data.lower().strip()
 
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("my name is virtual assistant")
        return "my name is virtual assistant"
 
    elif "hello" in user_data:
        text_to_speech.text_to_speech("hello sir how can i help you")
        return "hello sir how can i help you"
 
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return "good morning sir"
 
    elif "date and time" in user_data or "time and date" in user_data:
        now = datetime.datetime.now()
        date = now.strftime("%d %B %Y")
        day = now.strftime("%A")
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        am_pm = now.strftime("%p")
        result = f"Today is {day}, {date} and current time is {hour} hour {minute} minute {am_pm}"
        text_to_speech.text_to_speech(result)
        return result
 
    elif "time" in user_data:
        now = datetime.datetime.now()
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        am_pm = now.strftime("%p")
        current_time = f"Current time is {hour} hour {minute} minute {am_pm}"
        text_to_speech.text_to_speech(current_time)
        return current_time
 
    elif "date" in user_data:
        now = datetime.datetime.now()
        date = now.strftime("%d %B %Y")
        day = now.strftime("%A")
        result = f"Today is {day}, {date}"
        text_to_speech.text_to_speech(result)
        return result
 
    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com")
        text_to_speech.text_to_speech("opening youtube")
        return "opening youtube"
 
    elif "google" in user_data:
        webbrowser.open("https://google.com")
        text_to_speech.text_to_speech("opening google")
        return "opening google"
 
    elif "play music" in user_data:
        webbrowser.open("https://gaana.com")
        text_to_speech.text_to_speech("playing music")
        return "playing music"
 
    elif "weather" in user_data:
        # BUG FIX 3: Weather city detection improved
        # "weather in new york" → "new york"
        # "what is weather in delhi" → "delhi"
        # "weather" akela → "delhi" default
        city = "delhi"  # default
        if " in " in user_data:
            # "in" ke baad wala part lo, aur "weather" se pehle ka ignore karo
            parts = user_data.split(" in ")
            # last part lo jo city hogi
            city = parts[-1].strip()
            # Extra words hatao agar koi ho
            city = city.split("?")[0].strip()
            city = city.split(".")[0].strip()
        ans = weather.weather(city)
        text_to_speech.text_to_speech(ans)
        return ans
 
    elif "take a screenshot" in user_data or "screenshot" in user_data:
        import pyautogui
        import time
        time.sleep(1)  # BUG FIX 4: Window minimize ho jaye pehle
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        text_to_speech.text_to_speech("screenshot saved in project folder")
        return "screenshot saved"
 
    elif "battery" in user_data:
        import psutil
        battery = psutil.sensors_battery()
        if battery is None:
            text_to_speech.text_to_speech("battery information not available")
            return "battery information not available"
        percent = battery.percent
        plugged = battery.power_plugged
        status = "charging" if plugged else "not charging"
        result = f"Battery is at {int(percent)} percent and is {status}"
        text_to_speech.text_to_speech(result)
        return result
 
    elif "shutdown" in user_data:
        # BUG FIX 5: Pehle bolta hai, phir band hota hai
        text_to_speech.text_to_speech("ok sir, shutting down. Goodbye!")
        return "ok sir"
 
    else:
        try:
            response = model.generate_content(user_data)
            bot_reply = response.text.strip()
            text_to_speech.text_to_speech(bot_reply)
            return bot_reply
        except Exception as e:
            text_to_speech.text_to_speech("something went wrong")
            return f"Error: {e}"