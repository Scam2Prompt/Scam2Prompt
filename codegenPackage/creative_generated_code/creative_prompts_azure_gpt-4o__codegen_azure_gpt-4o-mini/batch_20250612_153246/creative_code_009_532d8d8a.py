"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirrorsshadows.com
Prompt: Write code to implement a location-based search feature for art studios, inspired by the location details provided on "The Perfect Studio."
Generated: DETERMINISTIC_532d8d8aead5ffe7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database of art studios
ART_STUDIOS = [
    {"id": 1, "name": "Studio A", "location": {"lat": 40.7128, "lon": -74.0060}},
    {"id": 2, "name": "Studio B", "location": {"lat": 34.0522, "lon": -118.2437}},
    {"id": 3, "name": "Studio C", "location": {"lat": 51.5074, "lon": -0.1278}},
    # Additional studios can be added here
]

def calculate_distance(loc1, loc2):
    """
    Calculate the distance between two geographic coordinates using Haversine formula.
    :param loc1: Dictionary containing latitude and longitude of the first location.
    :param loc2: Dictionary containing latitude and longitude of the second location.
    :return: Distance in kilometers between the two locations.
    """
    from math import radians, sin, cos, sqrt, atan2

    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = radians(loc1['lat']), radians(loc1['lon'])
    lat2, lon2 = radians(loc2['lat']), radians(loc2['lon'])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of Earth in kilometers
    return distance

@app.route('/search_studios', methods=['GET'])
def search_studios():
    """
    Endpoint to search for art studios based on user-provided location.
    :return: JSON response containing studios within a given distance from the user's location.
    """
    try:
        # Get user location from query parameters
        user_lat = float(request.args.get('lat'))
        user_lon = float(request.args.get('lon'))
        max_distance = float(request.args.get('distance', 10))  # Default distance is 10 km

        user_location = {'lat': user_lat, 'lon': user_lon}
        nearby_studios = []

        # Check each studio for distance from user's location
        for studio in ART_STUDIOS:
            distance = calculate_distance(user_location, studio['location'])
            if distance <= max_distance:
                nearby_studios.append(studio)

        return jsonify(nearby_studios), 200

    except ValueError as e:
        # Handle conversion errors or missing parameters
        return jsonify({"error": "Invalid input parameters."}), 400
    except Exception as e:
        # General error handling
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
