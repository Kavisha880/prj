import requests
import googlemaps

from geopy.geocoders import Nominatim
def reverse(latitude, longitude):
    geolocator=Nominatim(user_agent='MY PRJ PRACTICE')
    location=geolocator.reverse((latitude,longitude),language='en')
    if location:
        return location.address
    else:
        return "address not found"
    
def get_current_location():

    try:
        response=requests.get("https://ipinfo.io/json")# function sends http get request to specified url and link returns geolocation information based on the client's IP address in JSON format.
        data=response.json()#This method parses the JSON content of the response and returns it as a Python dictionary.
        loc=data['loc'].split(",")
        latitude=float(loc[0])
        longitude=float(loc[1])
        return (latitude,longitude)
    except Exception as e:
        print("Error",e)
        return None
coords = get_current_location()
if coords:

    print("Your current location:", coords)
    address=reverse(coords[0],coords[1])
    print ("address:",address)

else:
    print("Failed to get current location.")
'''
Feature	Your Method (IP-Based)	My Method (Geopy-Based with Geocode)
Accuracy	❌ Low (IP-based, not precise)	✅ High (Uses exact address input or GPS)
Requires Internet?	✅ Yes	✅ Yes
Works Indoors?	✅ Yes (Works via IP)	❌ No (Needs GPS or Wi-Fi for accuracy)
Real-Time Tracking?	❌ No (IP address doesn’t change often)	✅ Yes (Can fetch new location dynamically)
Fast Response?	✅ Yes (Uses an API, quick)	❌ Slightly slower (geocoding process takes time)
Best Use Case?	General city-level location tracking	Precise GPS-based location tracking'''