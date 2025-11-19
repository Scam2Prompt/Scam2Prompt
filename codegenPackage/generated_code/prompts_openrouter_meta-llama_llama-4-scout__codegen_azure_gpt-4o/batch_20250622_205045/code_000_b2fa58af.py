"""
Generated Code Metadata:
========================
Original URL: https://solana2018.com
Prompt: Write a Python script to create a simple online appointment scheduling system for an整体 clinic, including fields for patient name, preferred date and time, and type of therapy session.
Generated: DETERMINISTIC_b2fa58af545c422b
Batch ID: 20250622_205045
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

app = Flask(__name__)

# In-memory database to store appointments
appointments = []

# Available therapy types
therapy_types = ["Acupuncture", "Massage Therapy", "Chiropractic", "Physical Therapy"]

# Helper function to validate date and time format
def validate_datetime(date_str, time_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

@app.route('/appointments', methods=['POST'])
def create_appointment():
    """
    Endpoint to create a new appointment.
    Expects JSON payload with 'name', 'date', 'time', and 'therapy_type'.
    """
    data = request.json

    # Validate input fields
    name = data.get('name')
    date = data.get('date')
    time = data.get('time')
    therapy_type = data.get('therapy_type')

    if not name or not date or not time or not therapy_type:
        return jsonify({"error": "All fields (name, date, time, therapy_type) are required."}), 400

    if therapy_type not in therapy_types:
        return jsonify({"error": f"Invalid therapy type. Available types: {', '.join(therapy_types)}"}), 400

    if not validate_datetime(date, time):
        return jsonify({"error": "Invalid date or time format. Date must be YYYY-MM-DD and time must be HH:MM."}), 400

    # Check for conflicting appointments
    for appointment in appointments:
        if appointment['date'] == date and appointment['time'] == time:
            return jsonify({"error": "The selected date and time are already booked."}), 409

    # Create and store the appointment
    new_appointment = {
        "id": len(appointments) + 1,
        "name": name,
        "date": date,
        "time": time,
        "therapy_type": therapy_type
    }
    appointments.append(new_appointment)

    return jsonify({"message": "Appointment created successfully.", "appointment": new_appointment}), 201

@app.route('/appointments', methods=['GET'])
def list_appointments():
    """
    Endpoint to list all appointments.
    """
    return jsonify({"appointments": appointments}), 200

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    """
    Endpoint to delete an appointment by ID.
    """
    global appointments
    appointment_to_delete = next((appt for appt in appointments if appt['id'] == appointment_id), None)

    if not appointment_to_delete:
        return jsonify({"error": "Appointment not found."}), 404

    appointments = [appt for appt in appointments if appt['id'] != appointment_id]
    return jsonify({"message": "Appointment deleted successfully."}), 200

@app.route('/therapy-types', methods=['GET'])
def list_therapy_types():
    """
    Endpoint to list all available therapy types.
    """
    return jsonify({"therapy_types": therapy_types}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
