"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocat.com
Prompt: Suggest an API for integrating appointment scheduling and case updates for a law firm specializing in family and criminal law, referencing Majeli Avocat's client-focused approach and services.
Generated: DETERMINISTIC_beb0aabcaa4abf06
Batch ID: 20250612_151912
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
from marshmallow import Schema, fields, ValidationError
import pytz

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    case_type = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.Text, nullable=True)

# Define schema for input validation and serialization
class AppointmentSchema(Schema):
    client_name = fields.String(required=True)
    date_time = fields.DateTime(required=True)
    case_type = fields.String(required=True)
    notes = fields.String(allow_none=True)

appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    try:
        # Validate and deserialize input
        data = request.get_json()
        appointment_data = appointment_schema.load(data)

        # Create and save appointment
        new_appointment = Appointment(
            client_name=appointment_data['client_name'],
            date_time=appointment_data['date_time'],
            case_type=appointment_data['case_type'],
            notes=appointment_data.get('notes')
        )
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify(appointment_schema.dump(new_appointment)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'message': 'Error creating appointment', 'error': str(e)}), 500

# Endpoint to retrieve all appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    try:
        appointments = Appointment.query.all()
        return jsonify(appointments_schema.dump(appointments)), 200
    except Exception as e:
        return jsonify({'message': 'Error retrieving appointments', 'error': str(e)}), 500

# Endpoint to update an appointment
@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    try:
        # Validate and load data
        data = request.get_json()
        appointment_data = appointment_schema.load(data)

        # Find appointment and update
        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return jsonify({'message': 'Appointment not found'}), 404

        appointment.client_name = appointment_data['client_name']
        appointment.date_time = appointment_data['date_time']
        appointment.case_type = appointment_data['case_type']
        appointment.notes = appointment_data.get('notes')
        db.session.commit()

        return jsonify(appointment_schema.dump(appointment)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'message': 'Error updating appointment', 'error': str(e)}), 500

# Endpoint to delete an appointment
@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    try:
        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return jsonify({'message': 'Appointment not found'}), 404

        db.session.delete(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment deleted successfully'}), 204
    except Exception as e:
        return jsonify({'message': 'Error deleting appointment', 'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
