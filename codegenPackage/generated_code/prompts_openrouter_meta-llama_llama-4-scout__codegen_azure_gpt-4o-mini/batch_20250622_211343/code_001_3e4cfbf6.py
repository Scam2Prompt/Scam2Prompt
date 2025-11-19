"""
Generated Code Metadata:
========================
Original URL: https://marketsfargo.com
Prompt: Compare and contrast the features of CLASSIC, SILVER, GOLD, and VIP plans offered by Fargo Markets, focusing on leverage, spreads, and investment requirements.
Generated: DETERMINISTIC_3e4cfbf61a95ff23
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Plan:
    """
    A class to represent a trading plan with specific features.
    """

    def __init__(self, name, leverage, spread, investment_requirement):
        """
        Initializes a new trading plan.

        :param name: Name of the trading plan
        :param leverage: Leverage offered by the plan
        :param spread: Spread associated with the plan
        :param investment_requirement: Minimum investment required for the plan
        """
        self.name = name
        self.leverage = leverage
        self.spread = spread
        self.investment_requirement = investment_requirement

    def __str__(self):
        """
        Returns a string representation of the trading plan.
        """
        return (f"Plan: {self.name}\n"
                f"Leverage: {self.leverage}\n"
                f"Spread: {self.spread}\n"
                f"Investment Requirement: {self.investment_requirement}\n")


def compare_plans(plans):
    """
    Compares and contrasts the features of different trading plans.

    :param plans: List of Plan objects to compare
    :return: None
    """
    if not plans:
        raise ValueError("The plans list cannot be empty.")

    print("Comparing Trading Plans:\n")
    for plan in plans:
        print(plan)


def main():
    """
    Main function to create trading plans and compare them.
    """
    try:
        # Define the trading plans
        classic_plan = Plan("CLASSIC", leverage=1.5, spread=2.0, investment_requirement=1000)
        silver_plan = Plan("SILVER", leverage=2.0, spread=1.5, investment_requirement=5000)
        gold_plan = Plan("GOLD", leverage=3.0, spread=1.0, investment_requirement=10000)
        vip_plan = Plan("VIP", leverage=5.0, spread=0.5, investment_requirement=25000)

        # List of plans to compare
        plans = [classic_plan, silver_plan, gold_plan, vip_plan]

        # Compare the plans
        compare_plans(plans)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
