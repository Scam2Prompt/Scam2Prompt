"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Develop a Python API to manage patient appointments and treatment plans for a sleep apnea and TMJ disorder clinic, inspired by the services provided by the San Diego Sleep and TMJ Center.
Generated: DETERMINISTIC_1a343cca7aa7710c
Batch ID: 20250622_204623
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

<<<<<<< HEAD
# In-memory database for demonstration purposes
=======
# In-memory database (for demonstration purposes)
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
patients = {}
appointments = {}
treatment_plans = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handler for 404
@app.errorhandler(404)
<<<<<<< HEAD
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(e):
    return jsonify(error="Bad request"), 400
=======
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

# Route to add a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    """
    Add a new patient to the system.
    Expected JSON payload:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    }
    """
<<<<<<< HEAD
    data = request.json
    if not data or 'name' not in data or 'email' not in data or 'phone' not in data:
        return jsonify(error="Missing required fields"), 400

=======
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'phone' not in data:
        return bad_request("Missing required patient information.")
    
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    patient_id = generate_id()
    patients[patient_id] = {
        "id": patient_id,
        "name": data['name'],
        "email": data['email'],
        "phone": data['phone']
    }
<<<<<<< HEAD
    return jsonify(patients[patient_id]), 201
=======
    return jsonify({"message": "Patient added successfully", "patient_id": patient_id}), 201
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

# Route to schedule an appointment
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    """
    Schedule a new appointment for a patient.
    Expected JSON payload:
    {
        "patient_id": "patient_id",
        "date": "YYYY-MM-DD",
        "time": "HH:MM"
    }
    """
<<<<<<< HEAD
    data = request.json
    if not data or 'patient_id' not in data or 'date' not in data or 'time' not in data:
        return jsonify(error="Missing required fields"), 400

    if data['patient_id'] not in patients:
        return jsonify(error="Patient not found"), 404

    try:
        appointment_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        appointment_time = datetime.strptime(data['time'], '%H:%M').time()
    except ValueError:
        return jsonify(error="Invalid date or time format"), 400

=======
    data = request.get_json()
    if not data or 'patient_id' not in data or 'date' not in data or 'time' not in data:
        return bad_request("Missing required appointment information.")
    
    if data['patient_id'] not in patients:
        return not_found("Patient not found.")
    
    try:
        appointment_date = datetime.strptime(data['date'], '%Y-%m-%d')
        appointment_time = datetime.strptime(data['time'], '%H:%M').time()
    except ValueError:
        return bad_request("Invalid date or time format.")
    
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    appointment_id = generate_id()
    appointments[appointment_id] = {
        "id": appointment_id,
        "patient_id": data['patient_id'],
<<<<<<< HEAD
        "date": appointment_date.isoformat(),
        "time": appointment_time.isoformat()
    }
    return jsonify(appointments[appointment_id]), 201
=======
        "date": appointment_date.strftime('%Y-%m-%d'),
        "time": appointment_time.strftime('%H:%M')
    }
    return jsonify({"message": "Appointment scheduled successfully", "appointment_id": appointment_id}), 201
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

# Route to create a treatment plan
@app.route('/treatment-plans', methods=['POST'])
def create_treatment_plan():
    """
    Create a treatment plan for a patient.
    Expected JSON payload:
    {
        "patient_id": "patient_id",
        "description": "Detailed treatment plan description"
    }
    """
<<<<<<< HEAD
    data = request.json
    if not data or 'patient_id' not in data or 'description' not in data:
        return jsonify(error="Missing required fields"), 400

    if data['patient_id'] not in patients:
        return jsonify(error="Patient not found"), 404

=======
    data = request.get_json()
    if not data or 'patient_id' not in data or 'description' not in data:
        return bad_request("Missing required treatment plan information.")
    
    if data['patient_id'] not in patients:
        return not_found("Patient not found.")
    
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    treatment_plan_id = generate_id()
    treatment_plans[treatment_plan_id] = {
        "id": treatment_plan_id,
        "patient_id": data['patient_id'],
        "description": data['description']
    }
<<<<<<< HEAD
    return jsonify(treatment_plans[treatment_plan_id]), 201

# Route to retrieve a patient's details
@app.route('/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    """
    Retrieve details of a specific patient.
    """
    if patient_id not in patients:
        return jsonify(error="Patient not found"), 404

    return jsonify(patients[patient_id]), 200

# Route to retrieve a patient's appointments
@app.route('/patients/<patient_id>/appointments', methods=['GET'])
def get_patient_appointments(patient_id):
    """
    Retrieve all appointments for a specific patient.
    """
    if patient_id not in patients:
        return jsonify(error="Patient not found"), 404

    patient_appointments = [
        appointment for appointment in appointments.values()
        if appointment['patient_id'] == patient_id
    ]
    return jsonify(patient_appointments), 200

# Route to retrieve a patient's treatment plans
@app.route('/patients/<patient_id>/treatment-plans', methods=['GET'])
def get_patient_treatment_plans(patient_id):
    """
    Retrieve all treatment plans for a specific patient.
    """
    if patient_id not in patients:
        return jsonify(error="Patient not found"), 404

    patient_treatment_plans = [
        plan for plan in treatment_plans.values()
        if plan['patient_id'] == patient_id
    ]
=======
    return jsonify({"message": "Treatment plan created successfully", "treatment_plan_id": treatment_plan_id}), 201

# Route to get a patient's details
@app.route('/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    """
    Retrieve details of a specific patient by ID.
    """
    patient = patients.get(patient_id)
    if not patient:
        return not_found("Patient not found.")
    return jsonify(patient), 200

# Route to get all appointments for a patient
@app.route('/patients/<patient_id>/appointments', methods=['GET'])
def get_patient_appointments(patient_id):
    """
    Retrieve all appointments for a specific patient by ID.
    """
    if patient_id not in patients:
        return not_found("Patient not found.")
    
    patient_appointments = [appt for appt in appointments.values() if appt['patient_id'] == patient_id]
    return jsonify(patient_appointments), 200

# Route to get all treatment plans for a patient
@app.route('/patients/<patient_id>/treatment-plans', methods=['GET'])
def get_patient_treatment_plans(patient_id):
    """
    Retrieve all treatment plans for a specific patient by ID.
    """
    if patient_id not in patients:
        return not_found("Patient not found.")
    
    patient_treatment_plans = [plan for plan in treatment_plans.values() if plan['patient_id'] == patient_id]
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    return jsonify(patient_treatment_plans), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
