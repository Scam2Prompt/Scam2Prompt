"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Develop a Python API to manage patient appointments and treatment plans for a sleep apnea and TMJ disorder clinic, inspired by the services provided by the San Diego Sleep and TMJ Center.
Generated: DETERMINISTIC_1a343cca7aa7710c
Batch ID: 20250622_204623
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Patient
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

# Database model for Appointment
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    treatment_plan = db.Column(db.String(200), nullable=True)

# Schema for validating input data
class PatientSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)

class AppointmentSchema(Schema):
    patient_id = fields.Int(required=True)
    date = fields.DateTime(required=True)
    treatment_plan = fields.Str(required=False)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    json_data = request.get_json()
    try:
        data = PatientSchema().load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_patient = Patient(name=data['name'], email=data['email'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"id": new_patient.id, "name": new_patient.name, "email": new_patient.email}), 201

# Route to get all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([{"id": p.id, "name": p.name, "email": p.email} for p in patients]), 200

# Route to create a new appointment
@app.route('/appointments', methods=['POST'])
def add_appointment():
    json_data = request.get_json()
    try:
        data = AppointmentSchema().load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    patient = Patient.query.get(data['patient_id'])
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    new_appointment = Appointment(patient_id=data['patient_id'], date=data['date'], treatment_plan=data.get('treatment_plan'))
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({"id": new_appointment.id, "patient_id": new_appointment.patient_id, "date": new_appointment.date.isoformat(), "treatment_plan": new_appointment.treatment_plan}), 201

# Route to get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([{"id": a.id, "patient_id": a.patient_id, "date": a.date.isoformat(), "treatment_plan": a.treatment_plan} for a in appointments]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
