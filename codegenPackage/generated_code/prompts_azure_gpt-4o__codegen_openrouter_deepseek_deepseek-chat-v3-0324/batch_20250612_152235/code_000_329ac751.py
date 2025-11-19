"""
Generated Code Metadata:
========================
Original URL: https://cart3.pages.dev
Prompt: Write Python code to automate the calculation of tax returns for Australian businesses, incorporating self-managed super funds, as described by Carthew Chau & Co.
Generated: DETERMINISTIC_329ac751085d4d53
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Australian Tax Return Calculator for Businesses with Self-Managed Super Funds (SMSF)
This script automates tax return calculations based on Australian tax laws.
"""

import datetime
from decimal import Decimal, getcontext
from typing import Dict, List, Optional, Union

# Configure decimal precision for financial calculations
getcontext().prec = 6

class TaxCalculator:
    """
    Main tax calculator class for Australian business tax returns with SMSF support.
    """
    
    # Tax rates and thresholds (2023-2024 financial year)
    COMPANY_TAX_RATE = Decimal('0.30')  # Base rate for companies
    SMSF_TAX_RATE = Decimal('0.15')     # Tax rate for SMSF
    GST_RATE = Decimal('0.10')          # Goods and Services Tax
    
    def __init__(self):
        self.income_sources = []
        self.deductions = []
        self.smsf_contributions = Decimal('0')
        self.financial_year = self._get_current_financial_year()
    
    @staticmethod
    def _get_current_financial_year() -> str:
        """Return current financial year in format 'YYYY-YYYY'."""
        today = datetime.date.today()
        if today.month < 7:
            return f"{today.year - 1}-{today.year}"
        return f"{today.year}-{today.year + 1}"
    
    def add_income(self, amount: Union[Decimal, float, int], source: str, is_gst_inclusive: bool = False) -> None:
        """
        Add an income source to the calculation.
        
        Args:
            amount: Income amount
            source: Description of income source
            is_gst_inclusive: Whether GST is included in the amount
        """
        amount = Decimal(str(amount))
        if is_gst_inclusive:
            amount = amount / (1 + self.GST_RATE)
        self.income_sources.append({
            'amount': amount,
            'source': source,
            'gst_included': is_gst_inclusive
        })
    
    def add_deduction(self, amount: Union[Decimal, float, int], description: str, is_gst_inclusive: bool = False) -> None:
        """
        Add a tax deduction to the calculation.
        
        Args:
            amount: Deduction amount
            description: Description of the deduction
            is_gst_inclusive: Whether GST is included in the amount
        """
        amount = Decimal(str(amount))
        if is_gst_inclusive:
            amount = amount / (1 + self.GST_RATE)
        self.deductions.append({
            'amount': amount,
            'description': description,
            'gst_included': is_gst_inclusive
        })
    
    def add_smsf_contribution(self, amount: Union[Decimal, float, int]) -> None:
        """
        Add a contribution to the self-managed super fund.
        
        Args:
            amount: Contribution amount
        """
        self.smsf_contributions += Decimal(str(amount))
    
    def calculate_taxable_income(self) -> Decimal:
        """Calculate total taxable income after deductions."""
        total_income = sum(item['amount'] for item in self.income_sources)
        total_deductions = sum(item['amount'] for item in self.deductions)
        return max(total_income - total_deductions, Decimal('0'))
    
    def calculate_company_tax(self) -> Decimal:
        """Calculate company tax liability."""
        taxable_income = self.calculate_taxable_income()
        return taxable_income * self.COMPANY_TAX_RATE
    
    def calculate_smsf_tax(self) -> Decimal:
        """Calculate SMSF tax liability."""
        return self.smsf_contributions * self.SMSF_TAX_RATE
    
    def calculate_gst(self) -> Dict[str, Decimal]:
        """
        Calculate GST obligations.
        
        Returns:
            Dictionary with GST collected, GST paid, and net GST payable/refundable
        """
        gst_collected = sum(
            item['amount'] * self.GST_RATE 
            for item in self.income_sources 
            if item['gst_included']
        )
        
        gst_paid = sum(
            item['amount'] * self.GST_RATE 
            for item in self.deductions 
            if item['gst_included']
        )
        
        net_gst = gst_collected - gst_paid
        
        return {
            'gst_collected': gst_collected,
            'gst_paid': gst_paid,
            'net_gst': net_gst
        }
    
    def generate_tax_report(self) -> Dict[str, Union[str, Decimal, List]]:
        """
        Generate a comprehensive tax report.
        
        Returns:
            Dictionary containing all tax calculation results
        """
        taxable_income = self.calculate_taxable_income()
        company_tax = self.calculate_company_tax()
        smsf_tax = self.calculate_smsf_tax()
        gst_calculation = self.calculate_gst()
        
        return {
            'financial_year': self.financial_year,
            'total_income': sum(item['amount'] for item in self.income_sources),
            'total_deductions': sum(item['amount'] for item in self.deductions),
            'taxable_income': taxable_income,
            'company_tax_liability': company_tax,
            'smsf_contributions': self.smsf_contributions,
            'smsf_tax_liability': smsf_tax,
            'gst_details': gst_calculation,
            'income_sources': self.income_sources,
            'deductions': self.deductions,
            'total_tax_liability': company_tax + smsf_tax
        }

# Example usage
if __name__ == "__main__":
    calculator = TaxCalculator()
    
    # Add income sources
    calculator.add_income(100000, "Product Sales", is_gst_inclusive=True)
    calculator.add_income(50000, "Consulting Services", is_gst_inclusive=False)
    
    # Add deductions
    calculator.add_deduction(20000, "Office Expenses", is_gst_inclusive=True)
    calculator.add_deduction(15000, "Employee Salaries", is_gst_inclusive=False)
    
    # Add SMSF contributions
    calculator.add_smsf_contribution(25000)
    
    # Generate and print tax report
    report = calculator.generate_tax_report()
    print("Tax Report:")
    for key, value in report.items():
        if isinstance(value, (Decimal, int, float)):
            print(f"{key.replace('_', ' ').title()}: ${value:,.2f}")
        elif isinstance(value, dict):
            print(f"\n{key.replace('_', ' ').title()}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key.replace('_', ' ').title()}: ${sub_value:,.2f}")
        else:
            print(f"{key.replace('_', ' ').title()}: {value}")
```
