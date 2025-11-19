"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: Develop a RESTful API endpoint that allows users to book appointments with specialists for custom projects related to windows and doors in the Oise region.
Generated: DETERMINISTIC_2d99dc985b5b133d
Batch ID: 20250612_140107
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

# In-memory database for demonstration purposes
appointments = []

# Helper function to validate appointment data
def validate_appointment_data(data):
    required_fields = ['name', 'email', 'phone', 'specialist', 'date', 'time']
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    try:
        datetime.strptime(data['date'], '%Y-%m-%d')
        datetime.strptime(data['time'], '%H:%M')
    except ValueError:
        return "Invalid date or time format. Use 'YYYY-MM-DD' for date and 'HH:MM' for time."
    return None

@app.route('/api/appointments', methods=['POST'])
def book_appointment():
    """
    Endpoint to book an appointment with a specialist.
    Expects JSON payload with the following fields:
    - name: str, user's name
    - email: str, user's email
    - phone: str, user's phone number
    - specialist: str, name of the specialist
    - date: str, appointment date in 'YYYY-MM-DD' format
    - time: str, appointment time in 'HH:MM' format
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate appointment data
        validation_error = validate_appointment_data(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        # Generate a unique ID for the appointment
        appointment_id = str(uuid.uuid4())

        # Create appointment record
        appointment = {
            "id": appointment_id,
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "specialist": data['specialist'],
            "date": data['date'],
            "time": data['time'],
            "region": "Oise"
        }

        # Save appointment to the in-memory database
        appointments.append(appointment)

        # Return success response
        return jsonify({"message": "Appointment booked successfully", "appointment": appointment}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    """
    Endpoint to retrieve all booked appointments.
    Returns a list of appointments in JSON format.
    """
    return jsonify({"appointments": appointments}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
