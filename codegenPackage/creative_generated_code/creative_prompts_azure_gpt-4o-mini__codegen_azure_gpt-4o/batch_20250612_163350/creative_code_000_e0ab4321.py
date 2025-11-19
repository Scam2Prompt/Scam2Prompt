"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Generate a code snippet for a mobile application that allows users to schedule RV repair appointments with a service provider in Phoenix, Arizona.
Generated: DETERMINISTIC_e0ab4321094a870c
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python code snippet using the Flask framework to create a backend API for scheduling RV repair appointments. It is designed to be clean, production-ready, and well-documented.

```python
from flask import Flask, request, jsonify
from datetime import datetime
import re

app = Flask(__name__)

# In-memory storage for appointments (for simplicity, a database should be used in production)
appointments = []

# Function to validate email format
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Function to validate date format
def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    """
    API Endpoint: Schedule an appointment for RV repair.
    Method: POST
    Expected JSON Body:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890",
        "date": "2023-10-15",
        "time": "14:00",
        "details": "RV engine repair required"
    }
    """
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'date', 'time', 'details']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"{field} is required"}), 400

        # Validate email format
        if not is_valid_email(data['email']):
            return jsonify({"error": "Invalid email format"}), 400

        # Validate date format (YYYY-MM-DD)
        if not is_valid_date(data['date']):
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Validate time format (HH:MM)
        try:
            datetime.strptime(data['time'], '%H:%M')
        except ValueError:
            return jsonify({"error": "Invalid time format. Use HH:MM"}), 400

        # Create appointment object
        appointment = {
            "id": len(appointments) + 1,
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "date": data['date'],
            "time": data['time'],
            "details": data['details']
        }

        # Save to in-memory storage
        appointments.append(appointment)

        return jsonify({"message": "Appointment scheduled successfully", "appointment": appointment}), 201

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    API Endpoint: Get all scheduled appointments.
    Method: GET
    Response: List of all appointments
    """
    try:
        return jsonify({"appointments": appointments}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment_by_id(appointment_id):
    """
    API Endpoint: Get a specific appointment by ID.
    Method: GET
    URL Param: appointment_id (int)
    Response: Appointment details
    """
    try:
        appointment = next((appt for appt in appointments if appt['id'] == appointment_id), None)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404
        return jsonify({"appointment": appointment}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    """
    API Endpoint: Cancel a specific appointment by ID.
    Method: DELETE
    URL Param: appointment_id (int)
    Response: Cancellation confirmation
    """
    try:
        global appointments
        appointment = next((appt for appt in appointments if appt['id'] == appointment_id), None)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404

        appointments = [appt for appt in appointments if appt['id'] != appointment_id]
        return jsonify({"message": "Appointment cancelled successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

This code snippet provides a backend implementation for scheduling RV repair appointments. It includes endpoints for creating, retrieving, and canceling appointments, uses in-memory storage, validates user input, and handles errors gracefully.
