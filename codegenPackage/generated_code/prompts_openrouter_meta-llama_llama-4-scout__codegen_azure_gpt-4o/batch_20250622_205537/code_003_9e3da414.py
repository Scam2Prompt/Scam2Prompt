"""
Generated Code Metadata:
========================
Original URL: https://safesteth.com
Prompt: Create a RESTful API endpoint for managing appointments and emergencies, inspired by the services provided on SafeSteth.com.
Generated: DETERMINISTIC_9e3da41457903e97
Batch ID: 20250622_205537
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

# In-memory storage for appointments and emergencies
appointments = []
emergencies = []

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Helper function to validate appointment data
def validate_appointment(data):
    required_fields = ['patient_name', 'doctor_name', 'appointment_time']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    try:
        datetime.strptime(data['appointment_time'], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return False, "Invalid date format for appointment_time. Use 'YYYY-MM-DD HH:MM:SS'."
    return True, None

# Endpoint to create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    try:
        data = request.json
        is_valid, error_message = validate_appointment(data)
        if not is_valid:
            return jsonify({'error': error_message}), 400

        appointment = {
            'id': generate_id(),
            'patient_name': data['patient_name'],
            'doctor_name': data['doctor_name'],
            'appointment_time': data['appointment_time'],
            'created_at': datetime.now().isoformat()
        }
        appointments.append(appointment)
        return jsonify({'message': 'Appointment created successfully', 'appointment': appointment}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the appointment', 'details': str(e)}), 500

# Endpoint to list all appointments
@app.route('/appointments', methods=['GET'])
def list_appointments():
    return jsonify({'appointments': appointments}), 200

# Endpoint to create a new emergency
@app.route('/emergencies', methods=['POST'])
def create_emergency():
    try:
        data = request.json
        if 'description' not in data or 'patient_name' not in data:
            return jsonify({'error': 'Missing required fields: description, patient_name'}), 400

        emergency = {
            'id': generate_id(),
            'patient_name': data['patient_name'],
            'description': data['description'],
            'reported_at': datetime.now().isoformat()
        }
        emergencies.append(emergency)
        return jsonify({'message': 'Emergency reported successfully', 'emergency': emergency}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred while reporting the emergency', 'details': str(e)}), 500

# Endpoint to list all emergencies
@app.route('/emergencies', methods=['GET'])
def list_emergencies():
    return jsonify({'emergencies': emergencies}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal server error occurred'}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
