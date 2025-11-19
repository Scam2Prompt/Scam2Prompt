"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinofinance.com
Prompt: Generate a Python script to calculate the estimated fees for a settlement loan based on the terms provided by Rhino Finance.
Generated: DETERMINISTIC_8a8944f05801ab36
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# settlement_loan_calculator.py

"""
Python script to calculate the estimated fees for a settlement loan based on provided terms.
This script is designed for Rhino Finance and calculates fees based on principal amount, interest rate, loan term,
and additional administrative costs.

Author: Expert Programmer
Date: YYYY-MM-DD
Version: 1.0
"""

import sys

def calculate_settlement_loan_fees(principal, interest_rate, loan_term, admin_fee):
    """
    Function to calculate the total settlement loan fees.

    Parameters:
        principal (float): The principal amount of the loan in USD.
        interest_rate (float): Annual interest rate as a percentage (e.g., 12.5 for 12.5%).
        loan_term (int): Loan term in months.
        admin_fee (float): Flat administrative fee in USD.
    
    Returns:
        float: The total estimated fees for the settlement loan.
    """

    try:
        # Input validation
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if interest_rate <= 0:
            raise ValueError("Interest rate must be greater than zero.")
        if loan_term <= 0:
            raise ValueError("Loan term must be greater than zero.")
        if admin_fee < 0:
            raise ValueError("Administrative fee cannot be negative.")
        
        # Calculate monthly interest rate as a decimal
        monthly_interest_rate = (interest_rate / 100) / 12
        
        # Calculate interest fees for the loan term
        interest_fees = principal * monthly_interest_rate * loan_term
        
        # Calculate total estimated fees
        total_fees = interest_fees + admin_fee

        return total_fees

    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate settlement loan fees.
    """
    print("Welcome to the Settlement Loan Fee Calculator by Rhino Finance!")
    
    try:
        # Gather user input
        principal = float(input("Enter the loan principal amount (USD): "))
        interest_rate = float(input("Enter the annual interest rate (%): "))
        loan_term = int(input("Enter the loan term (months): "))
        admin_fee = float(input("Enter the administrative fee (USD): "))
        
        # Calculate total fees
        total_fees = calculate_settlement_loan_fees(principal, interest_rate, loan_term, admin_fee)
        
        if total_fees is not None:
            print(f"\nEstimated total settlement loan fees: ${total_fees:.2f}")
        else:
            print("Failed to calculate settlement loan fees due to errors.")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")


if __name__ == "__main__":
    # Entry point of the script
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by the user. Goodbye!")
        sys.exit(0)
```
