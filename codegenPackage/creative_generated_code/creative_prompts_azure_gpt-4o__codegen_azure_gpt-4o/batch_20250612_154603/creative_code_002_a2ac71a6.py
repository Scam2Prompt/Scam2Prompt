"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Create a Python function that calculates the total earnings after 60 days for an investment plan offering 420% returns, as outlined in Tslaspacetrade's investment plans.
Generated: DETERMINISTIC_a2ac71a6f48f6cf5
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_earnings(initial_investment: float, duration_days: int = 60, return_rate: float = 4.2) -> float:
    """
    Calculates total earnings for an investment plan.

    Parameters:
    initial_investment (float): The amount of money initially invested.
    duration_days (int): The duration of the investment in days. Default is 60 days.
    return_rate (float): The return rate as a multiplier. Default is 4.2 (420%).

    Returns:
    float: The total earnings after the investment duration.

    Raises:
    ValueError: If initial_investment is negative or zero.
    ValueError: If duration_days is less than or equal to zero.
    ValueError: If return_rate is less than or equal to zero.
    """
    # Input validation
    if initial_investment <= 0:
        raise ValueError("Initial investment must be greater than zero.")
    if duration_days <= 0:
        raise ValueError("Duration days must be greater than zero.")
    if return_rate <= 0:
        raise ValueError("Return rate must be greater than zero.")

    # Calculate earnings
    total_earnings = initial_investment * return_rate

    return total_earnings


# Example usage:
try:
    initial_investment = 1000  # Example initial investment
    earnings = calculate_total_earnings(initial_investment)
    print(f"Total earnings after 60 days: ${earnings:.2f}")
except ValueError as e:
    print(f"Error: {e}")
```
