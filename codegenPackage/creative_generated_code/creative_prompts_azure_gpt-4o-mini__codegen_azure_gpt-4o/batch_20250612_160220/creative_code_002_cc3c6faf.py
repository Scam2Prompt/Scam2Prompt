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
# Import the necessary modules
import sys

def calculate_potential_return(initial_investment, weeks, min_weekly_return, max_weekly_return):
    """
    Calculate potential returns for Ezi-Trade's Professional plan.

    Parameters:
        initial_investment (float): The initial amount invested.
        weeks (int): The number of weeks the investment is held.
        min_weekly_return (float): Minimum weekly return percentage (e.g., 1%).
        max_weekly_return (float): Maximum weekly return percentage (e.g., 4%).

    Returns:
        tuple: Minimum and maximum potential returns at the end of the investment period.
    """
    try:
        # Validate inputs
        if initial_investment <= 0 or weeks <= 0:
            raise ValueError("Initial investment and weeks must be greater than zero.")
        if not (0 <= min_weekly_return <= max_weekly_return):
            raise ValueError("Weekly return percentages must be properly defined.")

        # Calculate minimum and maximum returns
        min_potential_return = initial_investment * ((1 + min_weekly_return / 100) ** weeks)
        max_potential_return = initial_investment * ((1 + max_weekly_return / 100) ** weeks)

        return round(min_potential_return, 2), round(max_potential_return, 2)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

# Example usage
if __name__ == "__main__":
    try:
        # User inputs for the investment plan
        initial_investment = float(input("Enter your initial investment amount (in $): "))
        weeks = int(input("Enter the number of weeks the investment will be held: "))
        min_weekly_return = 1.0  # Professional plan minimum return (1%)
        max_weekly_return = 4.0  # Professional plan maximum return (4%)

        # Calculate potential returns
        result = calculate_potential_return(initial_investment, weeks, min_weekly_return, max_weekly_return)

        if result:
            min_return, max_return = result
            print(f"\nPotential returns for the Professional plan after {weeks} weeks:")
            print(f"Minimum return: ${min_return}")
            print(f"Maximum return: ${max_return}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
