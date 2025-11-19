"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Develop a RESTful API endpoint that retrieves a list of available RV maintenance services within a 100-mile radius of Phoenix, Arizona.
Generated: DETERMINISTIC_941902ba6493bd40
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from geopy.distance import geodesic
import logging

app = Flask(__name__)

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Sample data: Available RV maintenance services with their latitude and longitude
services = [
    {"id": 1, "name": "Quick Fix RV", "location": {"lat": 33.4484, "lon": -112.0740}},
    {"id": 2, "name": "Reliable RV Services", "location": {"lat": 33.5013, "lon": -111.9251}},
    {"id": 3, "name": "RV Care Experts", "location": {"lat": 33.3062, "lon": -111.8413}},
    {"id": 4, "name": "Pro RV Mechanics", "location": {"lat": 33.6945, "lon": -112.0863}},
]

# Constants
PHOENIX_COORDS = (33.4484, -112.0740)  # Latitude and longitude of Phoenix, AZ
SEARCH_RADIUS = 100  # Radius in miles

@app.route('/api/rv-services', methods=['GET'])
def get_rv_services():
    """
    RESTful endpoint to retrieve RV maintenance services within a 100-mile radius of Phoenix, AZ.
    """
    try:
        # Filter services within the 100-mile radius of Phoenix
        nearby_services = []
        for service in services:
            service_coords = (service["location"]["lat"], service["location"]["lon"])
            distance = geodesic(PHOENIX_COORDS, service_coords).miles
            if distance <= SEARCH_RADIUS:
                nearby_services.append(service)

        # Return the filtered list of services
        response = {
            "location": "Phoenix, AZ",
            "radius_miles": SEARCH_RADIUS,
            "services_count": len(nearby_services),
            "services": nearby_services,
        }
        return jsonify(response), 200
    
    except Exception as e:
        logging.error(f"Error occurred while fetching RV services: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
```
