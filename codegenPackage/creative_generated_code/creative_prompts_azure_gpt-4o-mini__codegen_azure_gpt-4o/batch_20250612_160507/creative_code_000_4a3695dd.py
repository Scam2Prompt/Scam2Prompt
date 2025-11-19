"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Generate a code snippet for a web application that allows users to get a quote for health insurance from KEK Insurance Brokers in Ghana.
Generated: DETERMINISTIC_4a3695dda7160d49
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: health_insurance_quote.py
# Description: A Flask web application to get health insurance quotes from KEK Insurance Brokers in Ghana.

from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for insurance plans
INSURANCE_PLANS = [
    {"id": 1, "name": "Basic Plan", "coverage": "100,000 GHC", "monthly_premium": "250 GHC"},
    {"id": 2, "name": "Standard Plan", "coverage": "250,000 GHC", "monthly_premium": "500 GHC"},
    {"id": 3, "name": "Premium Plan", "coverage": "500,000 GHC", "monthly_premium": "1000 GHC"},
]

# Endpoint to get a health insurance quote
@app.route('/get_quote', methods=['POST'])
def get_quote():
    """
    Endpoint to get a health insurance quote.
    Expects user data in JSON format: name, age, and preferred plan ID.
    Returns a detailed quote if input is valid.
    """
    try:
        # Parse JSON request data
        data = request.json
        name = data.get('name')
        age = data.get('age')
        plan_id = data.get('plan_id')

        # Validate input
        if not name or not age or not plan_id:
            return jsonify({"error": "Missing required fields: name, age, or plan_id"}), 400

        if not isinstance(age, int) or age <= 0:
            return jsonify({"error": "Age must be a positive integer"}), 400

        # Find the plan corresponding to the plan_id
        selected_plan = next((plan for plan in INSURANCE_PLANS if plan['id'] == plan_id), None)
        if not selected_plan:
            return jsonify({"error": "Invalid plan_id"}), 404

        # Generate quote
        quote = {
            "name": name,
            "age": age,
            "plan_details": selected_plan,
            "message": f"Dear {name}, you have selected the {selected_plan['name']} with coverage of {selected_plan['coverage']}."
        }
        return jsonify(quote), 200

    except Exception as e:
        # General error handler
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Endpoint to list available insurance plans
@app.route('/plans', methods=['GET'])
def list_plans():
    """
    Endpoint to list all available insurance plans.
    Returns a JSON list of insurance plans.
    """
    return jsonify({"plans": INSURANCE_PLANS}), 200

# Entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)  # Set debug=False for production
```
