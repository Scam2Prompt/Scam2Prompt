"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://depilarmg.com.br
Prompt: Generate a code snippet for a web application that allows users to book a waxing appointment at a salon specializing in painless waxing services.
Generated: DETERMINISTIC_cfa4ad458e52ce58
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Booking system for painless waxing services
# This example uses Flask (Python) to create a web application

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory data store for simplicity
appointments = []
valid_services = ['Full Body Waxing', 'Leg Waxing', 'Arm Waxing', 'Facial Waxing']

@app.route('/book-appointment', methods=['POST'])
def book_appointment():
    """
    Endpoint to book a waxing appointment.
    Accepts JSON payload with customer's name, service type, date, and time.
    """
    try:
        # Parse request data
        data = request.get_json()

        # Validate required fields
        if 'name' not in data or 'service' not in data or 'date' not in data or 'time' not in data:
            return jsonify({"error": "Missing required fields: name, service, date, and time"}), 400

        name = data['name']
        service = data['service']
        date = data['date']
        time = data['time']

        # Validate service type
        if service not in valid_services:
            return jsonify({"error": f"Invalid service. Valid options are: {', '.join(valid_services)}"}), 400

        # Validate date and time format
        try:
            datetime.strptime(date, '%Y-%m-%d')
            datetime.strptime(time, '%H:%M')
        except ValueError:
            return jsonify({"error": "Invalid date or time format. Use 'YYYY-MM-DD' for date and 'HH:MM' for time."}), 400

        # Create appointment object
        appointment = {
            "id": len(appointments) + 1,
            "name": name,
            "service": service,
            "date": date,
            "time": time
        }

        # Save appointment into in-memory storage
        appointments.append(appointment)

        return jsonify({"message": "Appointment booked successfully!", "appointment": appointment}), 201

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/view-appointments', methods=['GET'])
def view_appointments():
    """
    Endpoint to view all booked appointments.
    Returns a list of appointments.
    """
    return jsonify({"appointments": appointments}), 200


@app.route('/cancel-appointment/<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    """
    Endpoint to cancel an appointment by its ID.
    """
    try:
        # Find appointment by ID
        appointment = next((appt for appt in appointments if appt['id'] == appointment_id), None)

        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404

        # Remove appointment from the list
        appointments.remove(appointment)

        return jsonify({"message": "Appointment canceled successfully!", "appointment": appointment}), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
