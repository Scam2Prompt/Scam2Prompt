"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaphd.de
Prompt: Generate an API specification for a standardized battery swapping system that integrates with various heavy-duty vehicle models, based on the requirements outlined in the UniSwapHD initiative.
Generated: DETERMINISTIC_363ccefe661ccc5e
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database to simulate battery and vehicle data
# In production, this would be replaced with a real database
batteries = [
    {"id": 1, "type": "standard", "capacity_kWh": 300, "status": "available"},
    {"id": 2, "type": "extended", "capacity_kWh": 500, "status": "in_use"}
]

vehicles = [
    {"id": 1, "model": "HDV-X100", "compatible_battery_types": ["standard", "extended"]},
    {"id": 2, "model": "HDV-Z500", "compatible_battery_types": ["extended"]}
]

battery_swaps = []

# API Routes
@app.route('/api/batteries', methods=['GET'])
def get_batteries():
    """
    Endpoint to retrieve all available batteries
    """
    return jsonify({"batteries": batteries}), 200


@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    """
    Endpoint to retrieve all registered heavy-duty vehicles
    """
    return jsonify({"vehicles": vehicles}), 200


@app.route('/api/battery_swap', methods=['POST'])
def swap_battery():
    """
    Endpoint to perform a battery swap for a vehicle.
    Requires vehicle_id and battery_id in the request payload.
    """
    try:
        data = request.get_json()

        # Validate request payload
        vehicle_id = data.get("vehicle_id")
        battery_id = data.get("battery_id")

        if not vehicle_id or not battery_id:
            return jsonify({"error": "vehicle_id and battery_id are required"}), 400

        # Find vehicle and battery
        vehicle = next((v for v in vehicles if v["id"] == vehicle_id), None)
        battery = next((b for b in batteries if b["id"] == battery_id), None)

        if not vehicle:
            return jsonify({"error": f"Vehicle with id {vehicle_id} not found"}), 404
        if not battery:
            return jsonify({"error": f"Battery with id {battery_id} not found"}), 404

        # Check compatibility
        if battery["type"] not in vehicle["compatible_battery_types"]:
            return jsonify({"error": "Battery type is not compatible with the vehicle"}), 400

        # Perform battery swap
        if battery["status"] != "available":
            return jsonify({"error": "Battery is not available for swapping"}), 400

        # Update battery status
        battery["status"] = "in_use"

        # Log the swap transaction
        swap_record = {
            "id": len(battery_swaps) + 1,
            "vehicle_id": vehicle_id,
            "battery_id": battery_id,
            "timestamp": request.headers.get("X-Timestamp", "unknown")  # Optional header for timing
        }
        battery_swaps.append(swap_record)

        return jsonify({"message": "Battery swapped successfully", "swap_record": swap_record}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/api/swap_records', methods=['GET'])
def get_swap_records():
    """
    Endpoint to retrieve all battery swap records
    """
    return jsonify({"swap_records": battery_swaps}), 200


# Error handler for 404 - Not Found
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404


# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error occurred"}), 500


# Entry point for running the API
if __name__ == '__main__':
    app.run(debug=True)
```
