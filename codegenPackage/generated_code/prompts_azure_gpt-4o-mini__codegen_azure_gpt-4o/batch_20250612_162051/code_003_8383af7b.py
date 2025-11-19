"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Develop a RESTful API specification for a healthcare service that includes endpoints for scheduling appointments and managing patient information at a center like Centro Abakadabra.
Generated: DETERMINISTIC_8383af7b887053ee
Batch ID: 20250612_162051
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

# In-memory data storage for demonstration purposes
patients = {}
appointments = {}

# Helper function to generate unique IDs
def generate_id(data_store):
    return str(len(data_store) + 1)

# Endpoint: Create a new patient
@app.route('/patients', methods=['POST'])
def create_patient():
    """
    Create a new patient record.
    Request Body:
    {
        "name": "John Doe",
        "age": 30,
        "gender": "Male",
        "contact": "123-456-7890"
    }
    """
    try:
        data = request.json
        if not data or not all(key in data for key in ['name', 'age', 'gender', 'contact']):
            return jsonify({"error": "Invalid input"}), 400

        patient_id = generate_id(patients)
        patients[patient_id] = {
            "id": patient_id,
            "name": data['name'],
            "age": data['age'],
            "gender": data['gender'],
            "contact": data['contact']
        }
        return jsonify(patients[patient_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Get patient information
@app.route('/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    """
    Retrieve patient information by ID.
    """
    try:
        patient = patients.get(patient_id)
        if not patient:
            return jsonify({"error": "Patient not found"}), 404
        return jsonify(patient), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Schedule an appointment
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    """
    Schedule a new appointment.
    Request Body:
    {
        "patient_id": "1",
        "date": "2023-10-01",
        "time": "10:00 AM",
        "reason": "Routine Checkup"
    }
    """
    try:
        data = request.json
        if not data or not all(key in data for key in ['patient_id', 'date', 'time', 'reason']):
            return jsonify({"error": "Invalid input"}), 400

        if data['patient_id'] not in patients:
            return jsonify({"error": "Patient not found"}), 404

        appointment_id = generate_id(appointments)
        appointments[appointment_id] = {
            "id": appointment_id,
            "patient_id": data['patient_id'],
            "date": data['date'],
            "time": data['time'],
            "reason": data['reason']
        }
        return jsonify(appointments[appointment_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Get appointment information
@app.route('/appointments/<appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    """
    Retrieve appointment information by ID.
    """
    try:
        appointment = appointments.get(appointment_id)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404
        return jsonify(appointment), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: List all appointments for a patient
@app.route('/patients/<patient_id>/appointments', methods=['GET'])
def list_patient_appointments(patient_id):
    """
    List all appointments for a specific patient.
    """
    try:
        if patient_id not in patients:
            return jsonify({"error": "Patient not found"}), 404

        patient_appointments = [
            appointment for appointment in appointments.values()
            if appointment['patient_id'] == patient_id
        ]
        return jsonify(patient_appointments), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
