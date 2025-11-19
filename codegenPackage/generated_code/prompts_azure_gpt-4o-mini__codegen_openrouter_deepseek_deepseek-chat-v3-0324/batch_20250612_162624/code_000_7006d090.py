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
New Zealand Tax Deduction Calculator based on Jo Dutton, Chartered Accountant's guidelines.

This script calculates tax deductions for individuals in New Zealand based on the latest tax laws.
It includes common deductions like income tax, student loan repayments, and KiwiSaver contributions.

Author: [Your Name]
Date: [Current Date]
"""

import sys
from typing import Union, Dict, Tuple

# Constants for 2023-2024 tax year (update as needed)
INCOME_TAX_BRACKETS = [
    (0, 14000, 0.105),
    (14001, 48000, 0.175),
    (48001, 70000, 0.30),
    (70001, 180000, 0.33),
    (180001, float('inf'), 0.39)
]

STUDENT_LOAN_RATE = 0.12
KIWISAVER_RATES = {
    '3%': 0.03,
    '4%': 0.04,
    '6%': 0.06,
    '8%': 0.08,
    '10%': 0.10
}
ACC_EARNER_LEVY_RATE = 0.0119  # 1.19% as of 2023-2024

def calculate_income_tax(income: float) -> float:
    """
    Calculate income tax based on NZ tax brackets.
    
    Args:
        income (float): Annual taxable income
        
    Returns:
        float: Total income tax payable
    """
    tax = 0.0
    for bracket in INCOME_TAX_BRACKETS:
        lower, upper, rate = bracket
        if income > lower:
            taxable_amount = min(income, upper) - lower
            tax += taxable_amount * rate
    return round(tax, 2)

def calculate_student_loan(income: float, has_student_loan: bool) -> float:
    """
    Calculate student loan repayments if applicable.
    
    Args:
        income (float): Annual income
        has_student_loan (bool): Whether the person has a student loan
        
    Returns:
        float: Student loan repayment amount
    """
    if not has_student_loan or income < 22828:  # 2023-2024 repayment threshold
        return 0.0
    return round(income * STUDENT_LOAN_RATE, 2)

def calculate_kiwisaver(income: float, kiwisaver_rate: str) -> float:
    """
    Calculate KiwiSaver contributions.
    
    Args:
        income (float): Annual income
        kiwisaver_rate (str): Selected KiwiSaver rate (e.g., '3%')
        
    Returns:
        float: KiwiSaver contribution amount
        
    Raises:
        ValueError: If invalid KiwiSaver rate is provided
    """
    if kiwisaver_rate not in KIWISAVER_RATES:
        raise ValueError(f"Invalid KiwiSaver rate. Must be one of: {list(KIWISAVER_RATES.keys())}")
    return round(income * KIWISAVER_RATES[kiwisaver_rate], 2)

def calculate_acc_levy(income: float) -> float:
    """
    Calculate ACC Earners' Levy.
    
    Args:
        income (float): Annual income
        
    Returns:
        float: ACC levy amount
    """
    return round(income * ACC_EARNER_LEVY_RATE, 2)

def calculate_net_income(
    gross_income: float,
    has_student_loan: bool = False,
    kiwisaver_rate: str = '3%'
) -> Dict[str, Union[float, Dict[str, float]]]:
    """
    Calculate all deductions and net income.
    
    Args:
        gross_income (float): Annual gross income
        has_student_loan (bool): Whether the person has a student loan
        kiwisaver_rate (str): Selected KiwiSaver rate
        
    Returns:
        dict: Dictionary containing all deductions and net income
    """
    if gross_income < 0:
        raise ValueError("Income cannot be negative")
    
    try:
        income_tax = calculate_income_tax(gross_income)
        student_loan = calculate_student_loan(gross_income, has_student_loan)
        kiwisaver = calculate_kiwisaver(gross_income, kiwisaver_rate)
        acc_levy = calculate_acc_levy(gross_income)
        
        total_deductions = income_tax + student_loan + kiwisaver + acc_levy
        net_income = gross_income - total_deductions
        
        return {
            'gross_income': gross_income,
            'deductions': {
                'income_tax': income_tax,
                'student_loan': student_loan,
                'kiwisaver': kiwisaver,
                'acc_levy': acc_levy,
                'total_deductions': total_deductions
            },
            'net_income': net_income
        }
    except Exception as e:
        raise ValueError(f"Error in calculation: {str(e)}")

def main():
    """Main function to run the tax calculator."""
    print("New Zealand Tax Deduction Calculator")
    print("-----------------------------------")
    
    try:
        gross_income = float(input("Enter your annual gross income (before tax): $"))
        has_student_loan = input("Do you have a student loan? (yes/no): ").lower() == 'yes'
        
        print("\nAvailable KiwiSaver contribution rates:")
        for rate in KIWISAVER_RATES:
            print(f"- {rate}")
        
        kiwisaver_rate = input("Select your KiwiSaver contribution rate (e.g., '3%'): ")
        
        result = calculate_net_income(gross_income, has_student_loan, kiwisaver_rate)
        
        print("\nResults:")
        print(f"Gross Income: ${result['gross_income']:,.2f}")
        print("\nDeductions:")
        print(f"- Income Tax: ${result['deductions']['income_tax']:,.2f}")
        print(f"- Student Loan: ${result['deductions']['student_loan']:,.2f}")
        print(f"- KiwiSaver ({kiwisaver_rate}): ${result['deductions']['kiwisaver']:,.2f}")
        print(f"- ACC Earners' Levy: ${result['deductions']['acc_levy']:,.2f}")
        print(f"\nTotal Deductions: ${result['deductions']['total_deductions']:,.2f}")
        print(f"Net Income: ${result['net_income']:,.2f}")
        
    except ValueError as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
