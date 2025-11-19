"""
Generated Code Metadata:
========================
Original URL: https://ecg-eg.net
Prompt: Generate a Python script that calculates tax liabilities based on the latest regulations mentioned by Experts Consulting Group.
Generated: DETERMINISTIC_6cb99ed9a8cbfa0a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tax Liability Calculator based on the latest regulations by Experts Consulting Group.

This script calculates tax liabilities for individuals based on the latest tax brackets,
deductions, and credits as specified by the Experts Consulting Group.

Features:
- Supports multiple tax brackets
- Handles standard deductions
- Calculates tax credits
- Validates input data
"""

import sys
from typing import Tuple, Dict, List

# Tax brackets for 2023 (single filer) as per Experts Consulting Group
TAX_BRACKETS = [
    (0, 10275, 0.10),
    (10275, 41775, 0.12),
    (41775, 89075, 0.22),
    (89075, 170050, 0.24),
    (170050, 215950, 0.32),
    (215950, 539900, 0.35),
    (539900, float('inf'), 0.37)
]

STANDARD_DEDUCTION = 12950  # Standard deduction for single filers in 2023
TAX_CREDITS = {
    'child_tax_credit': 2000,  # Per qualifying child
    'earned_income_credit': None  # Calculated based on income and family size
}

def calculate_taxable_income(gross_income: float, deductions: float = None) -> float:
    """
    Calculate taxable income after applying deductions.
    
    Args:
        gross_income: Total income before deductions
        deductions: Optional itemized deductions. If None, uses standard deduction.
    
    Returns:
        Taxable income after applying deductions
    """
    if deductions is None:
        deductions = STANDARD_DEDUCTION
    return max(0, gross_income - deductions)

def calculate_income_tax(taxable_income: float) -> float:
    """
    Calculate income tax based on tax brackets.
    
    Args:
        taxable_income: Income after deductions
    
    Returns:
        Total tax liability before credits
    """
    tax = 0.0
    for bracket in TAX_BRACKETS:
        lower, upper, rate = bracket
        if taxable_income <= lower:
            continue
        bracket_amount = min(taxable_income, upper) - lower
        tax += bracket_amount * rate
    return tax

def calculate_earned_income_credit(income: float, children: int) -> float:
    """
    Calculate Earned Income Tax Credit based on income and number of children.
    
    Args:
        income: Adjusted gross income
        children: Number of qualifying children
    
    Returns:
        Amount of EITC credit
    """
    # Simplified EITC calculation (actual rules are more complex)
    if children == 0:
        if income < 17320:
            return income * 0.0765
        elif income < 16480:
            return 1328
        else:
            return max(0, 1328 - (income - 16480) * 0.0765)
    elif children == 1:
        if income < 25520:
            return min(3573, income * 0.34)
        elif income < 24620:
            return 3573
        else:
            return max(0, 3573 - (income - 24620) * 0.1598)
    else:  # 2 or more children
        if income < 25520:
            return min(5904, income * 0.40)
        elif income < 24620:
            return 5904
        else:
            return max(0, 5904 - (income - 24620) * 0.2106)

def calculate_tax_credits(income: float, credits_info: Dict) -> float:
    """
    Calculate total tax credits based on provided information.
    
    Args:
        income: Adjusted gross income
        credits_info: Dictionary containing credit information
    
    Returns:
        Total tax credits
    """
    total_credits = 0.0
    
    # Child Tax Credit
    children = credits_info.get('children', 0)
    total_credits += children * TAX_CREDITS['child_tax_credit']
    
    # Earned Income Credit
    if credits_info.get('calculate_eitc', False):
        total_credits += calculate_earned_income_credit(income, children)
    
    # Add other credits here as needed
    return total_credits

def validate_input(income: float, deductions: float = None) -> Tuple[bool, str]:
    """
    Validate input parameters.
    
    Args:
        income: Gross income
        deductions: Optional itemized deductions
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if income < 0:
        return (False, "Income cannot be negative")
    if deductions is not None and deductions < 0:
        return (False, "Deductions cannot be negative")
    return (True, "")

def calculate_tax_liability(gross_income: float, 
                          deductions: float = None,
                          credits_info: Dict = None) -> Dict:
    """
    Calculate total tax liability.
    
    Args:
        gross_income: Total income before deductions
        deductions: Optional itemized deductions
        credits_info: Dictionary containing credit information
    
    Returns:
        Dictionary containing tax details
    """
    # Initialize credits_info if not provided
    if credits_info is None:
        credits_info = {}
    
    # Validate input
    is_valid, error_msg = validate_input(gross_income, deductions)
    if not is_valid:
        return {"error": error_msg}
    
    # Calculate taxable income
    taxable_income = calculate_taxable_income(gross_income, deductions)
    
    # Calculate income tax
    income_tax = calculate_income_tax(taxable_income)
    
    # Calculate tax credits
    tax_credits = calculate_tax_credits(gross_income, credits_info)
    
    # Calculate final tax liability
    tax_liability = max(0, income_tax - tax_credits)
    
    return {
        "gross_income": gross_income,
        "taxable_income": taxable_income,
        "income_tax": income_tax,
        "tax_credits": tax_credits,
        "tax_liability": tax_liability
    }

def main():
    """Main function for command-line usage."""
    try:
        # Get input from user
        gross_income = float(input("Enter your gross income: $"))
        deductions = input("Enter itemized deductions (leave blank for standard deduction): $")
        deductions = float(deductions) if deductions.strip() else None
        
        children = int(input("Enter number of qualifying children: "))
        calculate_eitc = input("Calculate Earned Income Credit? (y/n): ").lower() == 'y'
        
        credits_info = {
            'children': children,
            'calculate_eitc': calculate_eitc
        }
        
        # Calculate tax liability
        result = calculate_tax_liability(gross_income, deductions, credits_info)
        
        if 'error' in result:
            print(f"Error: {result['error']}")
            sys.exit(1)
        
        # Display results
        print("\nTax Calculation Results:")
        print(f"Gross Income: ${result['gross_income']:,.2f}")
        print(f"Taxable Income: ${result['taxable_income']:,.2f}")
        print(f"Income Tax: ${result['income_tax']:,.2f}")
        print(f"Tax Credits: ${result['tax_credits']:,.2f}")
        print(f"Final Tax Liability: ${result['tax_liability']:,.2f}")
        
    except ValueError as e:
        print(f"Invalid input: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
