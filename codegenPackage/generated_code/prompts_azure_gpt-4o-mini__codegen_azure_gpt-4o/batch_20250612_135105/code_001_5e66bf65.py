"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: How can I implement a financing calculator for HVAC services that reflects the 9.99% financing options available at Quality Sheet Metal, Inc.?
Generated: DETERMINISTIC_5e66bf65c8669aca
Batch ID: 20250612_135105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financing_calculator.py

# Import necessary modules
import math

def calculate_monthly_payment(principal, annual_interest_rate, loan_term_years):
    """
    Calculate the monthly payment for a loan based on principal, annual interest rate, and loan term.

    Args:
        principal (float): The loan amount (in dollars).
        annual_interest_rate (float): The annual interest rate (in percentage).
        loan_term_years (int): The loan term (in years).

    Returns:
        float: The monthly payment amount (in dollars).
    """
    try:
        # Convert annual interest rate to monthly interest rate (as a decimal)
        monthly_interest_rate = (annual_interest_rate / 100) / 12

        # Convert loan term from years to months
        loan_term_months = loan_term_years * 12

        # Calculate monthly payment using the formula for fixed-rate loans
        if monthly_interest_rate > 0:
            monthly_payment = (
                principal
                * monthly_interest_rate
                * math.pow(1 + monthly_interest_rate, loan_term_months)
            ) / (math.pow(1 + monthly_interest_rate, loan_term_months) - 1)
        else:
            # If interest rate is 0, simply divide principal by loan term months
            monthly_payment = principal / loan_term_months

        return round(monthly_payment, 2)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while calculating the monthly payment: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate financing options.
    """
    print("Welcome to Quality Sheet Metal, Inc. Financing Calculator!")
    print("We offer a 9.99% annual interest rate financing option.")

    try:
        # Get user input for principal, loan term, and interest rate
        principal = float(input("Enter the loan amount (in dollars): "))
        loan_term_years = int(input("Enter the loan term (in years): "))
        annual_interest_rate = 9.99  # Fixed interest rate for Quality Sheet Metal, Inc.

        # Validate inputs
        if principal <= 0 or loan_term_years <= 0:
            print("Error: Loan amount and loan term must be positive values.")
            return

        # Calculate monthly payment
        monthly_payment = calculate_monthly_payment(
            principal, annual_interest_rate, loan_term_years
        )

        if monthly_payment is not None:
            print(f"Your estimated monthly payment is: ${monthly_payment}")
        else:
            print("Unable to calculate monthly payment due to an error.")

    except ValueError:
        # Handle invalid input
        print("Error: Please enter valid numeric values for loan amount and loan term.")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
