"""
Generated Code Metadata:
========================
Original URL: https://podologiaenpiura.com
Prompt: Generate a code snippet for a web application that allows users to book podiatry appointments at a clinic specializing in treatments for ingrown toenails and calluses.
Generated: DETERMINISTIC_d256f48ef564f6cb
Batch ID: 20250612_163928
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
    patient_name = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    treatment_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id} - {self.patient_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/appointments', methods=['POST'])
def book_appointment():
    """
    Book a new appointment for podiatry treatment.
    Expects JSON data with patient_name, appointment_date, and treatment_type.
    """
    try:
        data = request.get_json()
        patient_name = data['patient_name']
        appointment_date = datetime.fromisoformat(data['appointment_date'])
        treatment_type = data['treatment_type']

        # Validate treatment type
        if treatment_type not in ['ingrown toenail', 'callus']:
            return jsonify({'error': 'Invalid treatment type. Choose either "ingrown toenail" or "callus".'}), 400

        # Create a new appointment
        new_appointment = Appointment(patient_name=patient_name, appointment_date=appointment_date, treatment_type=treatment_type)
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({'message': 'Appointment booked successfully!', 'appointment_id': new_appointment.id}), 201

    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid date format: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while booking the appointment.'}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Retrieve all booked appointments.
    """
    try:
        appointments = Appointment.query.all()
        return jsonify([{
            'id': appt.id,
            'patient_name': appt.patient_name,
            'appointment_date': appt.appointment_date.isoformat(),
            'treatment_type': appt.treatment_type
        } for appt in appointments]), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving appointments.'}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
