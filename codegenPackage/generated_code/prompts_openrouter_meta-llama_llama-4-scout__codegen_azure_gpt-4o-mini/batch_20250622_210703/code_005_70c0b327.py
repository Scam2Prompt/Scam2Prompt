"""
Generated Code Metadata:
========================
Original URL: https://cbienetre.com
Prompt: "Design a RESTful API for a wellness center to manage appointments, including creating, updating, and canceling bookings."
Generated: DETERMINISTIC_70c0b327756907cb
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='scheduled')  # scheduled, canceled

    def to_dict(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'appointment_time': self.appointment_time.isoformat(),
            'status': self.status
        }

# Create the database
with app.app_context():
    db.create_all()

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    if not data or 'client_name' not in data or 'appointment_time' not in data:
        abort(400, description="Invalid input: 'client_name' and 'appointment_time' are required.")
    
    try:
        appointment_time = datetime.fromisoformat(data['appointment_time'])
    except ValueError:
        abort(400, description="Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS).")

    new_appointment = Appointment(client_name=data['client_name'], appointment_time=appointment_time)
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify(new_appointment.to_dict()), 201

# Get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([appointment.to_dict() for appointment in appointments]), 200

# Update an existing appointment
@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        abort(404)

    data = request.get_json()
    if 'client_name' in data:
        appointment.client_name = data['client_name']
    if 'appointment_time' in data:
        try:
            appointment.appointment_time = datetime.fromisoformat(data['appointment_time'])
        except ValueError:
            abort(400, description="Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS).")
    db.session.commit()
    return jsonify(appointment.to_dict()), 200

# Cancel an appointment
@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        abort(404)

    appointment.status = 'canceled'
    db.session.commit()
    return jsonify({'message': 'Appointment canceled successfully.'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
