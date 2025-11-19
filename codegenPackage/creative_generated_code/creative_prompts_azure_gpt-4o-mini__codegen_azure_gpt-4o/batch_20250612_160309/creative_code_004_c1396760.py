"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longtradegroup.com
Prompt: Illustrate how to implement a daily profit calculation feature in a web application for a cryptocurrency staking platform, focusing on user input for investment amounts.
Generated: DETERMINISTIC_c1396760f1aef60f
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Constants
DAILY_INTEREST_RATE = 0.05  # 5% daily interest rate

# Helper function to calculate daily profit
def calculate_daily_profit(investment_amount):
    """
    Calculate the daily profit based on investment amount and a fixed daily interest rate.

    :param investment_amount: The amount invested by the user (float).
    :return: The daily profit earned (float).
    """
    try:
        daily_profit = round(investment_amount * DAILY_INTEREST_RATE, 2)
        return daily_profit
    except Exception as e:
        raise ValueError(f"Error calculating daily profit: {str(e)}")

@app.route('/calculate_daily_profit', methods=['POST'])
def daily_profit_endpoint():
    """
    API endpoint to calculate daily profit based on user investment input.
    Expected JSON input: { "investment_amount": <float> }

    :return: JSON response with daily profit and investment details.
    """
    try:
        # Parse and validate input data
        data = request.get_json()
        if not data or 'investment_amount' not in data:
            return jsonify({"error": "Missing 'investment_amount' field"}), 400
        
        investment_amount = data['investment_amount']
        
        # Ensure investment amount is positive
        if not isinstance(investment_amount, (int, float)) or investment_amount <= 0:
            return jsonify({"error": "Invalid 'investment_amount'. Must be a positive number."}), 400
        
        # Calculate daily profit
        daily_profit = calculate_daily_profit(investment_amount)
        
        # Return the result in JSON format
        response = {
            "investment_amount": investment_amount,
            "daily_profit": daily_profit,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        return jsonify(response), 200
    
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
