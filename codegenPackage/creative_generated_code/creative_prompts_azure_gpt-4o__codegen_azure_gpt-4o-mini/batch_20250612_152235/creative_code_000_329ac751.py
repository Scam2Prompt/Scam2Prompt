"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Write Python code to automate the calculation of tax returns for Australian businesses, incorporating self-managed super funds, as described by Carthew Chau & Co.
Generated: DETERMINISTIC_329ac751085d4d53
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from dataclasses import dataclass

# Set the precision for decimal calculations
decimal.getcontext().prec = 4

@dataclass
class Business:
    income: decimal.Decimal
    expenses: decimal.Decimal
    superannuation_contributions: decimal.Decimal
    tax_rate: decimal.Decimal = decimal.Decimal('0.30')  # Default corporate tax rate in Australia

    def calculate_taxable_income(self) -> decimal.Decimal:
        """Calculate the taxable income for the business."""
        taxable_income = self.income - self.expenses
        return taxable_income if taxable_income > 0 else decimal.Decimal('0.00')

    def calculate_tax_payable(self) -> decimal.Decimal:
        """Calculate the tax payable based on taxable income and tax rate."""
        taxable_income = self.calculate_taxable_income()
        tax_payable = taxable_income * self.tax_rate
        return tax_payable

    def calculate_superannuation_tax_deduction(self) -> decimal.Decimal:
        """Calculate the tax deduction for superannuation contributions."""
        # Assuming that superannuation contributions are tax-deductible
        return self.superannuation_contributions

    def calculate_total_tax_liability(self) -> decimal.Decimal:
        """Calculate the total tax liability considering superannuation deductions."""
        tax_payable = self.calculate_tax_payable()
        superannuation_tax_deduction = self.calculate_superannuation_tax_deduction()
        
        total_tax_liability = tax_payable - superannuation_tax_deduction
        return total_tax_liability if total_tax_liability > 0 else decimal.Decimal('0.00')


def main():
    # Example values for business income, expenses and superannuation contributions
    income = decimal.Decimal('500000')  # Total business income
    expenses = decimal.Decimal('300000')  # Total business expenses
    superannuation_contributions = decimal.Decimal('20000')  # Total super contributions

    # Create a business instance
    business = Business(income, expenses, superannuation_contributions)

    try:
        # Calculate and print the results
        print(f"Taxable Income: AUD {business.calculate_taxable_income():.2f}")
        print(f"Tax Payable: AUD {business.calculate_tax_payable():.2f}")
        print(f"Superannuation Tax Deduction: AUD {business.calculate_superannuation_tax_deduction():.2f}")
        print(f"Total Tax Liability: AUD {business.calculate_total_tax_liability():.2f}")
    except Exception as e:
        print(f"An error occurred during tax calculation: {e}")


if __name__ == "__main__":
    main()
```
