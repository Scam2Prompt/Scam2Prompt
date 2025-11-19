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
Self-Employed Tax Calculator for Israel
Based on guidelines from יהודית בנדיקט's tax consulting services
"""

import math
from datetime import datetime
from typing import Dict, Union, Optional

class SelfEmployedTaxCalculator:
    """
    Calculates tax obligations for self-employed individuals in Israel
    according to current tax brackets and regulations.
    """
    
    def __init__(self):
        # Tax brackets for 2023 (updated annually)
        self.tax_brackets = [
            (0, 77400, 0.10),
            (77400, 110880, 0.14),
            (110880, 178080, 0.20),
            (178080, 247440, 0.31),
            (247440, 514920, 0.35),
            (514920, 663240, 0.47),
            (663240, math.inf, 0.50)
        ]
        
        # National insurance and health tax rates
        self.national_insurance_rate = 0.125  # 12.5%
        self.health_tax_rate = 0.05  # 5%
        self.minimum_national_insurance = 223  # Minimum monthly payment in NIS
        
        # VAT rate (for businesses required to charge VAT)
        self.vat_rate = 0.17  # 17%
        
        # Expense deduction rate (default percentage of income)
        self.default_expense_rate = 0.35  # 35%
        
        # Tax credits
        self.basic_tax_credit = 216  # Monthly
        self.additional_tax_credit = 0  # Can be updated based on personal status
        
    def calculate_tax(self, annual_income: float, expenses: Optional[float] = None) -> Dict[str, Union[float, Dict]]:
        """
        Calculate total tax obligations based on annual income and expenses.
        
        Args:
            annual_income: Total annual income before expenses
            expenses: Optional specific expenses amount. If None, uses default rate.
            
        Returns:
            Dictionary containing all tax components and totals
        """
        if annual_income < 0:
            raise ValueError("Annual income cannot be negative")
            
        if expenses is None:
            expenses = annual_income * self.default_expense_rate
        elif expenses < 0:
            raise ValueError("Expenses cannot be negative")
            
        taxable_income = annual_income - expenses
        if taxable_income < 0:
            taxable_income = 0
            
        income_tax = self._calculate_income_tax(taxable_income)
        national_insurance = self._calculate_national_insurance(taxable_income)
        health_tax = self._calculate_health_tax(taxable_income)
        tax_credits = self._calculate_tax_credits()
        
        total_tax = income_tax + national_insurance + health_tax - tax_credits
        if total_tax < 0:
            total_tax = 0
            
        return {
            "annual_income": annual_income,
            "expenses": expenses,
            "taxable_income": taxable_income,
            "tax_components": {
                "income_tax": income_tax,
                "national_insurance": national_insurance,
                "health_tax": health_tax,
                "tax_credits": tax_credits
            },
            "total_tax": total_tax,
            "monthly_payment": total_tax / 12,
            "effective_tax_rate": total_tax / annual_income if annual_income > 0 else 0
        }
    
    def _calculate_income_tax(self, taxable_income: float) -> float:
        """Calculate progressive income tax based on tax brackets."""
        remaining_income = taxable_income
        total_tax = 0.0
        
        for lower, upper, rate in self.tax_brackets:
            if remaining_income <= 0:
                break
                
            bracket_amount = min(remaining_income, upper - lower)
            total_tax += bracket_amount * rate
            remaining_income -= bracket_amount
            
        return total_tax
    
    def _calculate_national_insurance(self, taxable_income: float) -> float:
        """Calculate national insurance contributions."""
        monthly_income = taxable_income / 12
        if monthly_income * self.national_insurance_rate < self.minimum_national_insurance:
            return self.minimum_national_insurance * 12
        return taxable_income * self.national_insurance_rate
    
    def _calculate_health_tax(self, taxable_income: float) -> float:
        """Calculate health tax contributions."""
        return taxable_income * self.health_tax_rate
    
    def _calculate_tax_credits(self) -> float:
        """Calculate total annual tax credits."""
        return (self.basic_tax_credit + self.additional_tax_credit) * 12
    
    def calculate_vat(self, amount: float, is_input: bool = False) -> float:
        """
        Calculate VAT amount for a given sum.
        
        Args:
            amount: The amount to calculate VAT for
            is_input: Whether this is an input VAT (purchase) vs output (sale)
            
        Returns:
            VAT amount (positive for output, negative for input)
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
            
        vat_amount = amount * self.vat_rate
        return -vat_amount if is_input else vat_amount
    
    def generate_report(self, calculation_results: Dict) -> str:
        """Generate a human-readable tax report."""
        report = []
        report.append("Self-Employed Tax Calculation Report")
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d')}")
        report.append("=" * 50)
        report.append(f"Annual Income: {calculation_results['annual_income']:,.2f} NIS")
        report.append(f"Expenses: {calculation_results['expenses']:,.2f} NIS")
        report.append(f"Taxable Income: {calculation_results['taxable_income']:,.2f} NIS")
        report.append("\nTax Components:")
        for name, value in calculation_results['tax_components'].items():
            report.append(f"  {name.replace('_', ' ').title()}: {value:,.2f} NIS")
        report.append("\nSummary:")
        report.append(f"Total Annual Tax: {calculation_results['total_tax']:,.2f} NIS")
        report.append(f"Monthly Payment: {calculation_results['monthly_payment']:,.2f} NIS")
        report.append(f"Effective Tax Rate: {calculation_results['effective_tax_rate']:.1%}")
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    try:
        calculator = SelfEmployedTaxCalculator()
        
        # Example calculation
        annual_income = 300000  # Annual income in NIS
        expenses = 80000  # Annual expenses in NIS
        
        results = calculator.calculate_tax(annual_income, expenses)
        report = calculator.generate_report(results)
        print(report)
        
        # VAT example
        sale_amount = 10000
        vat_on_sale = calculator.calculate_vat(sale_amount)
        print(f"\nVAT on sale of {sale_amount:,.2f} NIS: {vat_on_sale:,.2f} NIS")
        
    except Exception as e:
        print(f"Error in tax calculation: {str(e)}")
```
