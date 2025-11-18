"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabkafuture.com
Prompt: Write a program to calculate the profit margin for Sabka Future's "STAIRSTEP BREAKWAT PLAN" based on the investment amount and daily returns.
Generated: DETERMINISTIC_db00fa5953d3e476
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ProfitMarginCalculator:
    """
    A class to calculate the profit margin for Sabka Future's
    "STAIRSTEP BREAKWAT PLAN" based on the investment amount
    and daily returns.
    """

    def __init__(self, investment_amount: float, daily_returns: float):
        """
        Initializes the ProfitMarginCalculator with an investment amount and daily returns.

        :param investment_amount: The total investment amount (must be a positive number).
        :param daily_returns: The daily returns as a percentage of the investment amount (must be between 0 and 100).
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if not (0 <= daily_returns <= 100):
            raise ValueError("Daily returns must be a percentage between 0 and 100.")

        self.investment_amount = investment_amount
        self.daily_returns = daily_returns / 100  # Convert percentage to decimal

    def calculate_daily_profit(self) -> float:
        """
        Calculates the daily profit based on the investment amount and daily returns.

        :return: Daily profit as a float.
        """
        daily_profit = self.investment_amount * self.daily_returns
        return daily_profit

    def calculate_profit_margin(self) -> float:
        """
        Calculates the profit margin.

        :return: Profit margin as a percentage.
        """
        daily_profit = self.calculate_daily_profit()
        profit_margin = (daily_profit / self.investment_amount) * 100
        return profit_margin

    def display_profit_details(self):
        """
        Displays the investment details and calculated profit margin.
        """
        try:
            daily_profit = self.calculate_daily_profit()
            profit_margin = self.calculate_profit_margin()
            print(f"Investment Amount: ${self.investment_amount:,.2f}")
            print(f"Daily Returns Rate: {self.daily_returns * 100:.2f}%")
            print(f"Daily Profit: ${daily_profit:,.2f}")
            print(f"Profit Margin: {profit_margin:.2f}%")
        except Exception as e:
            print(f"An error occurred while calculating profit details: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        investment = float(input("Enter the investment amount: "))
        returns = float(input("Enter the daily returns percentage: "))
        
        calculator = ProfitMarginCalculator(investment, returns)
        calculator.display_profit_details()
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
