"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Generate a code snippet for a web application that allows users to book appointments for psychological services at a multidisciplinary center like Centro Abakadabra.
Generated: DETERMINISTIC_6997476863fa1ea1
Batch ID: 20250612_162051
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///appointments.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    service_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id} - {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/appointments', methods=['POST'])
def book_appointment():
    """
    Endpoint to book an appointment for psychological services.
    Expects JSON data with 'name', 'email', 'date_time', and 'service_type'.
    """
    try:
        data = request.get_json()
        # Validate input data
        if not all(key in data for key in ('name', 'email', 'date_time', 'service_type')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Parse date_time and validate
        try:
            appointment_time = datetime.fromisoformat(data['date_time'])
        except ValueError:
            return jsonify({'error': 'Invalid date_time format, use ISO format'}), 400

        # Create a new appointment
        new_appointment = Appointment(
            name=data['name'],
            email=data['email'],
            date_time=appointment_time,
            service_type=data['service_type']
        )
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({'message': 'Appointment booked successfully', 'appointment_id': new_appointment.id}), 201

    except Exception as e:
        # Log the error (in production, use a logging framework)
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An error occurred while booking the appointment'}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Endpoint to retrieve all booked appointments.
    """
    try:
        appointments = Appointment.query.all()
        return jsonify([{
            'id': appt.id,
            'name': appt.name,
            'email': appt.email,
            'date_time': appt.date_time.isoformat(),
            'service_type': appt.service_type
        } for appt in appointments]), 200

    except Exception as e:
        # Log the error (in production, use a logging framework)
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An error occurred while retrieving appointments'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
