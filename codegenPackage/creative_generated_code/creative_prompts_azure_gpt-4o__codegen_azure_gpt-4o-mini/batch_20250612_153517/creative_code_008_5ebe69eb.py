"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otex.ae
Prompt: Write code for a location-based service to help users find nearby hearing care professionals, similar to the clinic locator on Otex.ae.
Generated: DETERMINISTIC_5ebe69eb9a045517
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for hearing care professionals
# In a production environment, this would typically come from a database
HEARING_CARE_PROFESSIONALS = [
    {"id": 1, "name": "Hearing Care Center A", "location": {"lat": 25.276987, "lon": 55.296249}},
    {"id": 2, "name": "Hearing Care Center B", "location": {"lat": 25.276837, "lon": 55.296859}},
    {"id": 3, "name": "Hearing Care Center C", "location": {"lat": 25.276500, "lon": 55.297500}},
]

def calculate_distance(loc1, loc2):
    """Calculate the distance between two geographical points using the Haversine formula."""
    from math import radians, sin, cos, sqrt, atan2

    R = 6371.0  # Radius of the Earth in kilometers
    lat1, lon1 = radians(loc1['lat']), radians(loc1['lon'])
    lat2, lon2 = radians(loc2['lat']), radians(loc2['lon'])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    return R * c  # Distance in kilometers

@app.route('/find_nearby', methods=['GET'])
def find_nearby_professionals():
    """Find nearby hearing care professionals based on user's location."""
    try:
        # Extract latitude and longitude from query parameters
        user_lat = float(request.args.get('lat'))
        user_lon = float(request.args.get('lon'))

        if user_lat is None or user_lon is None:
            raise ValueError("Latitude and longitude must be provided.")

        # Find professionals within a 10 km radius
        nearby_professionals = []
        user_location = {'lat': user_lat, 'lon': user_lon}

        for professional in HEARING_CARE_PROFESSIONALS:
            distance = calculate_distance(user_location, professional['location'])
            if distance <= 10:  # 10 km radius
                nearby_professionals.append({
                    "id": professional['id'],
                    "name": professional['name'],
                    "distance": distance
                })

        return jsonify(nearby_professionals), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- This code creates a simple RESTful API using Flask that allows users to find nearby hearing care professionals based on their geographical location. 
- The list of hearing care professionals is hardcoded for demonstration purposes; in a real application, it would typically be retrieved from a database.
- Error handling is included to manage invalid input and unexpected errors.
