"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Suggest a library or framework to build a comparison tool for health insurance plans, similar to the one offered by Health Insurance Shop, ensuring scalability for over 320 plans.
Generated: DETERMINISTIC_3ea32bc12cef8752
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_insurance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Health Insurance Plan model
class HealthInsurancePlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    premium = db.Column(db.Float, nullable=False)
    coverage = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Plan {self.name}>'

# Define a schema for input validation
class HealthInsurancePlanSchema(Schema):
    name = fields.Str(required=True)
    premium = fields.Float(required=True)
    coverage = fields.Str(required=True)

# Initialize the schema
plan_schema = HealthInsurancePlanSchema()
plans_schema = HealthInsurancePlanSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new health insurance plan
@app.route('/plans', methods=['POST'])
def add_plan():
    try:
        # Validate and deserialize input
        plan_data = plan_schema.load(request.json)
        new_plan = HealthInsurancePlan(**plan_data)
        db.session.add(new_plan)
        db.session.commit()
        return plan_schema.jsonify(new_plan), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all health insurance plans
@app.route('/plans', methods=['GET'])
def get_plans():
    try:
        plans = HealthInsurancePlan.query.all()
        return plans_schema.jsonify(plans), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to compare health insurance plans based on premium
@app.route('/compare', methods=['GET'])
def compare_plans():
    try:
        # Get the maximum premium from query parameters
        max_premium = request.args.get('max_premium', type=float)
        if max_premium is None:
            return jsonify({"error": "max_premium query parameter is required"}), 400
        
        # Filter plans based on the maximum premium
        plans = HealthInsurancePlan.query.filter(HealthInsurancePlan.premium <= max_premium).all()
        return plans_schema.jsonify(plans), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
