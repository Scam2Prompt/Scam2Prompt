"""
Generated Code Metadata:
========================
Original URL: https://bonk-rewarded.pages.dev
Prompt: Write a Python script to calculate the BONK rewards for a user locking a certain amount of $BONK for a specified duration, considering the multiplier and total locked amount.
Generated: DETERMINISTIC_4accf406317bbbf4
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Tuple

def calculate_bonk_rewards(
    user_locked_amount: float,
    total_locked_amount: float,
    lock_duration_days: int,
    base_apr: float = 0.1,  # 10% APR by default
    max_multiplier: float = 2.0,  # 2x multiplier for max duration
    max_duration_days: int = 365  # 1 year max duration
) -> Tuple[float, float]:
    """
    Calculate BONK rewards for a user based on locked amount and duration.

    Args:
        user_locked_amount: Amount of BONK tokens locked by the user.
        total_locked_amount: Total BONK tokens locked in the pool.
        lock_duration_days: Number of days the tokens are locked.
        base_apr: Base annual percentage rate (default: 10%).
        max_multiplier: Maximum reward multiplier (default: 2x).
        max_duration_days: Maximum lock duration in days (default: 365).

    Returns:
        Tuple containing:
        - reward_multiplier: Calculated multiplier based on lock duration
        - user_rewards: Calculated BONK rewards for the user

    Raises:
        ValueError: If any input parameter is invalid.
    """
    # Validate input parameters
    if user_locked_amount <= 0:
        raise ValueError("User locked amount must be positive")
    if total_locked_amount <= 0:
        raise ValueError("Total locked amount must be positive")
    if lock_duration_days <= 0:
        raise ValueError("Lock duration must be positive")
    if base_apr <= 0:
        raise ValueError("Base APR must be positive")
    if max_multiplier <= 1:
        raise ValueError("Max multiplier must be greater than 1")
    if max_duration_days <= 0:
        raise ValueError("Max duration must be positive")

    # Calculate duration multiplier (linear scaling from 1x to max_multiplier)
    duration_multiplier = 1 + (max_multiplier - 1) * min(lock_duration_days, max_duration_days) / max_duration_days

    # Calculate user's share of the pool
    user_share = user_locked_amount / total_locked_amount

    # Calculate daily reward rate with multiplier applied
    daily_reward_rate = (base_apr * duration_multiplier) / 365

    # Calculate total rewards for the lock duration
    user_rewards = user_locked_amount * daily_reward_rate * lock_duration_days

    return duration_multiplier, user_rewards

if __name__ == "__main__":
    try:
        # Example usage
        user_amount = float(input("Enter user locked BONK amount: "))
        total_amount = float(input("Enter total locked BONK amount: "))
        duration = int(input("Enter lock duration in days: "))

        multiplier, rewards = calculate_bonk_rewards(
            user_locked_amount=user_amount,
            total_locked_amount=total_amount,
            lock_duration_days=duration
        )

        print(f"\nReward Multiplier: {multiplier:.2f}x")
        print(f"Estimated BONK Rewards: {rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
