"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safewealthhaven.com.bartercorebase.com
Prompt: Generate code to create a profit calculator for investment plans, including features like daily return percentages and total capital, as described on Safe Wealth Haven.
Generated: DETERMINISTIC_3fd38ed55edb76eb
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    A class to represent an investment plan with daily return percentages
    and total capital. The class provides methods to calculate profit
    over a specified number of days.
    """

    def __init__(self, total_capital: float, daily_return_percentage: float):
        """
        Initializes the investment plan with total capital and daily return percentage.

        :param total_capital: Total amount invested.
        :param daily_return_percentage: Daily return percentage on the investment.
        """
        if total_capital <= 0:
            raise ValueError("Total capital must be greater than zero.")
        if daily_return_percentage < 0:
            raise ValueError("Daily return percentage cannot be negative.")
        
        self.total_capital = total_capital
        self.daily_return_percentage = daily_return_percentage

    def calculate_daily_return(self) -> float:
        """
        Calculates the daily return based on the total capital and
        daily return percentage.

        :return: Daily return amount.
        """
        return (self.daily_return_percentage / 100) * self.total_capital

    def calculate_total_profit(self, days: int) -> float:
        """
        Calculates the total profit over a specified number of days.

        :param days: Number of days to calculate profit for.
        :return: Total profit amount over the specified number of days.
        """
        if days < 0:
            raise ValueError("Number of days cannot be negative.")
        
        daily_return = self.calculate_daily_return()
        return daily_return * days

    def display_profit(self, days: int) -> None:
        """
        Displays the profit for the given number of days.

        :param days: Number of days to calculate profit for.
        """
        try:
            total_profit = self.calculate_total_profit(days)
            print(f"Total profit after {days} days: ${total_profit:.2f}")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create an investment plan instance
        investment = InvestmentPlan(total_capital=1000.0, daily_return_percentage=5.0)
        
        # Display profit for a specified number of days
        investment.display_profit(days=30)
    except ValueError as e:
        print(f"Initialization Error: {e}")
```
