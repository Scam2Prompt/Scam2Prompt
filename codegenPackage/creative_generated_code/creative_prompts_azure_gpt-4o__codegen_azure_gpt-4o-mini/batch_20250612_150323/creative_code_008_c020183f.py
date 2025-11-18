"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a Python script to calculate monthly payments for HVAC systems based on the TVA Heat Pump Program details provided by Quality Sheet Metal, Inc., including "no money down" and 10-year payment plans.
Generated: DETERMINISTIC_c020183f80a7f063
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3
"""
HVAC Monthly Payment Calculator

This script calculates the monthly payments for HVAC systems based on the TVA Heat Pump Program 
details provided by Quality Sheet Metal, Inc. It supports a "no money down" plan and a 10-year payment plan.
"""

def calculate_monthly_payment(loan_amount, years=10, interest_rate=0.0):
    """
    Calculate the monthly payment for a loan using the formula for an amortizing loan.

    Args:
    loan_amount (float): The total amount of the loan.
    years (int, optional): The duration of the loan in years. Default is 10 years.
    interest_rate (float, optional): The annual interest rate as a decimal. Default is 0.0 (no interest).

    Returns:
    float: The monthly payment amount.
    """
    try:
        # Validate input types
        if not isinstance(loan_amount, (int, float)) or loan_amount < 0:
            raise ValueError("Loan amount must be a non-negative number.")
        if not isinstance(years, int) or years <= 0:
            raise ValueError("Years must be a positive integer.")
        if not isinstance(interest_rate, (int, float)) or interest_rate < 0:
            raise ValueError("Interest rate must be a non-negative number.")

        # Monthly interest rate
        monthly_rate = interest_rate / 12
        
        # Total number of payments
        number_of_payments = years * 12

        # Monthly payment calculation using the amortization formula
        if interest_rate > 0:
            monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
        else:
            monthly_payment = loan_amount / number_of_payments
        
        return monthly_payment

    except ValueError as e:
        print(f"Input error: {e}")
        return None

def main():
    """
    Main function to execute the monthly payment calculation.
    """
    try:
        # Input for loan amount, interest rate, and payment plan
        loan_amount = float(input("Enter the loan amount for HVAC system: "))
        interest_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100

        # Calculate monthly payment
        monthly_payment = calculate_monthly_payment(loan_amount, interest_rate=interest_rate)
        
        # Check if calculation was successful
        if monthly_payment is not None:
            print(f"The monthly payment for the HVAC system is: ${monthly_payment:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for loan amount and interest rate.")

if __name__ == "__main__":
    main()
```
