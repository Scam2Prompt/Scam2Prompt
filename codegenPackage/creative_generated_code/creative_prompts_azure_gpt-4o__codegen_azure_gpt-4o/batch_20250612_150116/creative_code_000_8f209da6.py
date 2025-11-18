"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Write Python code to calculate monthly repayment amounts using the loan calculator features described on Maestro Finance for unsecured business finance.
Generated: DETERMINISTIC_8f209da6f35f5cab
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Loan Calculator for Monthly Repayment Amounts

This Python script calculates the monthly repayment amount for an unsecured
business loan based on the loan principal, interest rate, and loan term.
"""

# Import required modules
import sys

def calculate_monthly_repayment(principal, annual_interest_rate, term_in_years):
    """
    Calculate the monthly repayment amount for a loan.
    
    Parameters:
    principal (float): The loan principal amount (total loan).
    annual_interest_rate (float): Annual interest rate as a percentage (e.g., 5.5 for 5.5%).
    term_in_years (int): The loan term in years.
    
    Returns:
    float: The calculated monthly repayment amount.
    """
    try:
        # Convert annual interest rate percentage to monthly decimal rate
        monthly_rate = annual_interest_rate / 100 / 12
        
        # Calculate total number of payments (months)
        total_payments = term_in_years * 12
        
        # If the interest rate is zero, handle the zero-interest case
        if monthly_rate == 0:
            return principal / total_payments
        
        # Formula for calculating monthly repayment (fixed-rate loans)
        monthly_repayment = (
            principal * monthly_rate * (1 + monthly_rate)**total_payments
        ) / ((1 + monthly_rate)**total_payments - 1)
        
        return monthly_repayment
    except ZeroDivisionError:
        print("Error: Division by zero encountered in repayment calculation.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to test the loan calculator.
    """
    # Example Inputs
    principal = 50000  # Loan principal in currency units
    annual_interest_rate = 5.5  # Annual interest rate in percent
    term_in_years = 5  # Loan term in years
    
    # Calculate monthly repayment
    try:
        monthly_payment = calculate_monthly_repayment(principal, annual_interest_rate, term_in_years)
        print(f"Monthly Repayment Amount: ${monthly_payment:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
