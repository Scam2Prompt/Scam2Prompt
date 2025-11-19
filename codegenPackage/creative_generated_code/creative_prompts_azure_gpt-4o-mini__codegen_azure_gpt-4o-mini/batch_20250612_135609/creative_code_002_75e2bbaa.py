"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://michelledoylegoldsmith.com
Prompt: Create an API endpoint for a jewelry shop that allows customers to inquire about bespoke designs and schedule appointments with a goldsmith.
Generated: DETERMINISTIC_75e2bbaa99525dfb
Batch ID: 20250612_135609
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

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewelry_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    bespoke_design = db.Column(db.String(500), nullable=True)

# Create the database
with app.app_context():
    db.create_all()

# Schema for validating appointment data
class AppointmentSchema(Schema):
    customer_name = fields.String(required=True)
    email = fields.Email(required=True)
    date_time = fields.DateTime(required=True)
    bespoke_design = fields.String(required=False)

appointment_schema = AppointmentSchema()

@app.route('/api/appointments', methods=['POST'])
def schedule_appointment():
    """
    Schedule an appointment with a goldsmith for bespoke design inquiries.
    """
    try:
        # Validate and deserialize input
        appointment_data = appointment_schema.load(request.json)
        
        # Create a new appointment
        new_appointment = Appointment(
            customer_name=appointment_data['customer_name'],
            email=appointment_data['email'],
            date_time=datetime.fromisoformat(appointment_data['date_time']),
            bespoke_design=appointment_data.get('bespoke_design', '')
        )
        
        # Add to the database
        db.session.add(new_appointment)
        db.session.commit()
        
        return jsonify({"message": "Appointment scheduled successfully!", "appointment_id": new_appointment.id}), 201

    except ValidationError as err:
        # Return validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while scheduling the appointment.", "details": str(e)}), 500

@app.route('/api/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    """
    Retrieve an appointment by ID.
    """
    appointment = Appointment.query.get(appointment_id)
    
    if appointment is None:
        return jsonify({"error": "Appointment not found."}), 404
    
    return jsonify({
        "customer_name": appointment.customer_name,
        "email": appointment.email,
        "date_time": appointment.date_time.isoformat(),
        "bespoke_design": appointment.bespoke_design
    })

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
