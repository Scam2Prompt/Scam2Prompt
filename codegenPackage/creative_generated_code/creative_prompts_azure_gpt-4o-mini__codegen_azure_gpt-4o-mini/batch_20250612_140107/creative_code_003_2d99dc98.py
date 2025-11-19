"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-menuiserie.fr
Prompt: Develop a RESTful API endpoint that allows users to book appointments with specialists for custom projects related to windows and doors in the Oise region.
Generated: DETERMINISTIC_2d99dc985b5b133d
Batch ID: 20250612_140107
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    project_details = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for validating the appointment data
class AppointmentSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    date_time = fields.DateTime(required=True)
    project_details = fields.Str(required=True)

# Endpoint to book an appointment
@app.route('/api/appointments', methods=['POST'])
def book_appointment():
    schema = AppointmentSchema()
    
    # Validate the incoming JSON data
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new appointment instance
    new_appointment = Appointment(
        name=data['name'],
        email=data['email'],
        date_time=data['date_time'],
        project_details=data['project_details']
    )
    
    # Add the appointment to the database
    db.session.add(new_appointment)
    
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to book appointment", "details": str(e)}), 500

    return jsonify({"message": "Appointment booked successfully", "appointment_id": new_appointment.id}), 201

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
