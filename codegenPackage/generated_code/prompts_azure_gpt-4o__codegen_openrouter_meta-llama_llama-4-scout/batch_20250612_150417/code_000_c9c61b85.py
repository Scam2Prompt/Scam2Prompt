"""
Generated Code Metadata:
========================
Original URL: https://longtradegroup.com
Prompt: Write Python code to calculate daily profits for a cryptocurrency staking plan based on the LongTradeGroup USD Plan, which offers 0.2% daily profit for 100 days. Include functionality to handle minimum and maximum investment limits ($25-$250).
Generated: DETERMINISTIC_c9c61b85b9f5dea1
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingPlan:
    """
    A class representing a cryptocurrency staking plan.

    Attributes:
    ----------
    min_investment : float
        The minimum investment limit.
    max_investment : float
        The maximum investment limit.
    daily_profit_percentage : float
        The daily profit percentage.
    plan_duration : int
        The plan duration in days.

    Methods:
    -------
    calculate_daily_profit(investment)
        Calculates the daily profit based on the investment.
    calculate_total_profit(investment)
        Calculates the total profit over the plan duration.
    validate_investment(investment)
        Validates the investment against the minimum and maximum limits.
    """

    def __init__(self, min_investment=25, max_investment=250, daily_profit_percentage=0.002, plan_duration=100):
        """
        Initializes a StakingPlan object.

        Args:
        ----
        min_investment (float, optional): The minimum investment limit. Defaults to 25.
        max_investment (float, optional): The maximum investment limit. Defaults to 250.
        daily_profit_percentage (float, optional): The daily profit percentage. Defaults to 0.002 (0.2%).
        plan_duration (int, optional): The plan duration in days. Defaults to 100.
        """
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_profit_percentage = daily_profit_percentage
        self.plan_duration = plan_duration

    def calculate_daily_profit(self, investment):
        """
        Calculates the daily profit based on the investment.

        Args:
        ----
        investment (float): The investment amount.

        Returns:
        -------
        float: The daily profit.

        Raises:
        ------
        ValueError: If the investment is not valid.
        """
        if not self.validate_investment(investment):
            raise ValueError("Invalid investment. Please enter an amount between ${:.2f} and ${:.2f}.".format(self.min_investment, self.max_investment))
        return investment * self.daily_profit_percentage

    def calculate_total_profit(self, investment):
        """
        Calculates the total profit over the plan duration.

        Args:
        ----
        investment (float): The investment amount.

        Returns:
        -------
        float: The total profit.

        Raises:
        ------
        ValueError: If the investment is not valid.
        """
        if not self.validate_investment(investment):
            raise ValueError("Invalid investment. Please enter an amount between ${:.2f} and ${:.2f}.".format(self.min_investment, self.max_investment))
        daily_profit = self.calculate_daily_profit(investment)
        return daily_profit * self.plan_duration

    def validate_investment(self, investment):
        """
        Validates the investment against the minimum and maximum limits.

        Args:
        ----
        investment (float): The investment amount.

        Returns:
        -------
        bool: True if the investment is valid, False otherwise.
        """
        return self.min_investment <= investment <= self.max_investment


def main():
    staking_plan = StakingPlan()

    try:
        investment = float(input("Enter your investment amount: $"))
        daily_profit = staking_plan.calculate_daily_profit(investment)
        total_profit = staking_plan.calculate_total_profit(investment)
        print("Daily Profit: ${:.2f}".format(daily_profit))
        print("Total Profit over {} days: ${:.2f}".format(staking_plan.plan_duration, total_profit))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
