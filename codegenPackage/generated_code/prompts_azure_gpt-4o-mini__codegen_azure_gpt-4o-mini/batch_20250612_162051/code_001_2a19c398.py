"""
Generated Code Metadata:
========================
Original URL: https://amalfihospicecare.com
Prompt: Generate a REST API specification for a hospice care service that includes endpoints for patient intake, symptom tracking, and family support, inspired by the services offered by Amalfi Hospice Care.
Generated: DETERMINISTIC_2a19c398b29ea495
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospice_care.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    intake_date = db.Column(db.DateTime, default=datetime.utcnow)
    symptoms = db.relationship('Symptom', backref='patient', lazy=True)

# Symptom model
class Symptom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)

# Family Support model
class FamilySupport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    support_message = db.Column(db.String(200), nullable=False)

# Patient schema
class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient

# Symptom schema
class SymptomSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Symptom

# Family Support schema
class FamilySupportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FamilySupport

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint for patient intake
@app.route('/api/patients', methods=['POST'])
def add_patient():
    try:
        name = request.json['name']
        new_patient = Patient(name=name)
        db.session.add(new_patient)
        db.session.commit()
        return PatientSchema().jsonify(new_patient), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint for symptom tracking
@app.route('/api/patients/<int:patient_id>/symptoms', methods=['POST'])
def add_symptom(patient_id):
    try:
        description = request.json['description']
        new_symptom = Symptom(description=description, patient_id=patient_id)
        db.session.add(new_symptom)
        db.session.commit()
        return SymptomSchema().jsonify(new_symptom), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint for family support messages
@app.route('/api/patients/<int:patient_id>/support', methods=['POST'])
def add_family_support(patient_id):
    try:
        support_message = request.json['support_message']
        new_support = FamilySupport(support_message=support_message, patient_id=patient_id)
        db.session.add(new_support)
        db.session.commit()
        return FamilySupportSchema().jsonify(new_support), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
