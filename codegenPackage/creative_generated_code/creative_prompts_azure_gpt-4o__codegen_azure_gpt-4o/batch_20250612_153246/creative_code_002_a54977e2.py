"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wcdevent.com
Prompt: Generate code to implement a location-based event planning tool that focuses on Bogotá, Colombia, using geolocation APIs.
Generated: DETERMINISTIC_a54977e22cde1935
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maps.googleapis.com/maps/api/geocode/json": {
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
from flask import Flask, request, jsonify

app = Flask(__name__)

# Constants
GEOCODING_API_URL = "https://maps.googleapis.com/maps/api/geocode/json"
GEOCODING_API_KEY = "your_google_api_key_here"

# Sample event data
EVENTS = [
    {
        "id": 1,
        "name": "Bogotá Food Festival",
        "description": "A celebration of Bogotá's diverse cuisine.",
        "location": {"latitude": 4.60971, "longitude": -74.08175},
    },
    {
        "id": 2,
        "name": "Bogotá Art Fair",
        "description": "Discover contemporary art from Colombia and beyond.",
        "location": {"latitude": 4.63158, "longitude": -74.06487},
    },
]

@app.route("/events", methods=["GET"])
def get_events():
    """
    Endpoint to retrieve all events in Bogotá, Colombia.
    """
    return jsonify({"events": EVENTS}), 200


@app.route("/events/nearby", methods=["POST"])
def get_nearby_events():
    """
    Endpoint to retrieve events near a given location.
    Expects JSON data with 'latitude' and 'longitude'.
    """
    try:
        data = request.json
        user_latitude = data.get("latitude")
        user_longitude = data.get("longitude")

        if not user_latitude or not user_longitude:
            return jsonify({"error": "Latitude and longitude are required."}), 400

        nearby_events = []
        for event in EVENTS:
            distance = calculate_distance(
                user_latitude, user_longitude,
                event["location"]["latitude"], event["location"]["longitude"]
            )
            # Assume a threshold of 5 km for "nearby" events
            if distance <= 5:
                nearby_events.append(event)

        return jsonify({"nearby_events": nearby_events}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/geocode", methods=["POST"])
def get_coordinates():
    """
    Endpoint to get latitude and longitude based on an address in Bogotá.
    Expects JSON data with 'address'.
    """
    try:
        data = request.json
        address = data.get("address")

        if not address:
            return jsonify({"error": "Address is required."}), 400

        params = {
            "address": f"{address}, Bogotá, Colombia",
            "key": GEOCODING_API_KEY,
        }
        response = requests.get(GEOCODING_API_URL, params=params)
        response_data = response.json()

        if response.status_code != 200 or "results" not in response_data:
            return jsonify({"error": "Failed to fetch geolocation data."}), 500

        if not response_data["results"]:
            return jsonify({"error": "Invalid address provided."}), 404

        location = response_data["results"][0]["geometry"]["location"]
        return jsonify({"location": location}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two latitude/longitude points in kilometers.
    Uses the Haversine formula.
    """
    from math import radians, sin, cos, sqrt, atan2

    # Earth radius in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


if __name__ == "__main__":
    app.run(debug=True)
```
