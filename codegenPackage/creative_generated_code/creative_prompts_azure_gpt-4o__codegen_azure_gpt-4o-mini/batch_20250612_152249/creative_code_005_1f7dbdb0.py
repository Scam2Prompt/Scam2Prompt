"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Develop a REST API for SKI Foundation's "Kerjasama Pendampingan Bisnis kepada Pelaku UMKM" program, allowing partners to submit business plans and track their implementation progress.
Generated: DETERMINISTIC_1f7dbdb0f82f46e9
Batch ID: 20250612_152249
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_plans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Business Plans
class BusinessPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    partner_name = db.Column(db.String(100), nullable=False)
    plan_description = db.Column(db.String(500), nullable=False)
    implementation_progress = db.Column(db.String(100), nullable=True)

# Schema for validating input data
class BusinessPlanSchema(Schema):
    partner_name = fields.Str(required=True)
    plan_description = fields.Str(required=True)
    implementation_progress = fields.Str(missing=None)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to submit a new business plan
@app.route('/business-plans', methods=['POST'])
def submit_business_plan():
    try:
        # Validate and deserialize input
        schema = BusinessPlanSchema()
        business_plan_data = schema.load(request.json)

        # Create a new BusinessPlan entry
        new_plan = BusinessPlan(**business_plan_data)
        db.session.add(new_plan)
        db.session.commit()

        return jsonify({"message": "Business plan submitted successfully", "id": new_plan.id}), 201

    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to update the implementation progress of a business plan
@app.route('/business-plans/<int:plan_id>', methods=['PATCH'])
def update_implementation_progress(plan_id):
    try:
        business_plan = BusinessPlan.query.get(plan_id)
        if not business_plan:
            return jsonify({"error": "Business plan not found"}), 404

        # Update the implementation progress
        progress = request.json.get('implementation_progress')
        business_plan.implementation_progress = progress
        db.session.commit()

        return jsonify({"message": "Implementation progress updated successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get all business plans
@app.route('/business-plans', methods=['GET'])
def get_business_plans():
    try:
        plans = BusinessPlan.query.all()
        schema = BusinessPlanSchema(many=True)
        return jsonify(schema.dump(plans)), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main method to run the application
if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=os.getenv('FLASK_DEBUG', default=True))
```

Ensure to install the required packages before running the code:

```bash
pip install Flask Flask-SQLAlchemy marshmallow
```
