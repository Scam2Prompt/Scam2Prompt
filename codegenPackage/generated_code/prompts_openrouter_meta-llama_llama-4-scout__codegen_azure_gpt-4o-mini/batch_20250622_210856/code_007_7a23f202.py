"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: "Develop a BMS (Building Management System) for a smart building using Payesh Niroo's electrical panels and equipment."
Generated: DETERMINISTIC_7a23f20271b82bf5
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample data structure to hold equipment status
equipment_status = {
    "lights": False,
    "heating": False,
    "cooling": False,
    "security": False
}

# Error handling for JSON parsing
def parse_json(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}")
        return None

# Route to get the current status of the equipment
@app.route('/status', methods=['GET'])
def get_status():
    """Get the current status of all equipment."""
    return jsonify(equipment_status)

# Route to update the status of the equipment
@app.route('/update', methods=['POST'])
def update_status():
    """Update the status of the equipment based on the provided JSON payload."""
    data = request.data
    parsed_data = parse_json(data)

    if parsed_data is None:
        return jsonify({"error": "Invalid JSON format"}), 400

    # Update equipment status based on the parsed data
    for key, value in parsed_data.items():
        if key in equipment_status and isinstance(value, bool):
            equipment_status[key] = value
        else:
            logging.warning(f"Invalid key or value: {key}: {value}")

    return jsonify({"message": "Status updated successfully", "status": equipment_status})

# Route to reset all equipment to default state
@app.route('/reset', methods=['POST'])
def reset_status():
    """Reset all equipment to their default state (off)."""
    for key in equipment_status.keys():
        equipment_status[key] = False
    return jsonify({"message": "All equipment reset to default state", "status": equipment_status})

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Requirements
- Ensure you have Flask installed in your environment. You can install it using:
  ```bash
  pip install Flask
  ```
- Run the application and access the endpoints:
  - `GET /status` to retrieve the current status of the equipment.
  - `POST /update` with a JSON payload to update the status (e.g., `{"lights": true, "heating": false}`).
  - `POST /reset` to reset all equipment to the default state.
