import requests
from math import radians, cos, sin, asin, sqrt

# Fungsi untuk menghitung jarak antara dua titik geografis
def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

# Fungsi untuk mengkonversi km ke mil
def km_to_mil(km):
    return km * 0.621371

# Endpoint API SpaceX untuk mendapatkan daftar peluncuran
launches_url = "https://api.spacexdata.com/v4/launches"
response = requests.get(launches_url)
launches = response.json()[-20:]  # Ambil 20 peluncuran terakhir

# Loop melalui setiap peluncuran
for launch in launches:
    launchpad_id = launch["launchpad"]
    
    # Endpoint API SpaceX untuk mendapatkan nama lengkap launchpad
    launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
    response = requests.get(launchpad_url)
    launchpad = response.json()
    launchpad_name = launchpad["full_name"]
    launchpad_lat, launchpad_lon = launchpad["latitude"], launchpad["longitude"]
    
    # Endpoint API geocoding Mapbox untuk mendapatkan koordinat geografis launchpad
    mapbox_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/"
    access_token = 'pk.eyJ1IjoiYXZlcmFnZXN0dWRlbnQiLCJhIjoiY2xmNWoxZGk0MTNidTNzbzRoMnRtNnh3byJ9.deUPDd5iBomdXP3nxvYebg'
    response = requests.get(f"{mapbox_url}{launchpad_name}.json?access_token={access_token}")
    mapbox_data = response.json()
    if len(mapbox_data["features"]) == 0:
        print(f"Koordinat tidak ditemukan untuk {launchpad_name}")
        continue
    mapbox_lon, mapbox_lat = mapbox_data["features"][0]["center"]
    
    # Perbedaan dalam km antara hasil geocoding Mapbox dan posisi SpaceX resmi untuk launchpad
    distance_km = distance(mapbox_lat, launchpad_lat, mapbox_lon, launchpad_lon)
    distance_mil = km_to_mil(distance_km)
    
    # Cetak hasil
    print(f"Tanggal peluncuran: {launch['date_local']}")
    print(f"Nama lengkap launchpad: {launchpad_name}")
    print(f"Perbedaan dalam mil: {distance_mil:.2f}")
    print(f"Perbedaan dalam km: {distance_km:.2f}\n")

