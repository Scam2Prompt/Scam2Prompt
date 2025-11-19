"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Write a Python script to calculate the cost of long-term insurance based on a client's age, income, and desired coverage amount, considering the services offered by TSM Wealth.
Generated: DETERMINISTIC_cd0daaef072bd276
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# long_term_insurance_calculator.py

class LongTermInsuranceCalculator:
    """
    Calculates the cost of long-term insurance based on client's age, income, and desired coverage amount.
    """

    def __init__(self, age, income, coverage_amount):
        """
        Initializes the calculator with client's details.

        Args:
            age (int): Client's age.
            income (float): Client's annual income.
            coverage_amount (float): Desired coverage amount.
        """
        self.age = age
        self.income = income
        self.coverage_amount = coverage_amount

    def calculate_premium(self):
        """
        Calculates the premium based on client's age, income, and coverage amount.

        Returns:
            float: The calculated premium.
        """
        # Base premium rates
        base_rate_25_34 = 0.05
        base_rate_35_44 = 0.07
        base_rate_45_54 = 0.10
        base_rate_55_64 = 0.15
        base_rate_65_plus = 0.20

        # Income multiplier
        income_multiplier = self.income / 100000

        # Coverage multiplier
        coverage_multiplier = self.coverage_amount / 100000

        # Age-based premium rate
        if self.age >= 25 and self.age <= 34:
            base_rate = base_rate_25_34
        elif self.age >= 35 and self.age <= 44:
            base_rate = base_rate_35_44
        elif self.age >= 45 and self.age <= 54:
            base_rate = base_rate_45_54
        elif self.age >= 55 and self.age <= 64:
            base_rate = base_rate_55_64
        elif self.age >= 65:
            base_rate = base_rate_65_plus
        else:
            raise ValueError("Invalid age")

        # Calculate premium
        premium = base_rate * income_multiplier * coverage_multiplier

        # TSM Wealth service fees (10% of premium)
        service_fee = premium * 0.10
        total_premium = premium + service_fee

        return total_premium


def main():
    try:
        age = int(input("Enter client's age: "))
        income = float(input("Enter client's annual income: $"))
        coverage_amount = float(input("Enter desired coverage amount: $"))

        calculator = LongTermInsuranceCalculator(age, income, coverage_amount)
        premium = calculator.calculate_premium()

        print(f"Calculated premium: ${premium:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
