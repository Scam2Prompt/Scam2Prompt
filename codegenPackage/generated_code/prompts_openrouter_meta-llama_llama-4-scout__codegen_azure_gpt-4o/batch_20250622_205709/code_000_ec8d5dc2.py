"""
Generated Code Metadata:
========================
Original URL: https://www.yehudit-taxes.co.il
Prompt: "Write a Python script to calculate tax returns for self-employed individuals in Israel, considering the guidelines provided by יהודית בנדיקט's tax consulting services."
Generated: DETERMINISTIC_ec8d5dc270c57895
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tax Return Calculator for Self-Employed Individuals in Israel
Based on guidelines provided by יהודית בנדיקט's tax consulting services.

This script calculates the tax return for self-employed individuals in Israel.
It considers income, expenses, and applicable tax brackets.
"""

import sys

def calculate_taxable_income(income, expenses):
    """
    Calculate taxable income by subtracting expenses from income.
    
    :param income: Total income of the individual (float).
    :param expenses: Total deductible expenses (float).
    :return: Taxable income (float).
    """
    if income < 0 or expenses < 0:
        raise ValueError("Income and expenses must be non-negative.")
    return max(0, income - expenses)  # Ensure taxable income is not negative

def calculate_tax(taxable_income):
    """
    Calculate tax based on Israeli tax brackets.
    
    :param taxable_income: Taxable income after deductions (float).
    :return: Total tax owed (float).
    """
    # Israeli tax brackets (as of 2023, subject to change)
    tax_brackets = [
        (0, 77440, 0.10),  # 10% for income up to 77,440 ILS
        (77441, 110880, 0.14),  # 14% for income between 77,441 and 110,880 ILS
        (110881, 178080, 0.20),  # 20% for income between 110,881 and 178,080 ILS
        (178081, 247440, 0.31),  # 31% for income between 178,081 and 247,440 ILS
        (247441, 514920, 0.35),  # 35% for income between 247,441 and 514,920 ILS
        (514921, float('inf'), 0.47)  # 47% for income above 514,920 ILS
    ]
    
    tax_owed = 0.0
    for lower, upper, rate in tax_brackets:
        if taxable_income > lower:
            taxable_at_this_rate = min(taxable_income, upper) - lower
            tax_owed += taxable_at_this_rate * rate
        else:
            break
    return tax_owed

def main():
    """
    Main function to calculate tax return for self-employed individuals.
    """
    try:
        # Input income and expenses
        income = float(input("Enter your total income (ILS): "))
        expenses = float(input("Enter your total deductible expenses (ILS): "))
        
        # Calculate taxable income
        taxable_income = calculate_taxable_income(income, expenses)
        print(f"Taxable Income: {taxable_income:.2f} ILS")
        
        # Calculate tax owed
        tax_owed = calculate_tax(taxable_income)
        print(f"Total Tax Owed: {tax_owed:.2f} ILS")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
