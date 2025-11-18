"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Recommend a library or API for implementing a web-based booking system for medical clinics, specifically for scheduling exams like pHmetria esofágica and retossigmoidoscopia, as described on the Gastrolife website.
Generated: DETERMINISTIC_04f8c8dc6b1ca558
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python example using the Flask framework along with SQLAlchemy for implementing a web-based booking system. It includes routes for scheduling medical exams like pHmetria esofágica and retossigmoidoscopia.

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'  # Database in SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    exam_type = db.Column(db.String(50), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route: Register a new patient
@app.route('/patients', methods=['POST'])
def register_patient():
    try:
        data = request.json
        new_patient = Patient(name=data['name'], email=data['email'])
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({"message": "Patient registered successfully", "patient_id": new_patient.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route: Book an appointment
@app.route('/appointments', methods=['POST'])
def book_appointment():
    try:
        data = request.json
        patient = Patient.query.get(data['patient_id'])
        if not patient:
            return jsonify({"error": "Patient not found"}), 404
        
        # Validate exam type
        valid_exams = ['pHmetria esofágica', 'retossigmoidoscopia']
        if data['exam_type'] not in valid_exams:
            return jsonify({"error": "Invalid exam type"}), 400
        
        # Create appointment
        appointment = Appointment(
            patient_id=data['patient_id'],
            exam_type=data['exam_type'],
            date_time=datetime.strptime(data['date_time'], '%Y-%m-%d %H:%M:%S')
        )
        db.session.add(appointment)
        db.session.commit()
        return jsonify({"message": "Appointment booked successfully", "appointment_id": appointment.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route: List all appointments
@app.route('/appointments', methods=['GET'])
def list_appointments():
    try:
        appointments = Appointment.query.all()
        result = []
        for appointment in appointments:
            patient = Patient.query.get(appointment.patient_id)
            result.append({
                "appointment_id": appointment.id,
                "patient_name": patient.name,
                "patient_email": patient.email,
                "exam_type": appointment.exam_type,
                "date_time": appointment.date_time.strftime('%Y-%m-%d %H:%M:%S')
            })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Cancel an appointment
@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    try:
        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return jsonify({"error": "Appointment not found"}), 404
        
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({"message": "Appointment canceled successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Installation Instructions:
1. Install the required libraries:
   ```bash
   pip install flask flask-sqlalchemy
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Use tools like Postman or cURL to interact with the API endpoints.
