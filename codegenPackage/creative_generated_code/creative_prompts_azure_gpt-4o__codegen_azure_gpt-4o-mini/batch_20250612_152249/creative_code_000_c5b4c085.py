"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://askcardiologist.in
Prompt: Write Python code to create a REST API for booking appointments with Dr. S. Nagendra Boopathy, including endpoints for patient details, available time slots, and confirmation emails.
Generated: DETERMINISTIC_c5b4c08598f6579a
Batch ID: 20250612_152249
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
from flask_mail import Mail, Message
from datetime import datetime, timedelta
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Initialize database
db = SQLAlchemy(app)
mail = Mail(app)

# Database model for Patient details
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)

# Database model for Appointment
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)

# Create necessary tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to book an appointment
@app.route('/api/appointments', methods=['POST'])
def book_appointment():
    data = request.get_json()
    try:
        patient = Patient.query.filter_by(email=data['email']).first()
        if not patient:
            patient = Patient(name=data['name'], email=data['email'], phone=data['phone'])
            db.session.add(patient)
            db.session.commit()

        appointment_time = datetime.strptime(data['appointment_time'], '%Y-%m-%d %H:%M')
        new_appointment = Appointment(patient_id=patient.id, appointment_time=appointment_time)
        db.session.add(new_appointment)
        db.session.commit()

        send_confirmation_email(patient.email, appointment_time)
        return jsonify({'message': 'Appointment booked successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to get available time slots
@app.route('/api/available-slots', methods=['GET'])
def available_slots():
    try:
        today = datetime.now()
        slots = []
        # Generate available time slots for the next week
        for i in range(7):
            date = today + timedelta(days=i)
            for hour in range(9, 17):  # From 9 AM to 5 PM
                slot_time = datetime(date.year, date.month, date.day, hour)
                if not Appointment.query.filter_by(appointment_time=slot_time).first():
                    slots.append(slot_time.strftime('%Y-%m-%d %H:%M'))

        return jsonify({'available_slots': slots}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to send confirmation email
def send_confirmation_email(email, appointment_time):
    msg = Message('Appointment Confirmation',
                  sender='noreply@example.com',
                  recipients=[email])
    msg.body = f'Your appointment is confirmed for {appointment_time.strftime("%Y-%m-%d %H:%M")}.'
    try:
        mail.send(msg)
    except Exception as e:
        print(f'Failed to send email: {str(e)}')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to replace `smtp.example.com` and the email credentials with your actual SMTP server details before running the code.
