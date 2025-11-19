"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virasmile.it
Prompt: Develop a web application feature that allows users to schedule dental visits and view services like parodontologia and odontoiatria pediatrica, based on the functionalities highlighted on the Vira Palazzo site.
Generated: DETERMINISTIC_2a51307821377766
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.exceptions import BadRequest
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///dentistry.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)

    service = db.relationship('Service', back_populates='appointments')

Service.appointments = db.relationship('Appointment', order_by=Appointment.id, back_populates='service')

# Route to view all services
@app.route('/services', methods=['GET'])
def get_services():
    """Return a list of available dental services."""
    services = Service.query.all()
    return jsonify([{'id': service.id, 'name': service.name, 'description': service.description} for service in services])

# Route to schedule an appointment
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    """Schedule a new dental appointment."""
    data = request.get_json()

    # Validate input data
    if not data or not all(key in data for key in ['patient_name', 'service_id', 'appointment_date']):
        raise BadRequest('Missing required fields: patient_name, service_id, appointment_date')

    try:
        appointment_date = datetime.fromisoformat(data['appointment_date'])
    except ValueError:
        raise BadRequest('Invalid date format. Use YYYY-MM-DDTHH:MM:SS.')

    # Create a new appointment
    new_appointment = Appointment(
        patient_name=data['patient_name'],
        service_id=data['service_id'],
        appointment_date=appointment_date
    )
    
    db.session.add(new_appointment)
    db.session.commit()

    return jsonify({'message': 'Appointment scheduled successfully!', 'appointment_id': new_appointment.id}), 201

# Route to view all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    """Return a list of scheduled appointments."""
    appointments = Appointment.query.all()
    return jsonify([{
        'id': appointment.id,
        'patient_name': appointment.patient_name,
        'service': appointment.service.name,
        'appointment_date': appointment.appointment_date.isoformat()
    } for appointment in appointments])

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
