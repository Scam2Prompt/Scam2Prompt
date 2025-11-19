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
class IncomeTaxCalculator:
    """
    A class to calculate the income tax for individuals based on the 
    "Impuesto a la renta persona natural" course from AulaContable.
    """

    def __init__(self, income):
        """
        Initializes the IncomeTaxCalculator with the individual's income.

        :param income: The total income of the individual.
        """
        self.income = income

    def calculate_tax(self):
        """
        Calculates the income tax based on the income brackets.

        :return: The calculated income tax.
        """
        if self.income < 0:
            raise ValueError("Income cannot be negative.")

        tax = 0.0

        # Define tax brackets and rates
        brackets = [
            (0, 12000, 0.0),      # Up to 12,000: 0%
            (12001, 30000, 0.1),  # 12,001 to 30,000: 10%
            (30001, 70000, 0.2),  # 30,001 to 70,000: 20%
            (70001, float('inf'), 0.3)  # Above 70,000: 30%
        ]

        # Calculate tax based on brackets
        for lower, upper, rate in brackets:
            if self.income > lower:
                taxable_income = min(self.income, upper) - lower
                tax += taxable_income * rate

        return tax

def main():
    """
    Main function to execute the income tax calculation.
    """
    try:
        # Input income from the user
        income = float(input("Enter your total income: "))
        
        # Create an instance of the IncomeTaxCalculator
        calculator = IncomeTaxCalculator(income)
        
        # Calculate the tax
        tax = calculator.calculate_tax()
        
        # Output the result
        print(f"The calculated income tax is: {tax:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
