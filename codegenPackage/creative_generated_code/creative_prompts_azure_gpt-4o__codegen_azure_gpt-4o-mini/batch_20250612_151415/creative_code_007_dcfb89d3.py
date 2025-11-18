"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Develop a tool to calculate income tax liability for FY 2024–25, using the Income Tax Calculator described on the IFSC Finder webpage.
Generated: DETERMINISTIC_dcfb89d3322a0af4
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Income Tax Calculator for FY 2024-25

class IncomeTaxCalculator:
    """
    A class to calculate income tax liability for the financial year 2024-25.
    """

    def __init__(self, income: float):
        """
        Initializes the calculator with the provided income.

        :param income: The total income for which tax liability needs to be calculated.
        """
        if income < 0:
            raise ValueError("Income cannot be negative.")
        self.income = income

    def calculate_tax(self) -> float:
        """
        Calculates the income tax based on the income slab for FY 2024-25.

        :return: The calculated tax liability.
        """
        tax = 0.0
        # Define tax slabs and rates for FY 2024-25
        slabs = [
            (250000, 0.0),    # No tax for income up to 2.5 lakhs
            (500000, 0.05),   # 5% tax for income between 2.5 to 5 lakhs
            (1000000, 0.1),   # 10% tax for income between 5 to 10 lakhs
            (float('inf'), 0.3)  # 30% tax for income above 10 lakhs
        ]

        previous_limit = 0

        for limit, rate in slabs:
            if self.income > previous_limit:
                taxable_income = min(self.income, limit) - previous_limit
                tax += taxable_income * rate
                previous_limit = limit
            else:
                break

        return tax

    def display_tax_liability(self):
        """
        Displays the income tax liability in a user-friendly format.
        """
        try:
            tax = self.calculate_tax()
            print(f"Income: ₹{self.income:,.2f}")
            print(f"Income Tax Liability: ₹{tax:,.2f}")
        except Exception as e:
            print(f"Error calculating tax: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Input income from the user
        income_input = float(input("Enter your total income for FY 2024-25: ₹"))
        tax_calculator = IncomeTaxCalculator(income_input)
        tax_calculator.display_tax_liability()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
