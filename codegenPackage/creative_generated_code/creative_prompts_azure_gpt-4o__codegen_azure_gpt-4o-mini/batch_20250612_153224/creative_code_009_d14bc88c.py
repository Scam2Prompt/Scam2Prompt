"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Recommend libraries or APIs for managing online and onsite repair appointments, and write a sample implementation based on the services described by Geeks On Repair.
Generated: DETERMINISTIC_d14bc88ce05ab546
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
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample data structure to hold appointments
appointments = []

# Create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    try:
        data = request.json

        # Validate the incoming data
        if not all(key in data for key in ('service_type', 'customer_name', 'date', 'time', 'location')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Validate the date and time format
        appointment_datetime = f"{data['date']} {data['time']}"
        datetime.strptime(appointment_datetime, '%Y-%m-%d %H:%M')

        # Create a new appointment entry
        appointment = {
            'id': len(appointments) + 1,
            'service_type': data['service_type'],
            'customer_name': data['customer_name'],
            'date': data['date'],
            'time': data['time'],
            'location': data['location'],
        }

        appointments.append(appointment)
        return jsonify({'message': 'Appointment created successfully', 'appointment': appointment}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the appointment'}), 500

# Get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify(appointments), 200

# Get an appointment by its ID
@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = next((appt for appt in appointments if appt['id'] == appointment_id), None)
    if appointment:
        return jsonify(appointment), 200
    else:
        return jsonify({'error': 'Appointment not found'}), 404

# Delete an appointment
@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    global appointments
    appointments = [appt for appt in appointments if appt['id'] != appointment_id]
    return jsonify({'message': 'Appointment deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

This implementation utilizes Flask for a simple REST API that can manage online and onsite repair appointments. It includes endpoints for creating, retrieving, and deleting appointments, with error handling and input validation.
