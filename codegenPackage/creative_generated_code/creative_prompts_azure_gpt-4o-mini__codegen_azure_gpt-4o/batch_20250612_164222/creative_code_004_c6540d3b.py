"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana2018.com
Prompt: Provide an example of a REST API that could be used to manage patient data and session bookings for a holistic health clinic like Solana柔整体院.
Generated: DETERMINISTIC_c6540d3b61974e8d
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import uuid

app = Flask(__name__)

# In-memory data stores (for simplicity; replace with a database in production)
patients = {}
sessions = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handler to provide consistent error responses
@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, HTTPException):
        response = jsonify({"error": e.description})
        response.status_code = e.code
    else:
        response = jsonify({"error": "Internal server error"})
        response.status_code = 500
    return response

# Endpoint to get all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(list(patients.values())), 200

# Endpoint to add a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    try:
        data = request.json
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({"error": "Invalid payload"}), 400
        patient_id = generate_id()
        patients[patient_id] = {
            "id": patient_id,
            "name": data['name'],
            "email": data['email'],
            "phone": data.get('phone', None),
        }
        return jsonify(patients[patient_id]), 201
    except Exception:
        raise

# Endpoint to get a specific patient by ID
@app.route('/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = patients.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(patient), 200

# Endpoint to update a patient's details
@app.route('/patients/<patient_id>', methods=['PUT'])
def update_patient(patient_id):
    try:
        data = request.json
        patient = patients.get(patient_id)
        if not patient:
            return jsonify({"error": "Patient not found"}), 404
        patient['name'] = data.get('name', patient['name'])
        patient['email'] = data.get('email', patient['email'])
        patient['phone'] = data.get('phone', patient['phone'])
        return jsonify(patient), 200
    except Exception:
        raise

# Endpoint to delete a patient
@app.route('/patients/<patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    if patient_id not in patients:
        return jsonify({"error": "Patient not found"}), 404
    del patients[patient_id]
    return jsonify({"message": "Patient deleted successfully"}), 200

# Endpoint to get all sessions
@app.route('/sessions', methods=['GET'])
def get_sessions():
    return jsonify(list(sessions.values())), 200

# Endpoint to add a new session booking
@app.route('/sessions', methods=['POST'])
def add_session():
    try:
        data = request.json
        required_fields = ['patient_id', 'date', 'time']
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Invalid payload"}), 400
        if data['patient_id'] not in patients:
            return jsonify({"error": "Patient not found"}), 404
        session_id = generate_id()
        sessions[session_id] = {
            "id": session_id,
            "patient_id": data['patient_id'],
            "date": data['date'],
            "time": data['time'],
            "notes": data.get('notes', None),
        }
        return jsonify(sessions[session_id]), 201
    except Exception:
        raise

# Endpoint to delete a session booking
@app.route('/sessions/<session_id>', methods=['DELETE'])
def delete_session(session_id):
    if session_id not in sessions:
        return jsonify({"error": "Session not found"}), 404
    del sessions[session_id]
    return jsonify({"message": "Session deleted successfully"}), 200

# Application startup
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
