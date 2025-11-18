"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carthewchautaxreports.pages.dev
Prompt: Write Python code to calculate tax returns for Australian clients, incorporating the principles outlined by Carthew Chau & Co's tax and accounting services.
Generated: DETERMINISTIC_ee01cb390d3f572b
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TaxCalculator:
    """
    A class to calculate tax returns for Australian clients based on income and deductions.
    Incorporates principles outlined by Carthew Chau & Co's tax and accounting services.
    """

    def __init__(self, income: float, deductions: float):
        """
        Initializes the TaxCalculator with income and deductions.

        :param income: Total income for the year
        :param deductions: Total deductions for the year
        """
        self.income = income
        self.deductions = deductions

    def calculate_taxable_income(self) -> float:
        """
        Calculate the taxable income by subtracting deductions from income.

        :return: Taxable income
        """
        taxable_income = self.income - self.deductions
        return max(taxable_income, 0)  # Ensure taxable income does not go below zero

    def calculate_tax(self) -> float:
        """
        Calculate the tax based on the taxable income using progressive tax rates.

        :return: Calculated tax due
        """
        taxable_income = self.calculate_taxable_income()
        tax_due = 0

        # Define tax brackets and rates
        tax_brackets = [
            (18200, 0.0),    # Income up to $18,200 is tax-free
            (45000, 0.19),   # Next $45,000 taxed at 19%
            (120000, 0.325), # Next $120,000 taxed at 32.5%
            (180000, 0.37),  # Next $180,000 taxed at 37%
            (float('inf'), 0.45) # Income above $180,000 taxed at 45%
        ]

        previous_bracket_limit = 0

        for limit, rate in tax_brackets:
            if taxable_income > previous_bracket_limit:
                income_in_this_bracket = min(taxable_income, limit) - previous_bracket_limit
                tax_due += income_in_this_bracket * rate
                previous_bracket_limit = limit
            else:
                break

        return tax_due

    def get_tax_return(self) -> dict:
        """
        Get a summary of the tax return including income, deductions, taxable income, and tax due.

        :return: A dictionary containing the tax return details
        """
        try:
            return {
                'Income': self.income,
                'Deductions': self.deductions,
                'Taxable Income': self.calculate_taxable_income(),
                'Tax Due': self.calculate_tax()
            }
        except Exception as e:
            # Log the exception or handle it appropriately in a real application
            print(f"Error calculating tax return: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    # Example input for the TaxCalculator
    try:
        income = float(input("Enter total income: "))
        deductions = float(input("Enter total deductions: "))

        tax_calculator = TaxCalculator(income, deductions)
        tax_return = tax_calculator.get_tax_return()

        print("\nTax Return Summary:")
        for key, value in tax_return.items():
            print(f"{key}: {value}")

    except ValueError:
        print("Invalid input. Please enter numeric values for income and deductions.")
```
