"""
Generated Code Metadata:
========================
Original URL: https://ststoned.pages.dev
Prompt: Generate a function that calculates the potential rewards for locking LP tokens with STONE based on a given APY of 2.93%.
Generated: DETERMINISTIC_5c7cdc67e9e0e91a
Batch ID: 20250612_163443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_lp_rewards(
    lp_token_amount: float, 
    apy: float = 2.93, 
    lock_duration_days: int = 365
) -> float:
    """
    Calculate the potential rewards for locking LP tokens with STONE based on a given APY.

    Args:
        lp_token_amount (float): Amount of LP tokens to be locked.
        apy (float, optional): Annual Percentage Yield (default: 2.93).
        lock_duration_days (int, optional): Duration in days for locking tokens (default: 365).

    Returns:
        float: Potential rewards earned.

    Raises:
        ValueError: If any input parameter is invalid (negative or zero).
    """
    if lp_token_amount <= 0:
        raise ValueError("LP token amount must be positive.")
    if apy <= 0:
        raise ValueError("APY must be positive.")
    if lock_duration_days <= 0:
        raise ValueError("Lock duration must be positive.")

    # Convert APY from percentage to decimal
    apy_decimal = apy / 100

    # Calculate annual rewards
    annual_rewards = lp_token_amount * apy_decimal

    # Calculate rewards for the lock duration
    rewards = annual_rewards * (lock_duration_days / 365)

    return rewards
```
