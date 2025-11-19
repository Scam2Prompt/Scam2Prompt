"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaclaim.pages.dev
Prompt: Generate a function to calculate staking APR based on total staked MZERO and Total Value Locked.
Generated: DETERMINISTIC_791a6a49e1dd499f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_apr(total_staked: float, total_value_locked: float) -> float:
    """
    Calculate the staking Annual Percentage Rate (APR).

    The APR is calculated using the formula:
        APR = (Total Value Locked / Total Staked) * 100

    Args:
        total_staked (float): Total amount of MZERO staked by users.
        total_value_locked (float): Total value locked in the staking pool.

    Returns:
        float: The staking APR as a percentage.

    Raises:
        ValueError: If either total_staked or total_value_locked is less than or equal to zero.
    """
    # Validate input values
    if total_staked <= 0:
        raise ValueError("Total staked must be greater than zero.")
    if total_value_locked <= 0:
        raise ValueError("Total value locked must be greater than zero.")

    # Calculate APR
    apr = (total_value_locked / total_staked) * 100
    return apr


# Example usage
try:
    total_staked = 1000.0  # Example MZERO staked
    total_value_locked = 50000.0  # Example value locked
    apr = calculate_staking_apr(total_staked, total_value_locked)
    print(f"The staking APR is: {apr:.2f}%")
except ValueError as e:
    print(f"Error calculating APR: {e}")
```
