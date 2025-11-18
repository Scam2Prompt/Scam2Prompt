"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jinlinghospital.com
Prompt: Develop a REST API to manage Jinling Hospital’s pediatric department records, including endpoints for adding new patient data, retrieving developmental milestones, and updating vaccination schedules.
Generated: DETERMINISTIC_3eb3bac541ef3a24
Batch ID: 20250612_151024
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pediatric_records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for patient records
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    milestones = db.Column(db.JSON, nullable=True)
    vaccinations = db.Column(db.JSON, nullable=True)

    def __repr__(self):
        return f'<Patient {self.name}, Age {self.age}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new patient record
@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    
    if not all(k in data for k in ("name", "age")):
        return jsonify({"error": "Name and age are required."}), 400
    
    new_patient = Patient(name=data['name'], age=data['age'], milestones={}, vaccinations={})

    try:
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({"message": "Patient added successfully.", "id": new_patient.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Failed to add patient."}), 500

# Endpoint to retrieve a patient's developmental milestones
@app.route('/patients/<int:patient_id>/milestones', methods=['GET'])
def get_milestones(patient_id):
    patient = Patient.query.get(patient_id)
    
    if patient is None:
        return jsonify({"error": "Patient not found."}), 404
    
    return jsonify({"milestones": patient.milestones}), 200

# Endpoint to update a patient's vaccination schedule
@app.route('/patients/<int:patient_id>/vaccinations', methods=['PUT'])
def update_vaccinations(patient_id):
    data = request.get_json()
    
    patient = Patient.query.get(patient_id)
    
    if patient is None:
        return jsonify({"error": "Patient not found."}), 404
    
    if 'vaccinations' not in data:
        return jsonify({"error": "Vaccination data is required."}), 400
    
    patient.vaccinations = data['vaccinations']
    
    try:
        db.session.commit()
        return jsonify({"message": "Vaccination schedule updated successfully."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to update vaccinations: {str(e)}"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
