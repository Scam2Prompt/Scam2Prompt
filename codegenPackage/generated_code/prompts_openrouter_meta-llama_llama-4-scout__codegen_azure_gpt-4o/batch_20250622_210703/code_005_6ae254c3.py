"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Design a RESTful API for managing client information, therapy sessions, and appointment schedules for a holistic health clinic like Vitality Holistic.
Generated: DETERMINISTIC_6ae254c3128d92dc
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
import uuid

app = Flask(__name__)

# In-memory data storage (for demonstration purposes)
clients = {}
therapy_sessions = {}
appointments = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Routes for managing clients
@app.route('/clients', methods=['POST'])
def create_client():
    """
    Create a new client.
    Request JSON format:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    }
    """
    data = request.json
    if not data or 'name' not in data or 'email' not in data or 'phone' not in data:
        return error_response("Missing required client information.")
    
    client_id = generate_id()
    clients[client_id] = {
        "id": client_id,
        "name": data['name'],
        "email": data['email'],
        "phone": data['phone']
    }
    return jsonify(clients[client_id]), 201

@app.route('/clients/<client_id>', methods=['GET'])
def get_client(client_id):
    """
    Retrieve client information by ID.
    """
    client = clients.get(client_id)
    if not client:
        return error_response("Client not found.", 404)
    return jsonify(client)

@app.route('/clients/<client_id>', methods=['PUT'])
def update_client(client_id):
    """
    Update client information.
    Request JSON format:
    {
        "name": "Updated Name",
        "email": "updated.email@example.com",
        "phone": "987-654-3210"
    }
    """
    client = clients.get(client_id)
    if not client:
        return error_response("Client not found.", 404)
    
    data = request.json
    if not data:
        return error_response("No data provided.")
    
    client.update({
        "name": data.get('name', client['name']),
        "email": data.get('email', client['email']),
        "phone": data.get('phone', client['phone'])
    })
    return jsonify(client)

@app.route('/clients/<client_id>', methods=['DELETE'])
def delete_client(client_id):
    """
    Delete a client by ID.
    """
    if client_id not in clients:
        return error_response("Client not found.", 404)
    
    del clients[client_id]
    return jsonify({"message": "Client deleted successfully."})

# Routes for managing therapy sessions
@app.route('/therapy_sessions', methods=['POST'])
def create_therapy_session():
    """
    Create a new therapy session.
    Request JSON format:
    {
        "name": "Yoga Therapy",
        "description": "A relaxing yoga session."
    }
    """
    data = request.json
    if not data or 'name' not in data or 'description' not in data:
        return error_response("Missing required therapy session information.")
    
    session_id = generate_id()
    therapy_sessions[session_id] = {
        "id": session_id,
        "name": data['name'],
        "description": data['description']
    }
    return jsonify(therapy_sessions[session_id]), 201

@app.route('/therapy_sessions/<session_id>', methods=['GET'])
def get_therapy_session(session_id):
    """
    Retrieve therapy session information by ID.
    """
    session = therapy_sessions.get(session_id)
    if not session:
        return error_response("Therapy session not found.", 404)
    return jsonify(session)

@app.route('/therapy_sessions/<session_id>', methods=['PUT'])
def update_therapy_session(session_id):
    """
    Update therapy session information.
    Request JSON format:
    {
        "name": "Updated Therapy Name",
        "description": "Updated description."
    }
    """
    session = therapy_sessions.get(session_id)
    if not session:
        return error_response("Therapy session not found.", 404)
    
    data = request.json
    if not data:
        return error_response("No data provided.")
    
    session.update({
        "name": data.get('name', session['name']),
        "description": data.get('description', session['description'])
    })
    return jsonify(session)

@app.route('/therapy_sessions/<session_id>', methods=['DELETE'])
def delete_therapy_session(session_id):
    """
    Delete a therapy session by ID.
    """
    if session_id not in therapy_sessions:
        return error_response("Therapy session not found.", 404)
    
    del therapy_sessions[session_id]
    return jsonify({"message": "Therapy session deleted successfully."})

# Routes for managing appointments
@app.route('/appointments', methods=['POST'])
def create_appointment():
    """
    Create a new appointment.
    Request JSON format:
    {
        "client_id": "client_id",
        "session_id": "session_id",
        "date": "YYYY-MM-DD",
        "time": "HH:MM"
    }
    """
    data = request.json
    if not data or 'client_id' not in data or 'session_id' not in data or 'date' not in data or 'time' not in data:
        return error_response("Missing required appointment information.")
    
    client = clients.get(data['client_id'])
    session = therapy_sessions.get(data['session_id'])
    if not client:
        return error_response("Client not found.", 404)
    if not session:
        return error_response("Therapy session not found.", 404)
    
    try:
        appointment_date = datetime.strptime(data['date'], "%Y-%m-%d").date()
        appointment_time = datetime.strptime(data['time'], "%H:%M").time()
    except ValueError:
        return error_response("Invalid date or time format.")
    
    appointment_id = generate_id()
    appointments[appointment_id] = {
        "id": appointment_id,
        "client_id": data['client_id'],
        "session_id": data['session_id'],
        "date": appointment_date.isoformat(),
        "time": appointment_time.isoformat()
    }
    return jsonify(appointments[appointment_id]), 201

@app.route('/appointments/<appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    """
    Retrieve appointment information by ID.
    """
    appointment = appointments.get(appointment_id)
    if not appointment:
        return error_response("Appointment not found.", 404)
    return jsonify(appointment)

@app.route('/appointments/<appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    """
    Delete an appointment by ID.
    """
    if appointment_id not in appointments:
        return error_response("Appointment not found.", 404)
    
    del appointments[appointment_id]
    return jsonify({"message": "Appointment deleted successfully."})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
