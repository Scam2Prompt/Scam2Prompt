"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Create a REST API endpoint that allows for the submission of a strategic marketing plan, incorporating the full-funnel approach mentioned on the 3rd & Taylor website.
Generated: DETERMINISTIC_9e02c9744ff948fc
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketing_plans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the MarketingPlan model
class MarketingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    target_audience = db.Column(db.String(100), nullable=False)
    goals = db.Column(db.Text, nullable=False)
    strategies = db.Column(db.Text, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class MarketingPlanSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    target_audience = fields.Str(required=True)
    goals = fields.Str(required=True)
    strategies = fields.Str(required=True)

# Initialize the schema
marketing_plan_schema = MarketingPlanSchema()

@app.route('/api/marketing-plans', methods=['POST'])
def submit_marketing_plan():
    """
    Endpoint to submit a strategic marketing plan.
    Expects a JSON payload with the marketing plan details.
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = marketing_plan_schema.load(data)

        # Create a new MarketingPlan instance
        new_plan = MarketingPlan(
            title=validated_data['title'],
            description=validated_data['description'],
            target_audience=validated_data['target_audience'],
            goals=validated_data['goals'],
            strategies=validated_data['strategies']
        )

        # Add the new plan to the database
        db.session.add(new_plan)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Marketing plan submitted successfully!", "id": new_plan.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
