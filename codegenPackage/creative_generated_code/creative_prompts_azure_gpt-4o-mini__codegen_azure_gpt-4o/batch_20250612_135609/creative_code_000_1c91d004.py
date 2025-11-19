"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextmoney.co.th
Prompt: Write a Python script to calculate the loan amount for a motorcycle title loan based on the information provided by Next Money.
Generated: DETERMINISTIC_1c91d00429332f58
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Loan Calculation Script for Motorcycle Title Loan
This script calculates the loan amount based on the value of the motorcycle,
the annual interest rate, and the loan term. It uses industry-standard practices
such as error handling, input validation, and clear documentation.

Author: Your Name
Date: YYYY-MM-DD
"""

# Import necessary standard library
import sys

def calculate_loan_amount(motorcycle_value, interest_rate, loan_term_years):
    """
    Calculate the loan amount for a motorcycle title loan.

    Args:
        motorcycle_value (float): The estimated market value of the motorcycle.
        interest_rate (float): Annual interest rate (as a percentage).
        loan_term_years (int): Loan term in years.

    Returns:
        float: Total loan repayment amount.
    """
    try:
        # Validate inputs
        if motorcycle_value <= 0:
            raise ValueError("Motorcycle value must be greater than zero.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if loan_term_years <= 0:
            raise ValueError("Loan term must be greater than zero.")
        
        # Calculate annual interest
        annual_interest = motorcycle_value * (interest_rate / 100)
        
        # Calculate total repayment amount
        total_repayment = motorcycle_value + (annual_interest * loan_term_years)
        
        return total_repayment
    except Exception as e:
        # Handle unexpected errors
        print(f"Error: {e}")
        sys.exit(1)  # Exit the script with an error status code

def main():
    """
    Main function to interact with the user and calculate the loan amount.
    """
    print("Welcome to the Motorcycle Title Loan Calculator!")
    
    try:
        # Get user inputs
        motorcycle_value = float(input("Enter the estimated value of the motorcycle ($): "))
        interest_rate = float(input("Enter the annual interest rate (%): "))
        loan_term_years = int(input("Enter the loan term (years): "))
        
        # Calculate loan amount
        loan_amount = calculate_loan_amount(motorcycle_value, interest_rate, loan_term_years)
        
        # Display the result
        print(f"\nThe total loan repayment amount is: ${loan_amount:.2f}")
    except ValueError as ve:
        # Handle invalid inputs
        print(f"Invalid input: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Motorcycle Title Loan Calculator!")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
