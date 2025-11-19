"""
Generated Code Metadata:
========================
Original URL: https://tenlajk.top
Prompt: Create a MinerDog investment plan for a user with a minimum deposit of 100 USDT, assuming a 6.80% daily profit rate and a 150% total profit guarantee.
Generated: DETERMINISTIC_20899994c855bf2a
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MinerDogInvestmentPlan:
    """
    A class representing a MinerDog investment plan.

    Attributes:
    ----------
    min_deposit : float
        The minimum deposit required for the investment plan.
    daily_profit_rate : float
        The daily profit rate of the investment plan.
    total_profit_guarantee : float
        The total profit guarantee of the investment plan.

    Methods:
    -------
    calculate_daily_profit(investment_amount)
        Calculates the daily profit based on the investment amount.
    calculate_total_profit(investment_amount)
        Calculates the total profit based on the investment amount.
    validate_investment_amount(investment_amount)
        Validates if the investment amount meets the minimum deposit requirement.
    """

    def __init__(self, min_deposit=100, daily_profit_rate=0.068, total_profit_guarantee=1.5):
        """
        Initializes a MinerDogInvestmentPlan object.

        Args:
        ----
        min_deposit (float, optional): The minimum deposit required. Defaults to 100.
        daily_profit_rate (float, optional): The daily profit rate. Defaults to 0.068.
        total_profit_guarantee (float, optional): The total profit guarantee. Defaults to 1.5.
        """
        self.min_deposit = min_deposit
        self.daily_profit_rate = daily_profit_rate
        self.total_profit_guarantee = total_profit_guarantee

    def calculate_daily_profit(self, investment_amount):
        """
        Calculates the daily profit based on the investment amount.

        Args:
        ----
        investment_amount (float): The amount invested.

        Returns:
        -------
        float
            The daily profit.
        """
        return investment_amount * self.daily_profit_rate

    def calculate_total_profit(self, investment_amount):
        """
        Calculates the total profit based on the investment amount.

        Args:
        ----
        investment_amount (float): The amount invested.

        Returns:
        -------
        float
            The total profit.
        """
        return investment_amount * self.total_profit_guarantee

    def validate_investment_amount(self, investment_amount):
        """
        Validates if the investment amount meets the minimum deposit requirement.

        Args:
        ----
        investment_amount (float): The amount invested.

        Raises:
        ------
        ValueError
            If the investment amount is less than the minimum deposit.

        Returns:
        -------
        bool
            True if the investment amount is valid, False otherwise.
        """
        if investment_amount < self.min_deposit:
            raise ValueError(f"Minimum deposit of {self.min_deposit} USDT is required.")
        return True


def create_investment_plan(investment_amount):
    """
    Creates a MinerDog investment plan for a user.

    Args:
    ----
    investment_amount (float): The amount invested.

    Returns:
    -------
    dict
        A dictionary containing the investment plan details.
    """
    try:
        plan = MinerDogInvestmentPlan()
        plan.validate_investment_amount(investment_amount)

        daily_profit = plan.calculate_daily_profit(investment_amount)
        total_profit = plan.calculate_total_profit(investment_amount)

        investment_plan = {
            "investment_amount": investment_amount,
            "daily_profit": daily_profit,
            "total_profit": total_profit,
            "min_deposit": plan.min_deposit,
            "daily_profit_rate": plan.daily_profit_rate * 100,
            "total_profit_guarantee": plan.total_profit_guarantee * 100,
        }

        return investment_plan

    except ValueError as e:
        print(f"Error: {e}")
        return None


# Example usage
if __name__ == "__main__":
    investment_amount = 100  # in USDT
    investment_plan = create_investment_plan(investment_amount)

    if investment_plan:
        print("MinerDog Investment Plan:")
        for key, value in investment_plan.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
```
