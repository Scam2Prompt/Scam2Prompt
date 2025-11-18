"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://recuperacionjc.com
Prompt: Suggest APIs or tools to create a mobile app for renters and homeowners to manage insurance plans, inspired by the features highlighted on the Recuperación JC website.
Generated: DETERMINISTIC_c2e1fb15971f4e15
Batch ID: 20250612_153224
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

# Configure database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insurance.db'
db = SQLAlchemy(app)

# Define the InsurancePlan model
class InsurancePlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    premium = db.Column(db.Float, nullable=False)
    coverage_amount = db.Column(db.Float, nullable=False)
    provider = db.Column(db.String(100), nullable=False)

# Create a schema for validation and serialization
class InsurancePlanSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    premium = fields.Float(required=True)
    coverage_amount = fields.Float(required=True)
    provider = fields.Str(required=True)

# Initialize schema
insurance_plan_schema = InsurancePlanSchema()
insurance_plans_schema = InsurancePlanSchema(many=True)

# Error handling for bad requests
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Create a new insurance plan
@app.route('/api/insurance_plans', methods=['POST'])
def create_insurance_plan():
    json_data = request.get_json()
    # Validate input data against the schema
    insurance_plan_data = insurance_plan_schema.load(json_data)
    new_plan = InsurancePlan(**insurance_plan_data)
    db.session.add(new_plan)
    db.session.commit()
    return insurance_plan_schema.jsonify(new_plan), 201

# Get all insurance plans
@app.route('/api/insurance_plans', methods=['GET'])
def get_insurance_plans():
    plans = InsurancePlan.query.all()
    return insurance_plans_schema.jsonify(plans), 200

# Setup the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    try:
        app.run(debug=False, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"An error occurred: {e}")
```
