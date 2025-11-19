"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idetgroup.com
Prompt: Illustrate how to implement a patient management system that includes features for telemedicine and home visits, drawing from the services provided by Grupo Clínico IDET.
Generated: DETERMINISTIC_1c312dae4b1991e8
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Patient Management System for Telemedicine and Home Visits
This application is a simplified example of a patient management system
that includes features for telemedicine and home visits.

Language: Python
Dependencies: Flask (web framework), SQLite (database), SQLAlchemy (ORM)
Run: Install Flask and SQLAlchemy (`pip install flask sqlalchemy`) and run this script.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)  # Telemedicine or Home Visit

    def to_dict(self):
        """Convert patient object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'contact_info': self.contact_info,
            'service_type': self.service_type
        }

# Error handling for Flask routes
@app.errorhandler(404)
def handle_404(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def handle_500(error):
    return jsonify({'error': 'Internal server error'}), 500

# Route: Add a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    try:
        data = request.json
        name = data.get('name')
        age = data.get('age')
        contact_info = data.get('contact_info')
        service_type = data.get('service_type')

        if not name or not age or not contact_info or not service_type:
            return jsonify({'error': 'Missing required fields'}), 400

        if service_type not in ['Telemedicine', 'Home Visit']:
            return jsonify({'error': 'Invalid service type. Must be Telemedicine or Home Visit'}), 400

        new_patient = Patient(name=name, age=age, contact_info=contact_info, service_type=service_type)
        db.session.add(new_patient)
        db.session.commit()

        return jsonify({'message': 'Patient added successfully', 'patient': new_patient.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Get all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    try:
        patients = Patient.query.all()
        return jsonify([patient.to_dict() for patient in patients]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Get a patient by ID
@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    try:
        patient = Patient.query.get(patient_id)
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        return jsonify(patient.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Update a patient record
@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    try:
        patient = Patient.query.get(patient_id)
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404

        data = request.json
        patient.name = data.get('name', patient.name)
        patient.age = data.get('age', patient.age)
        patient.contact_info = data.get('contact_info', patient.contact_info)
        patient.service_type = data.get('service_type', patient.service_type)

        db.session.commit()
        return jsonify({'message': 'Patient updated successfully', 'patient': patient.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Delete a patient record
@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    try:
        patient = Patient.query.get(patient_id)
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404

        db.session.delete(patient)
        db.session.commit()
        return jsonify({'message': 'Patient deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database
@app.before_first_request
def initialize_database():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
