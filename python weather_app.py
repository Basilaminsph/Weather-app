import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        main_data = weather_data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Unable to fetch weather data. Please check your city name and API key.")

if __name__ == "default":
    api_key = "5f5a64d4ab6f1dd7b89c8d59491d08ae"  # Replace with your OpenWeatherMap API key
    city_name = input("Enter the name of your city: ")

    weather_data = get_weather(api_key, city_name)

    display_weather(weather_data)
