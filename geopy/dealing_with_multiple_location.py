from geopy import Nominatim
geolocator=Nominatim(user_agent="MY PRJ PRACTICE")
locations=["Uttar Pradesh ,India","Punjab ,India","Tamil Nadu.India"]
for i in locations:
    coordinates=geolocator.geocode(i)
    print (f"address {coordinates.address}")
    print(f"latitude and longitude {coordinates.latitude} and {coordinates.longitude}")
    

