"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-rewarded.pages.dev
Prompt: Create a function that simulates the locking process of $BONK tokens, including calculations for the total weighted locked amount and rewards multiplier as outlined on the Bonk Rewards page.
Generated: DETERMINISTIC_f2e6acc709e6c9ee
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Tuple

class BonkLockingException(Exception):
    """Custom exception for BONK locking errors."""
    pass

def calculate_locked_amount_and_multiplier(lock_periods: List[int], amounts: List[float]) -> Tuple[float, float]:
    """
    Simulates the locking process of BONK tokens, calculating the total weighted locked amount 
    and rewards multiplier based on lock periods and amounts.

    Parameters:
        lock_periods (List[int]): A list of lock periods in months. Each value must be between 1 and 48.
        amounts (List[float]): A list of token amounts to lock, corresponding to the lock periods.

    Returns:
        Tuple[float, float]: A tuple containing:
            - total_weighted_locked_amount: The sum of weighted locked amounts based on lock periods.
            - rewards_multiplier: The rewards multiplier based on the weighted average lock period.

    Raises:
        BonkLockingException: If the input data is invalid.
    """
    # Validate input
    if not lock_periods or not amounts:
        raise BonkLockingException("Lock periods and amounts cannot be empty.")
    if len(lock_periods) != len(amounts):
        raise BonkLockingException("Lock periods and amounts must have the same length.")
    if any(period < 1 or period > 48 for period in lock_periods):
        raise BonkLockingException("Lock periods must be between 1 and 48 months.")
    if any(amount <= 0 for amount in amounts):
        raise BonkLockingException("Amounts must be positive.")

    # Constants
    MAX_REWARD_MULTIPLIER = 2.0  # Maximum rewards multiplier
    MAX_LOCK_PERIOD = 48        # Maximum lock period in months

    # Calculate weighted locked amount and weighted average lock period
    total_weighted_locked_amount = 0.0
    total_amount = sum(amounts)
    weighted_lock_period = 0.0

    for period, amount in zip(lock_periods, amounts):
        # Weight is determined by the lock period (longer lock periods have higher weight)
        weight = period / MAX_LOCK_PERIOD
        total_weighted_locked_amount += amount * weight
        weighted_lock_period += period * (amount / total_amount)

    # Calculate rewards multiplier based on weighted average lock period
    rewards_multiplier = (weighted_lock_period / MAX_LOCK_PERIOD) * MAX_REWARD_MULTIPLIER

    return total_weighted_locked_amount, rewards_multiplier

# Example usage:
if __name__ == "__main__":
    try:
        lock_periods = [12, 24, 36]  # Lock periods in months
        amounts = [1000.0, 2000.0, 3000.0]  # Amounts in BONK tokens
        total_locked, multiplier = calculate_locked_amount_and_multiplier(lock_periods, amounts)
        print(f"Total Weighted Locked Amount: {total_locked}")
        print(f"Rewards Multiplier: {multiplier:.2f}")
    except BonkLockingException as e:
        print(f"Error: {e}")
```
