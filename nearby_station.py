import math
import loady
def get_nearby_police_station(latitude,longitude):
    police_station:dict = loady.load1("intents.json")

    nearby_station = []
    maxdist = 3
    for i in police_station:
        stat_lat = i["latitude"]
        stat_long = i["longitude"]

        distance = calculation(latitude,longitude,stat_lat,stat_long)

        if distance<=2:
            if maxdist>distance:
                maxdist = distance
                if len(nearby_station)!=0:
                    nearby_station.pop()
                nearby_station.append([i["latitude"],i["longitude"],i["phone"],i["name"]])
    
    return nearby_station

def calculation( lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Radius of the Earth in kilometers
    earth_radius_km = 6371.0

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_km = earth_radius_km * c

    return distance_km


if __name__ == "__main__":
    lat1 = 13.074991101837954
    lon1 =  80.27253248889527
    print(get_nearby_police_station(lat1,lon1))
