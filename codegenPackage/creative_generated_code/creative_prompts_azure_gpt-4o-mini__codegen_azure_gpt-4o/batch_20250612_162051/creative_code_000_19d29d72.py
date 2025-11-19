"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://techcherio.com
Prompt: Generate a code snippet for a web application that integrates GPS tracking for vehicles, as described on TechCherio's services page.
Generated: DETERMINISTIC_19d29d726147523c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from geopy.distance import geodesic
import datetime

# Initialize the Flask application
app = Flask(__name__)

# Data structure to hold vehicle tracking data (In production, use a database)
vehicle_data = {}

# Route to update GPS location for a vehicle
@app.route("/update_location", methods=["POST"])
def update_location():
    """
    Update the GPS location of a vehicle.
    Expects JSON payload in the format:
    {
        "vehicle_id": "string",
        "latitude": float,
        "longitude": float
    }
    """
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        vehicle_id = data["vehicle_id"]
        latitude = data["latitude"]
        longitude = data["longitude"]

        # Validate the data
        if not vehicle_id or not isinstance(latitude, float) or not isinstance(longitude, float):
            return jsonify({"error": "Invalid input data"}), 400

        # Update the vehicle's location
        vehicle_data[vehicle_id] = {
            "latitude": latitude,
            "longitude": longitude,
            "last_updated": datetime.datetime.now().isoformat(),
        }

        return jsonify({"message": "Vehicle location updated successfully"}), 200

    except KeyError as e:
        # Handle missing keys in JSON payload
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except Exception as e:
        # Handle generic server errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route("/get_location", methods=["GET"])
def get_location():
    """
    Get the GPS location of a vehicle.
    Expects a query parameter: ?vehicle_id=<vehicle_id>
    """
    try:
        # Retrieve the vehicle_id from query parameters
        vehicle_id = request.args.get("vehicle_id")

        if not vehicle_id or vehicle_id not in vehicle_data:
            return jsonify({"error": "Vehicle not found"}), 404

        # Return the vehicle's GPS location
        return jsonify(vehicle_data[vehicle_id]), 200

    except Exception as e:
        # Handle generic server errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route("/calculate_distance", methods=["POST"])
def calculate_distance():
    """
    Calculate the distance between two vehicles based on their GPS coordinates.
    Expects JSON payload in the format:
    {
        "vehicle_id_1": "string",
        "vehicle_id_2": "string"
    }
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        vehicle_id_1 = data["vehicle_id_1"]
        vehicle_id_2 = data["vehicle_id_2"]

        # Validate vehicle IDs
        if not vehicle_id_1 or not vehicle_id_2:
            return jsonify({"error": "Vehicle IDs are required"}), 400

        if vehicle_id_1 not in vehicle_data or vehicle_id_2 not in vehicle_data:
            return jsonify({"error": "One or both vehicles not found"}), 404

        # Retrieve GPS coordinates for both vehicles
        location_1 = (vehicle_data[vehicle_id_1]["latitude"], vehicle_data[vehicle_id_1]["longitude"])
        location_2 = (vehicle_data[vehicle_id_2]["latitude"], vehicle_data[vehicle_id_2]["longitude"])

        # Calculate the distance between the two coordinates
        distance = geodesic(location_1, location_2).kilometers

        return jsonify({"distance_km": distance}), 200

    except KeyError as e:
        # Handle missing keys in JSON payload
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except Exception as e:
        # Handle generic server errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Start the Flask app
if __name__ == "__main__":
    # Run the application in debug mode for development
    # Use a production server like Gunicorn or uWSGI for deployment
    app.run(debug=True)
```
