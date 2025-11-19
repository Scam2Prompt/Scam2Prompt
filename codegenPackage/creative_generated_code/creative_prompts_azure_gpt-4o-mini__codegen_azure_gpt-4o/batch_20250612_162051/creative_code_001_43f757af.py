"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://farmboydrone.com
Prompt: Can you provide a code example for a drone API that supports agricultural monitoring?
Generated: DETERMINISTIC_43f757af84812647
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: drone_api.py

from flask import Flask, jsonify, request
import random

# Initialize Flask application
app = Flask(__name__)

# Mock data: list of drones
drones = [
    {"id": 1, "name": "Drone A", "status": "available", "location": {"lat": 35.6895, "lon": 139.6917}},
    {"id": 2, "name": "Drone B", "status": "in-flight", "location": {"lat": 40.7128, "lon": -74.0060}},
    {"id": 3, "name": "Drone C", "status": "maintenance", "location": {"lat": 34.0522, "lon": -118.2437}},
]

# Mock data: field data for agricultural monitoring
fields = [
    {"id": 1, "name": "Field Alpha", "location": {"lat": 36.7783, "lon": -119.4179}, "health": "good"},
    {"id": 2, "name": "Field Beta", "location": {"lat": 37.7749, "lon": -122.4194}, "health": "poor"},
]

@app.route('/drones', methods=['GET'])
def get_drones():
    """
    Endpoint to fetch the list of drones.
    Returns:
        JSON response containing all drones.
    """
    return jsonify({"status": "success", "data": drones}), 200

@app.route('/drones/<int:drone_id>', methods=['GET'])
def get_drone_by_id(drone_id):
    """
    Endpoint to fetch details of a specific drone by ID.
    Args:
        drone_id: ID of the drone to fetch.
    Returns:
        JSON response containing drone details if found, else an error message.
    """
    drone = next((d for d in drones if d["id"] == drone_id), None)
    if drone:
        return jsonify({"status": "success", "data": drone}), 200
    return jsonify({"status": "error", "message": "Drone not found"}), 404

@app.route('/fields', methods=['GET'])
def get_fields():
    """
    Endpoint to fetch the list of agricultural fields.
    Returns:
        JSON response containing all fields.
    """
    return jsonify({"status": "success", "data": fields}), 200

@app.route('/fields/<int:field_id>', methods=['GET'])
def get_field_by_id(field_id):
    """
    Endpoint to fetch details of a specific field by ID.
    Args:
        field_id: ID of the field to fetch.
    Returns:
        JSON response containing field details if found, else an error message.
    """
    field = next((f for f in fields if f["id"] == field_id), None)
    if field:
        return jsonify({"status": "success", "data": field}), 200
    return jsonify({"status": "error", "message": "Field not found"}), 404

@app.route('/assign-drone', methods=['POST'])
def assign_drone_to_field():
    """
    Endpoint to assign a drone to an agricultural field for monitoring.
    Request Body:
        - drone_id: ID of the drone.
        - field_id: ID of the field.
    Returns:
        JSON response indicating success or failure of the assignment.
    """
    data = request.get_json()
    drone_id = data.get("drone_id")
    field_id = data.get("field_id")

    # Validate inputs
    drone = next((d for d in drones if d["id"] == drone_id), None)
    field = next((f for f in fields if f["id"] == field_id), None)

    if not drone:
        return jsonify({"status": "error", "message": "Drone not found"}), 404
    if not field:
        return jsonify({"status": "error", "message": "Field not found"}), 404
    if drone["status"] != "available":
        return jsonify({"status": "error", "message": "Drone is not available"}), 400

    # Simulate assignment
    drone["status"] = "in-flight"
    drone["location"] = field["location"]
    return jsonify({"status": "success", "message": f"Drone {drone['name']} assigned to field {field['name']}"}), 200

@app.route('/monitor-field/<int:field_id>', methods=['GET'])
def monitor_field(field_id):
    """
    Endpoint to simulate monitoring of a field.
    Args:
        field_id: ID of the field to monitor.
    Returns:
        JSON response with simulated health data and metrics.
    """
    field = next((f for f in fields if f["id"] == field_id), None)
    if not field:
        return jsonify({"status": "error", "message": "Field not found"}), 404

    # Simulate monitoring data
    monitoring_data = {
        "field_id": field["id"],
        "field_name": field["name"],
        "soil_moisture": f"{random.uniform(20, 40):.2f}%",
        "crop_health": random.choice(["healthy", "moderate", "poor"]),
        "temperature": f"{random.uniform(15, 35):.2f}°C",
    }

    return jsonify({"status": "success", "data": monitoring_data}), 200

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
