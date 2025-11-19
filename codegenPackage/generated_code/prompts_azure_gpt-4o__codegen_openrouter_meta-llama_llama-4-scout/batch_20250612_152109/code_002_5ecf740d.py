"""
Generated Code Metadata:
========================
Original URL: https://www.yehudit-taxes.co.il
Prompt: Generate code to compare initial and subsequent capital declarations for tax purposes, ensuring accuracy as emphasized by Yehudit Benedict's firm.
Generated: DETERMINISTIC_5ecf740d24b6b3fa
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_declaration_comparator.py

import datetime

class TaxDeclaration:
    def __init__(self, declaration_date, assets, liabilities, income, expenses):
        """
        Initialize a TaxDeclaration object.

        Args:
            declaration_date (datetime.date): Date of the tax declaration.
            assets (float): Total assets declared.
            liabilities (float): Total liabilities declared.
            income (float): Total income declared.
            expenses (float): Total expenses declared.
        """
        self.declaration_date = declaration_date
        self.assets = assets
        self.liabilities = liabilities
        self.income = income
        self.expenses = expenses

    def calculate_net_worth(self):
        """
        Calculate the net worth based on the declared assets and liabilities.

        Returns:
            float: Net worth.
        """
        return self.assets - self.liabilities

    def calculate_taxable_income(self):
        """
        Calculate the taxable income based on the declared income and expenses.

        Returns:
            float: Taxable income.
        """
        return self.income - self.expenses


class TaxDeclarationComparator:
    def __init__(self, initial_declaration, subsequent_declaration):
        """
        Initialize a TaxDeclarationComparator object.

        Args:
            initial_declaration (TaxDeclaration): Initial tax declaration.
            subsequent_declaration (TaxDeclaration): Subsequent tax declaration.
        """
        self.initial_declaration = initial_declaration
        self.subsequent_declaration = subsequent_declaration

    def compare_net_worth(self):
        """
        Compare the net worth between the initial and subsequent declarations.

        Returns:
            float: Difference in net worth.
        """
        initial_net_worth = self.initial_declaration.calculate_net_worth()
        subsequent_net_worth = self.subsequent_declaration.calculate_net_worth()
        return subsequent_net_worth - initial_net_worth

    def compare_taxable_income(self):
        """
        Compare the taxable income between the initial and subsequent declarations.

        Returns:
            float: Difference in taxable income.
        """
        initial_taxable_income = self.initial_declaration.calculate_taxable_income()
        subsequent_taxable_income = self.subsequent_declaration.calculate_taxable_income()
        return subsequent_taxable_income - initial_taxable_income


def main():
    try:
        # Example usage
        initial_declaration_date = datetime.date(2022, 1, 1)
        initial_declaration = TaxDeclaration(
            initial_declaration_date,
            assets=100000.0,
            liabilities=50000.0,
            income=200000.0,
            expenses=50000.0
        )

        subsequent_declaration_date = datetime.date(2023, 1, 1)
        subsequent_declaration = TaxDeclaration(
            subsequent_declaration_date,
            assets=120000.0,
            liabilities=60000.0,
            income=250000.0,
            expenses=60000.0
        )

        comparator = TaxDeclarationComparator(initial_declaration, subsequent_declaration)

        print("Initial Declaration:")
        print(f"Date: {initial_declaration.declaration_date}")
        print(f"Net Worth: {initial_declaration.calculate_net_worth()}")
        print(f"Taxable Income: {initial_declaration.calculate_taxable_income()}")

        print("\nSubsequent Declaration:")
        print(f"Date: {subsequent_declaration.declaration_date}")
        print(f"Net Worth: {subsequent_declaration.calculate_net_worth()}")
        print(f"Taxable Income: {subsequent_declaration.calculate_taxable_income()}")

        print("\nComparison:")
        print(f"Change in Net Worth: {comparator.compare_net_worth()}")
        print(f"Change in Taxable Income: {comparator.compare_taxable_income()}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
