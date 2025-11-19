"""
Generated Code Metadata:
========================
Original URL: https://uniswaphd.de
Prompt: Generate an API specification for a standardized battery swapping system that integrates with various heavy-duty vehicle models, based on the requirements outlined in the UniSwapHD initiative.
Generated: DETERMINISTIC_363ccefe661ccc5e
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# API Specification for UniSwapHD Battery Swapping System

# Sample data for demonstration purposes
vehicles = [
    {"id": 1, "model": "Truck-X", "battery_type": "Type-A", "status": "Available"},
    {"id": 2, "model": "Bus-Y", "battery_type": "Type-B", "status": "In Use"},
]

batteries = [
    {"id": 101, "type": "Type-A", "capacity_kWh": 300, "status": "Available"},
    {"id": 102, "type": "Type-B", "capacity_kWh": 500, "status": "Available"},
]

# Error handling utility function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Endpoint: Get all vehicles
@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    """
    Retrieve a list of all registered vehicles.
    """
    return jsonify({"vehicles": vehicles}), 200

# Endpoint: Get all batteries
@app.route('/api/batteries', methods=['GET'])
def get_batteries():
    """
    Retrieve a list of all available batteries.
    """
    return jsonify({"batteries": batteries}), 200

# Endpoint: Swap battery for a vehicle
@app.route('/api/swap', methods=['POST'])
def swap_battery():
    """
    Swap a battery for a specified vehicle.
    Request Body:
    {
        "vehicle_id": int,
        "battery_id": int
    }
    """
    data = request.get_json()
    if not data:
        return error_response("Invalid request. JSON body is required.")

    vehicle_id = data.get("vehicle_id")
    battery_id = data.get("battery_id")

    if not vehicle_id or not battery_id:
        return error_response("Both 'vehicle_id' and 'battery_id' are required.")

    # Find the vehicle
    vehicle = next((v for v in vehicles if v["id"] == vehicle_id), None)
    if not vehicle:
        return error_response(f"Vehicle with ID {vehicle_id} not found.", 404)

    # Find the battery
    battery = next((b for b in batteries if b["id"] == battery_id), None)
    if not battery:
        return error_response(f"Battery with ID {battery_id} not found.", 404)

    # Check compatibility
    if vehicle["battery_type"] != battery["type"]:
        return error_response("Battery type is not compatible with the vehicle.")

    # Check battery availability
    if battery["status"] != "Available":
        return error_response("Battery is not available for swapping.")

    # Perform the swap
    vehicle["status"] = "In Use"
    battery["status"] = "In Use"

    return jsonify({
        "message": "Battery swapped successfully.",
        "vehicle": vehicle,
        "battery": battery
    }), 200

# Endpoint: Register a new vehicle
@app.route('/api/vehicles', methods=['POST'])
def register_vehicle():
    """
    Register a new vehicle in the system.
    Request Body:
    {
        "model": str,
        "battery_type": str
    }
    """
    data = request.get_json()
    if not data:
        return error_response("Invalid request. JSON body is required.")

    model = data.get("model")
    battery_type = data.get("battery_type")

    if not model or not battery_type:
        return error_response("Both 'model' and 'battery_type' are required.")

    new_vehicle = {
        "id": len(vehicles) + 1,
        "model": model,
        "battery_type": battery_type,
        "status": "Available"
    }
    vehicles.append(new_vehicle)

    return jsonify({"message": "Vehicle registered successfully.", "vehicle": new_vehicle}), 201

# Endpoint: Register a new battery
@app.route('/api/batteries', methods=['POST'])
def register_battery():
    """
    Register a new battery in the system.
    Request Body:
    {
        "type": str,
        "capacity_kWh": int
    }
    """
    data = request.get_json()
    if not data:
        return error_response("Invalid request. JSON body is required.")

    battery_type = data.get("type")
    capacity_kWh = data.get("capacity_kWh")

    if not battery_type or not capacity_kWh:
        return error_response("Both 'type' and 'capacity_kWh' are required.")

    new_battery = {
        "id": len(batteries) + 1,
        "type": battery_type,
        "capacity_kWh": capacity_kWh,
        "status": "Available"
    }
    batteries.append(new_battery)

    return jsonify({"message": "Battery registered successfully.", "battery": new_battery}), 201

# Endpoint: Health check
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Check the health status of the API.
    """
    return jsonify({"status": "OK"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
