"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabkafuture.com
Prompt: Write a Python script to calculate daily returns for the "UNIQUE PLAN" investment offered by Sabka Future, using the provided investment amount and duration details.
Generated: DETERMINISTIC_54dd454150c1ba0f
Batch ID: 20250612_150417
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
    A class to calculate daily returns for the UNIQUE PLAN investment.

    Attributes:
        investment_amount (float): The initial amount invested.
        duration_days (int): The duration in days for the investment.
        daily_return_rate (float): The daily return rate (as a decimal).
    """

    def __init__(self, investment_amount, duration_days, daily_return_rate):
        """
        Initializes the InvestmentCalculator with investment details.

        Parameters:
            investment_amount (float): The initial investment amount.
            duration_days (int): The duration in days.
            daily_return_rate (float): The daily return rate (as a decimal).
        """
        self.investment_amount = investment_amount
        self.duration_days = duration_days
        self.daily_return_rate = daily_return_rate

    def calculate_daily_returns(self):
        """
        Calculates daily returns over the duration of the investment.

        Returns:
            pd.DataFrame: A DataFrame containing the daily returns.
        """
        try:
            # Create a list to store daily returns
            daily_returns = []

            for day in range(1, self.duration_days + 1):
                # Calculate the return for the current day
                daily_return = self.investment_amount * (1 + self.daily_return_rate) ** day - self.investment_amount
                daily_returns.append({
                    'Day': day,
                    'Daily Return': daily_return
                })
            
            # Convert the list to a DataFrame for better visualization
            return pd.DataFrame(daily_returns)

        except Exception as e:
            print(f"An error occurred while calculating daily returns: {e}")
            return pd.DataFrame(columns=['Day', 'Daily Return'])

def main():
    """
    Main function to execute the investment calculator.
    """
    # User-defined inputs
    investment_amount = 10000  # Example investment amount
    duration_days = 30          # Example duration in days
    daily_return_rate = 0.01    # Example return rate (1% daily)

    # Initialize the investment calculator
    investment_calculator = InvestmentCalculator(investment_amount, duration_days, daily_return_rate)

    # Calculate daily returns
    daily_returns_df = investment_calculator.calculate_daily_returns()

    # Output the results
    print(daily_returns_df)

if __name__ == "__main__":
    main()
```
