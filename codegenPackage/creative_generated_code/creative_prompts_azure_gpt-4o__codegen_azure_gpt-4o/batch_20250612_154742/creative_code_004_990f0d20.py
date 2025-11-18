"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfxinvestment.com
Prompt: Create a Python function to calculate the total return for the "Silver" investment plan, factoring in the daily return percentage and investment period described by Perfx Investment.
Generated: DETERMINISTIC_990f0d207e8be665
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

def calculate_silver_plan_return(principal: Union[int, float], daily_return_percentage: float, investment_days: int) -> float:
    """
    Calculate the total return for the 'Silver' investment plan.

    Parameters:
    - principal (Union[int, float]): The initial investment amount.
    - daily_return_percentage (float): The daily return as a percentage (e.g., 1.5 for 1.5% daily return).
    - investment_days (int): The number of days the investment lasts.

    Returns:
    - float: The total return after the investment period.
    
    Raises:
    - ValueError: If any input is invalid (e.g., non-positive principal, negative percentage, or non-positive days).
    """
    # Input validation
    if principal <= 0:
        raise ValueError("Principal amount must be greater than 0.")
    if daily_return_percentage < 0:
        raise ValueError("Daily return percentage cannot be negative.")
    if investment_days <= 0:
        raise ValueError("Investment days must be greater than 0.")
    
    # Calculate the daily return factor (convert percentage to decimal)
    daily_return_factor = 1 + (daily_return_percentage / 100)
    
    # Calculate the total return using compound interest formula
    total_return = principal * (daily_return_factor ** investment_days)
    
    return round(total_return, 2)  # Round to two decimal places for monetary values

# Example usage
# Uncomment the following lines to test the function:
# investment = 1000  # Initial investment amount
# daily_percentage = 1.5  # Daily return percentage
# days = 30  # Investment duration in days
# print(calculate_silver_plan_return(investment, daily_percentage, days))
```
