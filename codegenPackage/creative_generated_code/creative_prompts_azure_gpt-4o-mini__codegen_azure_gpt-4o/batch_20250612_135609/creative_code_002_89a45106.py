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
from werkzeug.exceptions import HTTPException
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key in production

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Define the Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.String(255), nullable=False)

# Define the Patient schema
class PatientSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Patient
        fields = ("id", "name", "age", "condition")

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description, "code": e.code}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e), "code": 500}), 500

# Endpoint: Add a new patient record (requires authentication)
@app.route('/patients', methods=['POST'])
@jwt_required()
def add_patient():
    try:
        data = request.json
        name = data.get('name')
        age = data.get('age')
        condition = data.get('condition')

        if not name or not age or not condition:
            return jsonify({"error": "Missing required fields"}), 400
        
        new_patient = Patient(name=name, age=age, condition=condition)
        db.session.add(new_patient)
        db.session.commit()

        return jsonify(patient_schema.dump(new_patient)), 201
    except Exception as e:
        return handle_exception(e)

# Endpoint: Get all patient records (requires authentication)
@app.route('/patients', methods=['GET'])
@jwt_required()
def get_patients():
    try:
        patients = Patient.query.all()
        return jsonify(patients_schema.dump(patients)), 200
    except Exception as e:
        return handle_exception(e)

# Endpoint: Get a specific patient record by ID (requires authentication)
@app.route('/patients/<int:id>', methods=['GET'])
@jwt_required()
def get_patient(id):
    try:
        patient = Patient.query.get(id)
        if not patient:
            return jsonify({"error": "Patient not found"}), 404
        return jsonify(patient_schema.dump(patient)), 200
    except Exception as e:
        return handle_exception(e)

# Endpoint: Update a specific patient record by ID (requires authentication)
@app.route('/patients/<int:id>', methods=['PUT'])
@jwt_required()
def update_patient(id):
    try:
        patient = Patient.query.get(id)
        if not patient:
            return jsonify({"error": "Patient not found"}), 404

        data = request.json
        patient.name = data.get('name', patient.name)
        patient.age = data.get('age', patient.age)
        patient.condition = data.get('condition', patient.condition)

        db.session.commit()
        return jsonify(patient_schema.dump(patient)), 200
    except Exception as e:
        return handle_exception(e)

# Endpoint: Delete a specific patient record by ID (requires authentication)
@app.route('/patients/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_patient(id):
    try:
        patient = Patient.query.get(id)
        if not patient:
            return jsonify({"error": "Patient not found"}), 404

        db.session.delete(patient)
        db.session.commit()
        return jsonify({"message": "Patient record deleted"}), 200
    except Exception as e:
        return handle_exception(e)

# Endpoint: Authentication for the API
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Replace with actual user authentication logic (e.g., database lookup)
        if username == "admin" and password == "password":  # Example only, use secure methods in production
            access_token = create_access_token(identity=username)
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return handle_exception(e)

# Initialize the database
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
