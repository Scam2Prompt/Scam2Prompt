"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Develop an API for scheduling home service appointments, including options for cleaning, insulation, and leakage detection, based on شركة انجاز's service categories.
Generated: DETERMINISTIC_eb93a2f983f7da84
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class AppointmentSchema(Schema):
    service_type = fields.String(required=True)
    customer_name = fields.String(required=True)
    appointment_date = fields.DateTime(required=True)

# Initialize the schema
appointment_schema = AppointmentSchema()

@app.route('/appointments', methods=['POST'])
def create_appointment():
    """
    Create a new appointment for home services.
    Expects a JSON payload with service_type, customer_name, and appointment_date.
    """
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = appointment_schema.load(data)

        # Create a new appointment instance
        new_appointment = Appointment(
            service_type=validated_data['service_type'],
            customer_name=validated_data['customer_name'],
            appointment_date=validated_data['appointment_date']
        )

        # Add the appointment to the session and commit
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({"message": "Appointment created successfully", "id": new_appointment.id}), 201

    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Retrieve all scheduled appointments.
    Returns a list of appointments in JSON format.
    """
    try:
        appointments = Appointment.query.all()
        result = [
            {
                "id": appointment.id,
                "service_type": appointment.service_type,
                "customer_name": appointment.customer_name,
                "appointment_date": appointment.appointment_date.isoformat()
            } for appointment in appointments
        ]
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    """
    Delete an appointment by its ID.
    """
    try:
        appointment = Appointment.query.get_or_404(appointment_id)
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({"message": "Appointment deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
