"""
Generated Code Metadata:
========================
Original URL: https://easyfxtrades-invest.com
Prompt: Write Python code to simulate daily returns for an investment plan based on the "Basic Plan" described on easyfxtrades-invest.com, which offers 5% returns for 7 days on investments between $300 and $4999.
Generated: DETERMINISTIC_0591ab8d88312ed9
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class InvestmentPlan:
    """
    A class to simulate daily returns for an investment plan.
    The Basic Plan offers 5% returns for 7 days on investments between $300 and $4999.
    """

    def __init__(self, investment_amount):
        """
        Initializes the InvestmentPlan with a specified investment amount.

        :param investment_amount: The amount to invest, must be between $300 and $4999.
        :raises ValueError: If the investment amount is outside the valid range.
        """
        if not (300 <= investment_amount <= 4999):
            raise ValueError("Investment amount must be between $300 and $4999.")
        self.investment_amount = investment_amount
        self.daily_return_rate = 0.05  # 5% daily return
        self.days = 7  # Duration of the investment plan

    def simulate_daily_returns(self):
        """
        Simulates daily returns for the investment over the specified duration.

        :return: A list of daily returns.
        """
        daily_returns = []
        for day in range(1, self.days + 1):
            daily_return = self.investment_amount * self.daily_return_rate
            daily_returns.append(daily_return)
            # Update the investment amount for the next day's return
            self.investment_amount += daily_return
        return daily_returns

    def total_return(self):
        """
        Calculates the total return after the investment period.

        :return: The total return amount after 7 days.
        """
        return sum(self.simulate_daily_returns())

def main():
    """
    Main function to execute the investment simulation.
    """
    try:
        # Example investment amount
        investment_amount = 1000  # Change this value to test different amounts
        investment_plan = InvestmentPlan(investment_amount)
        
        # Simulate daily returns
        daily_returns = investment_plan.simulate_daily_returns()
        print("Daily Returns for each day:")
        for day, return_amount in enumerate(daily_returns, start=1):
            print(f"Day {day}: ${return_amount:.2f}")

        # Calculate total return
        total = investment_plan.total_return()
        print(f"\nTotal return after {investment_plan.days} days: ${total:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
