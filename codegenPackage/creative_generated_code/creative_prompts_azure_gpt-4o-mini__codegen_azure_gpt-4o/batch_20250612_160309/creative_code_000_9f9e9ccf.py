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
# Import necessary libraries
import sys

def calculate_daily_profits(initial_investment, daily_return_rate, total_days):
    """
    Calculate daily profits for a cryptocurrency staking plan.

    Parameters:
        initial_investment (float): The amount of money initially invested.
        daily_return_rate (float): The daily return rate (e.g., 0.002 for 0.2%).
        total_days (int): The total number of days to calculate profits for.

    Returns:
        list: A list of tuples containing day and cumulative profit for each day.
    """
    try:
        # Validate inputs for investment boundaries
        if initial_investment < 25 or initial_investment > 250:
            raise ValueError("Initial investment must be between $25 and $250.")
        if daily_return_rate <= 0 or total_days <= 0:
            raise ValueError("Daily return rate and total days must be positive values.")
        
        # Initialize variables
        daily_profits = []
        cumulative_profit = 0

        # Calculate profits for each day
        for day in range(1, total_days + 1):
            daily_profit = initial_investment * daily_return_rate
            cumulative_profit += daily_profit
            daily_profits.append((day, round(cumulative_profit, 2)))  # Round to 2 decimal places for financial data

        return daily_profits

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return []


def display_profits(profits):
    """
    Display daily profits in a readable format.

    Parameters:
        profits (list): A list of tuples containing day and cumulative profit.
    """
    if profits:
        print("\nDaily Profits:")
        print(f"{'Day':<5} {'Cumulative Profit ($)':<20}")
        print("=" * 25)
        for day, profit in profits:
            print(f"{day:<5} {profit:<20}")
    else:
        print("No profits to display due to input errors.")


if __name__ == "__main__":
    # Define the parameters
    INITIAL_INVESTMENT = 100  # Change this value for different investments
    DAILY_RETURN_RATE = 0.002  # 0.2% daily return
    TOTAL_DAYS = 100  # Number of days to calculate profits

    # Calculate profits
    profits = calculate_daily_profits(INITIAL_INVESTMENT, DAILY_RETURN_RATE, TOTAL_DAYS)

    # Display profits
    display_profits(profits)
```
