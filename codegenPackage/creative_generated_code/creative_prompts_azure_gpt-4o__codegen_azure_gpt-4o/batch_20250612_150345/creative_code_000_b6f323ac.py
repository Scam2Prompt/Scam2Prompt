"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.com
Prompt: Write Python code to calculate daily returns for an investment plan based on the parameters provided by Astragoldbitx.com, including minimum investment, maximum investment, and daily return percentages.
Generated: DETERMINISTIC_b6f323acd2ba4524
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture errors and important information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_daily_returns(min_investment, max_investment, daily_return_percentage):
    """
    Calculate daily returns for an investment plan.

    Args:
        min_investment (float): Minimum investment amount.
        max_investment (float): Maximum investment amount.
        daily_return_percentage (float): Daily return percentage (e.g., 5 for 5%).

    Returns:
        dict: A dictionary with investment amount as key and daily return as value.

    Raises:
        ValueError: If input values are invalid.
    """
    try:
        # Validate inputs
        if min_investment <= 0 or max_investment <= 0:
            raise ValueError("Investment amounts must be greater than 0.")
        if daily_return_percentage <= 0:
            raise ValueError("Daily return percentage must be greater than 0.")
        if min_investment > max_investment:
            raise ValueError("Minimum investment cannot be greater than maximum investment.")

        # Calculate daily returns
        investment_plan = {}
        for investment in range(int(min_investment), int(max_investment) + 1):
            daily_return = investment * (daily_return_percentage / 100)
            investment_plan[investment] = round(daily_return, 2)

        return investment_plan

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Parameters for the investment plan
        min_investment = 100
        max_investment = 200
        daily_return_percentage = 5  # 5%

        # Calculate daily returns
        daily_returns = calculate_daily_returns(min_investment, max_investment, daily_return_percentage)

        # Output the results
        print("Investment Plan - Daily Returns:")
        for investment, daily_return in daily_returns.items():
            print(f"Investment: ${investment} => Daily Return: ${daily_return}")

    except Exception as error:
        print(f"Error: {error}")
```
