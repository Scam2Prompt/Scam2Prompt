"""
Generated Code Metadata:
========================
Original URL: https://maxonex.com
Prompt: "Design a function to calculate potential earnings on Maxonex for betting on political events, considering the 4.05% APY on cash and positions."
Generated: DETERMINISTIC_7f53227bf996ecfd
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

def calculate_potential_earnings(principal, days_held, apy=4.05):
    """
    Calculate potential earnings on Maxonex for betting on political events, 
    considering the 4.05% APY on cash and positions.

    Args:
        principal (float): The initial amount of money invested or held.
        days_held (int): The number of days the money is held or invested.
        apy (float): Annual Percentage Yield (default is 4.05%).

    Returns:
        float: The total earnings (interest) accrued over the specified period.
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if days_held < 0:
            raise ValueError("Days held cannot be negative.")
        if apy <= 0:
            raise ValueError("APY must be greater than zero.")

        # Convert APY to daily interest rate
        daily_rate = apy / 100 / 365

        # Calculate earnings
        earnings = principal * daily_rate * days_held

        return round(earnings, 2)  # Return earnings rounded to two decimal places

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return 0.0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0.0


# Example usage:
if __name__ == "__main__":
    # Example inputs
    principal_amount = 1000.0  # $1000 invested
    holding_period = 30        # Held for 30 days

    # Calculate potential earnings
    earnings = calculate_potential_earnings(principal_amount, holding_period)
    print(f"Potential earnings for ${principal_amount} held for {holding_period} days: ${earnings}")
```
