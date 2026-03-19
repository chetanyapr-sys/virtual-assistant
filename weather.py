import requests
import urllib3

urllib3.disable_warnings()

def weather(city):

    api_key = "9c640a3b141145d0b4601bec930dd8c1"

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params, verify=False)

    data = response.json()

    try:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        city_name = data["name"]

        return f"Temperature in {city_name} is {temperature}°C with {description}"

    except:
        return "City not found"
