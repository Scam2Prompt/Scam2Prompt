"""
Generated Code Metadata:
========================
Original URL: https://metamaskcoins.com
Prompt: Write Python code to calculate the expected profit for a cryptocurrency investment based on Meta Mask Coins' trading plans (e.g., Silver, Gold, Diamond) using the given trade duration and profit percentages.
Generated: DETERMINISTIC_3a1d4f32c9f45427
Batch ID: 20250612_150327
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
    A class to represent an investment plan for cryptocurrency trading.

    Attributes:
        name (str): The name of the investment plan.
        profit_percentage (float): The expected profit percentage for the plan.
    """

    def __init__(self, name: str, profit_percentage: float):
        """
        Initializes the InvestmentPlan with a name and profit percentage.

        Args:
            name (str): The name of the investment plan.
            profit_percentage (float): The expected profit percentage for the plan.
        """
        self.name = name
        self.profit_percentage = profit_percentage

    def calculate_profit(self, investment_amount: float, duration: int) -> float:
        """
        Calculates the expected profit based on the investment amount and duration.

        Args:
            investment_amount (float): The amount of money invested.
            duration (int): The duration of the investment in days.

        Returns:
            float: The expected profit from the investment.

        Raises:
            ValueError: If investment_amount or duration is negative.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount must be non-negative.")
        if duration < 0:
            raise ValueError("Duration must be non-negative.")

        # Calculate profit based on the profit percentage and investment amount
        profit = (self.profit_percentage / 100) * investment_amount * duration
        return profit


def main():
    """
    Main function to demonstrate the calculation of expected profit for different investment plans.
    """
    # Define investment plans with their respective profit percentages
    plans = [
        InvestmentPlan("Silver", 5.0),   # 5% profit per day
        InvestmentPlan("Gold", 10.0),     # 10% profit per day
        InvestmentPlan("Diamond", 15.0)    # 15% profit per day
    ]

    # Example investment amount and duration
    investment_amount = 1000.0  # Amount in currency
    duration = 30                # Duration in days

    # Calculate and display expected profits for each plan
    for plan in plans:
        try:
            expected_profit = plan.calculate_profit(investment_amount, duration)
            print(f"Expected profit for {plan.name} plan: ${expected_profit:.2f}")
        except ValueError as e:
            print(f"Error calculating profit for {plan.name} plan: {e}")


if __name__ == "__main__":
    main()
```
