"""
Generated Code Metadata:
========================
Original URL: https://supermining.website
Prompt: Write a code snippet that calculates potential earnings based on the Super Mining package rates for different investment plans.
Generated: DETERMINISTIC_9297afece6bfbb1c
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# super_mining_calculator.py

class SuperMiningCalculator:
    """
    Calculates potential earnings based on Super Mining package rates.

    Attributes:
        package_rates (dict): Dictionary of package rates with plan names as keys.
    """

    def __init__(self):
        # Define package rates as a dictionary with plan names as keys
        self.package_rates = {
            "Basic": 0.05,  # 5% daily return
            "Premium": 0.10,  # 10% daily return
            "Elite": 0.15,  # 15% daily return
        }

    def calculate_earnings(self, plan: str, investment: float, days: int) -> float:
        """
        Calculates potential earnings based on the given plan, investment, and days.

        Args:
            plan (str): Name of the investment plan.
            investment (float): Initial investment amount.
            days (int): Number of days to calculate earnings for.

        Returns:
            float: Potential earnings.

        Raises:
            ValueError: If the plan is not found or if investment or days are invalid.
        """
        if plan not in self.package_rates:
            raise ValueError(f"Invalid plan: {plan}")

        if investment <= 0:
            raise ValueError("Investment must be greater than zero")

        if days <= 0:
            raise ValueError("Days must be greater than zero")

        rate = self.package_rates[plan]
        earnings = investment * (1 + rate) ** days - investment
        return earnings

    def get_plans(self) -> list:
        """
        Returns a list of available investment plans.

        Returns:
            list: List of plan names.
        """
        return list(self.package_rates.keys())


def main():
    calculator = SuperMiningCalculator()

    print("Available plans:")
    for plan in calculator.get_plans():
        print(plan)

    plan = input("Enter the plan name: ")
    try:
        investment = float(input("Enter the investment amount: "))
        days = int(input("Enter the number of days: "))

        earnings = calculator.calculate_earnings(plan, investment, days)
        print(f"Potential earnings for {plan} plan: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
