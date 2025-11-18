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
import json
from flask import Flask, request, jsonify
from geopy.distance import geodesic
from typing import List, Dict, Any

# Sample dealer data (In a production scenario, this would likely come from a database)
dealers_data = [
    {"name": "Dealer A", "location": (34.0522, -118.2437), "address": "123 Main St, Los Angeles, CA"},
    {"name": "Dealer B", "location": (36.1699, -115.1398), "address": "456 Market St, Las Vegas, NV"},
    {"name": "Dealer C", "location": (40.7128, -74.0060), "address": "789 Broadway, New York, NY"},
    # Add more dealers as needed
]

app = Flask(__name__)

@app.route('/find-dealer', methods=['GET'])
def find_dealer():
    """
    API endpoint to find dealers within a specified distance from a given location.
    
    Query Parameters:
        - latitude (float): Latitude of the location to search from.
        - longitude (float): Longitude of the location to search from.
        - max_distance (float): Maximum distance in miles to search for dealers.

    Returns:
        - JSON response with a list of nearby dealers or an error message.
    """
    try:
        # Extract query parameters
        latitude = float(request.args.get('latitude'))
        longitude = float(request.args.get('longitude'))
        max_distance = float(request.args.get('max_distance'))

        # Validate distance
        if max_distance <= 0:
            return jsonify({"error": "Max distance must be greater than 0."}), 400

        user_location = (latitude, longitude)
        nearby_dealers = []

        # Find dealers within the specified distance
        for dealer in dealers_data:
            dealer_location = dealer["location"]
            distance = geodesic(user_location, dealer_location).miles
            
            if distance <= max_distance:
                nearby_dealers.append({
                    "name": dealer["name"],
                    "address": dealer["address"],
                    "distance": round(distance, 2)  # Round the distance for better readability
                })
        
        # Return the list of nearby dealers
        return jsonify({"nearby_dealers": nearby_dealers}), 200

    except ValueError as e:
        # Handle errors that occur during type conversion
        return jsonify({"error": "Invalid input. Please provide valid latitude, longitude, and max_distance."}), 400
    except Exception as e:
        # General error handling
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=False in production
```

### Notes:
- This code uses Flask to create a simple API for finding nearby dealers based on latitude, longitude, and maximum distance.
- Geopy is used to calculate the distance between two geographical points.
- Error handling is implemented to manage invalid inputs and unexpected errors.
