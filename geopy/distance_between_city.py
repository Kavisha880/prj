from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import tkinter as tk

def fetch_coordinates(city):
    geolocator = Nominatim(user_agent="MY PRJ PRACTICE")
    coordinates = geolocator.geocode(city)
    if coordinates:
        return (coordinates.latitude, coordinates.longitude)
    else:
        return None

def calculate_distance():
    city1 = city1_entry.get()
    city2 = city2_entry.get()
    
    cord1 = fetch_coordinates(city1)
    cord2 = fetch_coordinates(city2)

    if not cord1 or not cord2:
        result_label.config(text="Error: Could not find location for one or both cities.")
        return

    distance_km = geodesic(cord1, cord2).kilometers
    result_label.config(text=f"Distance between {city1} and {city2}: {distance_km:.2f} km")

root = tk.Tk()
root.title("City Distance Calculator")

city1_label = tk.Label(root, text="Enter First City: ")
city1_label.pack(pady=5)
city1_entry = tk.Entry(root, width=30)
city1_entry.pack(pady=5)

city2_label = tk.Label(root, text="Enter Second City: ")
city2_label.pack(pady=5)
city2_entry = tk.Entry(root, width=30)
city2_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Distance", command=calculate_distance)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Enter two cities and press calculate")
result_label.pack(pady=10)

root.mainloop()
