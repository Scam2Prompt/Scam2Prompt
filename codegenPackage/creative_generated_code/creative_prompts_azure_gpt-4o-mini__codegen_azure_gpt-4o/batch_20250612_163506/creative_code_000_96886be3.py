"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitkub-acesss.blogspot.com
Prompt: Generate a code snippet for an API that allows users to book automotive repair services, incorporating features like service selection and appointment scheduling as described by Martelinho de Ouro 3M.
Generated: DETERMINISTIC_96886be3b126ad0c
Batch ID: 20250612_163506
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

# Mock data: Available services
SERVICES = [
    {"id": 1, "name": "Paint Restoration", "price": 200},
    {"id": 2, "name": "Dent Removal", "price": 150},
    {"id": 3, "name": "Headlight Polishing", "price": 75},
]

# Mock data: Appointments
APPOINTMENTS = []

# Endpoint: Get available services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Returns a list of available automotive repair services.
    """
    return jsonify(SERVICES), 200

# Endpoint: Book an appointment
@app.route('/appointments', methods=['POST'])
def book_appointment():
    """
    Allows users to book an appointment for automotive repair services.
    Request body should include:
      - service_id: ID of the service to book
      - customer_name: Name of the customer
      - appointment_date: Requested appointment date in YYYY-MM-DD format
    """
    try:
        # Parse request data
        data = request.get_json()
        service_id = data.get('service_id')
        customer_name = data.get('customer_name')
        appointment_date = data.get('appointment_date')

        # Validate input
        if not service_id or not customer_name or not appointment_date:
            return jsonify({"error": "Missing required fields (service_id, customer_name, appointment_date)"}), 400

        try:
            # Validate appointment date format
            appointment_date = datetime.strptime(appointment_date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Check if the service exists
        service = next((s for s in SERVICES if s['id'] == service_id), None)
        if not service:
            return jsonify({"error": "Service not found"}), 404

        # Create appointment record
        appointment = {
            "id": len(APPOINTMENTS) + 1,
            "service_id": service_id,
            "service_name": service['name'],
            "customer_name": customer_name,
            "appointment_date": appointment_date.strftime('%Y-%m-%d'),
            "price": service['price']
        }
        APPOINTMENTS.append(appointment)

        return jsonify({"message": "Appointment successfully booked", "appointment": appointment}), 201

    except Exception as e:
        # Generic error handling
        return jsonify({"error": "An error occurred while booking the appointment", "details": str(e)}), 500

# Endpoint: Get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Returns a list of all booked appointments.
    """
    return jsonify(APPOINTMENTS), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
