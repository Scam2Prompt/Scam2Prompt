"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Create a Python script to simulate the calculation of income tax for individuals, based on the "Impuesto a la renta persona natural" course from AulaContable.
Generated: DETERMINISTIC_dc5f3cb704ecce9e
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Income Tax Calculator for Individuals
This script calculates income tax for individuals based on progressive tax brackets.
Tax brackets and rates are hypothetical and should be adjusted according to the provided course material.
"""

import sys

def calculate_income_tax(income):
    """
    Calculate the income tax based on progressive tax brackets.
    :param income: (float) The individual's taxable income.
    :return: (float) The total income tax to be paid.
    """
    # Define tax brackets (lower bound, upper bound, tax rate)
    tax_brackets = [
        (0, 10000, 0.0),        # 0% tax for income between 0 and 10,000
        (10000, 30000, 0.1),    # 10% tax for income between 10,000 and 30,000
        (30000, 60000, 0.2),    # 20% tax for income between 30,000 and 60,000
        (60000, float('inf'), 0.3)  # 30% tax for income above 60,000
    ]
    
    total_tax = 0.0
    
    for lower_bound, upper_bound, rate in tax_brackets:
        if income > lower_bound:
            taxable_income = min(income, upper_bound) - lower_bound
            total_tax += taxable_income * rate
    
    return total_tax

def main():
    """
    Main function to get user input and calculate income tax.
    """
    try:
        # Get the user's income as input
        income = float(input("Enter your annual taxable income: "))
        
        if income < 0:
            raise ValueError("Income cannot be negative.")
        
        # Calculate the income tax
        tax = calculate_income_tax(income)
        
        # Display the result
        print(f"Your calculated income tax is: ${tax:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Run the main function
    main()
```
