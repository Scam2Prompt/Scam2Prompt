"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Generate a code snippet for a web application that allows users to apply for a personal loan, incorporating features like flexible repayment terms and quick approval as described on SGFC Finance.
Generated: DETERMINISTIC_e088b20cb8acec74
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Simulated database for storing loan applications
loan_applications = []

# Constants for loan terms
MIN_LOAN_AMOUNT = 1000
MAX_LOAN_AMOUNT = 50000
MIN_REPAYMENT_MONTHS = 6
MAX_REPAYMENT_MONTHS = 60

@app.route('/apply-loan', methods=['POST'])
def apply_loan():
    """
    Endpoint to apply for a personal loan.
    Request JSON structure:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "loan_amount": 15000,
        "repayment_months": 24
    }
    """
    try:
        # Parse and validate input data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request format"}), 400

        name = data.get('name')
        email = data.get('email')
        loan_amount = data.get('loan_amount')
        repayment_months = data.get('repayment_months')

        # Ensure all required fields are present
        if not name or not email or not loan_amount or not repayment_months:
            return jsonify({"error": "Missing required fields"}), 400

        # Validate loan amount and repayment terms
        if not (MIN_LOAN_AMOUNT <= loan_amount <= MAX_LOAN_AMOUNT):
            return jsonify({"error": f"Loan amount must be between {MIN_LOAN_AMOUNT} and {MAX_LOAN_AMOUNT}"}), 400

        if not (MIN_REPAYMENT_MONTHS <= repayment_months <= MAX_REPAYMENT_MONTHS):
            return jsonify({"error": f"Repayment months must be between {MIN_REPAYMENT_MONTHS} and {MAX_REPAYMENT_MONTHS}"}), 400

        # Generate approval status (quick approval simulation)
        approval_status = "approved" if loan_amount <= 25000 else "pending"

        # Calculate repayment details
        monthly_installment = round(loan_amount / repayment_months, 2)
        repayment_end_date = datetime.now() + timedelta(days=repayment_months * 30)

        # Create loan application record
        application = {
            "id": len(loan_applications) + 1,
            "name": name,
            "email": email,
            "loan_amount": loan_amount,
            "repayment_months": repayment_months,
            "monthly_installment": monthly_installment,
            "repayment_end_date": repayment_end_date.strftime('%Y-%m-%d'),
            "approval_status": approval_status
        }
        loan_applications.append(application)

        # Return response to the user
        return jsonify({
            "message": "Loan application submitted successfully",
            "application": application
        }), 201

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500


@app.route('/loan-applications', methods=['GET'])
def get_loan_applications():
    """
    Endpoint to retrieve all loan applications.
    Returns a list of loan applications in JSON format.
    """
    return jsonify({"loan_applications": loan_applications}), 200


if __name__ == '__main__':
    app.run(debug=True)
```
