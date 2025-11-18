"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wealthfuned.com
Prompt: Create a Python program to simulate Wealthfuned.com's tariff pricing packages, including the minimum and maximum deposit amounts for each plan and the instant withdrawal feature.
Generated: DETERMINISTIC_b966252b8068109d
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TariffPlan:
    """
    A class to represent a Tariff Plan with minimum and maximum deposit amounts.
    """

    def __init__(self, name, min_deposit, max_deposit, instant_withdrawal):
        """
        Initializes a TariffPlan instance.

        Args:
            name (str): The name of the tariff plan.
            min_deposit (float): The minimum deposit amount for the plan.
            max_deposit (float): The maximum deposit amount for the plan.
            instant_withdrawal (bool): Indicates if the plan offers instant withdrawal.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.instant_withdrawal = instant_withdrawal

    def is_valid_deposit(self, amount):
        """
        Checks if a given deposit amount is valid for the plan.

        Args:
            amount (float): The deposit amount to check.

        Returns:
            bool: True if the amount is within the deposit limits, False otherwise.
        """
        return self.min_deposit <= amount <= self.max_deposit

    def __str__(self):
        return (f'Tariff Plan: {self.name}\n'
                f'Minimum Deposit: ${self.min_deposit}\n'
                f'Maximum Deposit: ${self.max_deposit}\n'
                f'Instant Withdrawal: {"Yes" if self.instant_withdrawal else "No"}')


class WealthFund:
    """
    A class to simulate Wealthfund.com's tariff pricing packages.
    """

    def __init__(self):
        """
        Initializes the WealthFund with predefined tariff plans.
        """
        self.plans = [
            TariffPlan("Basic Plan", 100, 1000, False),
            TariffPlan("Standard Plan", 1000, 5000, True),
            TariffPlan("Premium Plan", 5000, 20000, True),
            TariffPlan("VIP Plan", 20000, 100000, True)
        ]

    def display_plans(self):
        """
        Displays all available tariff plans.
        """
        print("Available Tariff Plans:\n")
        for plan in self.plans:
            print(plan)
            print("-" * 30)

    def process_deposit(self, plan_name, amount):
        """
        Processes a deposit for a given tariff plan name.

        Args:
            plan_name (str): The name of the tariff plan.
            amount (float): The deposit amount to process.

        Raises:
            ValueError: If the plan name is invalid or the deposit amount is not valid.
        """
        plan = next((p for p in self.plans if p.name == plan_name), None)
        if plan is None:
            raise ValueError(f"Invalid plan name: {plan_name}")

        if not plan.is_valid_deposit(amount):
            raise ValueError(f"Deposit amount of ${amount} is not valid for {plan_name}")

        print(f"Successfully processed a deposit of ${amount} into {plan_name}.")


if __name__ == "__main__":
    # Create an instance of the WealthFund
    wealth_fund = WealthFund()

    # Display available plans
    wealth_fund.display_plans()

    # Example deposit processing
    try:
        # Process a valid deposit
        wealth_fund.process_deposit("Standard Plan", 1500)

        # Process an invalid deposit
        wealth_fund.process_deposit("Basic Plan", 5000)
    except ValueError as e:
        print(f"Error: {e}")
```
