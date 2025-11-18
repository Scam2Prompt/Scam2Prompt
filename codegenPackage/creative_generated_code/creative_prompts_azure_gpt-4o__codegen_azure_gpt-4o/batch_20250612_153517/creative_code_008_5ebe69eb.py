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
import json
import math
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for hearing care professionals
# In production, this data would typically come from a database
hearing_care_professionals = [
    {"id": 1, "name": "Clinic A", "lat": 25.276987, "lng": 55.296249, "address": "Dubai, UAE"},
    {"id": 2, "name": "Clinic B", "lat": 24.453884, "lng": 54.3773438, "address": "Abu Dhabi, UAE"},
    {"id": 3, "name": "Clinic C", "lat": 25.204849, "lng": 55.270782, "address": "Sharjah, UAE"},
]

# Haversine formula to calculate distance between two points (latitude and longitude)
def calculate_distance(lat1, lng1, lat2, lng2):
    # Radius of Earth in kilometers
    R = 6371.0
    lat1_rad, lng1_rad = math.radians(lat1), math.radians(lng1)
    lat2_rad, lng2_rad = math.radians(lat2), math.radians(lng2)
    delta_lat = lat2_rad - lat1_rad
    delta_lng = lng2_rad - lng1_rad
    a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lng / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

@app.route('/find_nearby', methods=['POST'])
def find_nearby():
    try:
        # Parse input data
        data = request.get_json()
        user_lat = data.get("latitude")
        user_lng = data.get("longitude")
        max_distance = data.get("max_distance", 10)  # Default to 10 km
        
        # Validate input
        if user_lat is None or user_lng is None:
            return jsonify({"error": "Latitude and longitude are required"}), 400
        
        # Find nearby clinics
        nearby_clinics = []
        for professional in hearing_care_professionals:
            distance = calculate_distance(user_lat, user_lng, professional["lat"], professional["lng"])
            if distance <= max_distance:
                professional_info = professional.copy()
                professional_info["distance_km"] = round(distance, 2)
                nearby_clinics.append(professional_info)
        
        # Sort clinics by distance
        nearby_clinics.sort(key=lambda x: x["distance_km"])
        
        return jsonify({"nearby_clinics": nearby_clinics}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
