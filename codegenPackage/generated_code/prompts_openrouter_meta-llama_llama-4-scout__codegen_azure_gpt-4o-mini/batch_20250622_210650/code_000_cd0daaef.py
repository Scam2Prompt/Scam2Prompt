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
class InsuranceCalculator:
    """
    A class to calculate the cost of long-term insurance based on client details.
    """

    def __init__(self, age: int, income: float, coverage_amount: float):
        """
        Initializes the InsuranceCalculator with client details.

        :param age: Age of the client (in years)
        :param income: Annual income of the client (in dollars)
        :param coverage_amount: Desired coverage amount (in dollars)
        """
        self.age = age
        self.income = income
        self.coverage_amount = coverage_amount

    def calculate_base_rate(self) -> float:
        """
        Calculate the base insurance rate based on age.

        :return: Base rate as a float
        """
        if self.age < 18:
            raise ValueError("Age must be 18 or older.")
        elif self.age <= 30:
            return 0.05  # 5% of coverage amount
        elif self.age <= 50:
            return 0.07  # 7% of coverage amount
        elif self.age <= 65:
            return 0.1   # 10% of coverage amount
        else:
            return 0.15  # 15% of coverage amount for seniors

    def calculate_income_factor(self) -> float:
        """
        Calculate an income factor that affects the insurance cost.

        :return: Income factor as a float
        """
        if self.income < 30000:
            return 1.2  # Higher risk for lower income
        elif self.income <= 100000:
            return 1.0  # Standard risk
        else:
            return 0.8  # Lower risk for higher income

    def calculate_insurance_cost(self) -> float:
        """
        Calculate the total insurance cost based on age, income, and coverage amount.

        :return: Total insurance cost as a float
        """
        try:
            base_rate = self.calculate_base_rate()
            income_factor = self.calculate_income_factor()
            total_cost = base_rate * income_factor * self.coverage_amount
            return total_cost
        except ValueError as e:
            print(f"Error: {e}")
            return 0.0

def main():
    """
    Main function to execute the insurance cost calculation.
    """
    try:
        # Example client details
        age = 35
        income = 75000
        coverage_amount = 500000

        # Create an instance of InsuranceCalculator
        calculator = InsuranceCalculator(age, income, coverage_amount)

        # Calculate the insurance cost
        cost = calculator.calculate_insurance_cost()
        print(f"The estimated cost of long-term insurance is: ${cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
