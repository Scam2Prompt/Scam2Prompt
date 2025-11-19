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
import json

app = Flask(__name__)

# Sample data structure to simulate insurance plans
# In production, replace this with a proper database or external API
insurance_plans = [
    {
        "id": 1,
        "name": "Silver Plan",
        "monthly_premium": 300,
        "deductible": 5000,
        "coverage": ["general health", "vision", "dental"],
        "pre_existing_conditions_covered": False
    },
    {
        "id": 2,
        "name": "Gold Plan",
        "monthly_premium": 450,
        "deductible": 3000,
        "coverage": ["general health", "vision", "dental", "maternity"],
        "pre_existing_conditions_covered": True
    },
    {
        "id": 3,
        "name": "Platinum Plan",
        "monthly_premium": 600,
        "deductible": 1000,
        "coverage": ["general health", "vision", "dental", "maternity", "mental health"],
        "pre_existing_conditions_covered": True
    }
]

@app.route('/compare-plans', methods=['POST'])
def compare_plans():
    """
    API endpoint to compare health insurance plans.
    Expects a JSON payload with family criteria such as 'pre_existing_conditions' and 'required_coverage'.
    """
    try:
        # Parse request JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON payload"}), 400

        # Extract required criteria from the payload
        pre_existing_conditions = data.get("pre_existing_conditions", False)
        required_coverage = data.get("required_coverage", [])

        # Validate inputs
        if not isinstance(pre_existing_conditions, bool) or not isinstance(required_coverage, list):
            return jsonify({"error": "Invalid input format"}), 400

        # Filter plans based on criteria
        matching_plans = [
            plan for plan in insurance_plans
            if plan["pre_existing_conditions_covered"] >= pre_existing_conditions and
               set(required_coverage).issubset(plan["coverage"])
        ]

        # Return the matching plans
        return jsonify({"matching_plans": matching_plans}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

@app.route('/plans', methods=['GET'])
def get_all_plans():
    """
    API endpoint to retrieve all available health insurance plans.
    """
    try:
        return jsonify({"plans": insurance_plans}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving plans", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- To run this code, install Flask (`pip install flask`) and execute the script (`python script_name.py`).
- Use a tool like Postman or curl to interact with the API.
- Replace the sample data (`insurance_plans`) with a more robust database or external API integration in real-world applications.
