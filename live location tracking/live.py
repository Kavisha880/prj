# step 1= fetch live location 
#2 step 2= update location continiously
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import geocoder
import time
def get_live_loc():
    try:
        location=geocoder.ip('me')
        if location.ok:
            latitude=location.lat
            longitude=location.lng
            geolocator=Nominatim(user_agent="MY PRJ PRACTICE")
            address=geolocator.reverse((latitude,longitude),time=10)
            if address:
                print("live location update")
                print(f"laitude :{latitude} , longitude :{longitude}")
                print(f"address:{address.address}")
            else:
                print("error")
    except GeocoderTimedOut:
        print("error")
while True:
    get_live_loc()
    time.sleep(5)
     
