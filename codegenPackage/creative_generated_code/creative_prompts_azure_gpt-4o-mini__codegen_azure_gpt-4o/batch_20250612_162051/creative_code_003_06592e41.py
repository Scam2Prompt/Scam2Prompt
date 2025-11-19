"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vigilanciadomotica.es
Prompt: Provide a code example for integrating virtual assistants into a smart home system, based on the insights from the "Asistentes Virtuales" section.
Generated: DETERMINISTIC_06592e41d3e8f442
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready Python code for integrating virtual assistants into a smart home system. This example uses the Flask framework to simulate a smart home API, with endpoints for controlling devices and integrating virtual assistants:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Smart home device states
smart_home_devices = {
    "lights": {"status": "off"},
    "thermostat": {"temperature": 22},
    "door_lock": {"status": "locked"}
}

# Error handler for invalid requests
@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Invalid request", "details": str(error)}), 400

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found", "details": str(error)}), 404

# Endpoint to change the state of smart home devices
@app.route('/api/v1/device/<device_name>', methods=['POST'])
def control_device(device_name):
    if device_name not in smart_home_devices:
        return jsonify({"error": "Device not found"}), 404

    try:
        # Parse JSON input
        data = request.json
        if not data:
            raise ValueError("Request body must contain JSON data")

        # Update device state
        if device_name == "lights":
            smart_home_devices["lights"]["status"] = data.get("status", "off")
        elif device_name == "thermostat":
            smart_home_devices["thermostat"]["temperature"] = data.get("temperature", 22)
        elif device_name == "door_lock":
            smart_home_devices["door_lock"]["status"] = data.get("status", "locked")
        else:
            raise ValueError(f"Unsupported operation for device: {device_name}")

        # Return updated state
        return jsonify({"device": device_name, "state": smart_home_devices[device_name]})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to retrieve the current state of smart home devices
@app.route('/api/v1/device/<device_name>', methods=['GET'])
def get_device_state(device_name):
    if device_name not in smart_home_devices:
        return jsonify({"error": "Device not found"}), 404

    # Return the current state of the device
    return jsonify({"device": device_name, "state": smart_home_devices[device_name]})

# Simulated integration with virtual assistants (e.g., Alexa/Google Assistant)
@app.route('/api/v1/assistant/command', methods=['POST'])
def virtual_assistant_integration():
    try:
        data = request.json
        if not data:
            raise ValueError("Request body must contain JSON data")

        # Extract command and device from the assistant's request
        command = data.get("command")
        device_name = data.get("device_name")

        if device_name not in smart_home_devices:
            return jsonify({"error": "Device not found"}), 404

        if command == "turn on lights":
            smart_home_devices["lights"]["status"] = "on"
        elif command == "turn off lights":
            smart_home_devices["lights"]["status"] = "off"
        elif command == "set thermostat":
            temperature = data.get("temperature")
            if temperature is None:
                raise ValueError("Temperature value is required for thermostat")
            smart_home_devices["thermostat"]["temperature"] = temperature
        elif command == "lock door":
            smart_home_devices["door_lock"]["status"] = "locked"
        elif command == "unlock door":
            smart_home_devices["door_lock"]["status"] = "unlocked"
        else:
            return jsonify({"error": "Unsupported command"}), 400

        # Return confirmation of the command
        return jsonify({"success": True, "device": device_name, "updated_state": smart_home_devices[device_name]})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Main entry point for running the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

Make sure to install Flask before running the code:
```bash
pip install flask
```
