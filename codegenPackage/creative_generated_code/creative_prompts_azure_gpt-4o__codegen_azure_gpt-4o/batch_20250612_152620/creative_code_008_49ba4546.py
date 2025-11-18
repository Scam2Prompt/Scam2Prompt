"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-humanizedai.web.app
Prompt: Develop a feature that allows users to select staking percentages (e.g., 25%, 50%, 75%, MAX) and update the calculated earnings accordingly, as seen on the HumanizedAi staking page.
Generated: DETERMINISTIC_49ba4546cda5961a
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: staking_calculator.py

# Import necessary libraries
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user account balance (in tokens)
USER_BALANCE = 1000  # Example, user's balance in tokens

# Staking percentages options
STAKING_OPTIONS = {
    "25%": 0.25,
    "50%": 0.50,
    "75%": 0.75,
    "MAX": 1.00
}

# Annual Staking ROI (Return On Investment) in percentage
ANNUAL_ROI_PERCENTAGE = 12  # Example, 12% annual return

def calculate_earnings(staking_percentage, balance):
    """
    Calculate the earnings based on staking percentage and balance.

    :param staking_percentage: Percentage of balance staked (e.g., 0.25 for 25%)
    :param balance: User's total token balance
    :return: Calculated annual earnings and amount staked
    """
    try:
        # Calculate amount staked
        amount_staked = balance * staking_percentage
        
        # Calculate annual earnings based on ROI
        annual_earnings = amount_staked * (ANNUAL_ROI_PERCENTAGE / 100)

        return {
            "amount_staked": round(amount_staked, 2),
            "annual_earnings": round(annual_earnings, 2)
        }
    except Exception as e:
        raise ValueError(f"Error in calculation: {str(e)}")

@app.route('/stake', methods=['POST'])
def stake():
    """
    API endpoint to calculate staking earnings based on user input.

    Request Body:
    {
        "percentage": "25%"  # Options: "25%", "50%", "75%", "MAX"
    }

    Response:
    {
        "amount_staked": 250.0,
        "annual_earnings": 30.0
    }
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data or "percentage" not in data:
            return jsonify({"error": "Invalid request, 'percentage' is required."}), 400

        percentage = data["percentage"]

        # Validate staking percentage
        if percentage not in STAKING_OPTIONS:
            return jsonify({"error": "Invalid percentage option. Valid options are: '25%', '50%', '75%', 'MAX'."}), 400

        # Calculate staking earnings
        staking_percentage = STAKING_OPTIONS[percentage]
        result = calculate_earnings(staking_percentage, USER_BALANCE)

        return jsonify(result), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
