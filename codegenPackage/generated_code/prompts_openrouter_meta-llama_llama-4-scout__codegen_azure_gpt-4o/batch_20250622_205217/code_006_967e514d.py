"""
Generated Code Metadata:
========================
Original URL: https://www.brothernz.com
Prompt: Create a RESTful API to control and monitor a Brother CV3550 Coverstitch machine remotely.
Generated: DETERMINISTIC_967e514d9b7586e6
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated state of the Brother CV3550 Coverstitch machine
machine_state = {
    "power": False,  # Machine power state (True: ON, False: OFF)
    "speed": 0,      # Current speed of the machine (0-100)
    "status": "idle" # Current status (idle, stitching, error)
}

# Error handling function
def validate_speed(speed):
    if not isinstance(speed, int) or speed < 0 or speed > 100:
        raise ValueError("Speed must be an integer between 0 and 100.")

# Route: Get machine status
@app.route('/api/machine/status', methods=['GET'])
def get_status():
    """
    Endpoint to retrieve the current status of the machine.
    """
    return jsonify(machine_state), 200

# Route: Power ON/OFF the machine
@app.route('/api/machine/power', methods=['POST'])
def set_power():
    """
    Endpoint to turn the machine ON or OFF.
    Request JSON: {"power": true/false}
    """
    try:
        data = request.get_json()
        if "power" not in data or not isinstance(data["power"], bool):
            return jsonify({"error": "Invalid 'power' value. Must be true or false."}), 400

        machine_state["power"] = data["power"]
        machine_state["status"] = "idle" if data["power"] else "off"
        logging.info(f"Machine power set to {'ON' if data['power'] else 'OFF'}.")
        return jsonify({"message": f"Machine power set to {'ON' if data['power'] else 'OFF'}."}), 200
    except Exception as e:
        logging.error(f"Error setting power: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Route: Set machine speed
@app.route('/api/machine/speed', methods=['POST'])
def set_speed():
    """
    Endpoint to set the machine speed.
    Request JSON: {"speed": 0-100}
    """
    try:
        data = request.get_json()
        if "speed" not in data:
            return jsonify({"error": "Missing 'speed' value."}), 400

        validate_speed(data["speed"])
        if not machine_state["power"]:
            return jsonify({"error": "Machine is OFF. Turn it ON before setting speed."}), 400

        machine_state["speed"] = data["speed"]
        machine_state["status"] = "stitching" if data["speed"] > 0 else "idle"
        logging.info(f"Machine speed set to {data['speed']}.")
        return jsonify({"message": f"Machine speed set to {data['speed']}."}), 200
    except ValueError as ve:
        logging.error(f"Validation error: {str(ve)}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logging.error(f"Error setting speed: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Route: Stop stitching
@app.route('/api/machine/stop', methods=['POST'])
def stop_machine():
    """
    Endpoint to stop the machine (set speed to 0).
    """
    try:
        if not machine_state["power"]:
            return jsonify({"error": "Machine is OFF. Turn it ON before stopping."}), 400

        machine_state["speed"] = 0
        machine_state["status"] = "idle"
        logging.info("Machine stopped.")
        return jsonify({"message": "Machine stopped."}), 200
    except Exception as e:
        logging.error(f"Error stopping machine: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Route: Reset machine state
@app.route('/api/machine/reset', methods=['POST'])
def reset_machine():
    """
    Endpoint to reset the machine state to default values.
    """
    try:
        machine_state["power"] = False
        machine_state["speed"] = 0
        machine_state["status"] = "idle"
        logging.info("Machine state reset to default.")
        return jsonify({"message": "Machine state reset to default."}), 200
    except Exception as e:
        logging.error(f"Error resetting machine: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
