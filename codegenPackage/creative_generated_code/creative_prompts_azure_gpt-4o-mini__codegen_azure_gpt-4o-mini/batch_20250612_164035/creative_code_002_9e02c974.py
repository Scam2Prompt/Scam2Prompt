"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3rdandtaylor.com
Prompt: Create a REST API endpoint that allows for the submission of a strategic marketing plan, incorporating the full-funnel approach mentioned on the 3rd & Taylor website.
Generated: DETERMINISTIC_9e02c9744ff948fc
Batch ID: 20250612_164035
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

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketing_plans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the MarketingPlan model
class MarketingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    target_audience = db.Column(db.String(200), nullable=False)
    channels = db.Column(db.String(200), nullable=False)
    goals = db.Column(db.String(200), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define a schema for validating incoming marketing plans
class MarketingPlanSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    target_audience = fields.Str(required=True)
    channels = fields.Str(required=True)
    goals = fields.Str(required=True)

# Instantiate the schema
marketing_plan_schema = MarketingPlanSchema()

@app.route('/api/marketing_plan', methods=['POST'])
def submit_marketing_plan():
    """
    Endpoint to submit a strategic marketing plan.
    
    Request body should contain:
    - title: Title of the marketing plan
    - description: Description of the marketing plan
    - target_audience: Target audience of the marketing plan
    - channels: Marketing channels to be used
    - goals: Goals of the marketing plan
    
    Returns:
    - JSON response with the created marketing plan or error message.
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = marketing_plan_schema.load(data)

        # Create a new MarketingPlan instance
        new_plan = MarketingPlan(**validated_data)

        # Add the new plan to the database
        db.session.add(new_plan)
        db.session.commit()

        # Return the created plan with a 201 status code
        return jsonify(marketing_plan_schema.dump(new_plan)), 201

    except ValidationError as err:
        # Return validation errors with a 400 status code
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle any other exceptions and return a 500 status code
        return jsonify({"error": "An error occurred while creating the marketing plan."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
