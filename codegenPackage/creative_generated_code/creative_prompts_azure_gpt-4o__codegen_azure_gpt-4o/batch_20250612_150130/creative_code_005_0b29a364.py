"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeforcetd.com
Prompt: Create a REST API that allows users to input their deposit amount and investment plan (Basic, Flexible, or Advanced) for Finance Force Ltd, and returns the projected earnings and referral bonus.
Generated: DETERMINISTIC_0b29a364b7c9f426
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Investment plans configuration
investment_plans = {
    "Basic": {"rate": 0.05, "referral_bonus": 10},  # 5% ROI, $10 referral bonus
    "Flexible": {"rate": 0.07, "referral_bonus": 20},  # 7% ROI, $20 referral bonus
    "Advanced": {"rate": 0.1, "referral_bonus": 50},  # 10% ROI, $50 referral bonus
}

@app.route('/investment', methods=['POST'])
def calculate_earnings():
    """
    REST API endpoint to calculate projected earnings and referral bonus based on deposit amount and investment plan.
    Request Body:
    - deposit_amount (float): The amount to be deposited.
    - investment_plan (str): The investment plan chosen ("Basic", "Flexible", "Advanced").
    Response:
    - Returns a JSON object with projected earnings and referral bonus.
    """
    try:
        # Parse input data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. Please provide JSON data."}), 400
        
        deposit_amount = data.get("deposit_amount")
        investment_plan = data.get("investment_plan")
        
        # Validate deposit amount
        if not isinstance(deposit_amount, (float, int)) or deposit_amount <= 0:
            return jsonify({"error": "Invalid deposit amount. Must be a positive number."}), 400
        
        # Validate investment plan
        if investment_plan not in investment_plans:
            return jsonify({"error": f"Invalid investment plan. Choose from {list(investment_plans.keys())}."}), 400
        
        # Calculate projected earnings and referral bonus
        plan_details = investment_plans[investment_plan]
        projected_earnings = deposit_amount * plan_details["rate"]
        referral_bonus = plan_details["referral_bonus"]
        
        # Prepare response
        response = {
            "deposit_amount": deposit_amount,
            "investment_plan": investment_plan,
            "projected_earnings": round(projected_earnings, 2),
            "referral_bonus": referral_bonus
        }
        
        return jsonify(response), 200

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
