"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.com
Prompt: Write code to calculate the total returns for a 7-day investment plan based on the daily return percentages provided for the Basic, Silver, Premium, and VIP plans on Astragoldbitx.com.
Generated: DETERMINISTIC_32b7a2b80e94b5ea
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List

# Define a function to calculate total returns for a 7-day investment plan
def calculate_total_returns(plan: str, daily_returns: List[float], initial_investment: float) -> float:
    """
    Calculate the total returns for a 7-day investment plan.

    Args:
        plan (str): The name of the investment plan (e.g., Basic, Silver, Premium, VIP).
        daily_returns (List[float]): Daily return percentages for the 7-day period (e.g., [2.0, 1.5, 2.1, ...]).
        initial_investment (float): The initial investment amount.

    Returns:
        float: The total returns after 7 days.
    
    Raises:
        ValueError: If the plan name is invalid or if daily_returns does not contain exactly 7 values.
    """
    # Validate input
    valid_plans = {"Basic", "Silver", "Premium", "VIP"}
    if plan not in valid_plans:
        raise ValueError(f"Invalid plan name: {plan}. Plan must be one of {valid_plans}.")
    
    if len(daily_returns) != 7:
        raise ValueError("daily_returns must contain exactly 7 values (one for each day).")
    
    if initial_investment <= 0:
        raise ValueError("Initial investment must be greater than zero.")

    # Calculate total returns
    current_balance = initial_investment
    for daily_return in daily_returns:
        # daily_return is given in percentage (e.g., 2.0 means +2%)
        current_balance += current_balance * (daily_return / 100.0)
    
    return round(current_balance, 2)  # Round to 2 decimal places for currency precision


# Example usage of the function
if __name__ == "__main__":
    try:
        # Define the plan, daily returns, and initial investment
        investment_plan = "Premium"
        daily_return_percentages = [1.5, 2.0, 1.8, 2.2, 1.9, 2.1, 2.0]  # Example percentages
        initial_investment_amount = 1000.0  # Example initial investment

        # Calculate total returns
        total_returns = calculate_total_returns(investment_plan, daily_return_percentages, initial_investment_amount)

        # Output the result
        print(f"Total returns for the {investment_plan} plan after 7 days: ${total_returns}")
    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {e}")
```
