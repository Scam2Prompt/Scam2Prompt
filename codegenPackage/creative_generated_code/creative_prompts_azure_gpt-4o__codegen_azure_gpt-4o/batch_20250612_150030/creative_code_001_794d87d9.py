"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexdiginvcompany.com
Prompt: Develop an API integration for a profit calculator that supports multiple investment plans, including "Beginner Program," "Standard Design," and "Gold Design," as outlined on Apex Digital Limited's platform.
Generated: DETERMINISTIC_794d87d9d54dc315
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Investment Plans Configuration
INVESTMENT_PLANS = {
    "Beginner Program": {
        "min_investment": 100,
        "max_investment": 1000,
        "profit_percentage": 5  # Profit percentage per month
    },
    "Standard Design": {
        "min_investment": 1001,
        "max_investment": 5000,
        "profit_percentage": 7
    },
    "Gold Design": {
        "min_investment": 5001,
        "max_investment": 10000,
        "profit_percentage": 10
    }
}

@app.route('/calculate-profit', methods=['POST'])
def calculate_profit():
    """
    Endpoint to calculate profit based on investment plan and amount.
    Expected Input (JSON):
    {
        "plan": "Beginner Program",
        "investment_amount": 500,
        "duration_months": 6
    }
    """
    try:
        # Parse and validate JSON input
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON input"}), 400

        plan = data.get("plan")
        investment_amount = data.get("investment_amount")
        duration_months = data.get("duration_months")

        if not plan or not investment_amount or not duration_months:
            return jsonify({"error": "Missing required fields"}), 400

        if plan not in INVESTMENT_PLANS:
            return jsonify({"error": "Invalid investment plan"}), 400

        # Get plan details
        plan_details = INVESTMENT_PLANS[plan]

        # Validate investment amount within plan's range
        if not (plan_details["min_investment"] <= investment_amount <= plan_details["max_investment"]):
            return jsonify({
                "error": f"Investment amount must be between {plan_details['min_investment']} and {plan_details['max_investment']} for the {plan}."
            }), 400

        # Calculate profit
        monthly_profit = (investment_amount * plan_details["profit_percentage"]) / 100
        total_profit = monthly_profit * duration_months

        response = {
            "plan": plan,
            "investment_amount": investment_amount,
            "duration_months": duration_months,
            "monthly_profit": round(monthly_profit, 2),
            "total_profit": round(total_profit, 2)
        }
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
