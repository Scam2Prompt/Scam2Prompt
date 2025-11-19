"""
Generated Code Metadata:
========================
Original URL: https://www.facecar.mx
Prompt: "Generate a Python script to calculate monthly payments for a car loan in Mexico, considering the vehicle's price and loan term in months, similar to Facecar's financing options."
Generated: DETERMINISTIC_f58edab715e9ce89
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Car Loan Monthly Payment Calculator
=====================================

Calculates the monthly payment for a car loan in Mexico based on the vehicle's price and loan term.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_monthly_payment(vehicle_price, loan_term, annual_interest_rate=10.0):
    """
    Calculates the monthly payment for a car loan.

    Args:
        vehicle_price (float): The price of the vehicle.
        loan_term (int): The loan term in months.
        annual_interest_rate (float, optional): The annual interest rate. Defaults to 10.0.

    Returns:
        float: The monthly payment.

    Raises:
        ValueError: If the loan term is not a positive integer or the vehicle price is not a positive number.
    """
    if not isinstance(loan_term, int) or loan_term <= 0:
        raise ValueError("Loan term must be a positive integer.")
    if vehicle_price <= 0:
        raise ValueError("Vehicle price must be a positive number.")

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate monthly payment using the formula: M = P[r(1+r)^n]/[(1+r)^n – 1]
    monthly_payment = vehicle_price * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term) / ((1 + monthly_interest_rate) ** loan_term - 1)

    return round(monthly_payment, 2)


def main():
    try:
        vehicle_price = float(input("Enter the vehicle's price: $"))
        loan_term = int(input("Enter the loan term in months: "))

        monthly_payment = calculate_monthly_payment(vehicle_price, loan_term)

        print(f"The monthly payment is: ${monthly_payment}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
