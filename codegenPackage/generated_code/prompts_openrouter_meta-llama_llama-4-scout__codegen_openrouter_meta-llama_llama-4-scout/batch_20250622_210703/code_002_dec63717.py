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
# israeli_tax_calculator.py

class IsraeliTaxCalculator:
    """
    Calculates income tax and national insurance contributions for self-employed individuals in Israel.
    """

    def __init__(self, income, age, is_new_immigrant=False):
        """
        Initializes the calculator with income, age, and new immigrant status.

        Args:
            income (float): Annual income.
            age (int): Age of the individual.
            is_new_immigrant (bool): Whether the individual is a new immigrant. Defaults to False.
        """
        self.income = income
        self.age = age
        self.is_new_immigrant = is_new_immigrant

    def calculate_tax(self):
        """
        Calculates income tax based on Israeli tax brackets.

        Returns:
            float: Income tax amount.
        """
        # Israeli income tax brackets (2022)
        tax_brackets = [
            (0, 67080, 0.10),  # 10% on the first 67,080 ILS
            (67081, 108680, 0.14),  # 14% on 67,081 - 108,680 ILS
            (108681, 181560, 0.20),  # 20% on 108,681 - 181,560 ILS
            (181561, 429430, 0.29),  # 29% on 181,561 - 429,430 ILS
            (429431, float('inf'), 0.47)  # 47% on above 429,430 ILS
        ]

        tax = 0
        remaining_income = self.income
        for low, high, rate in tax_brackets:
            taxable_amount = min(remaining_income, high - low)
            if taxable_amount > 0:
                tax += taxable_amount * rate
                remaining_income -= taxable_amount
            if remaining_income <= 0:
                break

        return tax

    def calculate_national_insurance(self):
        """
        Calculates national insurance contributions.

        Returns:
            float: National insurance contributions amount.
        """
        # National insurance contribution rates (2022)
        if self.is_new_immigrant:
            # New immigrants are exempt from national insurance for 3 years
            return 0

        # 12.5% on income up to 60,120 ILS
        # 2% on income above 60,120 ILS
        national_insurance_rate_low = 0.125
        national_insurance_rate_high = 0.02
        national_insurance_cap = 60120

        national_insurance = min(self.income, national_insurance_cap) * national_insurance_rate_low
        if self.income > national_insurance_cap:
            national_insurance += (self.income - national_insurance_cap) * national_insurance_rate_high

        return national_insurance

    def calculate_total_tax_liability(self):
        """
        Calculates total tax liability, including income tax and national insurance contributions.

        Returns:
            float: Total tax liability.
        """
        income_tax = self.calculate_tax()
        national_insurance = self.calculate_national_insurance()

        return income_tax + national_insurance


def main():
    try:
        income = float(input("Enter annual income: "))
        age = int(input("Enter age: "))
        is_new_immigrant = input("Are you a new immigrant? (yes/no): ").lower() == "yes"

        calculator = IsraeliTaxCalculator(income, age, is_new_immigrant)
        income_tax = calculator.calculate_tax()
        national_insurance = calculator.calculate_national_insurance()
        total_tax_liability = calculator.calculate_total_tax_liability()

        print(f"Income Tax: {income_tax:.2f} ILS")
        print(f"National Insurance: {national_insurance:.2f} ILS")
        print(f"Total Tax Liability: {total_tax_liability:.2f} ILS")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
