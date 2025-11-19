"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doctoresjane.com
Prompt: Generate a code snippet for a web application that allows users to book dental appointments at Jané Clinic in Barcelona, integrating a personalized treatment plan feature.
Generated: DETERMINISTIC_d6e311c5bbeb1ad9
Batch ID: 20250612_161520
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
treatment_plans = {}

# Helper function for input validation
def validate_appointment_data(data):
    required_fields = ["name", "email", "phone", "date", "time", "treatment_plan"]
    for field in required_fields:
        if field not in data:
            return False
    return True

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    """
    Endpoint to book a dental appointment at Jané Clinic.
    Expects JSON input with the following fields:
        - name: Full name of the patient
        - email: Email address of the patient
        - phone: Phone number of the patient
        - date: Appointment date (format: YYYY-MM-DD)
        - time: Appointment time (format: HH:MM)
        - treatment_plan: Personalized treatment plan details
    Returns:
        - Success message if booking is successful
        - Error message if validation fails or other issues occur
    """
    try:
        # Parse JSON request data
        data = request.get_json()

        # Validate input data
        if not validate_appointment_data(data):
            return jsonify({"error": "Invalid input data. All fields are required."}), 400

        # Convert date and time to datetime object for validation
        try:
            appointment_datetime = datetime.strptime(f"{data['date']} {data['time']}", "%Y-%m-%d %H:%M")
        except ValueError:
            return jsonify({"error": "Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time."}), 400

        # Create unique appointment ID
        appointment_id = str(uuid.uuid4())

        # Save appointment details to the simulated database
        appointments.append({
            "id": appointment_id,
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "datetime": appointment_datetime,
            "treatment_plan": data["treatment_plan"]
        })

        # Save treatment plan details (associated with the appointment ID)
        treatment_plans[appointment_id] = data["treatment_plan"]

        return jsonify({"message": "Appointment booked successfully!", "appointment_id": appointment_id}), 201

    except Exception as e:
        # Return generic error message
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Endpoint to fetch all booked appointments.
    Returns:
        - List of all booked appointments
    """
    return jsonify(appointments), 200

@app.route('/treatment_plan/<appointment_id>', methods=['GET'])
def get_treatment_plan(appointment_id):
    """
    Endpoint to fetch the personalized treatment plan for a specific appointment.
    Args:
        - appointment_id: Unique ID of the appointment
    Returns:
        - Treatment plan details for the specified appointment
    """
    try:
        if appointment_id not in treatment_plans:
            return jsonify({"error": "Treatment plan not found for the specified appointment ID."}), 404

        return jsonify({"appointment_id": appointment_id, "treatment_plan": treatment_plans[appointment_id]}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
