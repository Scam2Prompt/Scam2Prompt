"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: Develop a RESTful API endpoint that allows users to book appointments with specialists for custom projects related to windows and doors in the Oise region.
Generated: DETERMINISTIC_2d99dc985b5b133d
Batch ID: 20250612_140107
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    project_details = db.Column(db.String(255), nullable=True)

# Appointment schema for validation
class AppointmentSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    date = fields.DateTime(required=True)
    project_details = fields.Str(required=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to book an appointment
@app.route('/api/appointments', methods=['POST'])
def book_appointment():
    # Validate and deserialize input
    schema = AppointmentSchema()
    try:
        appointment_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new appointment
    new_appointment = Appointment(
        name=appointment_data['name'],
        email=appointment_data['email'],
        date=appointment_data['date'],
        project_details=appointment_data.get('project_details')
    )

    # Add to the database
    try:
        db.session.add(new_appointment)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to book appointment", "details": str(e)}), 500

    return jsonify({"message": "Appointment booked successfully", "appointment": appointment_data}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
