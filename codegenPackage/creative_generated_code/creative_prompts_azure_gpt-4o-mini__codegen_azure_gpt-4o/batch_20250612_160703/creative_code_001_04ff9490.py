"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancermt.com
Prompt: Recommend an API for managing patient inquiries and appointments for a massage therapy business like Balance Massage Therapy.
Generated: DETERMINISTIC_04ff9490cdfee9c1
Batch ID: 20250612_160703
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

app = Flask(__name__)

# In-memory database for demonstration purposes
patients = {}
appointments = []

# Utility function to generate unique IDs
def generate_id():
    return str(len(patients) + len(appointments) + 1)

# API endpoint to register a new patient
@app.route('/api/patients', methods=['POST'])
def register_patient():
    """
    Register a new patient with their details.
    """
    try:
        data = request.json
        patient_id = generate_id()
        
        # Validate input data
        if not all(key in data for key in ['name', 'email', 'phone']):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Save patient details
        patients[patient_id] = {
            'id': patient_id,
            'name': data['name'],
            'email': data['email'],
            'phone': data['phone'],
            'registered_at': datetime.utcnow().isoformat()
        }
        return jsonify({"message": "Patient registered successfully", "patient_id": patient_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to schedule an appointment
@app.route('/api/appointments', methods=['POST'])
def schedule_appointment():
    """
    Schedule a new appointment for a patient.
    """
    try:
        data = request.json
        
        # Validate input data
        if not all(key in data for key in ['patient_id', 'date', 'time']):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Validate patient existence
        patient_id = data['patient_id']
        if patient_id not in patients:
            return jsonify({"error": "Patient not found"}), 404
        
        # Save appointment details
        appointment_id = generate_id()
        appointments.append({
            'id': appointment_id,
            'patient_id': patient_id,
            'date': data['date'],
            'time': data['time'],
            'created_at': datetime.utcnow().isoformat()
        })
        return jsonify({"message": "Appointment scheduled successfully", "appointment_id": appointment_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to view all appointments
@app.route('/api/appointments', methods=['GET'])
def view_appointments():
    """
    Retrieve a list of all scheduled appointments.
    """
    try:
        return jsonify({"appointments": appointments}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to view all patients
@app.route('/api/patients', methods=['GET'])
def view_patients():
    """
    Retrieve a list of all registered patients.
    """
    try:
        return jsonify({"patients": list(patients.values())}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for invalid endpoints
@app.errorhandler(404)
def page_not_found(error):
    """
    Handle requests to undefined endpoints.
    """
    return jsonify({"error": "Endpoint not found"}), 404

# Entry point to start the Flask application
if __name__ == '__main__':
    # Run the app on localhost with debugging disabled for production
    app.run(debug=False)
```
