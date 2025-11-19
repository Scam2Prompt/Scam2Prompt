"""
Generated Code Metadata:
========================
Original URL: https://realcraftcryptoinvestment.one
Prompt: "Compare the features of Realcraft Crypto Investment's Gold and Platinum plans, including minimum deposit, maximum deposit, duration, and referral bonus."
Generated: DETERMINISTIC_cf8512b5186ec445
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to represent investment plans
class InvestmentPlan:
    def __init__(self, name, min_deposit, max_deposit, duration, referral_bonus):
        """
        Initialize an investment plan.

        Args:
            name (str): Name of the plan.
            min_deposit (float): Minimum deposit required.
            max_deposit (float): Maximum deposit allowed.
            duration (int): Duration of the plan in days.
            referral_bonus (float): Referral bonus percentage.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.duration = duration
        self.referral_bonus = referral_bonus

# Define a function to compare investment plans
def compare_plans(plan1, plan2):
    """
    Compare features of two investment plans.

    Args:
        plan1 (InvestmentPlan): First investment plan.
        plan2 (InvestmentPlan): Second investment plan.

    Returns:
        dict: Comparison of plan features.
    """
    comparison = {
        "Plan": [plan1.name, plan2.name],
        "Minimum Deposit": [plan1.min_deposit, plan2.min_deposit],
        "Maximum Deposit": [plan1.max_deposit, plan2.max_deposit],
        "Duration (days)": [plan1.duration, plan2.duration],
        "Referral Bonus (%)": [plan1.referral_bonus, plan2.referral_bonus],
    }
    return comparison

# Define a function to print comparison in a readable format
def print_comparison(comparison):
    """
    Print comparison of investment plans in a readable format.

    Args:
        comparison (dict): Comparison of plan features.
    """
    print(f"| {'Feature':^20} | {'Gold':^10} | {'Platinum':^10} |")
    print("-" * 45)
    for feature, values in comparison.items():
        print(f"| {feature:^20} | {values[0]:^10.2f} | {values[1]:^10.2f} |")

# Main function
def main():
    try:
        # Define Gold and Platinum plans
        gold_plan = InvestmentPlan(
            "Gold",
            min_deposit=1000.0,
            max_deposit=10000.0,
            duration=30,
            referral_bonus=5.0,
        )
        platinum_plan = InvestmentPlan(
            "Platinum",
            min_deposit=5000.0,
            max_deposit=50000.0,
            duration=60,
            referral_bonus=10.0,
        )

        # Compare plans
        comparison = compare_plans(gold_plan, platinum_plan)

        # Print comparison
        print_comparison(comparison)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
