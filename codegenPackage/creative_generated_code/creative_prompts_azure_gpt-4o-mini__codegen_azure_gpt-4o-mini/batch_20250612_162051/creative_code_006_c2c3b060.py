"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okulistatrzebnica.pl
Prompt: Design a mobile app feature that allows patients to view their prescription history and upcoming appointments at an eye clinic like "Okulista Trzebnica."
Generated: DETERMINISTIC_c2c3b060d7df27b4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Prescription model
class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    medication_name = db.Column(db.String(100), nullable=False)
    date_issued = db.Column(db.DateTime, default=datetime.utcnow)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.String(200))

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get prescription history for a specific patient
@app.route('/prescriptions/<int:patient_id>', methods=['GET'])
def get_prescriptions(patient_id):
    try:
        prescriptions = Prescription.query.filter_by(patient_id=patient_id).all()
        return jsonify([{
            'id': p.id,
            'medication_name': p.medication_name,
            'date_issued': p.date_issued.strftime('%Y-%m-%d %H:%M:%S')
        } for p in prescriptions]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get upcoming appointments for a specific patient
@app.route('/appointments/<int:patient_id>', methods=['GET'])
def get_appointments(patient_id):
    try:
        now = datetime.utcnow()
        appointments = Appointment.query.filter(Appointment.patient_id == patient_id,
                                                Appointment.appointment_date >= now).all()
        return jsonify([{
            'id': a.id,
            'appointment_date': a.appointment_date.strftime('%Y-%m-%d %H:%M:%S'),
            'reason': a.reason
        } for a in appointments]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code sets up a simple Flask web application with two endpoints to retrieve prescription history and upcoming appointments for patients at an eye clinic. It includes error handling and utilizes best practices for structuring the code.
