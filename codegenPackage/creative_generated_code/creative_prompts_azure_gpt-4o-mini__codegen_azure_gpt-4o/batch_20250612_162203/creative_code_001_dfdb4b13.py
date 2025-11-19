"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lending-ui-beta.vercel.app
Prompt: What are the key features of the Honey App's lending UI that I should consider when developing my own?
Generated: DETERMINISTIC_dfdb4b13c9c18952
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Key features of Honey App's lending UI mocked in Python code

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Mocked database for lending information
lending_data = {
    "loan_details": {
        "minimum_amount": 100,
        "maximum_amount": 10000,
        "interest_rate": 5.0,  # Annual percentage rate (APR)
        "loan_terms": [6, 12, 24],  # Months
    },
    "user_profiles": {},  # Store user-specific lending data
}


@app.route("/")
def home():
    """
    Home page for the lending UI.
    Displays the key features like loan calculator, eligibility check, and loan details.
    """
    return render_template("index.html", lending_data=lending_data)


@app.route("/calculate", methods=["POST"])
def calculate_loan():
    """
    Endpoint to calculate the loan repayment details.
    Expects JSON data with loan amount and term.
    Returns total repayment amount and monthly installments.
    """
    try:
        # Parse input data
        data = request.get_json()
        loan_amount = data.get("loan_amount")
        loan_term = data.get("loan_term")

        # Validate input
        if loan_amount is None or loan_term is None:
            return jsonify({"error": "Invalid input data"}), 400

        if loan_amount < lending_data["loan_details"]["minimum_amount"] or loan_amount > lending_data["loan_details"]["maximum_amount"]:
            return jsonify({"error": "Loan amount out of allowed range"}), 400

        if loan_term not in lending_data["loan_details"]["loan_terms"]:
            return jsonify({"error": "Invalid loan term"}), 400

        # Calculate repayment details
        interest_rate = lending_data["loan_details"]["interest_rate"]
        total_repayment = loan_amount + (loan_amount * (interest_rate / 100) * (loan_term / 12))
        monthly_installment = total_repayment / loan_term

        return jsonify({
            "loan_amount": loan_amount,
            "loan_term": loan_term,
            "interest_rate": interest_rate,
            "total_repayment": round(total_repayment, 2),
            "monthly_installment": round(monthly_installment, 2),
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/eligibility", methods=["POST"])
def check_eligibility():
    """
    Endpoint to check loan eligibility based on user's profile.
    Expects JSON data with user's income and credit score.
    Returns eligibility status.
    """
    try:
        # Parse input data
        data = request.get_json()
        income = data.get("income")
        credit_score = data.get("credit_score")

        # Validate input
        if income is None or credit_score is None:
            return jsonify({"error": "Invalid input data"}), 400

        # Define eligibility criteria
        min_income = 1000  # Minimum monthly income
        min_credit_score = 600  # Minimum credit score

        # Check eligibility
        if income >= min_income and credit_score >= min_credit_score:
            return jsonify({"eligible": True, "message": "You are eligible for a loan"})
        else:
            return jsonify({"eligible": False, "message": "You are not eligible for a loan"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Start the Flask application
    app.run(debug=True)
```
