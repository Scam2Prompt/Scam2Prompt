"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziggyloan.com
Prompt: Write a Python script to calculate monthly payment amounts for loans, including interest rates and fees, based on the example provided on ziggyloan.com.
Generated: DETERMINISTIC_19845240890c535a
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Loan Payment Calculator

This script calculates the monthly payment for a loan, including interest rates and fees.
It uses the formula for fixed-rate monthly payments (amortization formula) and includes
additional fees in the calculation.

Inputs:
- Principal amount (loan amount)
- Annual interest rate (percentage)
- Loan term (in months)
- Additional fees (fixed amount)

Outputs:
- Monthly payment
"""

import sys

def calculate_monthly_payment(principal, annual_interest_rate, loan_term_months, additional_fees=0):
    """
    Calculate the monthly payment for the loan.
    
    :param principal: float - The loan amount.
    :param annual_interest_rate: float - Annual interest rate as a percentage (e.g., 5 for 5%).
    :param loan_term_months: int - Number of months for the loan term.
    :param additional_fees: float - Fixed fees added to the monthly payment. Default is 0.
    :return: float - Monthly payment amount.
    """
    try:
        # Convert annual interest rate percentage to monthly decimal rate
        monthly_interest_rate = (annual_interest_rate / 100) / 12
        
        # Calculate the fixed monthly payment using the amortization formula
        if monthly_interest_rate > 0:
            monthly_payment = (
                principal * monthly_interest_rate
                / (1 - (1 + monthly_interest_rate) ** -loan_term_months)
            )
        else:
            # No interest case
            monthly_payment = principal / loan_term_months
        
        # Add additional fees to the monthly payment
        monthly_payment += additional_fees
        
        return monthly_payment
    except ZeroDivisionError:
        # Handle division by zero error if loan_term_months is zero
        raise ValueError("Loan term months must be greater than zero.")
    except Exception as e:
        # Catch any other unexpected errors
        raise RuntimeError(f"An error occurred: {e}")

def main():
    """
    Main function to execute the loan payment calculation.
    """
    try:
        # Prompt user for inputs
        principal = float(input("Enter loan amount (principal): "))
        annual_interest_rate = float(input("Enter annual interest rate (percentage): "))
        loan_term_months = int(input("Enter loan term (in months): "))
        additional_fees = float(input("Enter additional monthly fees: "))

        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if loan_term_months <= 0:
            raise ValueError("Loan term months must be greater than zero.")
        if additional_fees < 0:
            raise ValueError("Additional fees cannot be negative.")

        # Calculate the monthly payment
        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, loan_term_months, additional_fees)

        # Display the result
        print(f"\nMonthly payment amount: ${monthly_payment:.2f}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
