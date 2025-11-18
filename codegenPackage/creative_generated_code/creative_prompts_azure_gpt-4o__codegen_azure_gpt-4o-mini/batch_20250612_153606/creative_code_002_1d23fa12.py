"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capinvest.ltd
Prompt: Generate code to calculate the daily profit for CAPINVEST LTD's investment plans, including the bonus percentages for 14, 30, 60, and 90-day periods.
Generated: DETERMINISTIC_1d23fa12ea759093
Batch ID: 20250612_153606
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
    A class to represent an investment plan for CAPINVEST LTD.

    Attributes:
        principal (float): The initial amount of money invested.
        daily_rate (float): The daily interest rate, as a percentage.
        bonuses (dict): Bonus percentages for different periods (in days).
    """

    def __init__(self, principal: float, daily_rate: float):
        """
        Initializes the InvestmentPlan with a principal and daily rate.

        Args:
            principal (float): The initial investment amount.
            daily_rate (float): The daily interest rate (as a percentage).

        Raises:
            ValueError: If principal or daily_rate is negative.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if daily_rate < 0:
            raise ValueError("Daily rate must be non-negative.")

        self.principal = principal
        self.daily_rate = daily_rate
        self.bonuses = {
            14: 0.02,   # 2% bonus for 14 days
            30: 0.05,   # 5% bonus for 30 days
            60: 0.10,   # 10% bonus for 60 days
            90: 0.15    # 15% bonus for 90 days
        }

    def calculate_daily_profit(self, days: int) -> float:
        """
        Calculates the daily profit based on the investment duration and applicable bonuses.

        Args:
            days (int): The number of days the investment is held.

        Returns:
            float: The total profit after the specified duration.

        Raises:
            ValueError: If days is not a positive integer.
        """
        if days <= 0:
            raise ValueError("Days must be a positive integer.")

        # Calculate daily profit without bonuses
        daily_profit = (self.principal * (self.daily_rate / 100))

        # Calculate total profit for the given days
        total_profit = daily_profit * days

        # Check and apply bonuses based on the investment period
        bonus_percentage = self.bonuses.get(days, 0)
        total_profit += total_profit * bonus_percentage

        return total_profit

# Example Usage:
if __name__ == "__main__":
    try:
        # Create an investment plan with a principal of 1000 and a daily rate of 1%
        plan = InvestmentPlan(principal=1000, daily_rate=1)

        # Calculate daily profit for various periods
        for period in [14, 30, 60, 90]:
            profit = plan.calculate_daily_profit(period)
            print(f"Total profit for {period} days: ${profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
