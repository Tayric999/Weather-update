import requests

def get_coordinates(city):
    """
    Step 1: Convert city name to latitude and longitude
    Using Open-Meteo’s free geocoding API.
    """
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(geo_url)

    if response.status_code == 200:
        data = response.json()
        if "results" in data:
            lat = data["results"][0]["latitude"]
            lon = data["results"][0]["longitude"]
            return lat, lon
        else:
            print("❌ City not found.")
            return None
    else:
        print("⚠️ Error fetching location data.")
        return None


def get_weather(city):
    """
    Step 2: Use the coordinates to get live weather data
    from Open-Meteo’s forecast API.
    """
    coords = get_coordinates(city)
    if not coords:
        return

    lat, lon = coords
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["current_weather"]
        print(f"\n🌦️ Current Weather in {city.title()}")
        print("-" * 30)
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Windspeed:  {weather['windspeed']} km/h")
        print(f"Time:       {weather['time']}")
    else:
        print("⚠️ Error fetching weather data.")


# 🧠 Step 3: Run the mini app
city_name = input("Enter city name: ")
get_weather(city_name)
