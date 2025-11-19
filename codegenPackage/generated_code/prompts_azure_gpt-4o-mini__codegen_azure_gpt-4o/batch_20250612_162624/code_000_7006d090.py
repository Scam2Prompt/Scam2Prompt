"""
Generated Code Metadata:
========================
Original URL: https://dutton.co.nz
Prompt: Generate a Python script to calculate tax deductions based on New Zealand tax laws as outlined by Jo Dutton, Chartered Accountant.
Generated: DETERMINISTIC_7006d0909b9470cc
Batch ID: 20250612_162624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tax Deduction Calculator for New Zealand Tax Laws
Author: [Your Name]
Date: [Today's Date]

This script calculates tax deductions based on New Zealand tax laws.
It uses predefined tax brackets and rates to compute the tax payable
for a given income. The script includes error handling and follows
best practices for clean, maintainable code.

Note: Ensure the tax brackets and rates are up-to-date as per the latest
New Zealand tax laws. Consult a Chartered Accountant for accuracy.
"""

def calculate_tax(income):
    """
    Calculate the tax payable based on New Zealand tax brackets.

    Args:
        income (float): The taxable income in NZD.

    Returns:
        float: The total tax payable in NZD.
    """
    if income < 0:
        raise ValueError("Income cannot be negative.")

    # New Zealand tax brackets and rates (as of the latest update)
    tax_brackets = [
        (14000, 0.105),  # 10.5% for income up to $14,000
        (48000, 0.175),  # 17.5% for income between $14,001 and $48,000
        (70000, 0.30),   # 30% for income between $48,001 and $70,000
        (float('inf'), 0.33)  # 33% for income above $70,000
    ]

    tax_payable = 0
    previous_bracket_limit = 0

    for bracket_limit, rate in tax_brackets:
        if income > previous_bracket_limit:
            taxable_amount = min(income, bracket_limit) - previous_bracket_limit
            tax_payable += taxable_amount * rate
            previous_bracket_limit = bracket_limit
        else:
            break

    return round(tax_payable, 2)


def main():
    """
    Main function to interact with the user and calculate tax deductions.
    """
    print("Welcome to the New Zealand Tax Deduction Calculator!")
    try:
        income = float(input("Please enter your taxable income in NZD: "))
        tax = calculate_tax(income)
        print(f"Your total tax payable is: ${tax:.2f}")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid numeric income.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
