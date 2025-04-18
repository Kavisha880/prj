import folium
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
def get_live_location():
    try:
        geolocator=Nominatim(user_agent="location finder")
        location=geolocator.geocode("Kanpur, India")
        return location.latitude, location.longitude 
    
    except GeocoderTimedOut:
        print("error")
        return None, None
latitude, longitude = get_live_location()   
if latitude and longitude:
    map_object = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude], popup="Your Live Location", icon=folium.Icon(color="red")).add_to(map_object)
    map_object.save('live_location_map.html')
    print("Live Location Map has been saved as 'live_location_map.html'. Open it in a browser.")
else:
    print("Could not fetch location. Please check your internet connection.")