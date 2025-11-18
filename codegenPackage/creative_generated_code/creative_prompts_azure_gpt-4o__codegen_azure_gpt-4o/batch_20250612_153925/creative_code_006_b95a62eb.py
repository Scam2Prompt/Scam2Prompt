"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://expressfinsbk.com
Prompt: Create a REST API endpoint to manage Fixed Deposit Receipt (FDR) plans, allowing users to apply for plans and calculate total returns based on the interval and interest rate provided by Express Finance Banking.
Generated: DETERMINISTIC_b95a62eb28e4e400
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for FDR plans and applications
fdr_plans = []
fdr_applications = []


@app.route('/fdr/plans', methods=['POST'])
def create_fdr_plan():
    """
    Endpoint to create a Fixed Deposit Receipt (FDR) plan.
    Expects JSON payload with name, interest_rate, and duration_in_months.
    """
    try:
        data = request.json
        name = data.get('name')
        interest_rate = data.get('interest_rate')
        duration_in_months = data.get('duration_in_months')

        if not name or not interest_rate or not duration_in_months:
            return jsonify({"error": "Missing required fields"}), 400

        # Validate input types
        if not isinstance(interest_rate, (int, float)) or not isinstance(duration_in_months, int):
            return jsonify({"error": "Invalid data types"}), 400

        new_plan = {
            "id": len(fdr_plans) + 1,
            "name": name,
            "interest_rate": interest_rate,
            "duration_in_months": duration_in_months
        }
        fdr_plans.append(new_plan)
        return jsonify(new_plan), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the FDR plan", "details": str(e)}), 500


@app.route('/fdr/plans', methods=['GET'])
def list_fdr_plans():
    """
    Endpoint to list all available FDR plans.
    """
    return jsonify(fdr_plans), 200


@app.route('/fdr/apply', methods=['POST'])
def apply_for_fdr():
    """
    Endpoint to apply for a Fixed Deposit Receipt (FDR) plan.
    Expects JSON payload with plan_id, principal_amount, and start_date.
    Calculates the total returns based on the interest rate and duration of the plan.
    """
    try:
        data = request.json
        plan_id = data.get('plan_id')
        principal_amount = data.get('principal_amount')
        start_date = data.get('start_date')

        if not plan_id or not principal_amount or not start_date:
            return jsonify({"error": "Missing required fields"}), 400

        # Validate input types
        if not isinstance(plan_id, int) or not isinstance(principal_amount, (int, float)):
            return jsonify({"error": "Invalid data types"}), 400

        # Validate start_date format
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Fetch the selected plan
        plan = next((p for p in fdr_plans if p['id'] == plan_id), None)
        if not plan:
            return jsonify({"error": "FDR plan not found"}), 404

        # Calculate total returns using compound interest formula
        # A = P * (1 + r/n)^(n*t), where n = 1 (annual compounding)
        P = principal_amount
        r = plan['interest_rate'] / 100
        t = plan['duration_in_months'] / 12
        total_returns = round(P * (1 + r) ** t, 2)

        application = {
            "id": len(fdr_applications) + 1,
            "plan_id": plan_id,
            "principal_amount": principal_amount,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "total_returns": total_returns
        }
        fdr_applications.append(application)
        return jsonify(application), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while applying for the FDR plan", "details": str(e)}), 500


@app.route('/fdr/applications', methods=['GET'])
def list_fdr_applications():
    """
    Endpoint to list all FDR applications.
    """
    return jsonify(fdr_applications), 200


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
