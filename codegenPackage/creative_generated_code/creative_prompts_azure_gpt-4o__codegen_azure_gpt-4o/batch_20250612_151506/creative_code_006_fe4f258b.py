"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Develop a Python script to calculate the return on investment (ROI) for MET LIFE INVESTS' plans, factoring in daily profit and capital return.
Generated: DETERMINISTIC_fe4f258b3c85e91e
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_roi(initial_investment, daily_profit_rate, days_invested, capital_return_rate):
    """
    Calculate the Return on Investment (ROI) based on daily profit and capital return.

    Parameters:
    - initial_investment (float): The amount of money invested initially.
    - daily_profit_rate (float): The daily profit rate as a percentage (e.g., 0.02 for 2% daily return).
    - days_invested (int): The number of days the investment has been active.
    - capital_return_rate (float): The percentage of capital returned at the end of the investment period (e.g., 1.0 for 100%).

    Returns:
    - float: The calculated ROI.
    """
    try:
        # Validate inputs
        if initial_investment <= 0 or daily_profit_rate < 0 or days_invested <= 0 or capital_return_rate < 0:
            raise ValueError("Input values must be positive, and profit rates cannot be negative.")

        # Calculate total profit from daily returns
        total_profit = initial_investment * daily_profit_rate * days_invested

        # Calculate capital return at the end of the period
        capital_return = initial_investment * capital_return_rate

        # Calculate ROI
        total_return = total_profit + capital_return
        roi = (total_return - initial_investment) / initial_investment * 100  # ROI as a percentage
        return roi
    except TypeError:
        print("Error: Invalid data types provided. Please ensure all inputs are numeric.", file=sys.stderr)
        return None
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None

def main():
    # Example usage
    print("MET LIFE INVESTS - ROI Calculator\n")
    try:
        # Input from user for calculations
        initial_investment = float(input("Enter the initial investment amount (e.g., 1000): "))
        daily_profit_rate = float(input("Enter the daily profit rate as percentage (e.g., 0.02 for 2%): "))
        days_invested = int(input("Enter the number of days invested: "))
        capital_return_rate = float(input("Enter the capital return rate as percentage (e.g., 1.0 for 100%): "))

        # Compute ROI
        roi = calculate_roi(initial_investment, daily_profit_rate, days_invested, capital_return_rate)
        if roi is not None:
            print(f"\nThe calculated ROI is: {roi:.2f}%")
    except ValueError:
        print("Error: Invalid input. Please provide numeric values for all fields.", file=sys.stderr)

if __name__ == "__main__":
    main()
```
