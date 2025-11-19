"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centroabakadabra.com
Prompt: Generate a code snippet for a web application that allows users to book appointments for psychological services at a multidisciplinary center like Centro Abakadabra.
Generated: DETERMINISTIC_6997476863fa1ea1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
db = SQLAlchemy(app)

# Model for Appointment
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Appointment {self.name} - {self.service}>"

# Schema for Appointment validation
class AppointmentSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    service = fields.Str(required=True)
    appointment_date = fields.DateTime(required=True)

# Initialize the appointment schema
appointment_schema = AppointmentSchema()

# Create database tables
with app.app_context():
    db.create_all()

# API endpoint to book an appointment
@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    try:
        # Validate and deserialize input data
        data = request.json
        appointment_data = appointment_schema.load(data)

        # Create a new appointment instance
        new_appointment = Appointment(
            name=appointment_data['name'],
            email=appointment_data['email'],
            service=appointment_data['service'],
            appointment_date=appointment_data['appointment_date']
        )

        # Save to the database
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({"message": "Appointment booked successfully!", "id": new_appointment.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```
