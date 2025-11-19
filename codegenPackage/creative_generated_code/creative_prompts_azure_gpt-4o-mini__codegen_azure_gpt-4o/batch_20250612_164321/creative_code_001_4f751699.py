"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuotaschevrolet.com.ar
Prompt: Can you provide code examples for integrating a financing calculator for Chevrolet cars on a website?
Generated: DETERMINISTIC_4f751699cc9125a0
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Financing Calculator for Chevrolet Cars

This program provides a backend for calculating car financing details.
It uses a simple interest formula to calculate monthly payments
based on car price, down payment, interest rate, and loan term.

"""

# Import required libraries
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Helper function to calculate financing details
def calculate_financing(car_price, down_payment, annual_interest_rate, loan_term_years):
    """
    Calculate the monthly payment for a car loan.

    Parameters:
    - car_price (float): Total price of the car.
    - down_payment (float): Initial payment made upfront.
    - annual_interest_rate (float): Annual interest rate in percentage.
    - loan_term_years (float): Loan term in years.

    Returns:
    - dict: Contains monthly payment, total payment, and total interest.
    """
    try:
        # Ensure inputs are valid
        if car_price <= 0 or down_payment < 0 or annual_interest_rate < 0 or loan_term_years <= 0:
            raise ValueError("Invalid input. Ensure all numbers are positive and loan term is greater than zero.")

        # Calculate principal loan amount
        loan_amount = car_price - down_payment

        # Convert annual interest rate to monthly interest rate
        monthly_interest_rate = annual_interest_rate / 12 / 100

        # Calculate total number of payments
        total_payments = loan_term_years * 12

        if monthly_interest_rate > 0:
            # Calculate monthly payment using the formula for simple interest loans
            monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
                              ((1 + monthly_interest_rate) ** total_payments - 1)
        else:
            # Special case: zero interest rate
            monthly_payment = loan_amount / total_payments

        # Calculate total payment and total interest
        total_payment = monthly_payment * total_payments
        total_interest = total_payment - loan_amount

        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_payment": round(total_payment, 2),
            "total_interest": round(total_interest, 2)
        }
    except ValueError as e:
        # Handle invalid input errors
        return {"error": str(e)}
    except Exception as e:
        # Handle unexpected errors
        return {"error": "An unexpected error occurred: " + str(e)}

# Define a route to handle financing calculation requests
@app.route('/calculate_financing', methods=['POST'])
def calculate_financing_endpoint():
    """
    Endpoint to calculate car financing details.

    Expects a JSON payload with the following attributes:
    - car_price (float): Total price of the car.
    - down_payment (float): Initial payment made upfront.
    - annual_interest_rate (float): Annual interest rate in percentage.
    - loan_term_years (float): Loan term in years.

    Returns:
    - JSON response containing monthly payment, total payment, and total interest.
    """
    try:
        # Parse JSON payload from the request
        data = request.get_json()

        # Extract parameters from the payload
        car_price = data.get("car_price", 0)
        down_payment = data.get("down_payment", 0)
        annual_interest_rate = data.get("annual_interest_rate", 0)
        loan_term_years = data.get("loan_term_years", 0)

        # Calculate financing details
        result = calculate_financing(car_price, down_payment, annual_interest_rate, loan_term_years)

        # Return result as JSON
        return jsonify(result), 200
    except Exception as e:
        # Handle unexpected errors in the endpoint
        return jsonify({"error": "An error occurred while processing your request: " + str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
