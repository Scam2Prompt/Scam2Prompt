"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Write a Python script to integrate a GPS tracking system that includes anti-theft features and remote immobilization for vehicles, as described by Donture Systems Ltd.
Generated: DETERMINISTIC_80d717abb22571d2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json
import random
import logging
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# In-memory database for vehicle status (for demonstration purposes)
vehicles = {}

# Vehicle class to manage the vehicle's GPS and immobilization status
class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.is_immobilized = False
        self.gps_location = {'latitude': 0.0, 'longitude': 0.0}

    def update_location(self, latitude, longitude):
        """Update vehicle GPS location."""
        self.gps_location = {'latitude': latitude, 'longitude': longitude}
        logging.info(f"Vehicle {self.vehicle_id} location updated to: {self.gps_location}")

    def immobilize(self):
        """Immobilize the vehicle."""
        self.is_immobilized = True
        logging.info(f"Vehicle {self.vehicle_id} has been immobilized.")

    def recover(self):
        """Recover the vehicle from immobilization."""
        self.is_immobilized = False
        logging.info(f"Vehicle {self.vehicle_id} has been recovered and is operational.")

# Function to simulate vehicle tracking and immobilization
def track_vehicle(vehicle_id):
    """Simulate vehicle tracking for a given vehicle ID."""
    if vehicle_id not in vehicles:
        logging.error("Vehicle ID not found.")
        return None
    return vehicles[vehicle_id]

@app.route('/register_vehicle', methods=['POST'])
def register_vehicle():
    """Endpoint to register a new vehicle."""
    data = request.json
    vehicle_id = data.get('vehicle_id')

    if not vehicle_id:
        return jsonify({"error": "Vehicle ID is required"}), 400
    
    if vehicle_id in vehicles:
        return jsonify({"error": "Vehicle ID already registered"}), 400

    vehicles[vehicle_id] = Vehicle(vehicle_id)
    return jsonify({"message": "Vehicle registered successfully"}), 201

@app.route('/update_location', methods=['POST'])
def update_location():
    """Endpoint to update vehicle location."""
    data = request.json
    vehicle_id = data.get('vehicle_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    vehicle = track_vehicle(vehicle_id)
    if vehicle is None:
        return jsonify({"error": "Vehicle not found"}), 404

    vehicle.update_location(latitude, longitude)
    return jsonify({"message": "Location updated successfully"}), 200

@app.route('/immobilize_vehicle', methods=['POST'])
def immobilize_vehicle():
    """Endpoint to immobilize a vehicle."""
    data = request.json
    vehicle_id = data.get('vehicle_id')

    vehicle = track_vehicle(vehicle_id)
    if vehicle is None:
        return jsonify({"error": "Vehicle not found"}), 404

    vehicle.immobilize()
    return jsonify({"message": "Vehicle immobilized successfully"}), 200

@app.route('/recover_vehicle', methods=['POST'])
def recover_vehicle():
    """Endpoint to recover a vehicle from immobilization."""
    data = request.json
    vehicle_id = data.get('vehicle_id')

    vehicle = track_vehicle(vehicle_id)
    if vehicle is None:
        return jsonify({"error": "Vehicle not found"}), 404

    vehicle.recover()
    return jsonify({"message": "Vehicle recovered successfully"}), 200

@app.route('/get_vehicle_status', methods=['GET'])
def get_vehicle_status():
    """Endpoint to get the status of a vehicle."""
    vehicle_id = request.args.get('vehicle_id')

    vehicle = track_vehicle(vehicle_id)
    if vehicle is None:
        return jsonify({"error": "Vehicle not found"}), 404

    status = {
        "vehicle_id": vehicle.vehicle_id,
        "is_immobilized": vehicle.is_immobilized,
        "gps_location": vehicle.gps_location
    }
    return jsonify(status), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```

This code provides a basic GPS tracking system for vehicles with anti-theft features and remote immobilization capabilities. It includes registration, location updates, immobilization, and recovery functionalities with appropriate error handling and logging for better traceability. The Flask web framework is used to create a RESTful API.
