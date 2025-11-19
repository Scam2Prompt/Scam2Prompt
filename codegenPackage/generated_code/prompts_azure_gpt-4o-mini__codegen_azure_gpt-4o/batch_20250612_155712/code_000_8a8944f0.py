"""
Generated Code Metadata:
========================
Original URL: https://rhinofinance.com
Prompt: Generate a Python script to calculate the estimated fees for a settlement loan based on the terms provided by Rhino Finance.
Generated: DETERMINISTIC_8a8944f05801ab36
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate estimated fees for a settlement loan based on terms provided by Rhino Finance.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_settlement_loan_fees(principal, interest_rate, loan_term_months, origination_fee_rate):
    """
    Calculate the estimated fees for a settlement loan.

    Parameters:
        principal (float): The loan amount (principal).
        interest_rate (float): Annual interest rate (as a percentage).
        loan_term_months (int): Loan term in months.
        origination_fee_rate (float): Origination fee rate (as a percentage).

    Returns:
        dict: A dictionary containing the breakdown of fees and total cost.
    """
    try:
        # Validate inputs
        if principal <= 0 or interest_rate < 0 or loan_term_months <= 0 or origination_fee_rate < 0:
            raise ValueError("Invalid input values. Ensure all values are positive and non-zero where applicable.")

        # Calculate monthly interest rate
        monthly_interest_rate = interest_rate / 100 / 12

        # Calculate total interest over the loan term
        total_interest = principal * monthly_interest_rate * loan_term_months

        # Calculate origination fee
        origination_fee = principal * (origination_fee_rate / 100)

        # Calculate total cost
        total_cost = principal + total_interest + origination_fee

        # Return a breakdown of fees
        return {
            "Principal": principal,
            "Total Interest": round(total_interest, 2),
            "Origination Fee": round(origination_fee, 2),
            "Total Cost": round(total_cost, 2)
        }

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the script.
    """
    try:
        # Example input values (can be replaced with user input or external data source)
        principal = 10000.0  # Loan amount in dollars
        interest_rate = 5.0  # Annual interest rate in percentage
        loan_term_months = 12  # Loan term in months
        origination_fee_rate = 2.0  # Origination fee rate in percentage

        # Calculate fees
        fees = calculate_settlement_loan_fees(principal, interest_rate, loan_term_months, origination_fee_rate)

        # Display the results
        print("Settlement Loan Fee Breakdown:")
        for key, value in fees.items():
            print(f"{key}: ${value}")

    except Exception as e:
        print(f"An error occurred in the main function: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
