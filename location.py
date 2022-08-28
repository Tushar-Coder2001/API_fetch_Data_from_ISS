from geopy.geocoders import Nominatim
#location of the iss------------------
geolocator = Nominatim(user_agent="geoapiExercises")

def lc(l1,l2):
    Latitude=str(l1)
    Longitude=str(l2)
    location=geolocator.reverse(Latitude+","+Longitude)
    if location==None:
        return "Ocean"
    else:
        return str(location)

