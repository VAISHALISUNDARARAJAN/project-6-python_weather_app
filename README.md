# Python Weather App Using API

A simple Python weather application that retrieves current weather information for a city using a weather API.

## Features

- User registration and login
- Password hashing
- User profiles
- Role-based access
- Admin and user menus
- Accepts a city name from the user
- Retrieves weather information using an API
- Displays temperature
- Displays humidity
- Displays weather conditions
- Uses Python Requests and JSON data
- Handles invalid city names
- Handles invalid API keys
- Handles network errors
- Handles request timeouts
- Keeps the API key outside the source code

## Technologies Used

- Python
- Requests
- JSON
- OpenWeather API
- SHA-256 password hashing

## Weather Information

The application displays:

- City name
- Temperature in Celsius
- Humidity percentage
- Weather condition

## Authentication

The application provides:

- User registration
- User login
- User profiles
- Role-based access

### Regular Users

Regular users can:

- Get weather information
- View their profile
- Logout

### Administrators

Administrators can:

- Get weather information
- View their profile
- View registered users
- Logout

## API Key Setup

The API key is not stored in the Python source code.

Set the API key as a Windows environment variable:

```text
setx OPENWEATHER_API_KEY "YOUR_API_KEY_HERE"

Error Handling
The application handles:
Empty city names
Invalid city names
Invalid or inactive API keys
Network connection errors
Request timeouts
Invalid login details
Duplicate usernames
Empty usernames and passwords
Unexpected API responses
Project Structure
python-weather-app/
│
├── weather_app.py
├── users.json
├── README.md
├── .gitignore
└── screenshots/
    ├── login.png
    ├── weather-result.png
    └── invalid-city.png
Demo Screenshots
The screenshots folder contains examples of:
User registration and login
User profile and role
Weather information
Invalid city handling
