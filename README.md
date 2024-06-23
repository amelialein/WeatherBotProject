# WeatherBot with Flask and OpenWeather API

WeatherBot is a Python ChatterBot that can tell you today and tomorrow's weather forecast in each location of Jo's travel itinerary.

## Installation

Please ensure the item in requirements.txt are installed correctly.

in terminal:
pip install -r requirements.txt

## Usage

Run from terminal:
python app.py

WeatherBot will return forecast when asked a question in the form of: "What is the maximum temp in Cambridge tomorrow?"
The locations available are listed in weather.py.
My WeatherBot can answer for Today and Tomorrow only as I ran out of time.

## Motivation
Python, Flask and ChatterBot project for my university course. Scenario was to create a weatherbot to be deployed on a travel to give information on the weather forecast in each of the locations on the itinerary.

## Limitations
Unfortunately, I only managed to get a perfectly working weather.py file. The chatbotsafe.py file works sometimes, I believe on the first time of installing, but once app.py has run, a threading issue breaks the app and chatbot is no longer able to train properly. Possibly something to do with the SQLite3 files that get created. I'm not a hundred percent on this, so any suggestions would be greatly appreciated!