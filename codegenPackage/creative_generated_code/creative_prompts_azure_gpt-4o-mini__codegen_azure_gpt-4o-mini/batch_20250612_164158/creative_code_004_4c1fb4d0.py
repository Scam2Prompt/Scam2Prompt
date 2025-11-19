"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-extension-web3-dapps.blogspot.com
Prompt: Suggest a framework for developing a mobile app for a physiotherapy clinic that includes features like exercise tracking and progress reporting for patients.
Generated: DETERMINISTIC_4c1fb4d0cfb70e9d
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
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///physio_clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Patient
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    exercises = db.relationship('Exercise', backref='patient', lazy=True)

# Database model for Exercise
class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    repetitions = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)

# Schema for input validation
class ExerciseSchema(Schema):
    name = fields.Str(required=True)
    repetitions = fields.Int(required=True)
    sets = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(name=data['name'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient added successfully!"}), 201

# Route to add an exercise for a patient
@app.route('/patients/<int:patient_id>/exercises', methods=['POST'])
def add_exercise(patient_id):
    data = request.get_json()
    try:
        exercise_schema = ExerciseSchema()
        validated_data = exercise_schema.load(data)
        
        new_exercise = Exercise(**validated_data, patient_id=patient_id)
        db.session.add(new_exercise)
        db.session.commit()
        return jsonify({"message": "Exercise added successfully!"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Route to get progress report for a patient
@app.route('/patients/<int:patient_id>/progress', methods=['GET'])
def get_progress(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    exercises = Exercise.query.filter_by(patient_id=patient_id).all()
    progress = [{"name": exercise.name, "repetitions": exercise.repetitions, "sets": exercise.sets} for exercise in exercises]
    return jsonify({"patient": patient.name, "progress": progress}), 200

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
