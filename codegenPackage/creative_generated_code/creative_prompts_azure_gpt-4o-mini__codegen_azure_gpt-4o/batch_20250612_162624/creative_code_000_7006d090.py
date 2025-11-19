"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dutton.co.nz
Prompt: Generate a Python script to calculate tax deductions based on New Zealand tax laws as outlined by Jo Dutton, Chartered Accountant.
Generated: DETERMINISTIC_7006d0909b9470cc
Batch ID: 20250612_162624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tax Deduction Calculator - New Zealand Tax Laws
Author: [Your Name]
Date: [Current Date]
Description: This script calculates tax deductions based on New Zealand tax laws.
Disclaimer: Always consult a qualified tax advisor or chartered accountant for accurate calculations.
"""

# Import necessary modules
import sys

# Constants for New Zealand tax brackets and rates (as per Jo Dutton, Chartered Accountant)
TAX_BRACKETS = [
    {"threshold": 14000, "rate": 0.105},  # 10.5% for income up to $14,000
    {"threshold": 48000, "rate": 0.175},  # 17.5% for income between $14,001 and $48,000
    {"threshold": 70000, "rate": 0.30},   # 30% for income between $48,001 and $70,000
    {"threshold": float('inf'), "rate": 0.33}  # 33% for income above $70,000
]

def calculate_tax(income):
    """
    Calculate the total tax based on New Zealand tax brackets.
    
    Parameters:
        income (float): The gross income of the individual.
        
    Returns:
        float: The total tax to be paid.
    """
    tax = 0
    last_threshold = 0
    
    # Iterate through tax brackets to calculate tax
    for bracket in TAX_BRACKETS:
        if income > bracket['threshold']:
            taxable_income = bracket['threshold'] - last_threshold
            tax += taxable_income * bracket['rate']
            last_threshold = bracket['threshold']
        else:
            taxable_income = income - last_threshold
            tax += taxable_income * bracket['rate']
            break
    
    return tax

def calculate_net_income(income):
    """
    Calculate the net income after tax.
    
    Parameters:
        income (float): The gross income of the individual.
        
    Returns:
        float: The net income after tax deductions.
    """
    tax = calculate_tax(income)
    return income - tax

def main():
    """
    Main function to execute the tax calculation script.
    """
    try:
        # Prompt user for input
        income = float(input("Enter your annual gross income in NZD: "))
        
        if income < 0:
            raise ValueError("Income cannot be negative.")
        
        # Perform calculations
        tax = calculate_tax(income)
        net_income = calculate_net_income(income)
        
        # Output results
        print(f"\nGross Income: ${income:,.2f}")
        print(f"Total Tax: ${tax:,.2f}")
        print(f"Net Income: ${net_income:,.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}. Please enter a valid numeric income.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the NZ Tax Deduction Calculator.")

if __name__ == "__main__":
    # Ensure script runs only when executed directly
    main()
```
