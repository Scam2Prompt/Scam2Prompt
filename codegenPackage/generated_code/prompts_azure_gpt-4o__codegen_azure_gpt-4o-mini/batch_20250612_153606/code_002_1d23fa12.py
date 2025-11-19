"""
Generated Code Metadata:
========================
Original URL: https://capinvest.ltd
Prompt: Generate code to calculate the daily profit for CAPINVEST LTD's investment plans, including the bonus percentages for 14, 30, 60, and 90-day periods.
Generated: DETERMINISTIC_1d23fa12ea759093
Batch ID: 20250612_153606
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
    A class to represent an investment plan for CAPINVEST LTD.

    Attributes:
        principal (float): The initial amount of money invested.
        daily_rate (float): The daily profit rate as a percentage.
        bonus_percentages (dict): A dictionary containing bonus percentages for different periods.
    """

    def __init__(self, principal: float, daily_rate: float):
        """
        Initializes the InvestmentPlan with a principal amount and daily rate.

        Args:
            principal (float): The initial investment amount.
            daily_rate (float): The daily profit rate as a percentage.

        Raises:
            ValueError: If principal or daily_rate is negative.
        """
        if principal < 0:
            raise ValueError("Principal amount cannot be negative.")
        if daily_rate < 0:
            raise ValueError("Daily rate cannot be negative.")

        self.principal = principal
        self.daily_rate = daily_rate
        self.bonus_percentages = {
            14: 0.05,  # 5% bonus for 14 days
            30: 0.10,  # 10% bonus for 30 days
            60: 0.15,  # 15% bonus for 60 days
            90: 0.20   # 20% bonus for 90 days
        }

    def calculate_daily_profit(self) -> float:
        """
        Calculates the daily profit based on the principal and daily rate.

        Returns:
            float: The daily profit amount.
        """
        return self.principal * (self.daily_rate / 100)

    def calculate_total_profit(self, days: int) -> float:
        """
        Calculates the total profit for a given number of days, including any applicable bonuses.

        Args:
            days (int): The number of days the investment is held.

        Returns:
            float: The total profit amount including bonuses.

        Raises:
            ValueError: If days is not a positive integer.
        """
        if days <= 0:
            raise ValueError("Days must be a positive integer.")

        daily_profit = self.calculate_daily_profit()
        total_profit = daily_profit * days

        # Check for applicable bonus
        bonus = self.bonus_percentages.get(days, 0)
        total_profit += total_profit * bonus

        return total_profit

# Example usage
if __name__ == "__main__":
    try:
        # Create an investment plan with a principal of 1000 and a daily rate of 1%
        investment = InvestmentPlan(principal=1000, daily_rate=1)

        # Calculate total profit for 30 days
        profit_30_days = investment.calculate_total_profit(days=30)
        print(f"Total profit for 30 days: ${profit_30_days:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
