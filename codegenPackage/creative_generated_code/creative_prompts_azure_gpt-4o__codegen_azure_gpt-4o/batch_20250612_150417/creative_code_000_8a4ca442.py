"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxprofitinvest.com.wadimorsarungkita.com
Prompt: Write Python code to calculate hourly profits for an investment plan offered by MaxProfit, using parameters like the initial investment amount and percentage profit per hour.
Generated: DETERMINISTIC_8a4ca442b77d4e6a
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Union

def calculate_hourly_profit(initial_investment: Union[int, float], hourly_profit_percent: Union[int, float]) -> float:
    """
    Calculate the hourly profit based on the initial investment and hourly profit percentage.

    Args:
        initial_investment (int | float): The amount of initial investment.
        hourly_profit_percent (int | float): The profit percentage per hour.

    Returns:
        float: The calculated hourly profit.
    """
    # Validate input parameters
    if initial_investment <= 0:
        raise ValueError("Initial investment must be greater than zero.")
    if hourly_profit_percent < 0:
        raise ValueError("Hourly profit percentage cannot be negative.")

    # Calculate hourly profit
    hourly_profit = initial_investment * (hourly_profit_percent / 100)
    return hourly_profit

def main():
    """
    Main function to demonstrate the calculation of hourly profits.
    """
    try:
        # Example inputs
        initial_investment = float(input("Enter the initial investment amount: "))
        hourly_profit_percent = float(input("Enter the profit percentage per hour: "))

        # Calculate profit
        profit = calculate_hourly_profit(initial_investment, hourly_profit_percent)
        print(f"Hourly Profit: ${profit:.2f}")
    except ValueError as e:
        # Handle invalid input errors
        print(f"Input Error: {e}")
    except Exception as e:
        # Handle any unforeseen errors
        print(f"An unexpected error occurred: {e}")

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
```
