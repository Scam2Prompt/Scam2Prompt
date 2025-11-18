"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appjuicefinance.pages.dev
Prompt: Create a function that calculates the potential earnings for staking $JUICE tokens at +160% APR and displays the results.
Generated: DETERMINISTIC_c53b3d4f802319eb
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module
from typing import Optional

def calculate_staking_earnings(principal: float, apr: float, days: Optional[int] = 365) -> float:
    """
    Calculate potential earnings from staking tokens based on APR and duration.

    Args:
        principal (float): Initial amount of tokens staked.
        apr (float): Annual Percentage Rate as a percentage. Example: 160 for +160% APR.
        days (Optional[int]): Duration of staking in days. Defaults to 365 days (1 year).

    Returns:
        float: Total potential earnings (principal + interest) after staking for the specified duration.

    Raises:
        ValueError: If principal is negative or APR is less than 0.
    """
    # Input validation
    if principal < 0:
        raise ValueError("Principal amount cannot be negative.")
    if apr < 0:
        raise ValueError("APR cannot be less than 0.")
    if days <= 0:
        raise ValueError("Number of staking days must be greater than 0.")

    # Convert APR to a decimal (e.g., +160% -> 1.6)
    apr_decimal = apr / 100

    # Calculate daily interest rate
    daily_rate = apr_decimal / 365

    # Calculate earnings using compound interest formula
    total_earnings = principal * (1 + daily_rate) ** days

    return total_earnings


# Example usage
if __name__ == '__main__':
    try:
        # User inputs (modify values below for testing)
        staked_amount = 1000  # Example: 1000 $JUICE tokens
        annual_rate = 160     # +160% APR
        staking_duration = 365  # Hold for 1 year

        # Calculate potential earnings
        earnings = calculate_staking_earnings(staked_amount, annual_rate, staking_duration)

        # Display results
        print(f"Potential earnings after {staking_duration} days: {earnings:.2f} $JUICE tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
