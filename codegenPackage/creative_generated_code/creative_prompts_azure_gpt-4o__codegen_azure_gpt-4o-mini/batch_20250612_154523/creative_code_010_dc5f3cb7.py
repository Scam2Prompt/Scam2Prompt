"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Create a Python script to simulate the calculation of income tax for individuals, based on the "Impuesto a la renta persona natural" course from AulaContable.
Generated: DETERMINISTIC_dc5f3cb704ecce9e
Batch ID: 20250612_154523
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
    """Class to calculate income tax for individuals."""

    # Define tax brackets as a list of tuples (upper_limit, rate)
    TAX_BRACKETS = [
        (12000, 0.0),   # Up to 12,000: 0%
        (20000, 0.1),   # 12,001 - 20,000: 10%
        (35000, 0.2),   # 20,001 - 35,000: 20%
        (50000, 0.3),   # 35,001 - 50,000: 30%
        (float('inf'), 0.4)  # Over 50,000: 40%
    ]

    def __init__(self, total_income):
        """Initialize the calculator with the total income."""
        if total_income < 0:
            raise ValueError("Total income must be a non-negative value.")
        self.total_income = total_income

    def calculate_tax(self):
        """Calculate the total income tax based on the defined brackets."""
        tax = 0.0
        remaining_income = self.total_income

        for upper_limit, rate in self.TAX_BRACKETS:
            if remaining_income <= 0:
                break

            # Calculate the taxable income for the current bracket
            taxable_income = min(remaining_income, upper_limit - (self.TAX_BRACKETS[self.TAX_BRACKETS.index((upper_limit, rate)) - 1][0] if self.TAX_BRACKETS.index((upper_limit, rate)) > 0 else 0))

            # Calculate tax for the current bracket
            tax += taxable_income * rate

            # Reduce the remaining income
            remaining_income -= taxable_income

        return tax

def main():
    """Main function to execute the tax calculation."""
    try:
        # User input for total income
        total_income = float(input("Enter the total income: "))
        calculator = TaxCalculator(total_income)
        tax_due = calculator.calculate_tax()
        
        print(f"The calculated tax for an income of {total_income} is: {tax_due:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
