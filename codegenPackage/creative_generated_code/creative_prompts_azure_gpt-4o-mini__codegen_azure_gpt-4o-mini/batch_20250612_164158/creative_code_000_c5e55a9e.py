"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-extension-web3-dapps.blogspot.com
Prompt: Generate a code snippet for a web application that integrates with a physiotherapy clinic's management system, focusing on patient tracking and appointment scheduling.
Generated: DETERMINISTIC_c5e55a9eb76b20e1
Batch ID: 20250612_164158
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.String(200), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to add a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            raise BadRequest("Missing patient information.")
        
        new_patient = Patient(name=data['name'], email=data['email'])
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({"id": new_patient.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to schedule a new appointment
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    try:
        data = request.get_json()
        if not data or 'patient_id' not in data or 'date' not in data or 'reason' not in data:
            raise BadRequest("Missing appointment information.")
        
        appointment_date = datetime.fromisoformat(data['date'])
        new_appointment = Appointment(patient_id=data['patient_id'], date=appointment_date, reason=data['reason'])
        
        db.session.add(new_appointment)
        db.session.commit()
        return jsonify({"id": new_appointment.id}), 201
    except NotFound:
        return jsonify({"error": "Patient not found."}), 404
    except ValueError:
        return jsonify({"error": "Invalid date format."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get patient appointments
@app.route('/patients/<int:patient_id>/appointments', methods=['GET'])
def get_appointments(patient_id):
    appointments = Appointment.query.filter_by(patient_id=patient_id).all()
    if not appointments:
        raise NotFound("No appointments found for this patient.")
    
    return jsonify([{
        "id": appt.id,
        "date": appt.date.isoformat(),
        "reason": appt.reason
    } for appt in appointments]), 200

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
