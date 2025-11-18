"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minebnb.pro
Prompt: Create a Python script that validates deposit amounts against the minimum and maximum limits for each tariff plan on MineBNB.
Generated: DETERMINISTIC_b65ea976d037ba41
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# deposit_validator.py

class TariffPlan:
    """Class representing a tariff plan with minimum and maximum deposit limits."""

    def __init__(self, name, min_deposit, max_deposit):
        """
        Initialize a TariffPlan instance.

        Args:
            name (str): The name of the tariff plan.
            min_deposit (float): The minimum deposit amount for this plan.
            max_deposit (float): The maximum deposit amount for this plan.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit

    def validate_deposit(self, deposit_amount):
        """
        Validate whether a deposit amount is within the tariff plan limits.

        Args:
            deposit_amount (float): The deposit amount to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if deposit_amount < self.min_deposit:
            print(f"Deposit amount is below the minimum limit for {self.name}.")
            return False
        elif deposit_amount > self.max_deposit:
            print(f"Deposit amount exceeds the maximum limit for {self.name}.")
            return False
        return True


def main():
    """Main function to validate deposit amounts for different tariff plans."""
    # Define the tariff plans with their limits
    tariff_plans = [
        TariffPlan("Basic Plan", 100, 1000),
        TariffPlan("Premium Plan", 500, 5000),
        TariffPlan("Gold Plan", 1000, 10000)
    ]

    # Example deposit amounts to validate
    deposit_amounts = [50, 150, 750, 3000, 12000]

    # Validate each deposit amount against all tariff plans
    for deposit in deposit_amounts:
        print(f"\nValidating deposit amount: {deposit}")
        for plan in tariff_plans:
            print(f"Checking against {plan.name}:")
            if plan.validate_deposit(deposit):
                print(f"Deposit of {deposit} is valid for {plan.name}.")
            else:
                print(f"Deposit of {deposit} is invalid for {plan.name}.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
