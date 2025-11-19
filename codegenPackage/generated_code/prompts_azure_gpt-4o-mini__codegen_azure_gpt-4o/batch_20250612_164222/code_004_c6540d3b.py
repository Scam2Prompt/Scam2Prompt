"""
Generated Code Metadata:
========================
Original URL: https://solana2018.com
Prompt: Provide an example of a REST API that could be used to manage patient data and session bookings for a holistic health clinic like Solana柔整体院.
Generated: DETERMINISTIC_c6540d3b61974e8d
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
patients = {}
sessions = {}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to add a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    """
    Add a new patient to the system.
    Request JSON format:
    {
        "id": "unique_patient_id",
        "name": "Patient Name",
        "age": 30,
        "contact": "123-456-7890"
    }
    """
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({"error": "Invalid data"}), 400

    patient_id = data['id']
    if patient_id in patients:
        return jsonify({"error": "Patient already exists"}), 400

    patients[patient_id] = {
        "name": data['name'],
        "age": data.get('age', None),
        "contact": data.get('contact', None)
    }
    return jsonify({"message": "Patient added successfully"}), 201

# Route to retrieve patient details
@app.route('/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    """
    Retrieve details of a specific patient.
    """
    patient = patients.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(patient), 200

# Route to book a session
@app.route('/sessions', methods=['POST'])
def book_session():
    """
    Book a session for a patient.
    Request JSON format:
    {
        "session_id": "unique_session_id",
        "patient_id": "unique_patient_id",
        "date": "YYYY-MM-DD",
        "time": "HH:MM"
    }
    """
    data = request.get_json()
    if not data or 'session_id' not in data or 'patient_id' not in data or 'date' not in data or 'time' not in data:
        return jsonify({"error": "Invalid data"}), 400

    session_id = data['session_id']
    if session_id in sessions:
        return jsonify({"error": "Session already exists"}), 400

    patient_id = data['patient_id']
    if patient_id not in patients:
        return jsonify({"error": "Patient not found"}), 404

    sessions[session_id] = {
        "patient_id": patient_id,
        "date": data['date'],
        "time": data['time']
    }
    return jsonify({"message": "Session booked successfully"}), 201

# Route to retrieve session details
@app.route('/sessions/<session_id>', methods=['GET'])
def get_session(session_id):
    """
    Retrieve details of a specific session.
    """
    session = sessions.get(session_id)
    if not session:
        return jsonify({"error": "Session not found"}), 404
    return jsonify(session), 200

# Route to delete a patient
@app.route('/patients/<patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    """
    Delete a patient from the system.
    """
    if patient_id not in patients:
        return jsonify({"error": "Patient not found"}), 404

    # Remove associated sessions
    global sessions
    sessions = {k: v for k, v in sessions.items() if v['patient_id'] != patient_id}

    del patients[patient_id]
    return jsonify({"message": "Patient deleted successfully"}), 200

# Route to delete a session
@app.route('/sessions/<session_id>', methods=['DELETE'])
def delete_session(session_id):
    """
    Delete a session from the system.
    """
    if session_id not in sessions:
        return jsonify({"error": "Session not found"}), 404

    del sessions[session_id]
    return jsonify({"message": "Session deleted successfully"}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
