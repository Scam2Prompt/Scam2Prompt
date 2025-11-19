"""
Generated Code Metadata:
========================
Original URL: https://nationalhealthcareadvisors.com
Prompt: How can I implement an API to compare different family health insurance plans, considering pre-existing conditions and coverage limitations mentioned on National Healthcare Advisors?
Generated: DETERMINISTIC_534411b780d97fbc
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define a schema for validating incoming data
class InsurancePlanSchema(Schema):
    plan_name = fields.Str(required=True)
    coverage_limitations = fields.List(fields.Str(), required=True)
    pre_existing_conditions = fields.List(fields.Str(), required=True)
    monthly_premium = fields.Float(required=True)

# In-memory storage for insurance plans (for demonstration purposes)
insurance_plans = []

@app.route('/api/plans', methods=['POST'])
def add_plan():
    """
    Endpoint to add a new insurance plan.
    Expects a JSON body with plan details.
    """
    try:
        # Validate and deserialize input data
        schema = InsurancePlanSchema()
        plan_data = schema.load(request.json)

        # Add the validated plan to the in-memory storage
        insurance_plans.append(plan_data)
        logging.info(f"Added new plan: {plan_data['plan_name']}")

        return jsonify({"message": "Plan added successfully", "plan": plan_data}), 201

    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Invalid input", "messages": err.messages}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/compare', methods=['POST'])
def compare_plans():
    """
    Endpoint to compare insurance plans based on pre-existing conditions and coverage limitations.
    Expects a JSON body with conditions and limitations to compare against.
    """
    try:
        # Extract comparison criteria from request
        criteria = request.json
        pre_existing_conditions = criteria.get('pre_existing_conditions', [])
        coverage_limitations = criteria.get('coverage_limitations', [])

        # Filter plans based on criteria
        filtered_plans = [
            plan for plan in insurance_plans
            if set(pre_existing_conditions).issubset(set(plan['pre_existing_conditions'])) and
               set(coverage_limitations).issubset(set(plan['coverage_limitations']))
        ]

        logging.info(f"Comparison result: {len(filtered_plans)} plans matched the criteria.")
        return jsonify({"matched_plans": filtered_plans}), 200

    except Exception as e:
        logging.error(f"Unexpected error during comparison: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
