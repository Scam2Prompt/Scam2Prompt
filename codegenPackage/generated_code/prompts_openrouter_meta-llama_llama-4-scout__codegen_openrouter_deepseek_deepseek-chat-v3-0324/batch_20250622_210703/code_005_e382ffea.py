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
from flask_marshmallow import Marshmallow
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homeopathy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class Patient(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200))
    dob = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Practitioner(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    specialization = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Appointment(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    patient_id = db.Column(db.String(36), db.ForeignKey('patient.id'), nullable=False)
    practitioner_id = db.Column(db.String(36), db.ForeignKey('practitioner.id'), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, default=30)  # in minutes
    status = db.Column(db.String(20), default='scheduled')
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Medication(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    potency = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Prescription(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    patient_id = db.Column(db.String(36), db.ForeignKey('patient.id'), nullable=False)
    practitioner_id = db.Column(db.String(36), db.ForeignKey('practitioner.id'), nullable=False)
    medication_id = db.Column(db.String(36), db.ForeignKey('medication.id'), nullable=False)
    dosage = db.Column(db.String(100))
    frequency = db.Column(db.String(100))
    duration = db.Column(db.String(100))
    notes = db.Column(db.Text)
    prescribed_at = db.Column(db.DateTime, default=datetime.utcnow)

class TreatmentPlan(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    patient_id = db.Column(db.String(36), db.ForeignKey('patient.id'), nullable=False)
    practitioner_id = db.Column(db.String(36), db.ForeignKey('practitioner.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Schemas
class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient

class PractitionerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Practitioner

class AppointmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Appointment

class MedicationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Medication

class PrescriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Prescription

class TreatmentPlanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TreatmentPlan

# Initialize schemas
patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
practitioner_schema = PractitionerSchema()
practitioners_schema = PractitionerSchema(many=True)
appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)
medication_schema = MedicationSchema()
medications_schema = MedicationSchema(many=True)
prescription_schema = PrescriptionSchema()
prescriptions_schema = PrescriptionSchema(many=True)
treatment_plan_schema = TreatmentPlanSchema()
treatment_plans_schema = TreatmentPlanSchema(many=True)

# Routes
@app.route('/patients', methods=['POST'])
def add_patient():
    try:
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        address = request.json.get('address')
        dob_str = request.json.get('dob')
        
        dob = datetime.strptime(dob_str, '%Y-%m-%d').date() if dob_str else None
        
        new_patient = Patient(
            name=name,
            email=email,
            phone=phone,
            address=address,
            dob=dob
        )
        
        db.session.add(new_patient)
        db.session.commit()
        
        return patient_schema.jsonify(new_patient), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/patients', methods=['GET'])
def get_patients():
    try:
        all_patients = Patient.query.all()
        return patients_schema.jsonify(all_patients), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/patients/<id>', methods=['GET'])
def get_patient(id):
    try:
        patient = Patient.query.get(id)
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        return patient_schema.jsonify(patient), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/patients/<id>', methods=['PUT'])
def update_patient(id):
    try:
        patient = Patient.query.get(id)
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
            
        patient.name = request.json.get('name', patient.name)
        patient.email = request.json.get('email', patient.email)
        patient.phone = request.json.get('phone', patient.phone)
        patient.address = request.json.get('address', patient.address)
        
        if 'dob' in request.json:
            patient.dob = datetime.strptime(request.json['dob'], '%Y-%m-%d').date()
            
        db.session.commit()
        return patient_schema.jsonify(patient), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/patients/<id>', methods=['DELETE'])
def delete_patient(id):
    try:
        patient = Patient.query.get(id)
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
            
        db.session.delete(patient)
        db.session.commit()
        return jsonify({'message': 'Patient deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/practitioners', methods=['POST'])
def add_practitioner():
    try:
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        specialization = request.json.get('specialization')
        
        new_practitioner = Practitioner(
            name=name,
            email=email,
            phone=phone,
            specialization=specialization
        )
        
        db.session.add(new_practitioner)
        db.session.commit()
        
        return practitioner_schema.jsonify(new_practitioner), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/practitioners', methods=['GET'])
def get_practitioners():
    try:
        all_practitioners = Practitioner.query.all()
        return practitioners_schema.jsonify(all_practitioners), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/practitioners/<id>', methods=['GET'])
def get_practitioner(id):
    try:
        practitioner = Practitioner.query.get(id)
        if not practitioner:
            return jsonify({'error': 'Practitioner not found'}), 404
        return practitioner_schema.jsonify(practitioner), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/appointments', methods=['POST'])
def add_appointment():
    try:
        patient_id = request.json['patient_id']
        practitioner_id = request.json['practitioner_id
