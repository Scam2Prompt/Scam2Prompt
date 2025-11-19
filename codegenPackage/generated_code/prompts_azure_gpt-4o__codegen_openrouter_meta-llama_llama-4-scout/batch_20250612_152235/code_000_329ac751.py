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
# tax_calculator.py

class TaxCalculator:
    """
    Calculates tax returns for Australian businesses with self-managed super funds.
    """

    def __init__(self, business_income, business_expenses, super_fund_income, super_fund_expenses, tax_rate=0.25):
        """
        Initializes the TaxCalculator.

        Args:
            business_income (float): The business income.
            business_expenses (float): The business expenses.
            super_fund_income (float): The self-managed super fund income.
            super_fund_expenses (float): The self-managed super fund expenses.
            tax_rate (float, optional): The tax rate. Defaults to 0.25.
        """
        self.business_income = business_income
        self.business_expenses = business_expenses
        self.super_fund_income = super_fund_income
        self.super_fund_expenses = super_fund_expenses
        self.tax_rate = tax_rate

    def calculate_business_tax(self):
        """
        Calculates the business tax.

        Returns:
            float: The business tax.
        """
        try:
            business_taxable_income = self.business_income - self.business_expenses
            if business_taxable_income < 0:
                business_taxable_income = 0
            business_tax = business_taxable_income * self.tax_rate
            return business_tax
        except Exception as e:
            print(f"Error calculating business tax: {str(e)}")
            return None

    def calculate_super_fund_tax(self):
        """
        Calculates the self-managed super fund tax.

        Returns:
            float: The self-managed super fund tax.
        """
        try:
            super_fund_taxable_income = self.super_fund_income - self.super_fund_expenses
            if super_fund_taxable_income < 0:
                super_fund_taxable_income = 0
            super_fund_tax = super_fund_taxable_income * 0.15  # 15% tax rate for super funds
            return super_fund_tax
        except Exception as e:
            print(f"Error calculating super fund tax: {str(e)}")
            return None

    def calculate_total_tax(self):
        """
        Calculates the total tax.

        Returns:
            float: The total tax.
        """
        business_tax = self.calculate_business_tax()
        super_fund_tax = self.calculate_super_fund_tax()
        if business_tax is not None and super_fund_tax is not None:
            return business_tax + super_fund_tax
        else:
            return None


def main():
    # Example usage
    business_income = 100000
    business_expenses = 50000
    super_fund_income = 50000
    super_fund_expenses = 10000

    calculator = TaxCalculator(business_income, business_expenses, super_fund_income, super_fund_expenses)
    business_tax = calculator.calculate_business_tax()
    super_fund_tax = calculator.calculate_super_fund_tax()
    total_tax = calculator.calculate_total_tax()

    print(f"Business Tax: ${business_tax:.2f}")
    print(f"Super Fund Tax: ${super_fund_tax:.2f}")
    print(f"Total Tax: ${total_tax:.2f}")


if __name__ == "__main__":
    main()
```
