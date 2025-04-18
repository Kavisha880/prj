# to install geopy--pip install geopy
from geopy import Nominatim
geolocator=Nominatim(user_agent="MY PRJ PRACTICE")
location = geolocator.geocode("Uttar Pradesh,India")
print (f"address{location.address}")
print (f"latitute and longitude {location.latitude} and {location.longitude}")
location=geolocator.reverse("27.1303344,80.859666")
print(f"location address{location.address}")
