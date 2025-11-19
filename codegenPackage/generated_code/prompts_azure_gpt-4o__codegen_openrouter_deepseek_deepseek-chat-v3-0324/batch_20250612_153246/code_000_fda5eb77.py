"""
Generated Code Metadata:
========================
Original URL: https://hameiriz.co.il
Prompt: Write Python code to calculate quarterly tax payments for an independent business owner, considering Israeli tax regulations as described by Zvika Hameiri's accounting services.
Generated: DETERMINISTIC_fda5eb7741dbaa52
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Quarterly Tax Calculator for Independent Business Owners in Israel
Based on Zvika Hameiri's accounting services guidelines
"""

from decimal import Decimal, getcontext
from datetime import date
from typing import Optional, Dict, Union

# Configure decimal precision
getcontext().prec = 2

class QuarterlyTaxCalculator:
    """
    Calculate quarterly tax payments for independent business owners in Israel.
    Handles VAT, income tax, and national insurance calculations.
    """
    
    def __init__(self):
        # Tax brackets and rates (updated for current year)
        self.income_tax_brackets = [
            (0, 77480, 0.10),
            (77480, 110880, 0.14),
            (110880, 178080, 0.20),
            (178080, 247440, 0.31),
            (247440, 514920, 0.35),
            (514920, 663240, 0.47),
            (663240, float('inf'), 0.50)
        ]
        
        self.national_insurance_rates = {
            'min_income': 6333,
            'max_income': 45855,
            'employee_rate': Decimal('0.04'),
            'employer_rate': Decimal('0.0355'),
            'self_employed_rate': Decimal('0.1273')
        }
        
        self.vat_rate = Decimal('0.17')
        self.preliminary_tax_rate = Decimal('0.90')  # 90% of estimated tax
        
    def calculate_income_tax(self, annual_income: Union[Decimal, float, int]) -> Decimal:
        """
        Calculate annual income tax based on progressive tax brackets.
        
        Args:
            annual_income: Total projected annual income
            
        Returns:
            Decimal: Calculated income tax amount
        """
        if not isinstance(annual_income, Decimal):
            annual_income = Decimal(str(annual_income))
            
        remaining_income = annual_income
        tax = Decimal('0')
        
        for bracket in self.income_tax_brackets:
            lower, upper, rate = bracket
            if remaining_income <= 0:
                break
                
            bracket_amount = min(remaining_income, Decimal(str(upper - lower)))
            if bracket_amount > 0:
                tax += bracket_amount * Decimal(str(rate))
                remaining_income -= bracket_amount
                
        return tax.quantize(Decimal('0.01'))
    
    def calculate_national_insurance(self, quarterly_income: Union[Decimal, float, int]) -> Decimal:
        """
        Calculate national insurance for self-employed individuals.
        
        Args:
            quarterly_income: Income for the quarter
            
        Returns:
            Decimal: National insurance amount
        """
        if not isinstance(quarterly_income, Decimal):
            quarterly_income = Decimal(str(quarterly_income))
            
        monthly_income = quarterly_income / Decimal('3')
        min_income = Decimal(str(self.national_insurance_rates['min_income']))
        max_income = Decimal(str(self.national_insurance_rates['max_income']))
        rate = self.national_insurance_rates['self_employed_rate']
        
        if monthly_income < min_income:
            return Decimal('0')
            
        taxable_income = min(monthly_income, max_income)
        monthly_ni = (taxable_income - min_income) * rate
        quarterly_ni = monthly_ni * Decimal('3')
        
        return quarterly_ni.quantize(Decimal('0.01'))
    
    def calculate_vat(self, quarterly_revenue: Union[Decimal, float, int], 
                     quarterly_expenses: Union[Decimal, float, int] = 0) -> Decimal:
        """
        Calculate VAT payment for the quarter.
        
        Args:
            quarterly_revenue: Total revenue including VAT
            quarterly_expenses: Total expenses including VAT
            
        Returns:
            Decimal: VAT amount to pay (positive) or receive (negative)
        """
        if not isinstance(quarterly_revenue, Decimal):
            quarterly_revenue = Decimal(str(quarterly_revenue))
        if not isinstance(quarterly_expenses, Decimal):
            quarterly_expenses = Decimal(str(quarterly_expenses))
            
        vat_on_revenue = quarterly_revenue * self.vat_rate / (Decimal('1') + self.vat_rate)
        vat_on_expenses = quarterly_expenses * self.vat_rate / (Decimal('1') + self.vat_rate)
        
        return (vat_on_revenue - vat_on_expenses).quantize(Decimal('0.01'))
    
    def calculate_quarterly_tax(
        self,
        quarterly_revenue: Union[Decimal, float, int],
        quarterly_expenses: Union[Decimal, float, int] = 0,
        previous_quarters_income: Union[Decimal, float, int] = 0,
        quarter: Optional[int] = None,
        is_vat_registered: bool = True
    ) -> Dict[str, Decimal]:
        """
        Calculate all quarterly tax obligations.
        
        Args:
            quarterly_revenue: Revenue for the quarter (including VAT if applicable)
            quarterly_expenses: Expenses for the quarter (including VAT if applicable)
            previous_quarters_income: Total income from previous quarters in the tax year
            quarter: Current quarter number (1-4), used for preliminary tax calculation
            is_vat_registered: Whether the business is VAT registered
            
        Returns:
            Dict containing all tax components
        """
        if not isinstance(quarterly_revenue, Decimal):
            quarterly_revenue = Decimal(str(quarterly_revenue))
        if not isinstance(quarterly_expenses, Decimal):
            quarterly_expenses = Decimal(str(quarterly_expenses))
        if not isinstance(previous_quarters_income, Decimal):
            previous_quarters_income = Decimal(str(previous_quarters_income))
            
        # Calculate quarterly profit
        quarterly_profit = quarterly_revenue - quarterly_expenses
        
        # Calculate projected annual income
        current_quarter_income = quarterly_profit
        if quarter is not None and 1 <= quarter <= 4:
            projection_factor = Decimal('4') / Decimal(str(quarter))
            projected_annual_income = (previous_quarters_income + current_quarter_income) * projection_factor
        else:
            projected_annual_income = previous_quarters_income + current_quarter_income
            
        # Calculate tax components
        results = {}
        
        # VAT calculation (only if registered)
        if is_vat_registered:
            results['vat'] = self.calculate_vat(quarterly_revenue, quarterly_expenses)
        else:
            results['vat'] = Decimal('0')
            
        # Income tax (preliminary payment)
        annual_income_tax = self.calculate_income_tax(projected_annual_income)
        quarterly_income_tax = annual_income_tax / Decimal('4') * self.preliminary_tax_rate
        results['income_tax'] = quarterly_income_tax.quantize(Decimal('0.01'))
        
        # National insurance
        results['national_insurance'] = self.calculate_national_insurance(current_quarter_income)
        
        # Total tax payment
        results['total'] = (
            results['income_tax'] + 
            results['national_insurance'] + 
            max(results['vat'], Decimal('0'))  # Only pay VAT if positive
        ).quantize(Decimal('0.01'))
        
        return results

# Example usage
if __name__ == "__main__":
    calculator = QuarterlyTaxCalculator()
    
    # Example for Q1 with 100,000 NIS revenue, 30,000 NIS expenses
    q1_tax = calculator.calculate_quarterly_tax(
        quarterly_revenue=100000,
        quarterly_expenses=30000,
        quarter=1,
        is_vat_registered=True
    )
    
    print("Q1 Tax Calculation:")
    for key, value in q1_tax.items():
        print(f"{key.replace('_', ' ').title()}: {value} NIS")
```
