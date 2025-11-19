"""
Generated Code Metadata:
========================
Original URL: https://fennextradingservices.com
Prompt: Create a function that simulates the process of opening an advisory account, funding it, selecting an investment plan, and tracking financial growth, as described on the Fennex Trading Services platform.
Generated: DETERMINISTIC_4599ca40dbded321
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AdvisoryAccount:
    """
    A class to represent an advisory account for investment purposes.
    """

    def __init__(self, account_holder: str):
        """
        Initializes a new advisory account.

        :param account_holder: The name of the account holder.
        """
        self.account_holder = account_holder
        self.balance = 0.0
        self.investment_plan = None
        self.growth_rate = 0.0
        self.investment_period = 0  # in years

    def fund_account(self, amount: float):
        """
        Funds the advisory account with a specified amount.

        :param amount: The amount to fund the account.
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Funding amount must be greater than zero.")
        self.balance += amount
        print(f"Account funded: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def select_investment_plan(self, plan: str, growth_rate: float, period: int):
        """
        Selects an investment plan and sets the expected growth rate and period.

        :param plan: The name of the investment plan.
        :param growth_rate: The expected annual growth rate (as a decimal).
        :param period: The investment period in years.
        :raises ValueError: If the growth rate is negative or period is non-positive.
        """
        if growth_rate < 0:
            raise ValueError("Growth rate must be non-negative.")
        if period <= 0:
            raise ValueError("Investment period must be greater than zero.")
        
        self.investment_plan = plan
        self.growth_rate = growth_rate
        self.investment_period = period
        print(f"Investment plan '{self.investment_plan}' selected with growth rate: {self.growth_rate:.2%} for {self.investment_period} years.")

    def track_growth(self):
        """
        Calculates and returns the projected growth of the investment over the specified period.

        :return: The projected value of the investment after the investment period.
        :raises ValueError: If no investment plan is selected or if the balance is zero.
        """
        if self.investment_plan is None:
            raise ValueError("No investment plan selected.")
        if self.balance <= 0:
            raise ValueError("Account balance must be greater than zero to track growth.")

        # Calculate future value using compound interest formula
        future_value = self.balance * (1 + self.growth_rate) ** self.investment_period
        print(f"Projected value after {self.investment_period} years: ${future_value:.2f}")
        return future_value


# Example usage
if __name__ == "__main__":
    try:
        account = AdvisoryAccount("John Doe")
        account.fund_account(10000)
        account.select_investment_plan("Aggressive Growth", 0.08, 5)
        projected_value = account.track_growth()
    except ValueError as e:
        print(f"Error: {e}")
```
