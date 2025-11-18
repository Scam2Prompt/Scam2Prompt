"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethminer.world
Prompt: Create a function in Python that calculates the daily earnings for a user based on the mining plan selected (V1.1, V1.2, or V1.3) and outputs the total ETH earned after a specified number of days.
Generated: DETERMINISTIC_7172633213bcbd0f
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from typing import Union

def calculate_earnings(plan: str, days: int) -> Union[float, str]:
    """
    Calculate the total Ethereum (ETH) earnings based on the mining plan
    selected and the number of days specified.

    Args:
        plan (str): The mining plan selected. Options are 'V1.1', 'V1.2', or 'V1.3'.
        days (int): The number of days the mining plan is active.

    Returns:
        Union[float, str]: The total ETH earned after the specified number of days,
                           or an error message if inputs are invalid.
    """
    # Define daily earnings rates for each plan
    daily_rates = {
        'V1.1': 0.005,  # Example: Plan V1.1 earns 0.005 ETH per day
        'V1.2': 0.010,  # Example: Plan V1.2 earns 0.010 ETH per day
        'V1.3': 0.015   # Example: Plan V1.3 earns 0.015 ETH per day
    }

    # Validate the inputs
    if plan not in daily_rates:
        return "Error: Invalid mining plan selected. Choose 'V1.1', 'V1.2', or 'V1.3'."
    if days <= 0:
        return "Error: Number of days must be a positive integer."

    # Calculate the total earnings
    daily_rate = daily_rates[plan]
    total_earnings = daily_rate * days

    return round(total_earnings, 6)  # Return earnings rounded to 6 decimal places

# Example usage
if __name__ == "__main__":
    # User inputs
    user_plan = "V1.2"  # Selected mining plan
    user_days = 30      # Number of days

    # Calculate and display the total earnings
    result = calculate_earnings(user_plan, user_days)
    print(f"Total ETH earned: {result}")
```
