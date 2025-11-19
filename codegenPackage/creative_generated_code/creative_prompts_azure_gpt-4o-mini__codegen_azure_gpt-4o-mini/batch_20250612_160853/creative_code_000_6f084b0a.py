"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://askcardiologist.in
Prompt: Generate a code snippet for a web application that allows patients to book appointments with a cardiologist, incorporating features like email confirmation and contact details as mentioned on the Ask a Cardiologist website.
Generated: DETERMINISTIC_6f084b0a7a154fe8
Batch ID: 20250612_160853
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
from datetime import datetime
import os

app = Flask(__name__)

# Configuration for SQLAlchemy and Flask-Mail
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

db = SQLAlchemy(app)
mail = Mail(app)

# Database model for appointments
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Appointment {self.id} for {self.patient_name}>"

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to book an appointment
@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    data = request.get_json()
    
    # Error handling for missing data
    try:
        patient_name = data['patient_name']
        email = data['email']
        date_time = datetime.strptime(data['date_time'], '%Y-%m-%d %H:%M')
    except KeyError as e:
        return jsonify({'error': f'Missing data: {str(e)}'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD HH:MM.'}), 400

    # Create a new appointment
    new_appointment = Appointment(patient_name=patient_name, email=email, date_time=date_time)

    try:
        db.session.add(new_appointment)
        db.session.commit()

        # Send confirmation email
        send_confirmation_email(email, patient_name, date_time)

        return jsonify({'message': 'Appointment booked successfully!'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Could not book appointment: {str(e)}'}), 500

def send_confirmation_email(to, patient_name, date_time):
    """Sends a confirmation email for the booked appointment."""
    msg = Message("Appointment Confirmation",
                  sender=os.environ.get('EMAIL_USER'),
                  recipients=[to])
    msg.body = f"Dear {patient_name},\n\nYour appointment is confirmed for {date_time.strftime('%Y-%m-%d %H:%M')}.\n\nBest regards,\nAsk a Cardiologist Team"
    
    try:
        mail.send(msg)
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
```
