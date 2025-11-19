"""
Generated Code Metadata:
========================
Original URL: https://microapexmarket.com
Prompt: Create a program to calculate potential profits based on trading plans (e.g., Basic, Silver, Gold, Platinum) offered by Microapexmarket.
Generated: DETERMINISTIC_6da240348d0b9353
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingPlan:
    """
    A class to represent a trading plan and calculate potential profits.
    """

    def __init__(self, name, investment, profit_percentage):
        """
        Initializes a TradingPlan instance.

        :param name: str - The name of the trading plan.
        :param investment: float - The amount of money invested in the plan.
        :param profit_percentage: float - The expected profit percentage from the investment.
        """
        self.name = name
        self.investment = investment
        self.profit_percentage = profit_percentage

    def calculate_profit(self):
        """
        Calculates the potential profit based on the investment and profit percentage.

        :return: float - The calculated profit.
        """
        if self.investment < 0:
            raise ValueError("Investment must be a non-negative value.")
        if not (0 <= self.profit_percentage <= 100):
            raise ValueError("Profit percentage must be between 0 and 100.")

        profit = (self.investment * self.profit_percentage) / 100
        return profit


def main():
    """
    Main function to execute the trading plan profit calculations.
    """
    # Define trading plans with their respective investment and profit percentages
    plans = [
        TradingPlan("Basic", 1000, 5),      # 5% profit
        TradingPlan("Silver", 5000, 10),    # 10% profit
        TradingPlan("Gold", 10000, 15),     # 15% profit
        TradingPlan("Platinum", 20000, 20)   # 20% profit
    ]

    # Calculate and display potential profits for each trading plan
    for plan in plans:
        try:
            profit = plan.calculate_profit()
            print(f"Trading Plan: {plan.name}, Investment: ${plan.investment}, "
                  f"Profit Percentage: {plan.profit_percentage}%, "
                  f"Potential Profit: ${profit:.2f}")
        except ValueError as e:
            print(f"Error calculating profit for {plan.name}: {e}")


if __name__ == "__main__":
    main()
```
