import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz
import geocoder


def get_local_timezone():
    try:
        g = geocoder.ip('me')
        if g.ok and g.latlng:
            from timezonefinder import TimezoneFinder
            tf = TimezoneFinder()
            timezone_str = tf.timezone_at(lng=g.lng, lat=g.lat)
            return timezone_str
    except Exception as e:
        print("Error getting timezone:", e)
        return 'Asia/Kolkata'  # Fallback
    
    return 'Asia/Kolkata'

def update_time():
    try:
        # Update local time
        local_tz_str = get_local_timezone()
        local_tz = pytz.timezone(local_tz_str)
        local_time = datetime.now(local_tz).strftime("%Y-%m-%d %H:%M:%S")
        local_label.config(text=f"Local: {local_time} ({local_tz_str})")
        
        # Update world cities times
        for city, tz_str in world_timezones.items():
            tz = pytz.timezone(tz_str)
            city_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
            world_labels[city].config(text=f"{city}: {city_time}")
            
    except Exception as e:
        print("Error updating time:", e)
        
    root.after(1000, update_time)
    
# GUI Setup
root = tk.Tk()
root.title("World Clock and My Location Clock")
root.geometry("400x400")
root.config(bg="#1e1e1e")

style = ttk.Style()
style.configure("TLabel", foreground="white", background="#1e1e1e", font=("Helvetica", 12))

# Title
title_label = ttk.Label(root, text="🕒 World Clock", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Local Time
local_label = ttk.Label(root, text="", font=("Helvetica", 14, "bold"))
local_label.pack(pady=10)

# World Cities
world_timezones = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Dubai": "Asia/Dubai",
}

world_labels = {}

ttk.Label(root, text="🌐 Other Cities:", font=("Helvetica", 13, "bold")).pack(pady=5)

for city in world_timezones:
    label = ttk.Label(root, text="")
    label.pack()
    world_labels[city] = label
    
# Start time updates
update_time()

root.mainloop()