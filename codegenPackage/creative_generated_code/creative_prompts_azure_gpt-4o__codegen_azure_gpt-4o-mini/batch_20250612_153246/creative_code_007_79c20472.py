"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reparaciondeturbo.cl
Prompt: Develop a REST API for a diesel turbo repair service that allows users to submit diagnostic data, book appointments, and receive repair status updates.
Generated: DETERMINISTIC_79c20472b94aa0f2
Batch ID: 20250612_153246
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

# Configure the database URI (example using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diesel_turbo_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    diagnostic_data = db.Column(db.String(500), nullable=True)
    appointment_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default='Pending')

# Create a schema for request validation
class AppointmentSchema(Schema):
    customer_name = fields.Str(required=True)
    diagnostic_data = fields.Str(required=False)
    appointment_date = fields.DateTime(required=True)

# Initialize the appointment schema
appointment_schema = AppointmentSchema()

# Create the database tables if they do not exist
with app.app_context():
    db.create_all()

# Route to submit diagnostic data and book an appointment
@app.route('/appointments', methods=['POST'])
def book_appointment():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = appointment_schema.load(data)

        # Create a new appointment
        new_appointment = Appointment(
            customer_name=validated_data['customer_name'],
            diagnostic_data=validated_data.get('diagnostic_data', ''),
            appointment_date=validated_data['appointment_date']
        )
        
        # Add and commit the new appointment to the database
        db.session.add(new_appointment)
        db.session.commit()
        
        return jsonify({"message": "Appointment booked successfully!", "appointment_id": new_appointment.id}), 201

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get the appointment status
@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment_status(appointment_id):
    try:
        appointment = Appointment.query.get_or_404(appointment_id)
        return jsonify({
            "id": appointment.id,
            "customer_name": appointment.customer_name,
            "diagnostic_data": appointment.diagnostic_data,
            "appointment_date": appointment.appointment_date.isoformat(),
            "status": appointment.status
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update the appointment status
@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment_status(appointment_id):
    try:
        data = request.get_json()
        appointment = Appointment.query.get_or_404(appointment_id)

        # Update the status if provided
        if 'status' in data:
            appointment.status = data['status']

        # Commit the changes to the database
        db.session.commit()
        
        return jsonify({"message": "Appointment status updated successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
