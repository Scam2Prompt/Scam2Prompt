"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safesteth.com
Prompt: Describe how to set up a consultation booking system using a library that allows users to find and book appointments with local doctors, similar to the services provided by SafeSteth.com.
Generated: DETERMINISTIC_1dbda8cd72b85c88
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for the Doctor
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

# Model for the Appointment
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    patient_name = db.Column(db.String(100), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)

# Route to create a new doctor
@app.route('/doctors', methods=['POST'])
def add_doctor():
    """Adds a new doctor to the system."""
    data = request.get_json()
    new_doctor = Doctor(name=data['name'], specialty=data['specialty'])
    
    db.session.add(new_doctor)
    try:
        db.session.commit()
        return jsonify({"message": "Doctor added successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Doctor could not be added."}), 400

# Route to book an appointment
@app.route('/appointments', methods=['POST'])
def book_appointment():
    """Books a new appointment with a doctor."""
    data = request.get_json()
    appointment_time = datetime.strptime(data['appointment_time'], '%Y-%m-%d %H:%M:%S')
    new_appointment = Appointment(
        doctor_id=data['doctor_id'],
        patient_name=data['patient_name'],
        appointment_time=appointment_time
    )
    
    db.session.add(new_appointment)
    try:
        db.session.commit()
        return jsonify({"message": "Appointment booked successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Appointment could not be booked."}), 400

# Route to view available doctors
@app.route('/doctors', methods=['GET'])
def get_doctors():
    """Retrieves a list of all doctors."""
    doctors = Doctor.query.all()
    return jsonify([{ 'id': doctor.id, 'name': doctor.name, 'specialty': doctor.specialty } for doctor in doctors]), 200

# Initialize the database (create tables)
@app.before_first_request
def create_tables():
    """Creates database tables before the first request."""
    db.create_all()

# Main entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
