"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: "Design a system architecture for a multidisciplinary team to manage patient data and therapy plans, considering outcome-based mindset and holistic assessment, as described in ICON's approach."
Generated: DETERMINISTIC_e488d0b9af35a183
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a system architecture for managing patient data and therapy plans. It uses Flask for the API layer, SQLAlchemy for database management, and follows best practices for modularity, error handling, and documentation.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patient_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Models
class Patient(db.Model):
    """
    Represents a patient in the system.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)

class TherapyPlan(db.Model):
    """
    Represents a therapy plan for a patient.
    """
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    outcome_goals = db.Column(db.Text, nullable=False)
    holistic_assessment = db.Column(db.Text, nullable=False)

    # Relationship
    patient = db.relationship('Patient', backref=db.backref('therapy_plans', lazy=True))

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

# Routes
@app.route('/patients', methods=['POST'])
def create_patient():
    """
    Create a new patient.
    """
    try:
        data = request.json
        new_patient = Patient(
            name=data['name'],
            age=data['age'],
            gender=data['gender'],
            contact_info=data['contact_info']
        )
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({"message": "Patient created successfully", "patient_id": new_patient.id}), 201
    except KeyError as e:
        logging.error(f"Missing field: {e}")
        return jsonify({"error": f"Missing field: {e}"}), 400
    except IntegrityError:
        db.session.rollback()
        logging.error("Database integrity error")
        return jsonify({"error": "Database integrity error"}), 400

@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    """
    Retrieve patient details by ID.
    """
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify({
        "id": patient.id,
        "name": patient.name,
        "age": patient.age,
        "gender": patient.gender,
        "contact_info": patient.contact_info
    })

@app.route('/therapy-plans', methods=['POST'])
def create_therapy_plan():
    """
    Create a new therapy plan for a patient.
    """
    try:
        data = request.json
        patient = Patient.query.get(data['patient_id'])
        if not patient:
            return jsonify({"error": "Patient not found"}), 404

        new_plan = TherapyPlan(
            patient_id=data['patient_id'],
            description=data['description'],
            outcome_goals=data['outcome_goals'],
            holistic_assessment=data['holistic_assessment']
        )
        db.session.add(new_plan)
        db.session.commit()
        return jsonify({"message": "Therapy plan created successfully", "plan_id": new_plan.id}), 201
    except KeyError as e:
        logging.error(f"Missing field: {e}")
        return jsonify({"error": f"Missing field: {e}"}), 400
    except IntegrityError:
        db.session.rollback()
        logging.error("Database integrity error")
        return jsonify({"error": "Database integrity error"}), 400

@app.route('/therapy-plans/<int:plan_id>', methods=['GET'])
def get_therapy_plan(plan_id):
    """
    Retrieve therapy plan details by ID.
    """
    plan = TherapyPlan.query.get(plan_id)
    if not plan:
        return jsonify({"error": "Therapy plan not found"}), 404
    return jsonify({
        "id": plan.id,
        "patient_id": plan.patient_id,
        "description": plan.description,
        "outcome_goals": plan.outcome_goals,
        "holistic_assessment": plan.holistic_assessment
    })

# Initialize database
@app.before_first_request
def setup_database():
    """
    Create database tables before the first request.
    """
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
