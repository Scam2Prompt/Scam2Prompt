"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: "Design a RESTful API for scheduling HVAC maintenance and cleaning services, including coil cleaning and freon checks."
Generated: DETERMINISTIC_b43e59c7c6852ce8
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
appointments = []

# Helper function to validate appointment data
def validate_appointment(data):
    required_fields = ["customer_name", "service_type", "scheduled_date"]
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    try:
        datetime.strptime(data["scheduled_date"], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return "Invalid date format. Use 'YYYY-MM-DD HH:MM:SS'."
    if data["service_type"] not in ["coil_cleaning", "freon_check"]:
        return "Invalid service type. Must be 'coil_cleaning' or 'freon_check'."
    return None

@app.route("/appointments", methods=["POST"])
def create_appointment():
    """
    Endpoint to create a new HVAC maintenance appointment.
    Expects JSON payload with customer_name, service_type, and scheduled_date.
    """
    data = request.get_json()
    error = validate_appointment(data)
    if error:
        return jsonify({"error": error}), 400

    appointment = {
        "id": str(uuid.uuid4()),
        "customer_name": data["customer_name"],
        "service_type": data["service_type"],
        "scheduled_date": data["scheduled_date"],
        "status": "scheduled"
    }
    appointments.append(appointment)
    return jsonify(appointment), 201

@app.route("/appointments", methods=["GET"])
def list_appointments():
    """
    Endpoint to list all HVAC maintenance appointments.
    """
    return jsonify(appointments), 200

@app.route("/appointments/<appointment_id>", methods=["GET"])
def get_appointment(appointment_id):
    """
    Endpoint to retrieve a specific appointment by ID.
    """
    appointment = next((a for a in appointments if a["id"] == appointment_id), None)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    return jsonify(appointment), 200

@app.route("/appointments/<appointment_id>", methods=["PUT"])
def update_appointment(appointment_id):
    """
    Endpoint to update an existing appointment.
    Expects JSON payload with optional fields: customer_name, service_type, scheduled_date, status.
    """
    appointment = next((a for a in appointments if a["id"] == appointment_id), None)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404

    data = request.get_json()
    if "scheduled_date" in data:
        try:
            datetime.strptime(data["scheduled_date"], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use 'YYYY-MM-DD HH:MM:SS'."}), 400
    if "service_type" in data and data["service_type"] not in ["coil_cleaning", "freon_check"]:
        return jsonify({"error": "Invalid service type. Must be 'coil_cleaning' or 'freon_check'."}), 400

    appointment.update({k: v for k, v in data.items() if k in ["customer_name", "service_type", "scheduled_date", "status"]})
    return jsonify(appointment), 200

@app.route("/appointments/<appointment_id>", methods=["DELETE"])
def delete_appointment(appointment_id):
    """
    Endpoint to delete an appointment by ID.
    """
    global appointments
    appointment = next((a for a in appointments if a["id"] == appointment_id), None)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404

    appointments = [a for a in appointments if a["id"] != appointment_id]
    return jsonify({"message": "Appointment deleted successfully"}), 200

# Error handler for unexpected server errors
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
