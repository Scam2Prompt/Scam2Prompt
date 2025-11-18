"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binarygoldenoptions.com
Prompt: Recommend libraries or APIs for implementing a profit calculator tool similar to the one described on Binary Golden Options, allowing users to calculate returns based on investment plans.
Generated: DETERMINISTIC_bb1b1de8b3a5d03d
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Profit Calculator Tool

This Python script demonstrates how to implement a profit calculator tool,
allowing users to calculate returns based on investment plans. It uses Python's
decimal library for precise calculations and provides a clean, modular approach.

Dependencies:
- Flask: For building a REST API to expose the profit calculation functionality.
Install Flask using `pip install flask`.
"""

from flask import Flask, request, jsonify
from decimal import Decimal, InvalidOperation

# Initialize Flask app
app = Flask(__name__)

# Error messages
INVALID_INPUT_ERROR = "Invalid input provided. Please ensure investment and rate are valid numbers."
MISSING_PARAMETERS_ERROR = "Missing required parameters: 'investment' and 'rate'."

# Constants
MAX_RATE = 100  # Maximum allowable rate, for validation purposes

def calculate_profit(investment: Decimal, rate: Decimal) -> Decimal:
    """
    Calculate profit based on the investment and rate.

    Args:
        investment (Decimal): The amount of investment.
        rate (Decimal): The return rate percentage.

    Returns:
        Decimal: The calculated profit.
    """
    # Ensure rate is within a valid range
    if rate < 0 or rate > MAX_RATE:
        raise ValueError(f"Rate must be between 0 and {MAX_RATE} percent.")
    
    # Calculate profit
    profit = investment * rate / 100
    return profit

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Flask route to handle profit calculations.

    Request Body (JSON):
        {
            "investment": <float>,
            "rate": <float>
        }

    Response (JSON):
        {
            "investment": <float>,
            "rate": <float>,
            "profit": <float>
        }
    """
    try:
        # Parse JSON data from request
        data = request.json
        if 'investment' not in data or 'rate' not in data:
            return jsonify({"error": MISSING_PARAMETERS_ERROR}), 400

        # Convert inputs to Decimal for precise calculations
        try:
            investment = Decimal(data['investment'])
            rate = Decimal(data['rate'])
        except InvalidOperation:
            return jsonify({"error": INVALID_INPUT_ERROR}), 400

        # Calculate profit
        profit = calculate_profit(investment, rate)

        # Respond with calculated values
        return jsonify({
            "investment": float(investment),
            "rate": float(rate),
            "profit": float(profit)
        })

    except ValueError as e:
        # Handle custom validation errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    """
    Start the Flask server.
    
    Note:
    This script is meant to run as a standalone application. For production,
    consider using a WSGI server like Gunicorn to deploy this API.
    """
    app.run(debug=True)
```
