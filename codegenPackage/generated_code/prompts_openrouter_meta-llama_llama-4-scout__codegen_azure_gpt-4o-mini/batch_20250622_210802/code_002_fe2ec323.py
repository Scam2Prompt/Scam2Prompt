"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Develop a Python script to calculate tax obligations for a company in South Africa, taking into account the latest tax guide provided by Lund & Kieck for the 2024/2025 period.
Generated: DETERMINISTIC_fe2ec323da71a3c6
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class TaxCalculator:
    """
    A class to calculate tax obligations for a company in South Africa
    based on the latest tax guide for the 2024/2025 period.
    """

    def __init__(self, income, expenses):
        """
        Initializes the TaxCalculator with income and expenses.

        :param income: Total income of the company
        :param expenses: Total expenses of the company
        """
        self.income = income
        self.expenses = expenses
        self.tax_rate = 0.28  # Corporate tax rate for South Africa

    def calculate_taxable_income(self):
        """
        Calculates the taxable income.

        :return: Taxable income
        """
        taxable_income = self.income - self.expenses
        if taxable_income < 0:
            raise ValueError("Taxable income cannot be negative.")
        return taxable_income

    def calculate_tax_obligation(self):
        """
        Calculates the tax obligation based on taxable income.

        :return: Tax obligation
        """
        taxable_income = self.calculate_taxable_income()
        tax_obligation = taxable_income * self.tax_rate
        return tax_obligation

def main():
    """
    Main function to execute the tax calculation.
    """
    try:
        # Example input data
        income = float(input("Enter the total income of the company: "))
        expenses = float(input("Enter the total expenses of the company: "))

        # Create a TaxCalculator instance
        tax_calculator = TaxCalculator(income, expenses)

        # Calculate tax obligation
        tax_obligation = tax_calculator.calculate_tax_obligation()

        # Output the result
        print(f"The tax obligation for the company is: R{tax_obligation:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
