"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Create a script to calculate estimated taxes for corporations, partnerships, and LLCs, incorporating deductions as outlined in the tax planning services provided by Hispanic Services.
Generated: DETERMINISTIC_b352c223f47c9502
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TaxCalculator:
    def __init__(self, income, deductions):
        """
        Initialize the TaxCalculator with income and deductions.

        :param income: Total income of the entity (float).
        :param deductions: Total deductions applicable (float).
        """
        self.income = income
        self.deductions = deductions
        self.tax_rate = 0.21  # Federal corporate tax rate as of 2023

    def calculate_taxable_income(self):
        """
        Calculate the taxable income by subtracting deductions from income.

        :return: Taxable income (float).
        """
        taxable_income = max(0, self.income - self.deductions)
        return taxable_income

    def calculate_tax(self):
        """
        Calculate the estimated taxes based on taxable income.

        :return: Estimated tax (float).
        """
        taxable_income = self.calculate_taxable_income()
        estimated_tax = taxable_income * self.tax_rate
        return estimated_tax

def main():
    """
    Main function to execute the tax calculation based on user inputs.
    """
    try:
        # Gather user inputs for income and deductions
        income = float(input("Enter the total income: "))
        deductions = float(input("Enter the total deductions: "))

        # Validate inputs
        if income < 0 or deductions < 0:
            raise ValueError("Income and deductions must be non-negative.")

        # Create a TaxCalculator instance
        tax_calculator = TaxCalculator(income, deductions)

        # Calculate estimated tax
        estimated_tax = tax_calculator.calculate_tax()

        # Output result
        print(f"Estimated Tax: ${estimated_tax:.2f}")

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
