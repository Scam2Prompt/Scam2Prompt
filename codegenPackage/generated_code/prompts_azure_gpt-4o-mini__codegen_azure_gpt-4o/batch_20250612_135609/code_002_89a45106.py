"""
Generated Code Metadata:
========================
Original URL: https://movilabtorremedica2.com
Prompt: Create a RESTful API endpoint for managing patient records in a medical facility like Movilab, ensuring data privacy and security.
Generated: DETERMINISTIC_89a45106cca1c287
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure JWT
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_secret_key')  # Replace with a secure key in production

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    medical_history = db.Column(db.Text, nullable=True)

# Patient schema for serialization
class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient
        load_instance = True

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Create a new patient record
@app.route('/api/patients', methods=['POST'])
@jwt_required()
def create_patient():
    try:
        data = request.json
        name = data.get('name')
        age = data.get('age')
        medical_history = data.get('medical_history', '')

        if not name or not age:
            return jsonify({"error": "Name and age are required"}), 400

        new_patient = Patient(name=name, age=age, medical_history=medical_history)
        db.session.add(new_patient)
        db.session.commit()

        return patient_schema.jsonify(new_patient), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all patient records
@app.route('/api/patients', methods=['GET'])
@jwt_required()
def get_patients():
    try:
        patients = Patient.query.all()
        return patients_schema.jsonify(patients), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a single patient record by ID
@app.route('/api/patients/<int:id>', methods=['GET'])
@jwt_required()
def get_patient(id):
    try:
        patient = Patient.query.get(id)
        if not patient:
            return jsonify({"error": "Patient not found"}), 404
        return patient_schema.jsonify(patient), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update a patient record
@app.route('/api/patients/<int:id>', methods=['PUT'])
@jwt_required()
def update_patient(id):
    try:
        patient = Patient.query.get(id)
        if not patient:
            return jsonify({"error": "Patient not found"}), 404

        data = request.json
        patient.name = data.get('name', patient.name)
        patient.age = data.get('age', patient.age)
        patient.medical_history = data.get('medical_history', patient.medical_history)

        db.session.commit()
        return patient_schema.jsonify(patient), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a patient record
@app.route('/api/patients/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_patient(id):
    try:
        patient = Patient.query.get(id)
        if not patient:
            return jsonify({"error": "Patient not found"}), 404

        db.session.delete(patient)
        db.session.commit()
        return jsonify({"message": "Patient record deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# User authentication (for demonstration purposes)
@app.route('/api/auth/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # In production, validate against a user database
        if username == 'admin' and password == 'password':  # Replace with secure validation
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
