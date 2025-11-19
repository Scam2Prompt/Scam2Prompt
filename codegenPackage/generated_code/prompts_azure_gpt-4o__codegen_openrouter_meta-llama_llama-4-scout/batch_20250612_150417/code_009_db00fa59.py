"""
Generated Code Metadata:
========================
Original URL: https://sabkafuture.com
Prompt: Write a program to calculate the profit margin for Sabka Future's "STAIRSTEP BREAKWAT PLAN" based on the investment amount and daily returns.
Generated: DETERMINISTIC_db00fa5953d3e476
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# stairstep_breakwat_plan_profit_margin_calculator.py

class StairstepBreakwatPlan:
    """
    Calculates the profit margin for Sabka Future's "STAIRSTEP BREAKWAT PLAN"
    based on the investment amount and daily returns.
    """

    def __init__(self, investment_amount, daily_returns, days):
        """
        Initializes the StairstepBreakwatPlan calculator.

        Args:
            investment_amount (float): The initial investment amount.
            daily_returns (list[float]): A list of daily returns as decimals.
            days (int): The number of days for the investment.

        Raises:
            ValueError: If investment_amount is not positive.
            ValueError: If daily_returns is empty or contains non-decimal values.
            ValueError: If days is not a positive integer.
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be positive.")

        if not daily_returns:
            raise ValueError("Daily returns must not be empty.")

        if not all(isinstance(x, (int, float)) and 0 <= x <= 1 for x in daily_returns):
            raise ValueError("Daily returns must be decimals between 0 and 1.")

        if not isinstance(days, int) or days <= 0:
            raise ValueError("Days must be a positive integer.")

        self.investment_amount = investment_amount
        self.daily_returns = daily_returns
        self.days = days

    def calculate_total_return(self):
        """
        Calculates the total return on investment.

        Returns:
            float: The total return on investment.
        """
        total_return = self.investment_amount
        for i in range(self.days):
            total_return *= (1 + self.daily_returns[i % len(self.daily_returns)])
        return total_return

    def calculate_profit_margin(self):
        """
        Calculates the profit margin.

        Returns:
            float: The profit margin as a decimal.
        """
        total_return = self.calculate_total_return()
        profit_margin = (total_return - self.investment_amount) / self.investment_amount
        return profit_margin

    def calculate_percentage_profit_margin(self):
        """
        Calculates the percentage profit margin.

        Returns:
            float: The percentage profit margin.
        """
        profit_margin = self.calculate_profit_margin()
        return profit_margin * 100


def main():
    try:
        investment_amount = float(input("Enter the investment amount: "))
        daily_returns = [float(x) for x in input("Enter daily returns (space-separated): ").split()]
        days = int(input("Enter the number of days: "))

        calculator = StairstepBreakwatPlan(investment_amount, daily_returns, days)
        profit_margin = calculator.calculate_percentage_profit_margin()

        print(f"The percentage profit margin is: {profit_margin:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
