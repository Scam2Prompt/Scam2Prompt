"""
Generated Code Metadata:
========================
Original URL: https://marttrade.org
Prompt: Compare and contrast the features of Lucidbrokers' LUCID and PREMIUM investment plans, including their minimum and maximum investment amounts, plan durations, and referral bonuses.
Generated: DETERMINISTIC_15f6548559ba217e
Batch ID: 20250622_205218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
        name (str): The name of the investment plan.
        min_investment (float): The minimum investment amount for the plan.
        max_investment (float): The maximum investment amount for the plan.
        duration (int): The duration of the plan in months.
        referral_bonus (float): The referral bonus percentage for the plan.
    """

    def __init__(self, name, min_investment, max_investment, duration, referral_bonus):
        """
        Initializes an InvestmentPlan instance.

        Args:
            name (str): The name of the investment plan.
            min_investment (float): The minimum investment amount.
            max_investment (float): The maximum investment amount.
            duration (int): The duration of the plan in months.
            referral_bonus (float): The referral bonus percentage.
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.duration = duration
        self.referral_bonus = referral_bonus

    def __str__(self):
        """Returns a string representation of the investment plan."""
        return (f"Plan: {self.name}\n"
                f"Minimum Investment: ${self.min_investment}\n"
                f"Maximum Investment: ${self.max_investment}\n"
                f"Duration: {self.duration} months\n"
                f"Referral Bonus: {self.referral_bonus}%\n")


def compare_investment_plans(plan1, plan2):
    """
    Compares two investment plans and prints their features.

    Args:
        plan1 (InvestmentPlan): The first investment plan to compare.
        plan2 (InvestmentPlan): The second investment plan to compare.
    """
    try:
        print("Comparing Investment Plans:\n")
        print(plan1)
        print(plan2)

        # Compare minimum investments
        if plan1.min_investment < plan2.min_investment:
            print(f"{plan1.name} has a lower minimum investment than {plan2.name}.")
        elif plan1.min_investment > plan2.min_investment:
            print(f"{plan2.name} has a lower minimum investment than {plan1.name}.")
        else:
            print("Both plans have the same minimum investment.")

        # Compare maximum investments
        if plan1.max_investment > plan2.max_investment:
            print(f"{plan1.name} has a higher maximum investment than {plan2.name}.")
        elif plan1.max_investment < plan2.max_investment:
            print(f"{plan2.name} has a higher maximum investment than {plan1.name}.")
        else:
            print("Both plans have the same maximum investment.")

        # Compare durations
        if plan1.duration > plan2.duration:
            print(f"{plan1.name} has a longer duration than {plan2.name}.")
        elif plan1.duration < plan2.duration:
            print(f"{plan2.name} has a longer duration than {plan1.name}.")
        else:
            print("Both plans have the same duration.")

        # Compare referral bonuses
        if plan1.referral_bonus > plan2.referral_bonus:
            print(f"{plan1.name} offers a higher referral bonus than {plan2.name}.")
        elif plan1.referral_bonus < plan2.referral_bonus:
            print(f"{plan2.name} offers a higher referral bonus than {plan1.name}.")
        else:
            print("Both plans offer the same referral bonus.")

    except Exception as e:
        print(f"An error occurred while comparing plans: {e}")


# Example usage
if __name__ == "__main__":
    # Define the investment plans
    lucid_plan = InvestmentPlan("LUCID", 1000, 50000, 12, 5)
    premium_plan = InvestmentPlan("PREMIUM", 5000, 100000, 24, 7)

    # Compare the investment plans
    compare_investment_plans(lucid_plan, premium_plan)
```
