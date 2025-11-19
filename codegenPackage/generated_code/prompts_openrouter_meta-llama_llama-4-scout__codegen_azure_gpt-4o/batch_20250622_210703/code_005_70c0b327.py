"""
Generated Code Metadata:
========================
Original URL: https://cbienetre.com
Prompt: "Design a RESTful API for a wellness center to manage appointments, including creating, updating, and canceling bookings."
Generated: DETERMINISTIC_70c0b327756907cb
Batch ID: 20250622_210703
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

# In-memory database for storing appointments
appointments = {}

# Helper function to generate unique appointment IDs
def generate_appointment_id():
    return str(len(appointments) + 1)

# Route to create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    """
    Create a new appointment.
    Request JSON should include:
    - 'name': Name of the person booking the appointment
    - 'date': Date of the appointment (YYYY-MM-DD)
    - 'time': Time of the appointment (HH:MM)
    """
    try:
        data = request.json
        name = data.get('name')
        date = data.get('date')
        time = data.get('time')

        # Validate input
        if not name or not date or not time:
            return jsonify({'error': 'Missing required fields: name, date, time'}), 400

        # Parse and validate date and time
        try:
            appointment_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            return jsonify({'error': 'Invalid date or time format'}), 400

        # Create appointment
        appointment_id = generate_appointment_id()
        appointments[appointment_id] = {
            'id': appointment_id,
            'name': name,
            'date': date,
            'time': time
        }

        return jsonify({'message': 'Appointment created successfully', 'appointment': appointments[appointment_id]}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update an existing appointment
@app.route('/appointments/<appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    """
    Update an existing appointment.
    Request JSON should include:
    - 'name': Updated name (optional)
    - 'date': Updated date (optional, YYYY-MM-DD)
    - 'time': Updated time (optional, HH:MM)
    """
    try:
        if appointment_id not in appointments:
            return jsonify({'error': 'Appointment not found'}), 404

        data = request.json
        name = data.get('name')
        date = data.get('date')
        time = data.get('time')

        # Update fields if provided
        if name:
            appointments[appointment_id]['name'] = name
        if date:
            appointments[appointment_id]['date'] = date
        if time:
            appointments[appointment_id]['time'] = time

        return jsonify({'message': 'Appointment updated successfully', 'appointment': appointments[appointment_id]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to cancel (delete) an appointment
@app.route('/appointments/<appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    """
    Cancel an appointment by its ID.
    """
    try:
        if appointment_id not in appointments:
            return jsonify({'error': 'Appointment not found'}), 404

        deleted_appointment = appointments.pop(appointment_id)
        return jsonify({'message': 'Appointment canceled successfully', 'appointment': deleted_appointment}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to list all appointments
@app.route('/appointments', methods=['GET'])
def list_appointments():
    """
    List all appointments.
    """
    try:
        return jsonify({'appointments': list(appointments.values())}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
