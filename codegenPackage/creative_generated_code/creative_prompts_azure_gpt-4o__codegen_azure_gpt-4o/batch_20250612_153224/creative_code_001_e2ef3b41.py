"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Generate a REST API design for booking a hair transplant consultation online, incorporating features like free follow-up for 5 months and session duration details as described by Auqual Hair Services.
Generated: DETERMINISTIC_e2ef3b41a850e1ca
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

# In-memory storage for simplicity (use a database in production)
appointments = {}

# Helper function to validate input data
def validate_appointment(data):
    required_fields = ['name', 'email', 'phone', 'preferred_date', 'session_duration']
    for field in required_fields:
        if field not in data:
            return f"Missing field: {field}"
    return None

@app.route('/api/appointments', methods=['POST'])
def create_appointment():
    """
    Endpoint to book a hair transplant consultation.
    Returns appointment details with free follow-up period included.
    """
    try:
        data = request.json
        error = validate_appointment(data)
        if error:
            return jsonify({"error": error}), 400

        # Parse preferred date and ensure it is not in the past
        try:
            preferred_date = datetime.strptime(data['preferred_date'], '%Y-%m-%d')
            if preferred_date < datetime.now():
                return jsonify({"error": "Preferred date must be in the future"}), 400
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Create appointment entry
        appointment_id = str(uuid.uuid4())
        follow_up_end_date = preferred_date + timedelta(days=5 * 30)  # Approx. 5 months

        appointment = {
            "id": appointment_id,
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "preferred_date": preferred_date.strftime('%Y-%m-%d'),
            "session_duration": data['session_duration'],
            "follow_up_end_date": follow_up_end_date.strftime('%Y-%m-%d')
        }

        # Save appointment in the in-memory storage
        appointments[appointment_id] = appointment

        return jsonify({"message": "Appointment created successfully", "appointment": appointment}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/appointments/<appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    """
    Endpoint to retrieve an appointment by ID.
    """
    try:
        appointment = appointments.get(appointment_id)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404
        
        return jsonify({"appointment": appointment}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/appointments/<appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    """
    Endpoint to delete an appointment by ID.
    """
    try:
        appointment = appointments.pop(appointment_id, None)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404
        
        return jsonify({"message": "Appointment deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/appointments', methods=['GET'])
def list_appointments():
    """
    Endpoint to list all appointments.
    """
    try:
        return jsonify({"appointments": list(appointments.values())}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
