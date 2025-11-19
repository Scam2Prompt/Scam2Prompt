"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fachriahyani.com
Prompt: Generate a code snippet for a legal consultation API that allows users to book appointments with an advocate like Fachri Ahyani.
Generated: DETERMINISTIC_c301c0d095c6103a
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
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database simulation
appointments = []

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    """
    Endpoint to book an appointment with an advocate.
    """
    try:
        # Extract data from request
        data = request.get_json()
        if not data:
            return error_response("Invalid JSON payload.")

        advocate_name = data.get('advocate_name')
        user_name = data.get('user_name')
        appointment_date = data.get('appointment_date')

        # Validate required fields
        if not advocate_name or not user_name or not appointment_date:
            return error_response("Missing required fields: advocate_name, user_name, appointment_date.")

        # Validate date format
        try:
            appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return error_response("Invalid date format. Use 'YYYY-MM-DD HH:MM:SS'.")

        # Create appointment record
        appointment = {
            "id": str(uuid.uuid4()),
            "advocate_name": advocate_name,
            "user_name": user_name,
            "appointment_date": appointment_date.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "booked"
        }

        # Save to in-memory database
        appointments.append(appointment)

        # Respond with appointment details
        return jsonify({"message": "Appointment booked successfully.", "appointment": appointment}), 201

    except Exception as e:
        # Catch unexpected errors
        return error_response(f"An unexpected error occurred: {str(e)}", 500)

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Endpoint to retrieve all booked appointments.
    """
    try:
        return jsonify({"appointments": appointments}), 200
    except Exception as e:
        return error_response(f"An unexpected error occurred: {str(e)}", 500)

# Entry point for the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
