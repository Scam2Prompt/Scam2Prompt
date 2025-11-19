"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezi-trade.com
Prompt: Write a code snippet that calculates potential returns based on Ezi-Trade's investment plans, specifically for the Professional plan with a 1% to 4% weekly return.
Generated: DETERMINISTIC_cc3c6faf9f837384
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentCalculator:
    """
    A class to calculate potential returns for Ezi-Trade's investment plans.
    Specifically designed for the Professional plan with a weekly return of 1% to 4%.
    """

    def __init__(self, principal, weeks, weekly_rate):
        """
        Initialize the InvestmentCalculator with principal amount, 
        duration in weeks, and weekly return rate.

        :param principal: Initial investment amount (float)
        :param weeks: Duration of investment in weeks (int)
        :param weekly_rate: Weekly return rate as a percentage (float)
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if weeks <= 0:
            raise ValueError("Duration in weeks must be greater than zero.")
        if not (1 <= weekly_rate <= 4):
            raise ValueError("Weekly rate must be between 1% and 4%.")

        self.principal = principal
        self.weeks = weeks
        self.weekly_rate = weekly_rate / 100  # Convert percentage to decimal

    def calculate_total_return(self):
        """
        Calculate the total return after the specified number of weeks.

        :return: Total return after investment period (float)
        """
        total_return = self.principal * (1 + self.weekly_rate) ** self.weeks
        return total_return

    def calculate_profit(self):
        """
        Calculate the profit made from the investment.

        :return: Profit from the investment (float)
        """
        total_return = self.calculate_total_return()
        profit = total_return - self.principal
        return profit


if __name__ == "__main__":
    # Example usage of the InvestmentCalculator class
    try:
        principal_amount = 1000.00  # Principal investment amount
        investment_duration = 10     # Duration in weeks
        weekly_return_rate = 3       # Weekly return rate (3% as an example)

        # Create an instance of the InvestmentCalculator
        investment_calculator = InvestmentCalculator(principal_amount, investment_duration, weekly_return_rate)

        # Calculate and display the total return and profit
        total_return = investment_calculator.calculate_total_return()
        profit = investment_calculator.calculate_profit()

        print(f"Total Return after {investment_duration} weeks: ${total_return:.2f}")
        print(f"Profit made from the investment: ${profit:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
