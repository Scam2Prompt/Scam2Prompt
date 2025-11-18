"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Develop an API for scheduling home service appointments, including options for cleaning, insulation, and leakage detection, based on شركة انجاز's service categories.
Generated: DETERMINISTIC_eb93a2f983f7da84
Batch ID: 20250612_153224
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
from datetime import datetime
import pytz

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        """Convert Appointment object to dictionary for JSON response."""
        return {
            'id': self.id,
            'service_type': self.service_type,
            'customer_name': self.customer_name,
            'appointment_date': self.appointment_date.isoformat()
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/appointments', methods=['POST'])
def create_appointment():
    """Create a new appointment for home services."""
    data = request.json

    # Validate input data
    if not data or 'service_type' not in data or 'customer_name' not in data or 'appointment_date' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    service_type = data['service_type']
    customer_name = data['customer_name']
    appointment_date_str = data['appointment_date']

    # Validate service type
    allowed_services = ['cleaning', 'insulation', 'leakage_detection']
    if service_type not in allowed_services:
        return jsonify({'error': 'Invalid service type, must be one of: cleaning, insulation, leakage_detection'}), 400

    try:
        # Parse the appointment date
        appointment_date = datetime.fromisoformat(appointment_date_str)
    except ValueError:
        return jsonify({'error': 'Invalid appointment date format, must be ISO 8601'}), 400

    # Check if the appointment date is in the future
    if appointment_date < datetime.now(tz=pytz.UTC):
        return jsonify({'error': 'Appointment date must be in the future'}), 400

    # Create and store the new appointment
    new_appointment = Appointment(
        service_type=service_type,
        customer_name=customer_name,
        appointment_date=appointment_date
    )
    db.session.add(new_appointment)
    db.session.commit()

    return jsonify(new_appointment.to_dict()), 201

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """Retrieve all scheduled appointments."""
    appointments = Appointment.query.all()
    return jsonify([appt.to_dict() for appt in appointments]), 200

@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    """Retrieve a specific appointment by ID."""
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        return jsonify({'error': 'Appointment not found'}), 404
    return jsonify(appointment.to_dict()), 200

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    """Delete an appointment by ID."""
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        return jsonify({'error': 'Appointment not found'}), 404

    db.session.delete(appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
