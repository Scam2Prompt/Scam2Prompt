"""
Generated Code Metadata:
========================
Original URL: https://marketsfargo.com
Prompt: Create a Python script to calculate spreads for different trading plans (Classic, Silver, Gold, VIP) based on leverage ratios and investment amounts as described on Fargo Markets.
Generated: DETERMINISTIC_87cd0f70165b8d96
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trading_plans.py

class TradingPlan:
    def __init__(self, name, leverage_ratio):
        """
        Initialize a TradingPlan object.

        Args:
            name (str): The name of the trading plan.
            leverage_ratio (float): The leverage ratio of the trading plan.
        """
        self.name = name
        self.leverage_ratio = leverage_ratio

    def calculate_spread(self, investment_amount):
        """
        Calculate the spread for the trading plan based on the investment amount.

        Args:
            investment_amount (float): The investment amount.

        Returns:
            float: The calculated spread.
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")

        # Assuming spread is calculated as a percentage of the investment amount
        # For simplicity, let's assume the spread percentage is 0.1% for now
        spread_percentage = 0.001

        spread = investment_amount * spread_percentage / self.leverage_ratio
        return spread


class FargoMarkets:
    def __init__(self):
        """
        Initialize a FargoMarkets object with predefined trading plans.
        """
        self.trading_plans = {
            "Classic": TradingPlan("Classic", 1.0),
            "Silver": TradingPlan("Silver", 2.0),
            "Gold": TradingPlan("Gold", 5.0),
            "VIP": TradingPlan("VIP", 10.0),
        }

    def get_trading_plan(self, plan_name):
        """
        Get a trading plan by name.

        Args:
            plan_name (str): The name of the trading plan.

        Returns:
            TradingPlan: The TradingPlan object if found, otherwise None.
        """
        return self.trading_plans.get(plan_name)

    def calculate_spread(self, plan_name, investment_amount):
        """
        Calculate the spread for a trading plan based on the investment amount.

        Args:
            plan_name (str): The name of the trading plan.
            investment_amount (float): The investment amount.

        Returns:
            float: The calculated spread.

        Raises:
            ValueError: If the plan name is not found or investment amount is invalid.
        """
        plan = self.get_trading_plan(plan_name)
        if plan is None:
            raise ValueError("Invalid trading plan name.")

        return plan.calculate_spread(investment_amount)


def main():
    fargo_markets = FargoMarkets()

    # Example usage:
    plan_name = "Gold"
    investment_amount = 10000.0

    try:
        spread = fargo_markets.calculate_spread(plan_name, investment_amount)
        print(f"The spread for {plan_name} plan with investment amount ${investment_amount:.2f} is ${spread:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
