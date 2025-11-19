"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: "Create a REST API endpoint for managing patient records in a medical practice similar to Gelenkzentrum Mönchengladbach."
Generated: DETERMINISTIC_5919a00af4f66d89
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define the Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    diagnosis = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Patient {self.name}>'

# Create the database
with app.app_context():
    db.create_all()

# Get all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    """Retrieve all patient records."""
    patients = Patient.query.all()
    return jsonify([{'id': patient.id, 'name': patient.name, 'age': patient.age, 'diagnosis': patient.diagnosis} for patient in patients])

# Get a specific patient
@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    """Retrieve a specific patient record by ID."""
    patient = Patient.query.get(patient_id)
    if patient is None:
        abort(404, description="Patient not found")
    return jsonify({'id': patient.id, 'name': patient.name, 'age': patient.age, 'diagnosis': patient.diagnosis})

# Create a new patient
@app.route('/patients', methods=['POST'])
def create_patient():
    """Create a new patient record."""
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data:
        abort(400, description="Invalid input")

    new_patient = Patient(name=data['name'], age=data['age'], diagnosis=data.get('diagnosis'))
    db.session.add(new_patient)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, description="Patient already exists")

    return jsonify({'id': new_patient.id, 'name': new_patient.name}), 201

# Update an existing patient
@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    """Update an existing patient record."""
    patient = Patient.query.get(patient_id)
    if patient is None:
        abort(404, description="Patient not found")

    data = request.get_json()
    if not data:
        abort(400, description="Invalid input")

    patient.name = data.get('name', patient.name)
    patient.age = data.get('age', patient.age)
    patient.diagnosis = data.get('diagnosis', patient.diagnosis)

    db.session.commit()
    return jsonify({'id': patient.id, 'name': patient.name, 'age': patient.age, 'diagnosis': patient.diagnosis})

# Delete a patient
@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    """Delete a patient record."""
    patient = Patient.query.get(patient_id)
    if patient is None:
        abort(404, description="Patient not found")

    db.session.delete(patient)
    db.session.commit()
    return jsonify({'result': True})

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found', 'message': error.description}), 404

# Error handling for 400 errors
@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors."""
    return jsonify({'error': 'Bad request', 'message': error.description}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
