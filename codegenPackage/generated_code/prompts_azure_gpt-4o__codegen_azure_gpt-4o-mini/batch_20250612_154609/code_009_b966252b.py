"""
Generated Code Metadata:
========================
Original URL: https://wealthfuned.com
Prompt: Create a Python program to simulate Wealthfuned.com's tariff pricing packages, including the minimum and maximum deposit amounts for each plan and the instant withdrawal feature.
Generated: DETERMINISTIC_b966252b8068109d
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TariffPlan:
    """
    A class to represent a tariff plan for Wealthfuned.com.

    Attributes:
        name (str): The name of the tariff plan.
        min_deposit (float): The minimum deposit amount for the plan.
        max_deposit (float): The maximum deposit amount for the plan.
        instant_withdrawal (bool): Indicates if instant withdrawal is available.
    """

    def __init__(self, name: str, min_deposit: float, max_deposit: float, instant_withdrawal: bool):
        """
        Initializes a TariffPlan instance.

        Args:
            name (str): The name of the tariff plan.
            min_deposit (float): The minimum deposit amount for the plan.
            max_deposit (float): The maximum deposit amount for the plan.
            instant_withdrawal (bool): Indicates if instant withdrawal is available.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.instant_withdrawal = instant_withdrawal

    def is_valid_deposit(self, amount: float) -> bool:
        """
        Checks if the deposit amount is valid for the tariff plan.

        Args:
            amount (float): The deposit amount to check.

        Returns:
            bool: True if the amount is valid, False otherwise.
        """
        return self.min_deposit <= amount <= self.max_deposit


class Wealthfuned:
    """
    A class to manage tariff plans for Wealthfuned.com.

    Attributes:
        plans (list): A list of available tariff plans.
    """

    def __init__(self):
        """Initializes the Wealthfuned instance with predefined tariff plans."""
        self.plans = [
            TariffPlan("Basic", 100.0, 1000.0, True),
            TariffPlan("Standard", 1000.0, 5000.0, True),
            TariffPlan("Premium", 5000.0, 20000.0, False),
        ]

    def display_plans(self):
        """Displays the available tariff plans with their details."""
        print("Available Tariff Plans:")
        for plan in self.plans:
            print(f"Name: {plan.name}, Min Deposit: {plan.min_deposit}, Max Deposit: {plan.max_deposit}, "
                  f"Instant Withdrawal: {'Yes' if plan.instant_withdrawal else 'No'}")

    def deposit(self, plan_name: str, amount: float) -> str:
        """
        Simulates a deposit into a specified tariff plan.

        Args:
            plan_name (str): The name of the tariff plan.
            amount (float): The deposit amount.

        Returns:
            str: A message indicating the result of the deposit attempt.
        """
        try:
            plan = next((p for p in self.plans if p.name == plan_name), None)
            if plan is None:
                return "Error: Tariff plan not found."

            if plan.is_valid_deposit(amount):
                return f"Successfully deposited {amount} into the {plan.name} plan."
            else:
                return f"Error: Deposit amount must be between {plan.min_deposit} and {plan.max_deposit}."
        except Exception as e:
            return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    wealthfuned = Wealthfuned()
    wealthfuned.display_plans()

    # Example deposit attempts
    print(wealthfuned.deposit("Basic", 150.0))  # Valid deposit
    print(wealthfuned.deposit("Standard", 6000.0))  # Invalid deposit
    print(wealthfuned.deposit("Premium", 10000.0))  # Valid deposit
    print(wealthfuned.deposit("Nonexistent", 500.0))  # Invalid plan
```
