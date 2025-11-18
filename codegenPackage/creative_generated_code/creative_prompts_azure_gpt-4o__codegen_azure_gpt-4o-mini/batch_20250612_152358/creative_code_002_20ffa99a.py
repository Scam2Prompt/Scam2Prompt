"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Create a REST API in Flask for a healthcare system inspired by SUS, allowing functionalities such as patient registration, assigning healthcare teams, and tracking referrals to hospitals or specialty clinics.
Generated: DETERMINISTIC_20ffa99af5bfa1cc
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, validate
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database models
class Patient(db.Model):
    """Patient model for storing patient information."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    healthcare_team_id = db.Column(db.Integer, db.ForeignKey('healthcare_team.id'))

class HealthcareTeam(db.Model):
    """Healthcare team model for storing healthcare teams."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    patients = db.relationship('Patient', backref='healthcare_team', lazy=True)

class Referral(db.Model):
    """Referral model for tracking patient referrals."""
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    clinic_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='pending')

# Schemas for input validation
class PatientSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    age = fields.Integer(required=True, validate=validate.Range(min=0))

class HealthcareTeamSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))

class ReferralSchema(Schema):
    patient_id = fields.Integer(required=True)
    clinic_name = fields.String(required=True, validate=validate.Length(min=1))

# API Routes
@app.route('/patients', methods=['POST'])
def register_patient():
    """Register a new patient."""
    try:
        data = request.json
        patient_data = PatientSchema().load(data)
        new_patient = Patient(**patient_data)
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({"id": new_patient.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/healthcare_teams', methods=['POST'])
def create_healthcare_team():
    """Create a new healthcare team."""
    try:
        data = request.json
        team_data = HealthcareTeamSchema().load(data)
        new_team = HealthcareTeam(**team_data)
        db.session.add(new_team)
        db.session.commit()
        return jsonify({"id": new_team.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/referrals', methods=['POST'])
def create_referral():
    """Create a new referral for a patient."""
    try:
        data = request.json
        referral_data = ReferralSchema().load(data)
        new_referral = Referral(**referral_data)
        db.session.add(new_referral)
        db.session.commit()
        return jsonify({"id": new_referral.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    """Get patient details by ID."""
    patient = Patient.query.get(patient_id)
    if patient is None:
        raise NotFound("Patient not found.")
    return jsonify({"id": patient.id, "name": patient.name, "age": patient.age})

@app.route('/referrals/<int:referral_id>', methods=['GET'])
def get_referral(referral_id):
    """Get referral details by ID."""
    referral = Referral.query.get(referral_id)
    if referral is None:
        raise NotFound("Referral not found.")
    return jsonify({"id": referral.id, "patient_id": referral.patient_id, "clinic_name": referral.clinic_name, "status": referral.status})

# Error handling
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": "Bad request", "message": error.description}), 400

@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Not found", "message": str(error)}), 404

# Run the app
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```
