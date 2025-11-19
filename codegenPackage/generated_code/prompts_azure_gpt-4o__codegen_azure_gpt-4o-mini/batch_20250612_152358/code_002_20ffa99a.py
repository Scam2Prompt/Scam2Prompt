"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Create a REST API in Flask for a healthcare system inspired by SUS, allowing functionalities such as patient registration, assigning healthcare teams, and tracking referrals to hospitals or specialty clinics.
Generated: DETERMINISTIC_20ffa99af5bfa1cc
Batch ID: 20250612_152358
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
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    healthcare_team_id = db.Column(db.Integer, db.ForeignKey('healthcare_team.id'))

class HealthcareTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    patients = db.relationship('Patient', backref='healthcare_team', lazy=True)

class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    destination = db.Column(db.String(100), nullable=False)
    patient = db.relationship('Patient', backref='referrals', lazy=True)

# Schemas for validation
class PatientSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)

class HealthcareTeamSchema(Schema):
    name = fields.Str(required=True)

class ReferralSchema(Schema):
    patient_id = fields.Int(required=True)
    destination = fields.Str(required=True)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for patient registration
@app.route('/patients', methods=['POST'])
def register_patient():
    try:
        data = request.get_json()
        patient_schema = PatientSchema()
        validated_data = patient_schema.load(data)
        new_patient = Patient(**validated_data)
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({"message": "Patient registered successfully", "patient_id": new_patient.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Error registering patient"}), 500

# Route for assigning healthcare teams
@app.route('/healthcare_teams', methods=['POST'])
def create_healthcare_team():
    try:
        data = request.get_json()
        team_schema = HealthcareTeamSchema()
        validated_data = team_schema.load(data)
        new_team = HealthcareTeam(**validated_data)
        db.session.add(new_team)
        db.session.commit()
        return jsonify({"message": "Healthcare team created successfully", "team_id": new_team.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Error creating healthcare team"}), 500

# Route for tracking referrals
@app.route('/referrals', methods=['POST'])
def create_referral():
    try:
        data = request.get_json()
        referral_schema = ReferralSchema()
        validated_data = referral_schema.load(data)
        new_referral = Referral(**validated_data)
        db.session.add(new_referral)
        db.session.commit()
        return jsonify({"message": "Referral created successfully", "referral_id": new_referral.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Error creating referral"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
