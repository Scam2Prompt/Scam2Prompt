"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gavasilva.adv.br
Prompt: Generate a code snippet for a web application that allows users to schedule legal consultations with Gava & Silva Advogados, incorporating features for both in-person and online appointments.
Generated: DETERMINISTIC_b487595849c8b6fc
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# In-memory storage for appointments (to be replaced with a proper database in production)
appointments = []

@app.route('/schedule', methods=['POST'])
def schedule_appointment():
    """
    Endpoint to schedule a legal consultation.

    JSON Payload Format:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "appointment_type": "in-person", # or "online"
        "appointment_date": "2023-10-25",
        "appointment_time": "14:00"
    }
    """
    try:
        data = request.json
        
        # Validate input fields
        required_fields = ['name', 'email', 'phone', 'appointment_type', 
                           'appointment_date', 'appointment_time']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"'{field}' is required"}), 400
        
        # Validate appointment type
        if data['appointment_type'] not in ['in-person', 'online']:
            return jsonify({"error": "Invalid appointment type. Must be 'in-person' or 'online'"}), 400
        
        # Parse and validate date and time
        try:
            appointment_date = datetime.datetime.strptime(data['appointment_date'], '%Y-%m-%d').date()
            appointment_time = datetime.datetime.strptime(data['appointment_time'], '%H:%M').time()
        except ValueError:
            return jsonify({"error": "Invalid date or time format"}), 400
        
        # Ensure appointment is in the future
        now = datetime.datetime.now()
        appointment_datetime = datetime.datetime.combine(appointment_date, appointment_time)
        if appointment_datetime <= now:
            return jsonify({"error": "Appointment must be in the future"}), 400
        
        # Create appointment entry
        appointment = {
            "id": len(appointments) + 1,  # Simple ID generation (use UUIDs in production)
            "name": data['name'],
            "email": data['email'],
            "phone": data['phone'],
            "appointment_type": data['appointment_type'],
            "appointment_date": str(appointment_date),
            "appointment_time": str(appointment_time),
        }
        
        # Save appointment
        appointments.append(appointment)
        return jsonify({"message": "Appointment scheduled successfully", "appointment": appointment}), 201

    except Exception as e:
        # Generic error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/appointments', methods=['GET'])
def list_appointments():
    """
    Endpoint to list all scheduled appointments.
    """
    return jsonify({"appointments": appointments}), 200


if __name__ == '__main__':
    app.run(debug=True)
```
