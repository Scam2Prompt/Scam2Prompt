"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Design a RESTful API using Flask or Django to manage appointment bookings for Red Horse Reflexology, including endpoints for creating, reading, updating, and deleting appointments.
Generated: DETERMINISTIC_dde25bbc50cf4f41
Batch ID: 20250622_210650
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
    service_type = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'appointment_time': self.appointment_time.isoformat(),
            'service_type': self.service_type
        }

# Create the database
with app.app_context():
    db.create_all()

# Endpoint to create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    if not data or 'client_name' not in data or 'appointment_time' not in data or 'service_type' not in data:
        abort(400, description="Invalid input data")

    new_appointment = Appointment(
        client_name=data['client_name'],
        appointment_time=datetime.fromisoformat(data['appointment_time']),
        service_type=data['service_type']
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify(new_appointment.to_dict()), 201

# Endpoint to get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([appointment.to_dict() for appointment in appointments]), 200

# Endpoint to get a specific appointment by ID
@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        abort(404, description="Appointment not found")
    return jsonify(appointment.to_dict()), 200

# Endpoint to update an existing appointment
@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        abort(404, description="Appointment not found")

    data = request.get_json()
    if 'client_name' in data:
        appointment.client_name = data['client_name']
    if 'appointment_time' in data:
        appointment.appointment_time = datetime.fromisoformat(data['appointment_time'])
    if 'service_type' in data:
        appointment.service_type = data['service_type']

    db.session.commit()
    return jsonify(appointment.to_dict()), 200

# Endpoint to delete an appointment
@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        abort(404, description="Appointment not found")

    db.session.delete(appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment deleted successfully'}), 204

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handling for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
