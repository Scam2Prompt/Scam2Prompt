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
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    client_email = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convert Appointment object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'client_name': self.client_name,
            'client_email': self.client_email,
            'appointment_date': self.appointment_date.strftime('%Y-%m-%d %H:%M:%S'),
            'notes': self.notes
        }

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    try:
        data = request.json
        client_name = data.get('client_name')
        client_email = data.get('client_email')
        appointment_date = datetime.strptime(data.get('appointment_date'), '%Y-%m-%d %H:%M:%S')
        notes = data.get('notes', '')

        if not client_name or not client_email or not appointment_date:
            return jsonify({'error': 'Missing required fields'}), 400

        new_appointment = Appointment(
            client_name=client_name,
            client_email=client_email,
            appointment_date=appointment_date,
            notes=notes
        )
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify(new_appointment.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    try:
        appointments = Appointment.query.all()
        return jsonify([appointment.to_dict() for appointment in appointments]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get a single appointment by ID
@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    try:
        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return jsonify({'error': 'Appointment not found'}), 404
        return jsonify(appointment.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to update an appointment by ID
@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    try:
        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return jsonify({'error': 'Appointment not found'}), 404

        data = request.json
        appointment.client_name = data.get('client_name', appointment.client_name)
        appointment.client_email = data.get('client_email', appointment.client_email)
        if 'appointment_date' in data:
            appointment.appointment_date = datetime.strptime(data.get('appointment_date'), '%Y-%m-%d %H:%M:%S')
        appointment.notes = data.get('notes', appointment.notes)

        db.session.commit()
        return jsonify(appointment.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete an appointment by ID
@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    try:
        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return jsonify({'error': 'Appointment not found'}), 404

        db.session.delete(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
