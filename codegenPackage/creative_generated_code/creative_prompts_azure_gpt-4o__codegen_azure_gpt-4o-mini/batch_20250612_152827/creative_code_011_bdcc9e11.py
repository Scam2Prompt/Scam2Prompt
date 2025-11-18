"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newworldtradex.com
Prompt: Create a program to calculate daily yields and total profits for a user investing in the "Premium Plan" with a capital of $100,000 over 5 days.
Generated: DETERMINISTIC_bdcc9e110ec890e5
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """A class to represent an investment plan."""

    def __init__(self, capital, daily_yield_rate, days):
        """
        Initialize the investment plan with capital, daily yield rate, and duration.

        Parameters:
        capital (float): The initial amount invested.
        daily_yield_rate (float): The daily yield rate (as a percentage).
        days (int): The number of days the investment is held.
        """
        self.capital = capital
        self.daily_yield_rate = daily_yield_rate / 100  # Convert percentage to decimal
        self.days = days

    def calculate_daily_yield(self):
        """
        Calculate the daily yield based on the current capital.

        Returns:
        float: The daily yield amount.
        """
        return self.capital * self.daily_yield_rate

    def calculate_total_profit(self):
        """
        Calculate the total profit over the specified duration.

        Returns:
        float: The total profit amount.
        """
        # Total profit is daily yield multiplied by the number of days
        return self.calculate_daily_yield() * self.days

    def display_results(self):
        """Display the daily yield and total profit."""
        try:
            daily_yield = self.calculate_daily_yield()
            total_profit = self.calculate_total_profit()

            print(f"Initial Capital: ${self.capital:,.2f}")
            print(f"Daily Yield: ${daily_yield:,.2f}")
            print(f"Total Profit over {self.days} days: ${total_profit:,.2f}")

        except Exception as e:
            print(f"An error occurred while displaying results: {e}")


def main():
    """Main function to execute the investment plan calculation."""
    try:
        # Define investment parameters
        capital = 100000  # Initial capital of $100,000
        daily_yield_rate = 2  # Daily yield rate of 2%
        days = 5  # Duration of investment in days

        # Create an instance of InvestmentPlan
        investment = InvestmentPlan(capital, daily_yield_rate, days)

        # Display the results
        investment.display_results()

    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
