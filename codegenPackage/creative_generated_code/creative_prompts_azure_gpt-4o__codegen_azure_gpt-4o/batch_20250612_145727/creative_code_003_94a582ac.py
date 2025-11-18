"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nocreditcheck.online
Prompt: Generate code for a web application that allows users to input their desired loan amount and repayment period, then matches them with suitable MFO offers, as seen on nocreditcheck.online.
Generated: DETERMINISTIC_94a582ace9272d6c
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Mock data for MFO (Microfinance Organization) offers
MFO_OFFERS = [
    {"name": "Quick Loan", "max_amount": 5000, "min_period": 1, "max_period": 12, "interest_rate": 0.03},
    {"name": "EasyCredit", "max_amount": 10000, "min_period": 3, "max_period": 24, "interest_rate": 0.025},
    {"name": "FastCash", "max_amount": 2000, "min_period": 1, "max_period": 6, "interest_rate": 0.04},
    {"name": "CashNow", "max_amount": 8000, "min_period": 6, "max_period": 18, "interest_rate": 0.02}
]

def calculate_monthly_payment(amount, period, interest_rate):
    """
    Calculate monthly payment using the formula for an amortized loan.
    Formula: M = P[r(1+r)^n]/[(1+r)^n - 1]
    where:
    M = monthly payment
    P = loan amount
    r = monthly interest rate
    n = total number of payments (months)
    """
    if interest_rate == 0:
        # If no interest, simply divide loan amount by the number of months
        return amount / period
    monthly_rate = interest_rate
    numerator = amount * monthly_rate * math.pow(1 + monthly_rate, period)
    denominator = math.pow(1 + monthly_rate, period) - 1
    return numerator / denominator

@app.route('/match-loan', methods=['POST'])
def match_loan():
    """
    Endpoint to match user loan amount and repayment period with suitable MFO offers.
    Request Body:
    {
        "amount": <int>,  # Desired loan amount
        "period": <int>   # Repayment period in months
    }
    Response:
    [
        {
            "name": <str>,              # MFO name
            "interest_rate": <float>,   # Interest rate
            "monthly_payment": <float>  # Calculated monthly payment
        },
        ...
    ]
    """
    try:
        # Parse and validate input
        data = request.get_json()
        if not data or 'amount' not in data or 'period' not in data:
            return jsonify({"error": "Invalid input format. Required fields: amount, period"}), 400

        amount = data['amount']
        period = data['period']

        if not isinstance(amount, (int, float)) or not isinstance(period, int) or amount <= 0 or period <= 0:
            return jsonify({"error": "Amount must be a positive number and period must be a positive integer."}), 400

        # Find matching MFO offers
        matching_offers = []
        for offer in MFO_OFFERS:
            if amount <= offer['max_amount'] and offer['min_period'] <= period <= offer['max_period']:
                monthly_payment = calculate_monthly_payment(amount, period, offer['interest_rate'])
                matching_offers.append({
                    "name": offer['name'],
                    "interest_rate": offer['interest_rate'],
                    "monthly_payment": round(monthly_payment, 2)
                })

        # Return results
        if not matching_offers:
            return jsonify({"message": "No suitable offers found for the given amount and period."}), 404

        return jsonify(matching_offers), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
