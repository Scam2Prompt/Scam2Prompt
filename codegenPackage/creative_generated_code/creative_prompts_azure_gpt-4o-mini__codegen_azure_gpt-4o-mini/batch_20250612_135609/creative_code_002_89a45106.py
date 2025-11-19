"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://movilabtorremedica2.com
Prompt: Create a RESTful API endpoint for managing patient records in a medical facility like Movilab, ensuring data privacy and security.
Generated: DETERMINISTIC_89a45106cca1c287
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
from werkzeug.exceptions import NotFound, BadRequest
from flask_marshmallow import Marshmallow
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI, assuming SQLite for simplicity; change for production
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///patients.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for Patient records
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    medical_history = db.Column(db.Text, nullable=True)

    def __init__(self, name, age, medical_history):
        self.name = name
        self.age = age
        self.medical_history = medical_history

# Schema for serializing Patient data
class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new patient record
@app.route('/patients', methods=['POST'])
def add_patient():
    """Add a new patient record."""
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'age' not in data:
            raise BadRequest("Missing required fields.")
        
        new_patient = Patient(
            name=data['name'],
            age=data['age'],
            medical_history=data.get('medical_history')
        )
        db.session.add(new_patient)
        db.session.commit()
        return PatientSchema().dump(new_patient), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all patient records
@app.route('/patients', methods=['GET'])
def get_patients():
    """Retrieve all patient records."""
    patients = Patient.query.all()
    return PatientSchema(many=True).dump(patients), 200

# Endpoint to retrieve a specific patient record by ID
@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    """Retrieve a patient record by ID."""
    patient = Patient.query.get(patient_id)
    if not patient:
        raise NotFound("Patient not found.")
    return PatientSchema().dump(patient), 200

# Endpoint to update a patient record by ID
@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    """Update a patient record by ID."""
    try:
        patient = Patient.query.get(patient_id)
        if not patient:
            raise NotFound("Patient not found.")
        
        data = request.get_json()
        if 'name' in data:
            patient.name = data['name']
        if 'age' in data:
            patient.age = data['age']
        if 'medical_history' in data:
            patient.medical_history = data['medical_history']
        
        db.session.commit()
        return PatientSchema().dump(patient), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a patient record by ID
@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    """Delete a patient record by ID."""
    patient = Patient.query.get(patient_id)
    if not patient:
        raise NotFound("Patient not found.")
    
    db.session.delete(patient)
    db.session.commit()
    return jsonify({"message": "Patient record deleted."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: Ensure you have the required packages installed (`Flask`, `Flask-SQLAlchemy`, `Flask-Marshmallow`, `python-dotenv`, etc.) and a `.env` file with the appropriate `DATABASE_URI`.
