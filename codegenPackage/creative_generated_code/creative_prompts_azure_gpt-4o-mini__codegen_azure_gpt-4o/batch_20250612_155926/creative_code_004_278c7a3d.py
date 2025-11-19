"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecoswap.us
Prompt: Suggest a RESTful API design for EcoSwap to enable users to check the availability of specific Apple devices in real-time.
Generated: DETERMINISTIC_278c7a3dac1e4182
Batch ID: 20250612_155926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Mock data for Apple devices availability
# In a production system, this data would come from a database
devices_availability = [
    {"id": 1, "name": "iPhone 14 Pro", "available": True, "quantity": 15},
    {"id": 2, "name": "MacBook Pro 16\"", "available": True, "quantity": 8},
    {"id": 3, "name": "iPad Air", "available": False, "quantity": 0},
    {"id": 4, "name": "Apple Watch Series 8", "available": True, "quantity": 10},
]

# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handles HTTP exceptions."""
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": str(e)})
    response.content_type = "application/json"
    return response

# Custom error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handles generic exceptions."""
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route for checking availability of specific Apple devices
@app.route("/api/devices", methods=["GET"])
def get_devices():
    """
    Returns the list of all Apple devices and their availability.

    Endpoint: /api/devices
    Method: GET
    Response: JSON object containing details for all Apple devices.
    """
    return jsonify({"devices": devices_availability}), 200

@app.route("/api/devices/<int:device_id>", methods=["GET"])
def get_device_by_id(device_id):
    """
    Returns the availability of a specific Apple device.

    Endpoint: /api/devices/<device_id>
    Method: GET
    Parameters:
        device_id (int): ID of the device to check availability for.
    Response: JSON object containing details for the requested device.
    """
    # Search for the device by ID
    device = next((d for d in devices_availability if d["id"] == device_id), None)

    if device:
        return jsonify(device), 200
    else:
        # Handle case where device is not found
        return jsonify({"error": "Device not found"}), 404

# Main entry point
if __name__ == "__main__":
    # Run the application
    # In production, use a more robust server (e.g., Gunicorn or uWSGI)
    app.run(debug=True, host="0.0.0.0", port=5000)
```
