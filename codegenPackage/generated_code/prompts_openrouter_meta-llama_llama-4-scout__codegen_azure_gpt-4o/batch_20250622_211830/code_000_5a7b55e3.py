"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: "Write a Python code snippet to calculate monthly payments for an unsecured business loan of £100,000 with a 5-year repayment term and an interest rate of 10% per annum."
Generated: DETERMINISTIC_5a7b55e35a6550e7
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary library
from math import pow

def calculate_monthly_payment(principal, annual_interest_rate, years):
    """
    Calculate the monthly payment for a loan using the formula for an amortizing loan.

    Args:
        principal (float): The loan amount (e.g., £100,000).
        annual_interest_rate (float): The annual interest rate as a percentage (e.g., 10 for 10%).
        years (int): The repayment term in years (e.g., 5 years).

    Returns:
        float: The monthly payment amount.
    """
    try:
        # Convert annual interest rate to monthly interest rate (as a decimal)
        monthly_interest_rate = (annual_interest_rate / 100) / 12
        
        # Total number of monthly payments
        total_months = years * 12
        
        # Calculate monthly payment using the loan amortization formula
        # Formula: M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
        if monthly_interest_rate == 0:  # Handle zero interest rate case
            monthly_payment = principal / total_months
        else:
            monthly_payment = principal * (monthly_interest_rate * pow(1 + monthly_interest_rate, total_months)) / \
                              (pow(1 + monthly_interest_rate, total_months) - 1)
        
        return monthly_payment
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while calculating the monthly payment: {e}")
        return None

# Loan details
principal_amount = 100000  # £100,000
annual_interest_rate = 10  # 10% per annum
repayment_term_years = 5   # 5 years

# Calculate the monthly payment
monthly_payment = calculate_monthly_payment(principal_amount, annual_interest_rate, repayment_term_years)

if monthly_payment is not None:
    # Display the result
    print(f"The monthly payment for the loan is: £{monthly_payment:.2f}")
else:
    print("Failed to calculate the monthly payment.")
```
