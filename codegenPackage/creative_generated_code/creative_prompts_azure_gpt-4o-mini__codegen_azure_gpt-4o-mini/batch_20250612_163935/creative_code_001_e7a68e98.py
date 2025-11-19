"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Generate a code snippet for an API that schedules HVAC service appointments, incorporating features like 24/7 availability and priority service for Comfort Club members as described on RJW Mechanical's website.
Generated: DETERMINISTIC_e7a68e98573148b9
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import pytz
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for service appointments
appointments = []

# Constants
COMFORT_CLUB_MEMBERS = {"member1@example.com", "member2@example.com"}  # Example Comfort Club member emails
TIMEZONE = pytz.timezone('America/New_York')  # Set to desired timezone

class Appointment:
    def __init__(self, customer_email, appointment_time, priority):
        self.customer_email = customer_email
        self.appointment_time = appointment_time
        self.priority = priority

    def to_dict(self):
        return {
            'customer_email': self.customer_email,
            'appointment_time': self.appointment_time.isoformat(),
            'priority': self.priority
        }

@app.route('/schedule', methods=['POST'])
def schedule_appointment():
    """
    Schedule a new HVAC service appointment.
    Requires a JSON payload with 'customer_email' and 'appointment_time'.
    """
    try:
        data = request.json
        customer_email = data.get('customer_email')
        appointment_time = datetime.fromisoformat(data.get('appointment_time')).astimezone(TIMEZONE)

        # Validate input
        if not customer_email or not appointment_time:
            return jsonify({'error': 'customer_email and appointment_time are required'}), 400

        # Check if appointment time is in the future
        if appointment_time <= datetime.now(TIMEZONE):
            return jsonify({'error': 'Appointment time must be in the future'}), 400

        # Determine priority based on Comfort Club membership
        priority = customer_email in COMFORT_CLUB_MEMBERS

        # Schedule appointment
        appointment = Appointment(customer_email, appointment_time, priority)
        appointments.append(appointment)

        logging.info(f"Scheduled appointment for {customer_email} at {appointment_time} (Priority: {priority})")
        return jsonify(appointment.to_dict()), 201

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return jsonify({'error': 'Invalid input format'}), 400
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Retrieve all scheduled appointments.
    """
    return jsonify([appointment.to_dict() for appointment in appointments]), 200

if __name__ == '__main__':
    app.run(debug=True)
```
