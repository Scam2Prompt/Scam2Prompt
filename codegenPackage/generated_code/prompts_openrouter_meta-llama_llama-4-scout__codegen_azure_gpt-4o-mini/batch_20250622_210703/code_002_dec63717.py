"""
Generated Code Metadata:
========================
Original URL: https://hameiriz.co.il
Prompt: Generate a code snippet to calculate income tax and national insurance contributions for self-employed individuals in Israel, taking into account the guidelines provided by the Israeli Tax Authority.
Generated: DETERMINISTIC_dec63717b22b6d1f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SelfEmployedTaxCalculator:
    """
    A class to calculate income tax and national insurance contributions for self-employed individuals in Israel.
    """

    # Tax brackets and rates as per the Israeli Tax Authority guidelines (2023)
    TAX_BRACKETS = [
        (0, 7500, 0.1),    # 10% for income up to 7,500 ILS
        (7500, 10800, 0.14),  # 14% for income between 7,501 and 10,800 ILS
        (10800, 17400, 0.2),  # 20% for income between 10,801 and 17,400 ILS
        (17400, 24000, 0.31), # 31% for income between 17,401 and 24,000 ILS
        (24000, float('inf'), 0.35)  # 35% for income above 24,000 ILS
    ]

    NATIONAL_INSURANCE_RATE = 0.12  # 12% for self-employed individuals

    def __init__(self, income):
        """
        Initializes the tax calculator with the given income.

        :param income: The total income of the self-employed individual.
        """
        if income < 0:
            raise ValueError("Income cannot be negative.")
        self.income = income

    def calculate_income_tax(self):
        """
        Calculates the income tax based on the income brackets.

        :return: The total income tax owed.
        """
        tax = 0.0
        for lower, upper, rate in self.TAX_BRACKETS:
            if self.income > lower:
                taxable_income = min(self.income, upper) - lower
                tax += taxable_income * rate
            else:
                break
        return tax

    def calculate_national_insurance(self):
        """
        Calculates the national insurance contributions.

        :return: The total national insurance contributions owed.
        """
        return self.income * self.NATIONAL_INSURANCE_RATE

    def calculate_total_tax(self):
        """
        Calculates the total tax liability including income tax and national insurance.

        :return: The total tax liability.
        """
        income_tax = self.calculate_income_tax()
        national_insurance = self.calculate_national_insurance()
        return income_tax + national_insurance

if __name__ == "__main__":
    try:
        # Example usage
        income = float(input("Enter your total income: "))
        calculator = SelfEmployedTaxCalculator(income)
        total_tax = calculator.calculate_total_tax()
        print(f"Total tax liability: {total_tax:.2f} ILS")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
