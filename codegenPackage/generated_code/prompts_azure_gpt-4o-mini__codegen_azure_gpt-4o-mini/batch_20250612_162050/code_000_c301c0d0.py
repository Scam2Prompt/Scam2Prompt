"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Generate a code snippet for a legal consultation API that allows users to book appointments with an advocate like Fachri Ahyani.
Generated: DETERMINISTIC_c301c0d095c6103a
Batch ID: 20250612_162050
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
    user_name = db.Column(db.String(100), nullable=False)
    advocate_name = db.Column(db.String(100), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id} - {self.user_name} with {self.advocate_name} at {self.appointment_time}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    """
    Endpoint to book an appointment with an advocate.
    Expects JSON data with 'user_name', 'advocate_name', and 'appointment_time'.
    """
    try:
        data = request.get_json()
        user_name = data.get('user_name')
        advocate_name = data.get('advocate_name', 'Fachri Ahyani')  # Default advocate
        appointment_time = datetime.fromisoformat(data.get('appointment_time'))

        # Validate input
        if not user_name or not appointment_time:
            return jsonify({'error': 'User name and appointment time are required.'}), 400

        # Create a new appointment
        new_appointment = Appointment(user_name=user_name, advocate_name=advocate_name, appointment_time=appointment_time)
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({'message': 'Appointment booked successfully!', 'appointment_id': new_appointment.id}), 201

    except ValueError as ve:
        return jsonify({'error': 'Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS).'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Endpoint to retrieve all booked appointments.
    """
    try:
        appointments = Appointment.query.all()
        return jsonify([{
            'id': appt.id,
            'user_name': appt.user_name,
            'advocate_name': appt.advocate_name,
            'appointment_time': appt.appointment_time.isoformat()
        } for appt in appointments]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
