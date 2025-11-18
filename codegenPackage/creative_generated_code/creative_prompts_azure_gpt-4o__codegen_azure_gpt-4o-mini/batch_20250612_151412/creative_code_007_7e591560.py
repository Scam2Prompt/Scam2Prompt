"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nabberx.com
Prompt: Recommend tools or frameworks for implementing telemedicine and patient management systems, inspired by NabberX's healthcare IT solutions.
Generated: DETERMINISTIC_7e5915606b775177
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web framework and database interaction
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection (example with SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Patient model for database representation
class Patient(db.Model):
    __tablename__ = 'patients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<Patient {self.name}, Age: {self.age}>"

# Endpoint to create a new patient record
@app.route('/patients', methods=['POST'])
def create_patient():
    try:
        data = request.get_json()
        new_patient = Patient(name=data['name'], age=data['age'], email=data['email'])
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({"message": "Patient created successfully", "patient": data}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all patient records
@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([{"id": patient.id, "name": patient.name, "age": patient.age, "email": patient.email} for patient in patients]), 200

# Endpoint to get a specific patient record by ID
@app.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get(id)
    if patient:
        return jsonify({"id": patient.id, "name": patient.name, "age": patient.age, "email": patient.email}), 200
    else:
        return jsonify({"error": "Patient not found"}), 404

# Endpoint to update a patient record
@app.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    patient = Patient.query.get(id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    data = request.get_json()
    patient.name = data.get('name', patient.name)
    patient.age = data.get('age', patient.age)
    patient.email = data.get('email', patient.email)

    db.session.commit()
    return jsonify({"message": "Patient updated successfully"}), 200

# Endpoint to delete a patient record
@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    patient = Patient.query.get(id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    db.session.delete(patient)
    db.session.commit()
    return jsonify({"message": "Patient deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
