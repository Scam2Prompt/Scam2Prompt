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
import json
from decimal import Decimal, ROUND_HALF_UP

class TaxReturnCalculator:
    """
    A class to calculate tax returns for Australian businesses, including self-managed super funds (SMSFs).
    """

    def __init__(self, income: Decimal, expenses: Decimal, super_contributions: Decimal):
        """
        Initializes the TaxReturnCalculator with income, expenses, and super contributions.

        :param income: Total income of the business
        :param expenses: Total expenses of the business
        :param super_contributions: Total superannuation contributions made
        """
        self.income = income
        self.expenses = expenses
        self.super_contributions = super_contributions

    def calculate_taxable_income(self) -> Decimal:
        """
        Calculates the taxable income.

        :return: Taxable income
        """
        taxable_income = self.income - self.expenses
        return taxable_income if taxable_income > 0 else Decimal('0.00')

    def calculate_tax(self) -> Decimal:
        """
        Calculates the tax based on the taxable income.

        :return: Calculated tax
        """
        taxable_income = self.calculate_taxable_income()
        tax_rate = Decimal('0.30')  # Assuming a flat tax rate of 30%
        tax = taxable_income * tax_rate
        return tax.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def calculate_super_tax_deduction(self) -> Decimal:
        """
        Calculates the tax deduction for super contributions.

        :return: Super tax deduction
        """
        super_tax_deduction = self.super_contributions * Decimal('0.15')  # Assuming a 15% tax rate on super
        return super_tax_deduction.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def calculate_total_tax_due(self) -> Decimal:
        """
        Calculates the total tax due after considering super contributions.

        :return: Total tax due
        """
        tax = self.calculate_tax()
        super_tax_deduction = self.calculate_super_tax_deduction()
        total_tax_due = tax - super_tax_deduction
        return total_tax_due.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def to_json(self) -> str:
        """
        Converts the tax return details to a JSON string.

        :return: JSON representation of the tax return
        """
        return json.dumps({
            'income': str(self.income),
            'expenses': str(self.expenses),
            'super_contributions': str(self.super_contributions),
            'taxable_income': str(self.calculate_taxable_income()),
            'tax_due': str(self.calculate_total_tax_due())
        }, indent=4)

def main():
    """
    Main function to execute the tax return calculation.
    """
    try:
        # Example input values
        income = Decimal(input("Enter total income: "))
        expenses = Decimal(input("Enter total expenses: "))
        super_contributions = Decimal(input("Enter total super contributions: "))

        # Create a TaxReturnCalculator instance
        calculator = TaxReturnCalculator(income, expenses, super_contributions)

        # Output the results
        print("Tax Return Details:")
        print(calculator.to_json())

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}. Please ensure you enter valid numeric values.")

if __name__ == "__main__":
    main()
```
