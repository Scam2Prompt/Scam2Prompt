"""
Generated Code Metadata:
========================
Original URL: https://echotradeoptions.com
Prompt: Write a code snippet that calculates trading earnings based on Echo Trade's profit calculator, taking into account the user's chosen trading plan and investment amount.
Generated: DETERMINISTIC_fbd6ef7947aebaf6
Batch ID: 20250622_210054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trading_earnings_calculator.py

class TradingPlan:
    """Represents a trading plan with its associated profit percentage."""

    def __init__(self, name, profit_percentage):
        """
        Initializes a TradingPlan object.

        Args:
            name (str): The name of the trading plan.
            profit_percentage (float): The profit percentage of the trading plan.
        """
        self.name = name
        self.profit_percentage = profit_percentage


class TradingEarningsCalculator:
    """Calculates trading earnings based on a chosen trading plan and investment amount."""

    def __init__(self):
        """Initializes a TradingEarningsCalculator object."""
        self.trading_plans = {
            "conservative": TradingPlan("Conservative", 0.05),
            "moderate": TradingPlan("Moderate", 0.10),
            "aggressive": TradingPlan("Aggressive", 0.20),
        }

    def calculate_earnings(self, trading_plan_name, investment_amount):
        """
        Calculates trading earnings based on the chosen trading plan and investment amount.

        Args:
            trading_plan_name (str): The name of the chosen trading plan.
            investment_amount (float): The investment amount.

        Returns:
            float: The calculated trading earnings.

        Raises:
            ValueError: If the trading plan name is not valid.
            TypeError: If the investment amount is not a positive number.
        """
        if trading_plan_name not in self.trading_plans:
            raise ValueError("Invalid trading plan name")

        if not isinstance(investment_amount, (int, float)) or investment_amount <= 0:
            raise TypeError("Investment amount must be a positive number")

        trading_plan = self.trading_plans[trading_plan_name]
        earnings = investment_amount * trading_plan.profit_percentage
        return earnings

    def get_trading_plans(self):
        """
        Returns a dictionary of available trading plans.

        Returns:
            dict: A dictionary of trading plans with their names as keys and profit percentages as values.
        """
        return {plan.name: plan.profit_percentage for plan in self.trading_plans.values()}


def main():
    calculator = TradingEarningsCalculator()
    print("Available Trading Plans:")
    for plan, profit_percentage in calculator.get_trading_plans().items():
        print(f"{plan}: {profit_percentage * 100}%")

    trading_plan_name = input("Enter the trading plan name (conservative, moderate, aggressive): ")
    try:
        investment_amount = float(input("Enter the investment amount: "))
        earnings = calculator.calculate_earnings(trading_plan_name, investment_amount)
        print(f"Trading Earnings: ${earnings:.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
