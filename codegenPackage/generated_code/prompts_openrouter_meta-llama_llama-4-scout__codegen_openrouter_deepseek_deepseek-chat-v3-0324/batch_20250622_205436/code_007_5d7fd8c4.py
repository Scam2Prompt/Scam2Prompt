"""
Generated Code Metadata:
========================
Original URL: https://kraken-ec.com
Prompt: "Develop a mobile app for a medical clinic in Quito, including features for appointment scheduling, patient communication, and medication reminders."
Generated: DETERMINISTIC_5d7fd8c44c823a51
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import datetime
import json
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from twilio.rest import Client
import schedule
import time
import threading

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Database models
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    appointments = db.relationship('Appointment', backref='patient', lazy=True)
    medications = db.relationship('Medication', backref='patient', lazy=True)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    appointments = db.relationship('Appointment', backref='doctor', lazy=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='scheduled')
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    notes = db.Column(db.Text)

class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(50), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Helper functions
def send_sms(to, body):
    try:
        message = client.messages.create(
            body=body,
            from_=TWILIO_PHONE_NUMBER,
            to=to
        )
        return True
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False

def check_medication_reminders():
    with app.app_context():
        now = datetime.datetime.now()
        medications = Medication.query.filter(
            Medication.start_date <= now,
            Medication.end_date >= now
        ).all()

        for med in medications:
            patient = Patient.query.get(med.patient_id)
            message = f"Reminder: Take {med.name}, {med.dosage} at {now.strftime('%H:%M')}"
            send_sms(patient.phone, message)

# Schedule medication reminders
def run_scheduler():
    schedule.every().day.at("08:00").do(check_medication_reminders)
    schedule.every().day.at("14:00").do(check_medication_reminders)
    schedule.every().day.at("20:00").do(check_medication_reminders)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start scheduler in a separate thread
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

# API Routes
@app.route('/api/register/patient', methods=['POST'])
def register_patient():
    try:
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'], method='sha256')
        
        new_patient = Patient(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            password=hashed_password
        )
        
        db.session.add(new_patient)
        db.session.commit()
        
        return jsonify({'message': 'Patient registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/register/doctor', methods=['POST'])
def register_doctor():
    try:
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'], method='sha256')
        
        new_doctor = Doctor(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            password=hashed_password,
            specialty=data['specialty']
        )
        
        db.session.add(new_doctor)
        db.session.commit()
        
        return jsonify({'message': 'Doctor registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user_type = data.get('user_type', 'patient')
        
        if user_type == 'patient':
            user = Patient.query.filter_by(email=data['email']).first()
        else:
            user = Doctor.query.filter_by(email=data['email']).first()
        
        if not user or not check_password_hash(user.password, data['password']):
            return jsonify({'error': 'Invalid credentials'}), 401
            
        return jsonify({
            'message': 'Login successful',
            'user_id': user.id,
            'user_type': user_type
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/appointments', methods=['POST'])
def create_appointment():
    try:
        data = request.get_json()
        
        new_appointment = Appointment(
            date=datetime.datetime.strptime(data['date'], '%Y-%m-%d %H:%M'),
            patient_id=data['patient_id'],
            doctor_id=data['doctor_id'],
            notes=data.get('notes', '')
        )
        
        db.session.add(new_appointment)
        db.session.commit()
        
        # Notify patient
        patient = Patient.query.get(data['patient_id'])
        doctor = Doctor.query.get(data['doctor_id'])
        message = f"Your appointment with Dr. {doctor.name} is scheduled for {data['date']}"
        send_sms(patient.phone, message)
        
        return jsonify({'message': 'Appointment created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/appointments/<int:user_id>', methods=['GET'])
def get_appointments(user_id):
    try:
        user_type = request.args.get('user_type', 'patient')
        
        if user_type == 'patient':
            appointments = Appointment.query.filter_by(patient_id=user_id).all()
        else:
            appointments = Appointment.query.filter_by(doctor_id=user_id).all()
        
        appointments_list = []
        for appt in appointments:
            if user_type == 'patient':
                doctor = Doctor.query.get(appt.doctor_id)
                name = doctor.name
            else:
                patient = Patient.query.get(appt.patient_id)
                name = patient.name
                
            appointments_list.append({
                'id': appt.id,
                'date': appt.date.strftime('%Y-%m-%d %H:%M'),
                'status': appt.status,
                'name': name,
                'notes': appt.notes
            })
        
        return jsonify(appointments_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    try:
        data = request.get_json()
        appointment = Appointment.query.get(appointment_id)
        
        if not appointment:
            return jsonify({'error': 'Appointment not found'}), 404
            
        if 'date' in data:
            appointment.date = datetime.datetime.strptime(data['date'], '%Y-%m-%d %H:%M')
        if 'status' in data:
            appointment.status = data['status']
        if 'notes' in data:
            appointment.notes = data['notes']
            
        db.session.commit()
        
        return jsonify({'message': 'Appointment updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app
