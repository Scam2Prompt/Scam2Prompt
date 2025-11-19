"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: "Write a Python script to calculate the monthly payment for a $10000 HVAC system with 9.99% financing for 60 months."
Generated: DETERMINISTIC_166a236edce78ec8
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import the necessary library for mathematical operations
import math

def calculate_monthly_payment(principal, annual_interest_rate, months):
    """
    Calculate the monthly payment for a loan.

    Parameters:
    principal (float): The total amount of the loan.
    annual_interest_rate (float): The annual interest rate (as a percentage).
    months (int): The number of months over which the loan will be repaid.

    Returns:
    float: The monthly payment amount.
    """
    # Convert annual interest rate from percentage to decimal
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    
    # Handle the case where the interest rate is 0
    if monthly_interest_rate == 0:
        return principal / months
    
    # Calculate the monthly payment using the formula
    monthly_payment = (principal * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -months))
    
    return monthly_payment

def main():
    # Loan details
    principal = 10000  # Total amount of the HVAC system
    annual_interest_rate = 9.99  # Annual interest rate in percentage
    months = 60  # Loan term in months

    try:
        # Calculate the monthly payment
        payment = calculate_monthly_payment(principal, annual_interest_rate, months)
        
        # Output the result
        print(f"The monthly payment for a ${principal} HVAC system at {annual_interest_rate}% financing for {months} months is: ${payment:.2f}")
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while calculating the monthly payment: {e}")

if __name__ == "__main__":
    main()
```
