"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centroabakadabra.com
Prompt: Generate a code snippet for a web application that allows users to book appointments for psychological services at a multidisciplinary center like Centro Abakadabra.
Generated: DETERMINISTIC_6997476863fa1ea1
Batch ID: 20250612_162051
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

# In-memory database for simplicity (use a real database in production)
appointments = []

# Define allowed services
SERVICES = [
    "Psychology Counseling",
    "Speech Therapy",
    "Occupational Therapy",
    "Behavior Therapy"
]

# Route to book an appointment
@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    """
    Endpoint to book an appointment.
    Expected JSON request:
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "service": "Psychology Counseling",
        "date": "2023-10-01",
        "time": "10:00"
    }
    """
    try:
        # Parse request data
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        service = data.get('service')
        date = data.get('date')
        time = data.get('time')

        # Validate required fields
        if not name or not email or not service or not date or not time:
            return jsonify({"error": "All fields are required."}), 400

        # Validate service
        if service not in SERVICES:
            return jsonify({"error": f"Invalid service. Available services: {', '.join(SERVICES)}"}), 400

        # Validate date and time format
        try:
            appointment_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            return jsonify({"error": "Invalid date or time format. Use YYYY-MM-DD and HH:MM."}), 400

        # Check for conflicting appointments
        for appointment in appointments:
            if appointment['service'] == service and appointment['datetime'] == appointment_datetime:
                return jsonify({"error": "The chosen time slot is already booked."}), 409

        # Save appointment
        new_appointment = {
            "id": len(appointments) + 1,
            "name": name,
            "email": email,
            "service": service,
            "datetime": appointment_datetime
        }
        appointments.append(new_appointment)

        # Respond with success
        return jsonify({"message": "Appointment successfully booked!", "appointment": new_appointment}), 201
    
    except Exception as e:
        # General error handling
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Route to list all appointments
@app.route('/appointments', methods=['GET'])
def list_appointments():
    """
    Endpoint to list all appointments.
    """
    try:
        return jsonify({"appointments": appointments}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
