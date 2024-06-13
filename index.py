from flask import Flask, render_template, request
import requests

app = Flask(__name__)
def get_weather_data(city_name):
    api_key = "58b77f6721deeb116ded623ceb4b7351"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None

def display_weather_data(weather_data):
    if weather_data:
        print("Current Weather:")
        print(f"Temperature: {weather_data['main']['temp']} °C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Description: {weather_data['weather'][0]['description']}")
    else:
        print("No weather data available for the given city.")

def main():
    city_name = input("Enter the name of the city: ").strip()
    if not city_name:
        print("City name cannot be empty.")
        return
    
    weather_data = get_weather_data(city_name)
    display_weather_data(weather_data)

    

if __name__ == "__main__":
    main()
   