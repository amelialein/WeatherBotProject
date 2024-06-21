# Imports
from pprint import pprint
import requests
import os
from dotenv import load_dotenv

# Save API key to a variable
load_dotenv()
API_key = os.getenv('OpenWeather_API_key')

# Create a dictionary of the locations and their coordinates
locations = {
    'Cumbria': [54.4609, -3.0886],
    'Corfe Castle': [50.6395, -2.0566],
    'The Cotswolds': [51.8330, -1.8433],
    'Cambridge': [52.2053, 0.1218],
    'Bristol': [51.4545, -2.5879],
    'Oxford': [51.7520, -1.2577],
    'Norwich': [52.6309, 1.2974],
    'Stonehenge': [51.1789, -1.8262],
    'Watergate Bay': [50.4429, -5.0553],
    'Birmingham': [52.4862, -1.8904]
}


# Retrieve weather data from Open Weather API
# Define get_weather function
def get_weather(lat, lon, api_key=API_key):
    # Fetching a response
    resp = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
                        f"&units=metric")
    # Display error message
    if resp.status_code != 200:
        print(f"Error {resp.status_code}: Unable to fetch weather data.")
    else:
        # Converting to JSON
        data = resp.json()
        return data


# Formatting the weather data
# Establishing list of dictionaries
forecast = []

# Creating a dictionary for each place
for place in locations:
    data = get_weather(locations[place][0], locations[place][1])
    cities = list(locations.keys())
    days = [2, 10, 18, 26, 34]
    i = 1
    week = {}
    week["Place"] = place

    # Creating key value pairs for each day
    for day in days:
        max_temp = data['list'][day]['main']['temp_max']
        dt = data['list'][day]['dt_txt']
        week[dt] = max_temp
        i += 1

    # Add each place to the list of dictionaries
    forecast.append(week)


# Creating the training data for my chatbot
# Establish weather_talk array
weather_talk = []

# Create other frequently referenced variables
dates = list(forecast[0].keys())
places = list(locations.keys())


# Define Max Temp Today function
def get_today_max(place):
    conv = [f"What is the maximum temperature for {place} today?"]
    today = dates[1]
    index = places.index(place)
    text = f"In {place}, today's maximum is {forecast[index][today]} degrees Celsius."
    conv.append(text)
    weather_talk.append(conv)


# Populate weather_talk with get_today_max Q and As
for place in places:
    get_today_max(place)


# Define get tomorrow max
def get_tomorrow_max(place):
    conv = [f"What is the maximum temperature for {place} tomorrow?"]
    tomorrow = dates[2]
    index = places.index(place)
    text = f"In {place}, tomorrow's maximum is {forecast[index][tomorrow]} degrees Celsius."
    conv.append(text)
    weather_talk.append(conv)


# Populate weather_talk with get_tomorrow_max Q and As
for place in places:
    get_tomorrow_max(place)

pprint(weather_talk)
