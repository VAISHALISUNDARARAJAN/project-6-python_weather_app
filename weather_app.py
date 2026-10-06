import json
import os
import hashlib
import requests


USERS_FILE = "users.json"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_users():
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


users = load_users()


def register_user():
    print("\n===== REGISTER =====")

    username = input("Enter username: ").strip()

    if username == "":
        print("Username cannot be empty.")
        return

    for user in users:
        if user["username"].lower() == username.lower():
            print("Username already exists.")
            return

    password = input("Enter password: ").strip()

    if password == "":
        print("Password cannot be empty.")
        return

    user = {
        "username": username,
        "password": hash_password(password),
        "role": "user"
    }

    users.append(user)
    save_users()

    print("Registration successful!")


def login_user():
    print("\n===== LOGIN =====")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    password_hash = hash_password(password)

    for user in users:
        if (user["username"].lower() == username.lower()
                and user["password"] == password_hash):

            print(f"Login successful! Welcome, {user['username']}.")
            return user

    print("Invalid username or password.")
    return None


def show_profile(user):
    print("\n===== PROFILE =====")
    print(f"Username: {user['username']}")
    print(f"Role: {user['role']}")


def get_weather():
    api_key = os.environ.get("OPENWEATHER_API_KEY")

    if not api_key:
        print("\nAPI key not found.")
        print("Please set the OPENWEATHER_API_KEY environment variable.")
        return

    city = input("Enter city name: ").strip()

    if city == "":
        print("City name cannot be empty.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404:
            print("Invalid city name. Please try again.")
            return

        if response.status_code == 401:
            print("Invalid or inactive API key.")
            return

        response.raise_for_status()

        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        print("\n===== WEATHER INFORMATION =====")
        print(f"City: {data['name']}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Condition: {condition.title()}")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Network error. Please check your internet connection.")

    except requests.exceptions.RequestException:
        print("Unable to retrieve weather information.")

    except (KeyError, ValueError):
        print("Unexpected response received from the weather API.")


def admin_menu(user):
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. Get Weather")
        print("2. View Profile")
        print("3. View Registered Users")
        print("4. Logout")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            get_weather()

        elif choice == "2":
            show_profile(user)

        elif choice == "3":
            print("\n===== REGISTERED USERS =====")

            if not users:
                print("No users registered.")
            else:
                for registered_user in users:
                    print(
                        f"Username: {registered_user['username']} | "
                        f"Role: {registered_user['role']}"
                    )

        elif choice == "4":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


def user_menu(user):
    while True:
        print("\n===== USER MENU =====")
        print("1. Get Weather")
        print("2. View Profile")
        print("3. Logout")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            get_weather()

        elif choice == "2":
            show_profile(user)

        elif choice == "3":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please enter 1-3.")


def main():
    print("===== WEATHER APP USING API =====")

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            register_user()

        elif choice == "2":
            user = login_user()

            if user:
                if user["role"] == "admin":
                    admin_menu(user)
                else:
                    user_menu(user)

        elif choice == "3":
            print("Thank you for using the Weather App!")
            break

        else:
            print("Invalid choice. Please enter 1-3.")


main()
