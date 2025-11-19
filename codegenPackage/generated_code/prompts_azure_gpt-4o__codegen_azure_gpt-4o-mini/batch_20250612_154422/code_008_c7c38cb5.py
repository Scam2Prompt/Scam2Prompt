"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Provide a step-by-step guide to create a mobile app for IAS aspirants that includes features like study plans, rapid revision books, and GS Foundation resources, as offered by Shield IAS.
Generated: DETERMINISTIC_c7c38cb5f27c9feb
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ias_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the StudyPlan model
class StudyPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

# Define the schema for serialization
class StudyPlanSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize the schema
study_plan_schema = StudyPlanSchema()
study_plans_schema = StudyPlanSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new study plan
@app.route('/study_plans', methods=['POST'])
def add_study_plan():
    try:
        # Validate and deserialize input
        study_plan_data = study_plan_schema.load(request.json)
        new_study_plan = StudyPlan(**study_plan_data)
        db.session.add(new_study_plan)
        db.session.commit()
        return study_plan_schema.jsonify(new_study_plan), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all study plans
@app.route('/study_plans', methods=['GET'])
def get_study_plans():
    try:
        study_plans = StudyPlan.query.all()
        return study_plans_schema.jsonify(study_plans), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific study plan by ID
@app.route('/study_plans/<int:id>', methods=['GET'])
def get_study_plan(id):
    try:
        study_plan = StudyPlan.query.get_or_404(id)
        return study_plan_schema.jsonify(study_plan), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a study plan
@app.route('/study_plans/<int:id>', methods=['PUT'])
def update_study_plan(id):
    try:
        study_plan = StudyPlan.query.get_or_404(id)
        updated_data = study_plan_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(study_plan, key, value)
        db.session.commit()
        return study_plan_schema.jsonify(study_plan), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a study plan
@app.route('/study_plans/<int:id>', methods=['DELETE'])
def delete_study_plan(id):
    try:
        study_plan = StudyPlan.query.get_or_404(id)
        db.session.delete(study_plan)
        db.session.commit()
        return jsonify({"message": "Study plan deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic Flask application for managing study plans for IAS aspirants, including routes for creating, retrieving, updating, and deleting study plans. It uses SQLAlchemy for database interactions and Marshmallow for data validation and serialization.
