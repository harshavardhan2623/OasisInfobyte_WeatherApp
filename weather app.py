import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.location_label = tk.Label(root, text="Enter Location:")
        self.location_entry = tk.Entry(root)
        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        
        self.location_label.grid(row=0, column=0, padx=10, pady=10)
        self.location_entry.grid(row=0, column=1, padx=10, pady=10)
        self.get_weather_button.grid(row=1, column=0, columnspan=2, pady=10)

    def get_weather(self):
        location = self.location_entry.get()
        if not location:
            messagebox.showerror("Error", "Please enter a location.")
            return

        try:
            api_key = "109ebd4b44c407edcdf64afc1e00dbf2"
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            params = {"q": location, "appid": api_key, "units": "metric"}

            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                messagebox.showinfo("Weather", f"Temperature: {temperature}°C\nDescription: {description}")
            else:
                error_message = f"Failed to get weather data. Status Code: {response.status_code}\n{data.get('message', '')}"
                messagebox.showerror("Error", error_message)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
