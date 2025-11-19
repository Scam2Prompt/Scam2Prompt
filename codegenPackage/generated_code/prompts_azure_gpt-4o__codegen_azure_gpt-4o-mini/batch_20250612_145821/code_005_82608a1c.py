"""
Generated Code Metadata:
========================
Original URL: https://clientfuel.digital
Prompt: Write code to optimize a sales funnel for pre-selling services and booking appointments, based on the "Click, Capture, Close" model described on the Client Fuel website.
Generated: DETERMINISTIC_82608a1c62770f37
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sales_funnel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for capturing leads
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Lead {self.name}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/capture', methods=['POST'])
def capture_lead():
    """
    Capture lead information from the request.
    Expects JSON with 'name', 'email', and optional 'phone'.
    """
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        if not name or not email:
            return jsonify({'error': 'Name and email are required.'}), 400

        # Create a new lead
        new_lead = Lead(name=name, email=email, phone=phone)
        db.session.add(new_lead)
        db.session.commit()

        logging.info(f'Lead captured: {new_lead}')
        return jsonify({'message': 'Lead captured successfully!'}), 201

    except Exception as e:
        logging.error(f'Error capturing lead: {e}')
        return jsonify({'error': 'An error occurred while capturing the lead.'}), 500

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    """
    Book an appointment for a lead.
    Expects JSON with 'email' and 'appointment_time'.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        appointment_time = data.get('appointment_time')

        if not email or not appointment_time:
            return jsonify({'error': 'Email and appointment time are required.'}), 400

        # Here you would typically add logic to book the appointment
        # For demonstration, we will just log the appointment
        logging.info(f'Appointment booked for {email} at {appointment_time}')
        return jsonify({'message': 'Appointment booked successfully!'}), 200

    except Exception as e:
        logging.error(f'Error booking appointment: {e}')
        return jsonify({'error': 'An error occurred while booking the appointment.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
