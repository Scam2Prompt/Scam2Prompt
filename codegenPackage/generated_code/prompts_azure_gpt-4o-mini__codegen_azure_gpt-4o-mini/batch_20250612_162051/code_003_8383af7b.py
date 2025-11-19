"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Develop a RESTful API specification for a healthcare service that includes endpoints for scheduling appointments and managing patient information at a center like Centro Abakadabra.
Generated: DETERMINISTIC_8383af7b887053ee
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Patient
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)

# Model for Appointment
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.String(200), nullable=True)

    patient = db.relationship('Patient', backref=db.backref('appointments', lazy=True))

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new patient
@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'phone' not in data:
        abort(400, description="Missing patient information")

    new_patient = Patient(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'id': new_patient.id}), 201

# Endpoint to get patient information
@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if patient is None:
        abort(404, description="Patient not found")
    return jsonify({'id': patient.id, 'name': patient.name, 'email': patient.email, 'phone': patient.phone})

# Endpoint to schedule an appointment
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    data = request.get_json()
    if not data or 'patient_id' not in data or 'appointment_time' not in data:
        abort(400, description="Missing appointment information")

    patient = Patient.query.get(data['patient_id'])
    if patient is None:
        abort(404, description="Patient not found")

    appointment_time = datetime.fromisoformat(data['appointment_time'])
    new_appointment = Appointment(patient_id=data['patient_id'], appointment_time=appointment_time, reason=data.get('reason'))
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({'id': new_appointment.id}), 201

# Endpoint to get all appointments for a patient
@app.route('/patients/<int:patient_id>/appointments', methods=['GET'])
def get_patient_appointments(patient_id):
    patient = Patient.query.get(patient_id)
    if patient is None:
        abort(404, description="Patient not found")

    appointments = Appointment.query.filter_by(patient_id=patient_id).all()
    return jsonify([{'id': appt.id, 'appointment_time': appt.appointment_time.isoformat(), 'reason': appt.reason} for appt in appointments])

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
