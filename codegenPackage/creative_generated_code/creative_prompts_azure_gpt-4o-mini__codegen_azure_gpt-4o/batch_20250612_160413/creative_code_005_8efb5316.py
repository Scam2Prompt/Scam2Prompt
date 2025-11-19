"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradetoearnoptions.com
Prompt: Design a RESTful API endpoint that allows users to check their investment maturity periods and earnings for different plans on Tradetoearnoption.
Generated: DETERMINISTIC_8efb53167de61064
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Sample investment plans data (would typically come from a database)
investment_plans = {
    "plan_1": {
        "name": "Silver Plan",
        "maturity_period_days": 180,
        "interest_rate": 0.05  # 5% annual interest
    },
    "plan_2": {
        "name": "Gold Plan",
        "maturity_period_days": 365,
        "interest_rate": 0.10  # 10% annual interest
    },
    "plan_3": {
        "name": "Platinum Plan",
        "maturity_period_days": 730,
        "interest_rate": 0.15  # 15% annual interest
    }
}

@app.route('/api/investment/maturity', methods=['POST'])
def calculate_investment_maturity():
    """
    Endpoint to calculate investment maturity periods and earnings.
    User submits their investment plan and initial investment amount.
    """
    try:
        # Parse input data from the request
        data = request.json
        if not data:
            return jsonify({"error": "Invalid input. Please provide JSON data."}), 400
        
        # Validate input fields
        plan_id = data.get("plan_id")
        initial_investment = data.get("initial_investment")
        if not plan_id or plan_id not in investment_plans:
            return jsonify({"error": "Invalid or missing plan_id."}), 400
        if not initial_investment or not isinstance(initial_investment, (int, float)) or initial_investment <= 0:
            return jsonify({"error": "Invalid or missing initial_investment. Must be a positive number."}), 400

        # Fetch the plan details
        plan = investment_plans[plan_id]
        maturity_period_days = plan["maturity_period_days"]
        interest_rate = plan["interest_rate"]

        # Calculate maturity date
        maturity_date = datetime.now() + timedelta(days=maturity_period_days)
        maturity_date_str = maturity_date.strftime('%Y-%m-%d')

        # Calculate earnings
        # Assumes simple interest formula: Interest = Principal * Rate * Time
        time_years = maturity_period_days / 365.0
        earnings = initial_investment * interest_rate * time_years
        total_amount = initial_investment + earnings

        # Response payload
        response = {
            "plan_name": plan["name"],
            "maturity_date": maturity_date_str,
            "maturity_period_days": maturity_period_days,
            "initial_investment": initial_investment,
            "earnings": round(earnings, 2),
            "total_amount": round(total_amount, 2)
        }

        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
```
