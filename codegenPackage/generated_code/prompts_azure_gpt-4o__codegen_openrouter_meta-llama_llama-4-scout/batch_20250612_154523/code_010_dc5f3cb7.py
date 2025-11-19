"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Create a Python script to simulate the calculation of income tax for individuals, based on the "Impuesto a la renta persona natural" course from AulaContable.
Generated: DETERMINISTIC_dc5f3cb704ecce9e
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# income_tax_calculator.py

class IncomeTaxCalculator:
    """
    Calculates income tax for individuals based on the Impuesto a la renta persona natural course from AulaContable.
    """

    def __init__(self, income, deductions, tax_credits):
        """
        Initializes the calculator with income, deductions, and tax credits.

        Args:
            income (float): The individual's income.
            deductions (float): The individual's deductions.
            tax_credits (float): The individual's tax credits.
        """
        self.income = income
        self.deductions = deductions
        self.tax_credits = tax_credits

    def calculate_taxable_income(self):
        """
        Calculates the taxable income by subtracting deductions from income.

        Returns:
            float: The taxable income.
        """
        return max(self.income - self.deductions, 0)

    def calculate_income_tax(self):
        """
        Calculates the income tax based on the taxable income.

        Returns:
            float: The income tax.
        """
        taxable_income = self.calculate_taxable_income()

        # Impuesto a la renta persona natural course from AulaContable tax brackets
        tax_brackets = [
            (0, 5_000, 0.00),  # 0 - 5,000: 0%
            (5_001, 20_000, 0.10),  # 5,001 - 20,000: 10%
            (20_001, 50_000, 0.15),  # 20,001 - 50,000: 15%
            (50_001, float('inf'), 0.20)  # 50,001+: 20%
        ]

        income_tax = 0
        previous_bracket_max = 0

        for bracket_min, bracket_max, rate in tax_brackets:
            taxable_in_bracket = min(max(taxable_income - previous_bracket_max, 0), bracket_max - bracket_min)

            if taxable_in_bracket > 0:
                income_tax += taxable_in_bracket * rate

            previous_bracket_max = bracket_max

            if taxable_income <= bracket_max:
                break

        return income_tax

    def calculate_total_tax_liability(self):
        """
        Calculates the total tax liability by subtracting tax credits from income tax.

        Returns:
            float: The total tax liability.
        """
        income_tax = self.calculate_income_tax()
        return max(income_tax - self.tax_credits, 0)


def main():
    try:
        income = float(input("Enter your income: "))
        deductions = float(input("Enter your deductions: "))
        tax_credits = float(input("Enter your tax credits: "))

        calculator = IncomeTaxCalculator(income, deductions, tax_credits)
        taxable_income = calculator.calculate_taxable_income()
        income_tax = calculator.calculate_income_tax()
        total_tax_liability = calculator.calculate_total_tax_liability()

        print(f"Taxable income: {taxable_income:.2f}")
        print(f"Income tax: {income_tax:.2f}")
        print(f"Total tax liability: {total_tax_liability:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
