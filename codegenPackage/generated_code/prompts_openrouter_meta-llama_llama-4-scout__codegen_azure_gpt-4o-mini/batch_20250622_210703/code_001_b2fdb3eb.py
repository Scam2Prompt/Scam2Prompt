"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Recommend APIs or libraries for creating a web application to book appointments for tire and wheel services, considering features like mobile service requests.
Generated: DETERMINISTIC_b2fdb3ebedf57281
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///appointments.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    mobile_service = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Appointment {self.id} - {self.customer_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    try:
        data = request.get_json()
        new_appointment = Appointment(
            customer_name=data['customer_name'],
            service_type=data['service_type'],
            appointment_time=datetime.fromisoformat(data['appointment_time']),
            mobile_service=data.get('mobile_service', False)
        )
        db.session.add(new_appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment created successfully!', 'id': new_appointment.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    try:
        appointments = Appointment.query.all()
        return jsonify([{
            'id': appt.id,
            'customer_name': appt.customer_name,
            'service_type': appt.service_type,
            'appointment_time': appt.appointment_time.isoformat(),
            'mobile_service': appt.mobile_service
        } for appt in appointments]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a specific appointment by ID
@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    try:
        appointment = Appointment.query.get_or_404(appointment_id)
        return jsonify({
            'id': appointment.id,
            'customer_name': appointment.customer_name,
            'service_type': appointment.service_type,
            'appointment_time': appointment.appointment_time.isoformat(),
            'mobile_service': appointment.mobile_service
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Flask
- Flask-SQLAlchemy

### Instructions
1. Set up a virtual environment and install the required libraries.
2. Set the `DATABASE_URL` environment variable for production use.
3. Run the application and use a tool like Postman to test the API endpoints.
