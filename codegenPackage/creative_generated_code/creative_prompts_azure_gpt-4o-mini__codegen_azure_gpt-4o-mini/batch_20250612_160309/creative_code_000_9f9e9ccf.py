"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longtradegroup.com
Prompt: Generate code to calculate daily profits for a cryptocurrency staking plan with a 0.2% daily return over 100 days, using an investment range of $25 to $250.
Generated: DETERMINISTIC_9f9e9ccf8b184664
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingPlan:
    """
    A class to represent a cryptocurrency staking plan.

    Attributes
    ----------
    daily_return_rate : float
        The daily return rate as a decimal (0.2% = 0.002).
    investment_range : tuple
        A tuple containing the minimum and maximum investment amounts.
    duration_days : int
        The duration for the staking plan in days.
    """

    def __init__(self, daily_return_rate=0.002, investment_range=(25, 250), duration_days=100):
        """
        Initializes the StakingPlan with default values for daily return rate, investment range, and duration.

        Parameters
        ----------
        daily_return_rate : float, optional
            The daily return rate as a decimal (default is 0.002).
        investment_range : tuple, optional
            A tuple containing (min_investment, max_investment) (default is (25, 250)).
        duration_days : int, optional
            The duration for the staking plan in days (default is 100).
        """
        self.daily_return_rate = daily_return_rate
        self.investment_range = investment_range
        self.duration_days = duration_days

    def calculate_daily_profits(self, investment_amount):
        """
        Calculate daily profits based on the investment amount.

        Parameters
        ----------
        investment_amount : float
            The amount of money invested in the staking plan.

        Returns
        -------
        float
            The calculated daily profit.

        Raises
        ------
        ValueError
            If investment_amount is outside the predefined range.
        """
        if not (self.investment_range[0] <= investment_amount <= self.investment_range[1]):
            raise ValueError(f"Investment amount must be between {self.investment_range[0]} and {self.investment_range[1]}.")

        daily_profit = investment_amount * self.daily_return_rate
        return daily_profit

    def calculate_total_profits(self, investment_amount):
        """
        Calculate total profits over the staking duration.

        Parameters
        ----------
        investment_amount : float
            The amount of money invested in the staking plan.

        Returns
        -------
        float
            The total profits after the staking duration.

        Raises
        ------
        ValueError
            If investment_amount is outside the predefined range.
        """
        daily_profit = self.calculate_daily_profits(investment_amount)
        total_profit = daily_profit * self.duration_days
        return total_profit

# Example usage:
if __name__ == "__main__":
    try:
        staking_plan = StakingPlan()
        investment = 100  # Example investment amount
        daily_profit = staking_plan.calculate_daily_profits(investment)
        total_profit = staking_plan.calculate_total_profits(investment)

        print(f"Daily Profit for ${investment}: ${daily_profit:.2f}")
        print(f"Total Profit over {staking_plan.duration_days} days: ${total_profit:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
