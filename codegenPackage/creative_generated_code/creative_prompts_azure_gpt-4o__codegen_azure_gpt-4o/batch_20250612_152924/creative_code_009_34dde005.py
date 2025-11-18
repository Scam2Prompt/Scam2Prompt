"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Create a REST API for scheduling meetings and consultations for glass and aluminum project assessments, inspired by CristalesGraf's customer service model.
Generated: DETERMINISTIC_34dde005b5933de7
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for meetings and consultations
appointments = []

# Helper function to validate appointment data
def validate_appointment(data):
    required_fields = ['name', 'email', 'phone', 'project_type', 'date', 'time']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    try:
        datetime.strptime(data['date'], '%Y-%m-%d')
        datetime.strptime(data['time'], '%H:%M')
    except ValueError:
        return False, "Invalid date or time format"
    return True, None

@app.route('/api/appointments', methods=['POST'])
def schedule_appointment():
    """
    Endpoint to schedule a new meeting or consultation.

    Request Body:
    {
        "name": String (required),
        "email": String (required),
        "phone": String (required),
        "project_type": String (required),
        "date": String (YYYY-MM-DD, required),
        "time": String (HH:MM, required),
        "additional_notes": String (optional)
    }

    Response:
    - 201: Appointment created successfully
    - 400: Invalid input data
    """
    try:
        data = request.json
        is_valid, error_message = validate_appointment(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400
        
        appointment = {
            "id": str(uuid.uuid4()),
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "project_type": data['project_type'],
            "date": data['date'],
            "time": data['time'],
            "additional_notes": data.get('additional_notes', ''),
            "created_at": datetime.utcnow().isoformat()
        }
        appointments.append(appointment)
        return jsonify({"message": "Appointment scheduled successfully", "appointment": appointment}), 201
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/api/appointments', methods=['GET'])
def list_appointments():
    """
    Endpoint to retrieve all scheduled appointments.

    Response:
    - 200: List of all appointments
    """
    try:
        return jsonify({"appointments": appointments}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/api/appointments/<appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    """
    Endpoint to retrieve a specific appointment by ID.

    Response:
    - 200: Appointment details
    - 404: Appointment not found
    """
    try:
        appointment = next((appt for appt in appointments if appt['id'] == appointment_id), None)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404
        return jsonify({"appointment": appointment}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/api/appointments/<appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    """
    Endpoint to delete a specific appointment by ID.

    Response:
    - 200: Appointment deleted successfully
    - 404: Appointment not found
    """
    try:
        global appointments
        appointment = next((appt for appt in appointments if appt['id'] == appointment_id), None)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404
        
        appointments = [appt for appt in appointments if appt['id'] != appointment_id]
        return jsonify({"message": "Appointment deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
