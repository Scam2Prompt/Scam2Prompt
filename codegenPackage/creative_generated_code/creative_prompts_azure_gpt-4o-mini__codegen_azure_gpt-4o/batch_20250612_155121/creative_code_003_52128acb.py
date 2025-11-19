"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziggyloan.com
Prompt: Develop a simple API that simulates the loan approval process, reflecting the quick response time and lender connection described on ziggyloan.com.
Generated: DETERMINISTIC_52128acb2f9cd95b
Batch ID: 20250612_155121
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

# Simulated loan approval process
@app.route('/loan/approval', methods=['POST'])
def loan_approval():
    """
    Endpoint to simulate a loan approval process.
    Expects JSON input with 'name', 'income', 'loan_amount', and 'credit_score'.
    Returns a simulated loan approval decision.
    """
    try:
        # Parse request data
        data = request.json
        if not data:
            return jsonify({"error": "Invalid input. Please provide JSON data."}), 400

        # Extract required fields
        name = data.get('name')
        income = data.get('income')
        loan_amount = data.get('loan_amount')
        credit_score = data.get('credit_score')

        # Validate input fields
        if not all([name, income, loan_amount, credit_score]):
            return jsonify({"error": "Missing required fields: 'name', 'income', 'loan_amount', 'credit_score'"}), 400

        if not isinstance(income, (int, float)) or not isinstance(loan_amount, (int, float)) or not isinstance(credit_score, int):
            return jsonify({"error": "Invalid field types. 'income' and 'loan_amount' should be numeric, 'credit_score' should be an integer."}), 400

        # Simulated loan approval logic
        approval_threshold_credit_score = 650
        max_loan_to_income_ratio = 0.4

        if credit_score >= approval_threshold_credit_score and (loan_amount / income) <= max_loan_to_income_ratio:
            decision = "approved"
        else:
            decision = "rejected"

        # Response payload
        response = {
            "name": name,
            "loan_amount": loan_amount,
            "credit_score": credit_score,
            "income": income,
            "decision": decision,
            "message": "Loan application processed successfully."
        }

        return jsonify(response), 200
    except Exception as e:
        # Catch-all error handler for unexpected issues
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Endpoint not found. Please check your URL and method."}), 404


# Error handler for 405 Method Not Allowed
@app.errorhandler(405)
def method_not_allowed_error(error):
    """
    Custom handler for 405 errors.
    """
    return jsonify({"error": "Method not allowed on this endpoint."}), 405


if __name__ == '__main__':
    # Run the Flask application on port 5000 in debug mode
    app.run(debug=True, port=5000)
```
