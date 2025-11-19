"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dutton.co.nz
Prompt: Generate a Python script to calculate tax deductions based on New Zealand tax laws as outlined by Jo Dutton, Chartered Accountant.
Generated: DETERMINISTIC_7006d0909b9470cc
Batch ID: 20250612_162624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TaxDeductionCalculator:
    """
    A class to calculate tax deductions based on New Zealand tax laws.
    """

    def __init__(self, income):
        """
        Initialize the calculator with the annual income.

        :param income: Annual income as a float.
        """
        if income < 0:
            raise ValueError("Income cannot be negative.")
        self.income = income

    def calculate_tax_deduction(self):
        """
        Calculate tax deductions based on income.

        :return: Tax deduction as a float.
        """
        if self.income <= 14000:
            tax_rate = 0.105
        elif self.income <= 48000:
            tax_rate = 0.175
        elif self.income <= 70000:
            tax_rate = 0.30
        else:
            tax_rate = 0.33

        tax_deduction = self.income * tax_rate
        return tax_deduction

def main():
    """
    Main function to execute the tax deduction calculation.
    """
    try:
        income_input = input("Enter your annual income: ")

        # Attempt to convert the input to a float
        income = float(income_input)

        # Create an instance of the calculator
        calculator = TaxDeductionCalculator(income)

        # Calculate the tax deduction
        deduction = calculator.calculate_tax_deduction()

        print(f"Your tax deduction is: ${deduction:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
