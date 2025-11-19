"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centroabakadabra.com
Prompt: Develop a RESTful API specification for a healthcare service that includes endpoints for scheduling appointments and managing patient information at a center like Centro Abakadabra.
Generated: DETERMINISTIC_8383af7b887053ee
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

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
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

# Model for Appointment
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.String(255), nullable=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'phone' not in data:
        abort(400, description="Invalid input data")

    new_patient = Patient(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'id': new_patient.id}), 201

# Endpoint to retrieve a patient by ID
@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if patient is None:
        abort(404, description="Patient not found")
    
    return jsonify({
        'id': patient.id,
        'name': patient.name,
        'email': patient.email,
        'phone': patient.phone
    })

# Endpoint for scheduling an appointment
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    data = request.get_json()
    if not data or 'patient_id' not in data or 'appointment_time' not in data:
        abort(400, description="Invalid input data")

    patient = Patient.query.get(data['patient_id'])
    if patient is None:
        abort(404, description="Patient not found")

    appointment_time = datetime.strptime(data['appointment_time'], "%Y-%m-%d %H:%M:%S")
    new_appointment = Appointment(patient_id=data['patient_id'], appointment_time=appointment_time, reason=data.get('reason'))
    db.session.add(new_appointment)
    db.session.commit()
    
    return jsonify({'id': new_appointment.id}), 201

# Endpoint to retrieve appointments for a patient
@app.route('/patients/<int:patient_id>/appointments', methods=['GET'])
def get_patient_appointments(patient_id):
    patient = Patient.query.get(patient_id)
    if patient is None:
        abort(404, description="Patient not found")

    appointments = Appointment.query.filter_by(patient_id=patient_id).all()
    return jsonify([{
        'id': appointment.id,
        'appointment_time': appointment.appointment_time.strftime("%Y-%m-%d %H:%M:%S"),
        'reason': appointment.reason
    } for appointment in appointments])

if __name__ == '__main__':
    app.run(debug=True)
```
