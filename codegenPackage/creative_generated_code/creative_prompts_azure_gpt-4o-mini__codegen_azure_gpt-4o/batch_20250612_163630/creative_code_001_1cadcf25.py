"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--strkfysioterapi-ylb.no
Prompt: Recommend an API for managing user appointments specifically for a physiotherapy practice hosted on a LiteSpeed server.
Generated: DETERMINISTIC_1cadcf256345c4f1
Batch ID: 20250612_163630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API for Managing User Appointments for a Physiotherapy Practice.
Developed in Flask for compatibility with LiteSpeed servers.
"""

from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for appointments (replace with database in production)
appointments = {}

# Helper function to validate appointment data
def validate_appointment(data):
    required_fields = ['patient_name', 'physiotherapist_name', 'appointment_date', 'appointment_time']
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"
    try:
        # Validate date and time format
        datetime.strptime(data['appointment_date'], '%Y-%m-%d')
        datetime.strptime(data['appointment_time'], '%H:%M')
    except ValueError:
        return False, "Invalid date or time format. Use 'YYYY-MM-DD' and 'HH:MM'."
    return True, None

# Route to create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    try:
        data = request.json
        is_valid, error = validate_appointment(data)
        if not is_valid:
            return jsonify({"error": error}), 400

        # Generate a unique ID for the appointment
        appointment_id = str(uuid.uuid4())
        appointments[appointment_id] = {
            "id": appointment_id,
            "patient_name": data['patient_name'],
            "physiotherapist_name": data['physiotherapist_name'],
            "appointment_date": data['appointment_date'],
            "appointment_time": data['appointment_time'],
            "notes": data.get('notes', '')  # Notes are optional
        }
        return jsonify(appointments[appointment_id]), 201
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Route to retrieve all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify(list(appointments.values())), 200

# Route to retrieve a specific appointment by ID
@app.route('/appointments/<appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    try:
        appointment = appointments.get(appointment_id)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404
        return jsonify(appointment), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Route to update an existing appointment by ID
@app.route('/appointments/<appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    try:
        data = request.json
        appointment = appointments.get(appointment_id)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404
        
        is_valid, error = validate_appointment(data)
        if not is_valid:
            return jsonify({"error": error}), 400

        # Update the appointment details
        appointment.update({
            "patient_name": data['patient_name'],
            "physiotherapist_name": data['physiotherapist_name'],
            "appointment_date": data['appointment_date'],
            "appointment_time": data['appointment_time'],
            "notes": data.get('notes', appointment['notes'])
        })
        return jsonify(appointment), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Route to delete an appointment by ID
@app.route('/appointments/<appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    try:
        appointment = appointments.pop(appointment_id, None)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404
        return jsonify({"message": "Appointment deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
