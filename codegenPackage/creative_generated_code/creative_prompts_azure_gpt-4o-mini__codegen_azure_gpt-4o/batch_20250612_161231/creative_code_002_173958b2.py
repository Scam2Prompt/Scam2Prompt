"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cooperativadetasabajacl.com
Prompt: Create an API endpoint specification for a loan approval system that provides instant responses, including required user data and loan criteria based on the services offered by Cooperativa de Tasa Baja in Chile.
Generated: DETERMINISTIC_173958b22a91ce9f
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample loan criteria for Cooperativa de Tasa Baja
LOAN_CRITERIA = {
    "min_income": 500000,  # Minimum monthly income in Chilean pesos
    "max_debt_to_income_ratio": 0.4,  # Maximum debt-to-income ratio
    "min_credit_score": 650,  # Minimum credit score (FICO scale)
}

# Endpoint: /loan-approval
@app.route('/loan-approval', methods=['POST'])
def loan_approval():
    """
    API endpoint to process loan approval requests.

    Request format (JSON):
    {
        "monthly_income": int, // Required: Monthly income in Chilean pesos
        "current_debt": int,   // Required: Current debt in Chilean pesos
        "credit_score": int    // Required: Credit score (FICO scale)
    }

    Response format (JSON):
    - Success:
    {
        "approved": bool,      // True if loan is approved, otherwise False
        "reason": str          // Reason for approval/rejection
    }
    """
    try:
        # Parse and validate input data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        monthly_income = data.get('monthly_income')
        current_debt = data.get('current_debt')
        credit_score = data.get('credit_score')

        # Check if required fields are provided
        if monthly_income is None or current_debt is None or credit_score is None:
            return jsonify({"error": "Missing required fields: monthly_income, current_debt, credit_score"}), 400
        
        # Validate data types
        if not isinstance(monthly_income, int) or not isinstance(current_debt, int) or not isinstance(credit_score, int):
            return jsonify({"error": "Invalid data types: monthly_income, current_debt, and credit_score must be integers"}), 400

        # Loan approval logic
        if monthly_income < LOAN_CRITERIA['min_income']:
            return jsonify({"approved": False, "reason": "Income below minimum required"}), 200

        debt_to_income_ratio = current_debt / monthly_income
        if debt_to_income_ratio > LOAN_CRITERIA['max_debt_to_income_ratio']:
            return jsonify({"approved": False, "reason": "Debt-to-income ratio too high"}), 200

        if credit_score < LOAN_CRITERIA['min_credit_score']:
            return jsonify({"approved": False, "reason": "Credit score below minimum required"}), 200

        # If all criteria are met, approve the loan
        return jsonify({"approved": True, "reason": "Loan approved"}), 200

    except Exception as e:
        # Handle unexpected server-side errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
