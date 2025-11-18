"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coineehub.com
Prompt: Generate a Python script to automate the calculation of daily returns for CoineeHub's investment packages, using input data such as investment amount and duration.
Generated: DETERMINISTIC_577c39c7459d8176
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class InvestmentCalculator:
    """
    A class to calculate daily returns for CoineeHub's investment packages.
    """

    def __init__(self, investment_amount, duration_days, daily_rate):
        """
        Initializes the InvestmentCalculator with investment amount, duration, and daily return rate.

        :param investment_amount: float, the total amount invested
        :param duration_days: int, the duration of the investment in days
        :param daily_rate: float, the daily return rate as a percentage (e.g., 0.05 for 0.05%)
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if duration_days <= 0:
            raise ValueError("Duration must be greater than zero.")
        if daily_rate < 0:
            raise ValueError("Daily rate must not be negative.")

        self.investment_amount = investment_amount
        self.duration_days = duration_days
        self.daily_rate = daily_rate / 100  # Convert percentage to decimal

    def calculate_daily_returns(self):
        """
        Calculates daily returns over the duration of the investment.

        :return: DataFrame containing the day and the corresponding daily return
        """
        # Create a list to store daily returns
        daily_returns = []

        # Calculate daily returns for each day
        for day in range(1, self.duration_days + 1):
            daily_return = self.investment_amount * self.daily_rate
            daily_returns.append({'Day': day, 'Daily Return': daily_return})

        # Create a DataFrame from the daily returns list
        return pd.DataFrame(daily_returns)

def main():
    """
    Main function to run the investment calculator.
    """
    try:
        # Example input values
        investment_amount = float(input("Enter the investment amount: "))
        duration_days = int(input("Enter the duration in days: "))
        daily_rate = float(input("Enter the daily return rate (%): "))

        # Initialize the InvestmentCalculator
        calculator = InvestmentCalculator(investment_amount, duration_days, daily_rate)

        # Calculate daily returns
        returns_df = calculator.calculate_daily_returns()

        # Output the results
        print("\nDaily Returns Over Investment Duration:")
        print(returns_df)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
