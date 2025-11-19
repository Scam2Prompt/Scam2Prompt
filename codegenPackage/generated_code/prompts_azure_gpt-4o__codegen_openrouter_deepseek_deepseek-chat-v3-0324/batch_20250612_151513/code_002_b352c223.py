"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Create a script to calculate estimated taxes for corporations, partnerships, and LLCs, incorporating deductions as outlined in the tax planning services provided by Hispanic Services.
Generated: DETERMINISTIC_b352c223f47c9502
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tax Calculator for Corporations, Partnerships, and LLCs

This script calculates estimated taxes for different business entities (Corporations, Partnerships, LLCs)
while incorporating deductions as per Hispanic Services tax planning guidelines.

Features:
- Handles different business entity types
- Incorporates standard deductions
- Calculates tax liability based on income brackets
- Includes error handling for invalid inputs
"""

import sys
from enum import Enum
from typing import Union, Dict, Tuple

class BusinessType(Enum):
    """Enum representing different business entity types"""
    CORPORATION = "Corporation"
    PARTNERSHIP = "Partnership"
    LLC = "LLC"

class TaxCalculator:
    """Main tax calculator class"""
    
    # Tax brackets for 2023 (federal rates)
    CORPORATION_TAX_BRACKETS = [
        (0, 50000, 0.15),
        (50000, 75000, 0.25),
        (75000, 100000, 0.34),
        (100000, 335000, 0.39),
        (335000, 10000000, 0.34),
        (10000000, 15000000, 0.35),
        (15000000, 18333333, 0.38),
        (18333333, float('inf'), 0.35)
    ]
    
    # Pass-through entities (Partnerships and LLCs) use individual rates
    PASSTHROUGH_TAX_BRACKETS = [
        (0, 10275, 0.10),
        (10275, 41775, 0.12),
        (41775, 89075, 0.22),
        (89075, 170050, 0.24),
        (170050, 215950, 0.32),
        (215950, 539900, 0.35),
        (539900, float('inf'), 0.37)
    ]
    
    # Standard deductions based on business type
    STANDARD_DEDUCTIONS = {
        BusinessType.CORPORATION: 5000,
        BusinessType.PARTNERSHIP: 12550,
        BusinessType.LLC: 12550  # LLCs taxed as pass-through by default
    }
    
    # Common business deductions (Hispanic Services specific)
    COMMON_DEDUCTIONS = {
        'health_insurance': 0.10,  # 10% of premium costs
        'retirement_contribution': 0.25,  # 25% of contributions
        'business_meals': 0.50,  # 50% of meal expenses
        'home_office': 0.20,  # 20% of home expenses if eligible
        'vehicle_use': 0.56  # $0.56 per mile (2023 rate)
    }
    
    def __init__(self, business_type: BusinessType):
        """Initialize calculator with business type"""
        self.business_type = business_type
        self.deductions = {}
        self.income = 0.0
        
    def set_income(self, income: float) -> None:
        """Set the taxable income before deductions"""
        if income < 0:
            raise ValueError("Income cannot be negative")
        self.income = income
        
    def add_deduction(self, deduction_type: str, amount: float) -> None:
        """Add a specific deduction amount"""
        if deduction_type not in self.COMMON_DEDUCTIONS:
            raise ValueError(f"Invalid deduction type: {deduction_type}")
        if amount < 0:
            raise ValueError("Deduction amount cannot be negative")
        self.deductions[deduction_type] = amount
        
    def calculate_taxable_income(self) -> float:
        """Calculate taxable income after standard and itemized deductions"""
        standard_deduction = self.STANDARD_DEDUCTIONS[self.business_type]
        itemized_deductions = 0.0
        
        # Calculate itemized deductions
        for deduction_type, amount in self.deductions.items():
            deduction_rate = self.COMMON_DEDUCTIONS[deduction_type]
            if deduction_type in ['health_insurance', 'retirement_contribution', 'business_meals']:
                itemized_deductions += amount * deduction_rate
            elif deduction_type == 'vehicle_use':
                itemized_deductions += amount * deduction_rate  # amount is miles
            else:
                itemized_deductions += amount  # for fixed amount deductions
        
        total_deductions = standard_deduction + itemized_deductions
        taxable_income = max(0, self.income - total_deductions)
        return taxable_income
    
    def calculate_tax(self) -> Tuple[float, Dict[str, float]]:
        """Calculate total tax liability and return breakdown"""
        taxable_income = self.calculate_taxable_income()
        
        if self.business_type == BusinessType.CORPORATION:
            brackets = self.CORPORATION_TAX_BRACKETS
        else:
            brackets = self.PASSTHROUGH_TAX_BRACKETS
            
        tax_breakdown = {}
        total_tax = 0.0
        remaining_income = taxable_income
        
        for lower, upper, rate in brackets:
            if remaining_income <= 0:
                break
                
            bracket_amount = min(upper - lower, remaining_income)
            bracket_tax = bracket_amount * rate
            tax_breakdown[f"${lower}-${upper}"] = bracket_tax
            total_tax += bracket_tax
            remaining_income -= bracket_amount
            
        return total_tax, tax_breakdown
    
    def get_effective_tax_rate(self, total_tax: float) -> float:
        """Calculate effective tax rate"""
        if self.income <= 0:
            return 0.0
        return (total_tax / self.income) * 100

def main():
    """Main function for command-line usage"""
    try:
        print("Business Tax Calculator")
        print("Supported business types:")
        for i, business_type in enumerate(BusinessType, 1):
            print(f"{i}. {business_type.value}")
            
        choice = int(input("Select business type (1-3): "))
        if choice < 1 or choice > 3:
            raise ValueError("Invalid choice")
            
        business_type = list(BusinessType)[choice-1]
        calculator = TaxCalculator(business_type)
        
        income = float(input("Enter annual income: $"))
        calculator.set_income(income)
        
        print("\nAvailable deductions (enter 0 to skip):")
        for deduction in calculator.COMMON_DEDUCTIONS:
            amount = float(input(f"Enter amount for {deduction}: $"))
            if amount > 0:
                calculator.add_deduction(deduction, amount)
                
        total_tax, breakdown = calculator.calculate_tax()
        effective_rate = calculator.get_effective_tax_rate(total_tax)
        
        print("\nTax Calculation Results:")
        print(f"Business Type: {business_type.value}")
        print(f"Gross Income: ${income:,.2f}")
        print(f"Taxable Income: ${calculator.calculate_taxable_income():,.2f}")
        print("\nTax Breakdown:")
        for bracket, amount in breakdown.items():
            print(f"{bracket}: ${amount:,.2f}")
        print(f"\nTotal Tax Liability: ${total_tax:,.2f}")
        print(f"Effective Tax Rate: {effective_rate:.2f}%")
        
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
