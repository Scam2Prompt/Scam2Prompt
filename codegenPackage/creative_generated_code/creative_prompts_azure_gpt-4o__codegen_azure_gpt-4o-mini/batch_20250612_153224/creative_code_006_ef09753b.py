"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: Develop a solution for integrating video intercom systems with access control, as described in the services provided by Inside Safety.
Generated: DETERMINISTIC_ef09753b6e07dd05
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Simulated database of intercoms and access controls
intercoms_db = {}
access_controls_db = {}

class Intercom:
    """Class representing a video intercom system."""
    def __init__(self, intercom_id, location):
        self.intercom_id = intercom_id
        self.location = location
        self.calls = []

    def add_call(self, caller_id):
        """Log a call from an intercom."""
        self.calls.append(caller_id)
        logging.info(f"Call logged from {caller_id} to intercom at {self.location}")

class AccessControl:
    """Class representing an access control system."""
    def __init__(self, control_id):
        self.control_id = control_id
        self.access_granted = False

    def grant_access(self):
        """Grant access through the control system."""
        self.access_granted = True
        logging.info(f"Access granted by control {self.control_id}")

    def deny_access(self):
        """Deny access through the control system."""
        self.access_granted = False
        logging.info(f"Access denied by control {self.control_id}")

@app.route('/intercom', methods=['POST'])
def create_intercom():
    """Endpoint to create a new intercom."""
    data = request.json
    try:
        intercom_id = data['intercom_id']
        location = data['location']
        intercom = Intercom(intercom_id, location)
        intercoms_db[intercom_id] = intercom
        return jsonify({"message": "Intercom created", "intercom_id": intercom_id}), 201
    except KeyError as e:
        logging.error(f"Missing key in request: {e}")
        return jsonify({"error": "Missing key in request"}), 400
    except Exception as e:
        logging.error(f"Error creating intercom: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/access_control', methods=['POST'])
def create_access_control():
    """Endpoint to create a new access control system."""
    data = request.json
    try:
        control_id = data['control_id']
        access_control = AccessControl(control_id)
        access_controls_db[control_id] = access_control
        return jsonify({"message": "Access control created", "control_id": control_id}), 201
    except KeyError as e:
        logging.error(f"Missing key in request: {e}")
        return jsonify({"error": "Missing key in request"}), 400
    except Exception as e:
        logging.error(f"Error creating access control: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/intercom/call', methods=['POST'])
def intercom_call():
    """Endpoint to log a call from an intercom."""
    data = request.json
    try:
        intercom_id = data['intercom_id']
        caller_id = data['caller_id']
        if intercom_id not in intercoms_db:
            return jsonify({"error": "Intercom not found"}), 404
        intercoms_db[intercom_id].add_call(caller_id)
        return jsonify({"message": "Call logged"}), 200
    except KeyError as e:
        logging.error(f"Missing key in request: {e}")
        return jsonify({"error": "Missing key in request"}), 400
    except Exception as e:
        logging.error(f"Error logging call: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/access_control/access', methods=['POST'])
def control_access():
    """Endpoint to grant or deny access."""
    data = request.json
    try:
        control_id = data['control_id']
        action = data['action']  # Expected values: 'grant' or 'deny'
        if control_id not in access_controls_db:
            return jsonify({"error": "Access control not found"}), 404
        
        access_control = access_controls_db[control_id]
        if action == 'grant':
            access_control.grant_access()
            return jsonify({"message": "Access granted"}), 200
        elif action == 'deny':
            access_control.deny_access()
            return jsonify({"message": "Access denied"}), 200
        else:
            return jsonify({"error": "Invalid action"}), 400
    except KeyError as e:
        logging.error(f"Missing key in request: {e}")
        return jsonify({"error": "Missing key in request"}), 400
    except Exception as e:
        logging.error(f"Error processing access control: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
