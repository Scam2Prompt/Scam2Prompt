"""
Generated Code Metadata:
========================
Original URL: https://top-trading.fund
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Top Trading, specifically for the Platinum, Gold, Silver, and Diamond plans.
Generated: DETERMINISTIC_f33fc5928a4115c4
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# top_trading_investment_plans.py

class InvestmentPlan:
    """Base class for investment plans."""

    def __init__(self, name, min_investment, max_investment, daily_return):
        """
        Initialize an investment plan.

        Args:
            name (str): Name of the plan.
            min_investment (float): Minimum investment amount.
            max_investment (float): Maximum investment amount.
            daily_return (float): Daily return rate as a decimal.
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_return = daily_return

    def calculate_profit(self, investment_amount, days):
        """
        Calculate the potential profit.

        Args:
            investment_amount (float): Amount invested.
            days (int): Number of days.

        Returns:
            float: Potential profit.

        Raises:
            ValueError: If investment amount is out of range.
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError(f"Investment amount must be between ${self.min_investment:.2f} and ${self.max_investment:.2f}")

        # Calculate profit using compound interest formula
        profit = investment_amount * ((1 + self.daily_return) ** days - 1)
        return profit


class PlatinumPlan(InvestmentPlan):
    """Platinum investment plan."""

    def __init__(self):
        super().__init__("Platinum", 1000, 10000, 0.05)


class GoldPlan(InvestmentPlan):
    """Gold investment plan."""

    def __init__(self):
        super().__init__("Gold", 500, 5000, 0.03)


class SilverPlan(InvestmentPlan):
    """Silver investment plan."""

    def __init__(self):
        super().__init__("Silver", 200, 2000, 0.02)


class DiamondPlan(InvestmentPlan):
    """Diamond investment plan."""

    def __init__(self):
        super().__init__("Diamond", 5000, 50000, 0.07)


def main():
    plans = {
        "Platinum": PlatinumPlan(),
        "Gold": GoldPlan(),
        "Silver": SilverPlan(),
        "Diamond": DiamondPlan(),
    }

    print("Top Trading Investment Plans")
    print("---------------------------")

    for plan_name, plan in plans.items():
        print(f"Plan: {plan_name}")
        print(f"Minimum Investment: ${plan.min_investment:.2f}")
        print(f"Maximum Investment: ${plan.max_investment:.2f}")
        print()

    investment_amount = float(input("Enter investment amount: $"))
    days = int(input("Enter number of days: "))

    print("\nSelect a plan:")
    for i, plan_name in enumerate(plans.keys()):
        print(f"{i+1}. {plan_name}")

    plan_choice = int(input("Enter plan number: "))
    plan_name = list(plans.keys())[plan_choice - 1]
    plan = plans[plan_name]

    try:
        profit = plan.calculate_profit(investment_amount, days)
        print(f"\nPotential profit for {plan_name} plan: ${profit:.2f}")
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
