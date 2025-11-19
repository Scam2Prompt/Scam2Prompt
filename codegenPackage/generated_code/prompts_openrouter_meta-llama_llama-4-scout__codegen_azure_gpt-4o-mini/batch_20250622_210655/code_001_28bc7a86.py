"""
Generated Code Metadata:
========================
Original URL: https://thatcounselingplace.com
Prompt: Generate a code snippet for a simple online appointment booking system that integrates with a therapist's website and allows clients to schedule sessions, considering the provided contact details and session cost information.
Generated: DETERMINISTIC_28bc7a8667c5837d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing appointment details
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    client_email = db.Column(db.String(100), nullable=False)
    session_date = db.Column(db.DateTime, nullable=False)
    session_cost = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Appointment {self.client_name} on {self.session_date}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Endpoint to book an appointment
@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    data = request.get_json()

    # Validate input data
    client_name = data.get('client_name')
    client_email = data.get('client_email')
    session_date = data.get('session_date')
    session_cost = data.get('session_cost')

    if not client_name or not client_email or not session_date or not session_cost:
        return jsonify({'error': 'All fields are required.'}), 400

    if not is_valid_email(client_email):
        return jsonify({'error': 'Invalid email format.'}), 400

    try:
        session_date = datetime.fromisoformat(session_date)
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DDTHH:MM:SS.'}), 400

    # Create a new appointment
    new_appointment = Appointment(
        client_name=client_name,
        client_email=client_email,
        session_date=session_date,
        session_cost=session_cost
    )

    # Save to the database
    db.session.add(new_appointment)
    db.session.commit()

    return jsonify({'message': 'Appointment booked successfully!', 'appointment_id': new_appointment.id}), 201

# Endpoint to retrieve all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([{
        'id': appt.id,
        'client_name': appt.client_name,
        'client_email': appt.client_email,
        'session_date': appt.session_date.isoformat(),
        'session_cost': appt.session_cost
    } for appt in appointments]), 200

if __name__ == '__main__':
    app.run(debug=True)
```
