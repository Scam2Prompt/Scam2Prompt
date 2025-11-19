"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centroabakadabra.com
Prompt: Develop a RESTful API specification for a healthcare service that includes endpoints for scheduling appointments and managing patient information at a center like Centro Abakadabra.
Generated: DETERMINISTIC_8383af7b887053ee
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (for demonstration purposes)
patients = {}
appointments = {}

# Error handler for 404 - Endpoint Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400 - Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Endpoint: Get all patients
@app.route('/patients', methods=['GET'])
def get_all_patients():
    """
    Get a list of all registered patients.
    Returns:
        JSON: A dictionary of all patients.
    """
    return jsonify({"patients": patients}), 200

# Endpoint: Add a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    """
    Add a new patient to the system.
    Request Body:
        JSON: { "id": str, "name": str, "age": int, "contact": str }
    Returns:
        JSON: Message indicating success or failure.
    """
    data = request.json
    if not data or 'id' not in data or 'name' not in data or 'age' not in data or 'contact' not in data:
        return jsonify({"error": "Invalid patient data"}), 400

    patient_id = data['id']
    if patient_id in patients:
        return jsonify({"error": "Patient with this ID already exists"}), 400

    patients[patient_id] = {
        "name": data['name'],
        "age": data['age'],
        "contact": data['contact']
    }
    return jsonify({"message": "Patient added successfully"}), 201

# Endpoint: Get patient information by ID
@app.route('/patients/<string:patient_id>', methods=['GET'])
def get_patient(patient_id):
    """
    Get information of a specific patient by ID.
    URL Parameter:
        patient_id (str): The unique ID of the patient.
    Returns:
        JSON: Patient information or error message.
    """
    patient = patients.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    return jsonify({"patient": patient}), 200

# Endpoint: Schedule an appointment
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    """
    Schedule an appointment for a patient.
    Request Body:
        JSON: { "appointment_id": str, "patient_id": str, "date": str, "time": str, "doctor": str }
    Returns:
        JSON: Message indicating success or failure.
    """
    data = request.json
    if not data or 'appointment_id' not in data or 'patient_id' not in data or 'date' not in data or 'time' not in data or 'doctor' not in data:
        return jsonify({"error": "Invalid appointment data"}), 400

    appointment_id = data['appointment_id']
    if appointment_id in appointments:
        return jsonify({"error": "Appointment with this ID already exists"}), 400

    patient_id = data['patient_id']
    if patient_id not in patients:
        return jsonify({"error": "Patient does not exist"}), 404

    appointments[appointment_id] = {
        "patient_id": patient_id,
        "date": data['date'],
        "time": data['time'],
        "doctor": data['doctor']
    }
    return jsonify({"message": "Appointment scheduled successfully"}), 201

# Endpoint: Get all appointments
@app.route('/appointments', methods=['GET'])
def get_all_appointments():
    """
    Get a list of all scheduled appointments.
    Returns:
        JSON: A dictionary of all appointments.
    """
    return jsonify({"appointments": appointments}), 200

# Endpoint: Get appointment details by ID
@app.route('/appointments/<string:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    """
    Get details of a specific appointment by ID.
    URL Parameter:
        appointment_id (str): The unique ID of the appointment.
    Returns:
        JSON: Appointment information or error message.
    """
    appointment = appointments.get(appointment_id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404

    return jsonify({"appointment": appointment}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
