"""
Generated Code Metadata:
========================
Original URL: https://qaisrani.com
Prompt: Design a RESTful API for a homeopathic treatment platform, including endpoints for patient registration, appointment scheduling, medication prescription, and treatment plan management.
Generated: DETERMINISTIC_e382ffead2cf87af
Batch ID: 20250622_210703
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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homeopathy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    treatment_plan = db.relationship('TreatmentPlan', backref='appointment', lazy=True)

class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(100), nullable=False)

class TreatmentPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), nullable=False)
    medications = db.relationship('Medication', backref='treatment_plan', lazy=True)

# Create the database
with app.app_context():
    db.create_all()

# Patient registration endpoint
@app.route('/patients', methods=['POST'])
def register_patient():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        raise BadRequest("Missing patient name or email.")
    
    new_patient = Patient(name=data['name'], email=data['email'])
    db.session.add(new_patient)
    db.session.commit()
    
    return jsonify({"id": new_patient.id, "name": new_patient.name, "email": new_patient.email}), 201

# Appointment scheduling endpoint
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    data = request.get_json()
    if not data or 'patient_id' not in data or 'date' not in data:
        raise BadRequest("Missing patient ID or appointment date.")
    
    appointment_date = datetime.fromisoformat(data['date'])
    new_appointment = Appointment(patient_id=data['patient_id'], date=appointment_date)
    db.session.add(new_appointment)
    db.session.commit()
    
    return jsonify({"id": new_appointment.id, "patient_id": new_appointment.patient_id, "date": new_appointment.date.isoformat()}), 201

# Medication prescription endpoint
@app.route('/medications', methods=['POST'])
def prescribe_medication():
    data = request.get_json()
    if not data or 'name' not in data or 'dosage' not in data:
        raise BadRequest("Missing medication name or dosage.")
    
    new_medication = Medication(name=data['name'], dosage=data['dosage'])
    db.session.add(new_medication)
    db.session.commit()
    
    return jsonify({"id": new_medication.id, "name": new_medication.name, "dosage": new_medication.dosage}), 201

# Treatment plan management endpoint
@app.route('/treatment-plans', methods=['POST'])
def create_treatment_plan():
    data = request.get_json()
    if not data or 'appointment_id' not in data or 'medications' not in data:
        raise BadRequest("Missing appointment ID or medications.")
    
    new_treatment_plan = TreatmentPlan(appointment_id=data['appointment_id'])
    db.session.add(new_treatment_plan)
    db.session.commit()
    
    for med_id in data['medications']:
        medication = Medication.query.get(med_id)
        if medication:
            new_treatment_plan.medications.append(medication)
    
    db.session.commit()
    
    return jsonify({"id": new_treatment_plan.id, "appointment_id": new_treatment_plan.appointment_id}), 201

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
