"""
Generated Code Metadata:
========================
Original URL: https://samaalnaser.co
Prompt: What are the best practices for developing a remote medical consultation application like the Tadawy Application from Sama Al-Naser Group, and can you provide a sample API structure?
Generated: DETERMINISTIC_9bc863adfd2b79d6
Batch ID: 20250612_161700
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
from werkzeug.exceptions import NotFound, BadRequest
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical_consultation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Define the Doctor model
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

# Define the Consultation model
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    date_time = db.Column(db.String(100), nullable=False)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new patient
@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        raise BadRequest("Missing patient name or email.")
    
    new_patient = Patient(name=data['name'], email=data['email'])
    db.session.add(new_patient)
    db.session.commit()
    
    return jsonify({"id": new_patient.id, "name": new_patient.name, "email": new_patient.email}), 201

# API endpoint to create a new doctor
@app.route('/doctors', methods=['POST'])
def create_doctor():
    data = request.get_json()
    if not data or 'name' not in data or 'specialty' not in data:
        raise BadRequest("Missing doctor name or specialty.")
    
    new_doctor = Doctor(name=data['name'], specialty=data['specialty'])
    db.session.add(new_doctor)
    db.session.commit()
    
    return jsonify({"id": new_doctor.id, "name": new_doctor.name, "specialty": new_doctor.specialty}), 201

# API endpoint to schedule a consultation
@app.route('/consultations', methods=['POST'])
def schedule_consultation():
    data = request.get_json()
    if not data or 'patient_id' not in data or 'doctor_id' not in data or 'date_time' not in data:
        raise BadRequest("Missing patient_id, doctor_id, or date_time.")
    
    new_consultation = Consultation(patient_id=data['patient_id'], doctor_id=data['doctor_id'], date_time=data['date_time'])
    db.session.add(new_consultation)
    db.session.commit()
    
    return jsonify({"id": new_consultation.id, "patient_id": new_consultation.patient_id, "doctor_id": new_consultation.doctor_id, "date_time": new_consultation.date_time}), 201

# API endpoint to get all consultations
@app.route('/consultations', methods=['GET'])
def get_consultations():
    consultations = Consultation.query.all()
    return jsonify([{"id": c.id, "patient_id": c.patient_id, "doctor_id": c.doctor_id, "date_time": c.date_time} for c in consultations]), 200

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
