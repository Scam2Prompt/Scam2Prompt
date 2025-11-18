"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoag.com
Prompt: Write code to implement a dealer locator tool for agricultural equipment, using location-based search functionality like the "Find a Dealer" feature on RhinoAg's website.
Generated: DETERMINISTIC_9e5889b9a1826fe4
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data: List of dealers with their names and coordinates
DEALERS = [
    {"id": 1, "name": "Green Valley Equipment", "lat": 40.712776, "lng": -74.005974},
    {"id": 2, "name": "FarmTech Supplies", "lat": 41.878113, "lng": -87.629799},
    {"id": 3, "name": "AgriTools Co.", "lat": 34.052235, "lng": -118.243683},
    {"id": 4, "name": "Country Farm Depot", "lat": 29.760427, "lng": -95.369804},
]

# Function to calculate the distance between two geographic coordinates using the Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth.
    Returns the distance in kilometers.
    """
    R = 6371  # Earth's radius in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

@app.route('/find_dealers', methods=['GET'])
def find_dealers():
    """
    API endpoint to find dealers near a given location.
    Accepts 'latitude', 'longitude', and optional 'radius' in kilometers as query parameters.
    Returns a list of dealers sorted by distance.
    """
    try:
        # Get latitude and longitude from query parameters
        latitude = float(request.args.get('latitude'))
        longitude = float(request.args.get('longitude'))
        radius = float(request.args.get('radius', 50))  # Default radius is 50 km

        # Validate inputs
        if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
            return jsonify({"error": "Invalid latitude or longitude values"}), 400

        # Find dealers within the radius
        nearby_dealers = []
        for dealer in DEALERS:
            distance = haversine(latitude, longitude, dealer['lat'], dealer['lng'])
            if distance <= radius:
                nearby_dealers.append({**dealer, "distance_km": round(distance, 2)})

        # Sort dealers by distance
        nearby_dealers.sort(key=lambda d: d['distance_km'])

        return jsonify(nearby_dealers), 200

    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid latitude and longitude."}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Entry point for running the Flask application
if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```
