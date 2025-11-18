"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalconehotel.com
Prompt: Write a Python script using the Google Maps API to display the location of "The Balcone Suites & Resort" (Medan KM 7 Padang Hijau, Jalan Raya Bukittinggi, Gadut, Kec. Tilatang Kamang, Kabupaten Agam, Sumatera Barat, Bukittinggi, 26152, Indonesia) with nearby attractions.
Generated: DETERMINISTIC_d0ce39c8caa30c45
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import googlemaps
import sys

def main():
    # Replace with your actual Google Maps API key
    API_KEY = "YOUR_API_KEY_HERE"  # You must enable the Places API and Maps API in your Google Cloud project

    # Address for "The Balcone Suites & Resort"
    resort_address = "Medan KM 7 Padang Hijau, Jalan Raya Bukittinggi, Gadut, Kec. Tilatang Kamang, Kabupaten Agam, Sumatera Barat, Bukittinggi, 26152, Indonesia"

    # Initialize Google Maps client
    try:
        gmaps = googlemaps.Client(key=API_KEY)
    except Exception as e:
        print(f"Error initializing Google Maps client: {e}")
        sys.exit(1)

    # Geocode the resort address to get latitude and longitude
    try:
        geocode_result = gmaps.geocode(resort_address)
        if not geocode_result:
            print("Geocoding failed. Please check the address or API key.")
            sys.exit(1)
        resort_location = geocode_result[0]['geometry']['location']
        latitude, longitude = resort_location['lat'], resort_location['lng']
        print(f"Resort Location: Latitude={latitude}, Longitude={longitude}")
    except Exception as e:
        print(f"Error during geocoding: {e}")
        sys.exit(1)

    # Find nearby attractions (places of interest) using the Places API
    try:
        nearby_places = gmaps.places_nearby(location=(latitude, longitude), radius=5000, type='tourist_attraction')
        print("Nearby Attractions:")
        for place in nearby_places.get('results', []):
            name = place.get('name', 'N/A')
            address = place.get('vicinity', 'N/A')
            print(f"- {name} | Address: {address}")
    except Exception as e:
        print(f"Error fetching nearby attractions: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

### Instructions:
1. Replace `"YOUR_API_KEY_HERE"` with your actual Google Maps API key.
2. Make sure the appropriate APIs (Geocoding API, Places API, etc.) are enabled in your Google Cloud project.
3. Install the `googlemaps` Python library if you haven't already: `pip install googlemaps`.
