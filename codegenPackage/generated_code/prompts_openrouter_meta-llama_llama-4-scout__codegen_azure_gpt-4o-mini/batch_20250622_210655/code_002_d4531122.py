"""
Generated Code Metadata:
========================
Original URL: https://ecg-eg.net
Prompt: "Generate a Python script to calculate tax liabilities for Egyptian businesses based on current regulations, considering factors like income, deductions, and tax brackets."
Generated: DETERMINISTIC_d453112244140d6c
Batch ID: 20250622_210655
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
    A class to calculate tax liabilities for Egyptian businesses based on current regulations.
    """

    # Define tax brackets and rates as per current Egyptian tax regulations
    TAX_BRACKETS = [
        (0, 30000, 0.0),      # Income up to 30,000 EGP: 0% tax
        (30001, 45000, 0.02), # Income from 30,001 to 45,000 EGP: 2% tax
        (45001, 60000, 0.1),  # Income from 45,001 to 60,000 EGP: 10% tax
        (60001, 200000, 0.2), # Income from 60,001 to 200,000 EGP: 20% tax
        (200001, float('inf'), 0.22) # Income above 200,000 EGP: 22% tax
    ]

    def __init__(self, income: float, deductions: float = 0.0):
        """
        Initialize the TaxCalculator with income and optional deductions.

        :param income: Total income of the business
        :param deductions: Total deductions applicable to the business
        """
        if income < 0 or deductions < 0:
            raise ValueError("Income and deductions must be non-negative values.")
        
        self.income = income
        self.deductions = deductions

    def calculate_taxable_income(self) -> float:
        """
        Calculate the taxable income after deductions.

        :return: Taxable income
        """
        taxable_income = self.income - self.deductions
        return max(taxable_income, 0)  # Ensure taxable income is not negative

    def calculate_tax(self) -> float:
        """
        Calculate the total tax liability based on the taxable income.

        :return: Total tax liability
        """
        taxable_income = self.calculate_taxable_income()
        tax_liability = 0.0

        for lower_bound, upper_bound, rate in self.TAX_BRACKETS:
            if taxable_income > lower_bound:
                # Calculate the amount within the current bracket
                amount_in_bracket = min(taxable_income, upper_bound) - lower_bound
                tax_liability += amount_in_bracket * rate

        return tax_liability

def main():
    """
    Main function to execute the tax calculation.
    """
    try:
        # Example input values
        income = float(input("Enter the total income of the business (EGP): "))
        deductions = float(input("Enter the total deductions (EGP): "))

        # Create a TaxCalculator instance
        tax_calculator = TaxCalculator(income, deductions)

        # Calculate and display the tax liability
        tax_liability = tax_calculator.calculate_tax()
        print(f"The total tax liability is: {tax_liability:.2f} EGP")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
