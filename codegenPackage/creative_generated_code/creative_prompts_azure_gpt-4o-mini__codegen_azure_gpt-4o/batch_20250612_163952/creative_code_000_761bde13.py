"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.martingodwinequine.com
Prompt: Write a code snippet for a web application that allows users to request personalized equine care appointments, similar to the services offered by Martin Godwin Equine Services.
Generated: DETERMINISTIC_761bde13544d5a74
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify
from datetime import datetime
import re

app = Flask(__name__)

# Hard-coded list of available services for simplicity (could be replaced with a database)
AVAILABLE_SERVICES = ["Basic Grooming", "Hoof Care", "Dental Care", "Veterinary Checkup"]

# Helper function to validate email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Route to request an equine care appointment
@app.route('/request-appointment', methods=['POST'])
def request_appointment():
    try:
        # Parse request data
        data = request.json
        name = data.get('name')
        email = data.get('email')
        horse_name = data.get('horse_name')
        appointment_date = data.get('appointment_date')
        service_requested = data.get('service_requested')

        # Validate user input
        if not name or not email or not horse_name or not appointment_date or not service_requested:
            return jsonify({"error": "All fields are required"}), 400
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email address"}), 400
        if service_requested not in AVAILABLE_SERVICES:
            return jsonify({"error": f"Service not available. Choose from {AVAILABLE_SERVICES}"}), 400

        # Validate appointment date
        try:
            appointment_date_obj = datetime.strptime(appointment_date, '%Y-%m-%d')
            if appointment_date_obj < datetime.now():
                return jsonify({"error": "Appointment date must be in the future"}), 400
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Create the appointment
        appointment = {
            "id": datetime.now().strftime('%Y%m%d%H%M%S'),
            "name": name,
            "email": email,
            "horse_name": horse_name,
            "appointment_date": appointment_date,
            "service_requested": service_requested,
        }

        # In production, this would be stored in a database
        print("New appointment created:", appointment)

        # Respond with success
        return jsonify({"message": "Appointment successfully created", "appointment": appointment}), 201

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Route to list available services
@app.route('/services', methods=['GET'])
def list_services():
    return jsonify({"available_services": AVAILABLE_SERVICES}), 200


if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

To run this code:
1. Install Flask (`pip install flask`).
2. Save the code into a file named `app.py`.
3. Run the script (`python app.py`).
4. Access the API endpoints:
   - `POST /request-appointment` for creating an appointment.
   - `GET /services` for listing available equine care services.
