import tkinter as tk
import requests
import threading

def get_weather_threaded():
    threading.Thread(target=get_weather).start()


def get_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    url = f"https://api.weatherapi.com/v1/current.json?key=b17a4020b41e41eba8472905250108&q={city}"

    try:
        response = requests.get(url)
        data = response.json()

        if "current" in data:
            temp = data["current"]["temp_c"]
            wind = data["current"]["wind_kph"]
            humidity = data["current"]["humidity"]
            cloud = data["current"]["cloud"]
            feels = data["current"]["feelslike_c"]
            desc = data["current"]["condition"]["text"]
            result_label.config(
                text=f"{city.title()}\nTemperature: {temp}°C\nCondition: {desc}\nWind speed: {wind}kph\nHumidity: {humidity}\nCloud: {cloud}\nFeels like: {feels}")
        else:
            result_label.config(text="City not found 😕")
    except Exception as e:
        result_label.config(text="Error fetching data.")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")
root.config(bg="#4b79b4")

tk.Label(root, text="Enter City Name:", bg="#4b79b4", font=("Helvetica", 12)).pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=5)
city_entry.bind("<Return>", lambda event: get_weather())

tk.Button(root, text="Get Weather", command=get_weather_threaded, font=("Helvetica", 12), bg="#60a5fa", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", bg="#c1c9d3", font=("Helvetica", 12))
result_label.pack(pady=20)

root.mainloop()
