"""
Generated Code Metadata:
========================
Original URL: https://coinex-tradings.ltd
Prompt: Write Python code to simulate the investment plans offered by Coinex Tradings, including calculations for daily returns based on the percentages provided (e.g., 5% daily for 30 days).
Generated: DETERMINISTIC_edac2a1fffb54eee
Batch ID: 20250612_152240
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
    A class to represent an investment plan with daily returns.
    """

    def __init__(self, principal: float, daily_rate: float, duration_days: int):
        """
        Initializes the investment plan with principal amount, daily return rate, and duration.

        :param principal: Initial investment amount (float).
        :param daily_rate: Daily return rate as a percentage (float).
        :param duration_days: Duration of the investment in days (int).
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if daily_rate < 0:
            raise ValueError("Daily rate must be non-negative.")
        if duration_days <= 0:
            raise ValueError("Duration must be greater than zero.")

        self.principal = principal
        self.daily_rate = daily_rate / 100  # Convert percentage to decimal
        self.duration_days = duration_days

    def calculate_daily_returns(self):
        """
        Calculates the daily returns for the investment plan.

        :return: A list of daily returns for each day of the investment.
        """
        daily_returns = []
        for day in range(1, self.duration_days + 1):
            daily_return = self.principal * (1 + self.daily_rate) ** day - self.principal
            daily_returns.append(daily_return)
        return daily_returns

    def total_return(self):
        """
        Calculates the total return after the investment duration.

        :return: Total return amount after the investment duration.
        """
        total_return = self.principal * (1 + self.daily_rate) ** self.duration_days
        return total_return

    def display_investment_summary(self):
        """
        Displays a summary of the investment plan including daily returns and total return.
        """
        print(f"Investment Summary:")
        print(f"Principal Amount: ${self.principal:.2f}")
        print(f"Daily Return Rate: {self.daily_rate * 100:.2f}%")
        print(f"Duration: {self.duration_days} days")
        print(f"Total Return after {self.duration_days} days: ${self.total_return():.2f}")
        print("Daily Returns:")
        for day, daily_return in enumerate(self.calculate_daily_returns(), start=1):
            print(f"Day {day}: ${daily_return:.2f}")


if __name__ == "__main__":
    try:
        # Example usage
        principal_amount = 1000.0  # Initial investment
        daily_return_rate = 5.0     # Daily return rate in percentage
        investment_duration = 30     # Duration in days

        # Create an investment plan
        investment_plan = InvestmentPlan(principal_amount, daily_return_rate, investment_duration)

        # Display the investment summary
        investment_plan.display_investment_summary()

    except ValueError as e:
        print(f"Error: {e}")
```
