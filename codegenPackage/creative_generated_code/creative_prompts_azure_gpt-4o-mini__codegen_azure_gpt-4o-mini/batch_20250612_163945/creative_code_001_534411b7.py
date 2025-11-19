"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nationalhealthcareadvisors.com
Prompt: How can I implement an API to compare different family health insurance plans, considering pre-existing conditions and coverage limitations mentioned on National Healthcare Advisors?
Generated: DETERMINISTIC_534411b780d97fbc
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Sample data representing health insurance plans
insurance_plans = [
    {
        "id": 1,
        "name": "Basic Health Plan",
        "coverage": ["doctor visits", "emergency care"],
        "pre_existing_conditions": ["diabetes"],
        "limitations": "No coverage for specialist visits."
    },
    {
        "id": 2,
        "name": "Comprehensive Health Plan",
        "coverage": ["doctor visits", "emergency care", "specialist visits"],
        "pre_existing_conditions": [],
        "limitations": "None."
    },
    # Additional plans can be added here
]

# Input schema for validation
class InsurancePlanSchema(Schema):
    pre_existing_conditions = fields.List(fields.String(), required=True)
    coverage_needed = fields.List(fields.String(), required=True)

# API route to compare health insurance plans
@app.route('/compare_plans', methods=['POST'])
def compare_plans():
    # Validate input data
    try:
        data = request.json
        schema = InsurancePlanSchema()
        validated_data = schema.load(data)
    except ValidationError as err:
        logger.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Invalid input", "messages": err.messages}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

    pre_existing_conditions = validated_data['pre_existing_conditions']
    coverage_needed = validated_data['coverage_needed']

    # Find matching plans based on pre-existing conditions and coverage
    matching_plans = []

    for plan in insurance_plans:
        if all(condition in plan['pre_existing_conditions'] for condition in pre_existing_conditions) and \
           all(item in plan['coverage'] for item in coverage_needed):
            matching_plans.append(plan)

    # Return results or a message if no plans match
    if matching_plans:
        return jsonify(matching_plans), 200
    else:
        return jsonify({"message": "No plans match your criteria."}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
