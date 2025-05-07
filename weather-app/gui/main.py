import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data
def get_weather():
    city = city_entry.get()
    api_key = "06a6092bb1b9115e855e687a38802b22"  # Replace with your API key

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description'].capitalize()

            result_label.config(
                text=f"Weather in {city}:\n"
                     f"Temperature: {temp}°C\n"
                     f"Humidity: {humidity}%\n"
                     f"Description: {description}"
            )
        else:
            result_label.config(text=f"Error: {data['message']}")
    except Exception as e:
        result_label.config(text=f"Request failed: {e}")

# Create GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

root.mainloop()
