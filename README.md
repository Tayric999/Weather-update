Weather Update App is a simple yet powerful Python program that lets you fetch live weather data for any city in the world 🌍.
It uses the Open-Meteo API, which is free and doesn’t require an API key.
The app converts a city name (like Nairobi or Kampala) into geographic coordinates, then fetches and displays current weather details such as temperature, wind speed, and time of observation.

⚙️ Features
✅ Fetches real-time weather data from Open-Meteo
✅ Works for any city worldwide
✅ Requires no API key or signup
✅ Handles errors gracefully (invalid city, connection issues)
✅ Uses requests library for HTTP calls
✅ Beginner-friendly and well-commented code

🧠 How It Works
You enter a city name (e.g., Nairobi).
The app calls Open-Meteo’s geocoding API to get its latitude & longitude.
Using those coordinates, it calls the forecast API to get live weather data.

The script displays:
🌡️ Temperature (°C)
🌬️ Windspeed (km/h)
🕓 Time of measurement

💻 Example Run
$ python weather_update.py
Enter city name: Nairobi

🌦️ Current Weather in Nairobi
------------------------------
Temperature: 25.4°C
Windspeed:  10.3 km/h
Time:       2025-10-26T11:00

📁 Folder Structure
project/
│
├── weather_update.py
└── README.md

🧰 Requirements

Python 3.x
requests library
Install the dependency:
pip install requests

🧩 Code Overview

Key parts of the code:
get_coordinates(city) → fetches latitude and longitude
get_weather(city) → fetches live weather for that city
Uses requests.get() to send HTTP requests
Checks for response.status_code == 200 to ensure successful API calls
Gracefully handles invalid input or connection failures

🛡️ Error Handling
The app includes checks for:
Network connection errors
Non-existent cities (no results)
Invalid responses from the API
When an issue occurs, the program prints a clear message instead of crashing.

🧾 Example APIs Used
🌍 Geocoding API:
https://geocoding-api.open-meteo.com/v1/search?name={city}
🌦️ Forecast API:
https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true
Both are free and require no key.

🚀 Future Enhancements
 Add weather icons (☀️🌧️🌩️) based on weather code
 Add humidity, pressure, and visibility details
 Display data in a GUI or web interface
 Log requests in a history file
