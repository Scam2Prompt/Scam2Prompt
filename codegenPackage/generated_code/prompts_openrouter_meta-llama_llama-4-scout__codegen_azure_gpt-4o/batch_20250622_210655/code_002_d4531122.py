"""
Generated Code Metadata:
========================
Original URL: https://ecg-eg.net
Prompt: "Generate a Python script to calculate tax liabilities for Egyptian businesses based on current regulations, considering factors like income, deductions, and tax brackets."
Generated: DETERMINISTIC_d453112244140d6c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tax Liability Calculator for Egyptian Businesses

This script calculates the tax liabilities for Egyptian businesses based on current regulations.
It considers factors such as income, deductions, and tax brackets.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_tax(income, deductions):
    """
    Calculate the tax liability based on income, deductions, and tax brackets.

    Args:
        income (float): Total income of the business.
        deductions (float): Total deductions applicable to the business.

    Returns:
        float: Total tax liability.
    """
    try:
        # Validate inputs
        if income < 0 or deductions < 0:
            raise ValueError("Income and deductions must be non-negative.")

        # Calculate taxable income
        taxable_income = max(0, income - deductions)

        # Define tax brackets and rates (Egyptian regulations as of YYYY)
        tax_brackets = [
            (0, 15000, 0.0),    # 0% tax for income up to 15,000 EGP
            (15001, 30000, 0.1), # 10% tax for income between 15,001 and 30,000 EGP
            (30001, 45000, 0.15), # 15% tax for income between 30,001 and 45,000 EGP
            (45001, float('inf'), 0.20) # 20% tax for income above 45,000 EGP
        ]

        # Calculate tax liability
        tax_liability = 0.0
        for lower, upper, rate in tax_brackets:
            if taxable_income > lower:
                taxable_amount = min(taxable_income, upper) - lower
                tax_liability += taxable_amount * rate

        return tax_liability

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate tax liability.
    """
    try:
        # Get user input
        print("Welcome to the Egyptian Business Tax Liability Calculator!")
        income = float(input("Enter your total income (EGP): "))
        deductions = float(input("Enter your total deductions (EGP): "))

        # Calculate tax liability
        tax_liability = calculate_tax(income, deductions)

        # Display the result
        print(f"Your total tax liability is: {tax_liability:.2f} EGP")

    except ValueError:
        print("Invalid input. Please enter numeric values for income and deductions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
