"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Design a RESTful API for managing repair services for white goods, including endpoints for scheduling appointments, tracking repair status, and providing diagnostic information, inspired by the services offered on the Ankara Teknik Servisi website.
Generated: DETERMINISTIC_062785b5e8e8aa2a
Batch ID: 20250622_204722
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repair_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    appliance_type = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default='Scheduled')

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'appliance_type': self.appliance_type,
            'appointment_date': self.appointment_date.isoformat(),
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to schedule a new appointment
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    data = request.get_json()
    if not data or 'customer_name' not in data or 'appliance_type' not in data or 'appointment_date' not in data:
        abort(400, description="Invalid input data")

    try:
        appointment_date = datetime.fromisoformat(data['appointment_date'])
    except ValueError:
        abort(400, description="Invalid date format")

    new_appointment = Appointment(
        customer_name=data['customer_name'],
        appliance_type=data['appliance_type'],
        appointment_date=appointment_date
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
    appointment = Appointment.query.get_or_404(appointment_id)
    return jsonify(appointment.to_dict()), 200

# Endpoint to update the status of an appointment
@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment_status(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    data = request.get_json()
    if 'status' not in data:
        abort(400, description="Status is required")

    appointment.status = data['status']
    db.session.commit()
    return jsonify(appointment.to_dict()), 200

# Endpoint to provide diagnostic information
@app.route('/diagnostics', methods=['GET'])
def get_diagnostics():
    diagnostics_info = {
        "message": "For diagnostic information, please contact our support.",
        "support_contact": "support@ankaratservisi.com"
    }
    return jsonify(diagnostics_info), 200

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
