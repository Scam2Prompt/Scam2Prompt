"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.us
Prompt: Develop a web application to calculate credit repayment schedules based on the "Simulation crédit à la consommation" tool provided by Crédit Agricole.
Generated: DETERMINISTIC_ca429aa57927889a
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import math

# Initialize Flask application
app = Flask(__name__)

# Function to calculate credit repayment schedule
def calculate_repayment_schedule(amount, duration, annual_rate):
    """
    Calculate the credit repayment schedule.

    :param amount: Loan amount (principal) in euros.
    :param duration: Duration of loan in months.
    :param annual_rate: Annual interest rate in percentage.
    :return: List of monthly payments and total repayment summary.
    """
    try:
        # Convert annual interest rate to monthly rate (percentage to decimal)
        monthly_rate = annual_rate / 100 / 12

        # Calculate monthly payment using the amortizing loan formula
        monthly_payment = amount * (monthly_rate * math.pow(1 + monthly_rate, duration)) / (math.pow(1 + monthly_rate, duration) - 1)

        # Create repayment schedule
        schedule = []
        remaining_balance = amount
        for month in range(1, duration + 1):
            # Calculate interest for the current month
            interest_payment = remaining_balance * monthly_rate

            # Calculate principal payment for the current month
            principal_payment = monthly_payment - interest_payment

            # Update remaining balance
            remaining_balance -= principal_payment

            # Append payment details for the month
            schedule.append({
                "month": month,
                "monthly_payment": round(monthly_payment, 2),
                "principal_payment": round(principal_payment, 2),
                "interest_payment": round(interest_payment, 2),
                "remaining_balance": round(remaining_balance, 2)
            })

        # Calculate total repayment summary
        total_repaid = round(monthly_payment * duration, 2)
        total_interest = round(total_repaid - amount, 2)
        summary = {
            "total_repaid": total_repaid,
            "total_interest": total_interest
        }

        return {"schedule": schedule, "summary": summary}
    except Exception as e:
        raise ValueError(f"An error occurred during calculation: {str(e)}")

# Route for calculating credit repayment schedule
@app.route('/calculate-repayment', methods=['POST'])
def calculate_repayment():
    """
    API endpoint to calculate the credit repayment schedule.
    Expects JSON payload with 'amount', 'duration', and 'annual_rate'.

    :return: JSON response containing repayment schedule and total summary.
    """
    try:
        # Parse JSON payload from request
        data = request.json
        amount = data.get('amount')
        duration = data.get('duration')
        annual_rate = data.get('annual_rate')

        # Validate input parameters
        if not (amount and duration and annual_rate):
            return jsonify({"error": "Missing required parameters: 'amount', 'duration', 'annual_rate'"}), 400
        if amount <= 0 or duration <= 0 or annual_rate < 0:
            return jsonify({"error": "Invalid input values. All values must be positive."}), 400

        # Calculate repayment schedule
        result = calculate_repayment_schedule(amount, duration, annual_rate)

        # Return result as JSON response
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

This code defines a Flask web application with a single endpoint for calculating credit repayment schedules. It includes detailed comments, proper error handling, and adheres to best practices for readability and maintainability.
