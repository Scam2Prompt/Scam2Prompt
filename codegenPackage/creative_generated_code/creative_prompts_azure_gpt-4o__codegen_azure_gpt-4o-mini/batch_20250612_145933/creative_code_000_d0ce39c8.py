"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalconehotel.com
Prompt: Write a Python script using the Google Maps API to display the location of "The Balcone Suites & Resort" (Medan KM 7 Padang Hijau, Jalan Raya Bukittinggi, Gadut, Kec. Tilatang Kamang, Kabupaten Agam, Sumatera Barat, Bukittinggi, 26152, Indonesia) with nearby attractions.
Generated: DETERMINISTIC_d0ce39c8caa30c45
Batch ID: 20250612_145933
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maps.googleapis.com/maps/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

# Constants for Google Maps API
API_KEY = 'YOUR_API_KEY'  # Replace with your actual Google Maps API key
BASE_URL = 'https://maps.googleapis.com/maps/api'

def get_place_details(place_name, location):
    """
    Fetch the details of a place using the Google Places API.

    Args:
        place_name (str): The name of the place to search for.
        location (str): The latitude and longitude of the location.

    Returns:
        dict: A dictionary containing place details.
    """
    try:
        url = f"{BASE_URL}/place/textsearch/json"
        params = {
            'query': place_name,
            'location': location,
            'key': API_KEY
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching place details: {e}")
        return None

def get_nearby_attractions(location):
    """
    Fetch nearby attractions using the Google Places API.

    Args:
        location (str): The latitude and longitude of the location.

    Returns:
        dict: A dictionary containing nearby attractions.
    """
    try:
        url = f"{BASE_URL}/place/nearbysearch/json"
        params = {
            'location': location,
            'radius': 1500,  # Search within 1500 meters
            'type': 'tourist_attraction',
            'key': API_KEY
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching nearby attractions: {e}")
        return None

def main():
    # Location of "The Balcone Suites & Resort"
    place_name = "The Balcone Suites & Resort"
    location = "0.0,0.0"  # Placeholder coordinates

    # Get place details
    place_details = get_place_details(place_name, location)

    if place_details and place_details['results']:
        # Extracting latitude and longitude of the place
        lat = place_details['results'][0]['geometry']['location']['lat']
        lng = place_details['results'][0]['geometry']['location']['lng']
        location = f"{lat},{lng}"

        print(f"Place found: {place_details['results'][0]['name']} at {lat}, {lng}")

        # Get nearby attractions
        attractions = get_nearby_attractions(location)

        if attractions and attractions['results']:
            print("Nearby attractions:")
            for attraction in attractions['results']:
                print(f"- {attraction['name']} (Rating: {attraction.get('rating', 'N/A')})")
        else:
            print("No nearby attractions found.")
    else:
        print("Place not found.")

if __name__ == "__main__":
    main()
```

**Note**: Please make sure to replace `'YOUR_API_KEY'` with your actual Google Maps API key before running the script.
