"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mluce-ginza.net
Prompt: Create an API endpoint for managing client inquiries and bookings for an art makeup salon, incorporating features like service selection and appointment reminders.
Generated: DETERMINISTIC_8ae715b6105d0a3f
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

# In-memory database (for demonstration purposes)
clients_db = {}
appointments_db = {}

# Available services
SERVICES = ["Eyebrow Design", "Lip Blush", "Eyeliner Enhancement"]

# Helper function to validate service
def is_valid_service(service):
    return service in SERVICES

# Helper function to send appointment reminder (mock implementation)
def send_reminder(client_email, appointment_id, appointment_date):
    # In a real-world scenario, integrate with an email or SMS service
    print(f"Reminder sent to {client_email} for appointment {appointment_id} on {appointment_date}")

# API endpoint: Add a new client inquiry
@app.route('/api/clients', methods=['POST'])
def add_client_inquiry():
    try:
        # Validate input
        data = request.json
        if not data or 'name' not in data or 'email' not in data or 'service' not in data:
            return jsonify({'error': 'Invalid input. Name, email, and service are required.'}), 400

        # Validate service
        if not is_valid_service(data['service']):
            return jsonify({'error': f"Invalid service selected. Available services: {SERVICES}"}), 400

        # Create a new client record
        client_id = str(uuid.uuid4())
        clients_db[client_id] = {
            'name': data['name'],
            'email': data['email'],
            'service': data['service'],
            'created_at': datetime.utcnow()
        }
        return jsonify({'message': 'Client inquiry added successfully.', 'client_id': client_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint: Book an appointment
@app.route('/api/appointments', methods=['POST'])
def book_appointment():
    try:
        # Validate input
        data = request.json
        if not data or 'client_id' not in data or 'appointment_date' not in data:
            return jsonify({'error': 'Invalid input. Client ID and appointment date are required.'}), 400

        # Validate client existence
        client_id = data['client_id']
        if client_id not in clients_db:
            return jsonify({'error': 'Client ID not found.'}), 404

        # Validate appointment date format
        try:
            appointment_date = datetime.strptime(data['appointment_date'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD HH:MM:SS.'}), 400

        # Create a new appointment record
        appointment_id = str(uuid.uuid4())
        appointments_db[appointment_id] = {
            'client_id': client_id,
            'appointment_date': appointment_date,
            'created_at': datetime.utcnow()
        }

        # Send mock reminder (reminder is sent 24 hours before the appointment)
        reminder_date = appointment_date - timedelta(days=1)
        send_reminder(clients_db[client_id]['email'], appointment_id, reminder_date)

        return jsonify({'message': 'Appointment booked successfully.', 'appointment_id': appointment_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint: List all appointments
@app.route('/api/appointments', methods=['GET'])
def list_appointments():
    try:
        appointments = []
        for appointment_id, details in appointments_db.items():
            client = clients_db[details['client_id']]
            appointments.append({
                'appointment_id': appointment_id,
                'client_name': client['name'],
                'service': client['service'],
                'appointment_date': details['appointment_date'].strftime('%Y-%m-%d %H:%M:%S')
            })
        return jsonify(appointments), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint: List all clients
@app.route('/api/clients', methods=['GET'])
def list_clients():
    try:
        clients = []
        for client_id, details in clients_db.items():
            clients.append({
                'client_id': client_id,
                'name': details['name'],
                'email': details['email'],
                'service': details['service'],
                'created_at': details['created_at'].strftime('%Y-%m-%d %H:%M:%S')
            })
        return jsonify(clients), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
