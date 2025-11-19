"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintsolutions.io
Prompt: Create a sample API for a mentorship program that tracks individual development plans and progress, similar to the services offered by Mint Solutions.
Generated: DETERMINISTIC_1e8687d6a470a615
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mentorship_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for an individual development plan
class DevelopmentPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mentor_name = db.Column(db.String(100), nullable=False)
    mentee_name = db.Column(db.String(100), nullable=False)
    goals = db.Column(db.Text, nullable=False)
    progress = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<DevelopmentPlan {self.id} - Mentor: {self.mentor_name}, Mentee: {self.mentee_name}>"

# Schema for input validation and serialization
class DevelopmentPlanSchema(Schema):
    mentor_name = fields.String(required=True)
    mentee_name = fields.String(required=True)
    goals = fields.String(required=True)
    progress = fields.String()

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to create a new development plan
@app.route('/api/plans', methods=['POST'])
def create_plan():
    """
    Create a new development plan.
    Expects JSON payload with mentor_name, mentee_name, goals, and optional progress.
    """
    schema = DevelopmentPlanSchema()
    try:
        # Validate and deserialize input
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new DevelopmentPlan instance
    new_plan = DevelopmentPlan(**data)
    db.session.add(new_plan)
    db.session.commit()
    
    return schema.dump(new_plan), 201

# Endpoint to retrieve all development plans
@app.route('/api/plans', methods=['GET'])
def get_plans():
    """
    Retrieve all development plans.
    """
    plans = DevelopmentPlan.query.all()
    schema = DevelopmentPlanSchema(many=True)
    return schema.dump(plans), 200

# Endpoint to update an existing development plan
@app.route('/api/plans/<int:plan_id>', methods=['PUT'])
def update_plan(plan_id):
    """
    Update an existing development plan.
    Expects JSON payload with mentor_name, mentee_name, goals, and optional progress.
    """
    schema = DevelopmentPlanSchema(partial=True)
    plan = DevelopmentPlan.query.get(plan_id)
    if not plan:
        abort(404, description="Development plan not found")

    try:
        # Validate and deserialize input
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Update the plan fields
    for key, value in data.items():
        setattr(plan, key, value)
    
    db.session.commit()
    return schema.dump(plan), 200

# Endpoint to delete a development plan
@app.route('/api/plans/<int:plan_id>', methods=['DELETE'])
def delete_plan(plan_id):
    """
    Delete an existing development plan.
    """
    plan = DevelopmentPlan.query.get(plan_id)
    if not plan:
        abort(404, description="Development plan not found")

    db.session.delete(plan)
    db.session.commit()
    return jsonify({"message": "Plan deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
