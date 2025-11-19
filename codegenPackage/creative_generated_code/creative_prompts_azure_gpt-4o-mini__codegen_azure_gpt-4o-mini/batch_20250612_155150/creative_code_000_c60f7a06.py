"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: How can I implement a mobile service for ultrasonic fuel injector cleaning based on the techniques used by specialists in Brisbane?
Generated: DETERMINISTIC_c60f7a06697e638f
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fuel_injector_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing service appointments
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    vehicle_model = db.Column(db.String(100), nullable=False)
    service_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default="Scheduled")

    def to_dict(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "vehicle_model": self.vehicle_model,
            "service_date": self.service_date.isoformat(),
            "status": self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/appointments', methods=['POST'])
def create_appointment():
    """Create a new service appointment."""
    try:
        data = request.json
        new_appointment = Appointment(
            customer_name=data['customer_name'],
            vehicle_model=data['vehicle_model'],
            service_date=datetime.fromisoformat(data['service_date'])
        )
        db.session.add(new_appointment)
        db.session.commit()
        return jsonify(new_appointment.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """Retrieve all service appointments."""
    try:
        appointments = Appointment.query.all()
        return jsonify([appointment.to_dict() for appointment in appointments]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    """Update an existing service appointment."""
    try:
        appointment = Appointment.query.get_or_404(appointment_id)
        data = request.json
        appointment.status = data.get('status', appointment.status)
        db.session.commit()
        return jsonify(appointment.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    """Delete a service appointment."""
    try:
        appointment = Appointment.query.get_or_404(appointment_id)
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({"message": "Appointment deleted"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- This code snippet creates a simple RESTful API for managing ultrasonic fuel injector cleaning service appointments using Flask and SQLAlchemy.
- The code includes error handling and appropriate HTTP response codes.
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment to run this code.
