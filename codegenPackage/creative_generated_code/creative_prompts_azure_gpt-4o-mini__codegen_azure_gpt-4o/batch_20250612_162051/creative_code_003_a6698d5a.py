"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Provide an example of an API that can be used to monitor energy consumption in real-time, similar to the systems recommended by Digar Green for enhancing energy self-sufficiency.
Generated: DETERMINISTIC_a6698d5a6ff81ac1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import datetime
import random

app = Flask(__name__)

# Simulated energy data for demonstration purposes
energy_data = {
    "device_1": {"name": "Solar Panel 1", "type": "solar", "watts": random.uniform(500, 1500)},
    "device_2": {"name": "Wind Turbine 1", "type": "wind", "watts": random.uniform(800, 2000)},
    "device_3": {"name": "Battery Backup", "type": "battery", "watts": random.uniform(200, 500)},
}

# Error messages for validation
ERROR_MESSAGES = {
    "device_not_found": "Device not found. Please check the device ID.",
    "invalid_request": "Invalid request. Please provide valid query parameters.",
}


@app.route('/api/energy-monitor', methods=['GET'])
def energy_monitor():
    """
    Endpoint for monitoring energy consumption in real-time.
    Returns energy data for all devices or a specific device if a device_id is provided.

    Query Parameters:
        device_id (optional): ID of the device to fetch energy data for.

    Returns:
        JSON response containing energy consumption data.
    """
    try:
        # Get the optional device_id parameter from the query string
        device_id = request.args.get('device_id')

        if device_id:
            # If device_id is provided, fetch and return specific device data
            if device_id in energy_data:
                response = {
                    "timestamp": datetime.datetime.now().isoformat(),
                    "device": energy_data[device_id],
                }
                return jsonify(response), 200
            else:
                # Return error if device_id is invalid
                return jsonify({"error": ERROR_MESSAGES["device_not_found"]}), 404
        else:
            # If no device_id is provided, return all device data
            response = {
                "timestamp": datetime.datetime.now().isoformat(),
                "devices": energy_data,
            }
            return jsonify(response), 200
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500


@app.route('/api/energy-monitor/add-device', methods=['POST'])
def add_device():
    """
    Endpoint for adding a new energy monitoring device.

    Request Body:
        JSON object containing:
            device_id: Unique identifier for the new device.
            name: Name of the device.
            type: Type of the device (e.g., solar, wind, battery).
            watts: Initial energy consumption in watts.

    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.get_json()
        device_id = data.get("device_id")
        name = data.get("name")
        device_type = data.get("type")
        watts = data.get("watts")

        # Validate the input data
        if not device_id or not name or not device_type or not watts:
            return jsonify({"error": ERROR_MESSAGES["invalid_request"]}), 400

        # Check if the device_id already exists
        if device_id in energy_data:
            return jsonify({"error": "Device ID already exists."}), 400

        # Add the new device to the energy_data dictionary
        energy_data[device_id] = {
            "name": name,
            "type": device_type,
            "watts": watts,
        }

        return jsonify({"message": "Device added successfully."}), 201
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500


@app.route('/api/energy-monitor/remove-device', methods=['DELETE'])
def remove_device():
    """
    Endpoint for removing an existing energy monitoring device.

    Query Parameters:
        device_id: ID of the device to remove.

    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Get the device_id parameter from the query string
        device_id = request.args.get("device_id")

        if not device_id:
            return jsonify({"error": ERROR_MESSAGES["invalid_request"]}), 400

        # Check if the device exists
        if device_id in energy_data:
            del energy_data[device_id]
            return jsonify({"message": "Device removed successfully."}), 200
        else:
            return jsonify({"error": ERROR_MESSAGES["device_not_found"]}), 404
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500


# Main entry point to run the Flask application
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
```
