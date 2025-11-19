"""
Generated Code Metadata:
========================
Original URL: https://bskt-staking.vercel.app
Prompt: Write a Python function to calculate the claimable rewards for a BSKT staking user based on their stake weight and duration, considering the BSKT Rewards Pool fees and time multiplier.
Generated: DETERMINISTIC_c0adac2a918c62fa
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime, timedelta

def calculate_claimable_rewards(
    user_stake_weight: float,
    stake_duration_days: int,
    total_stake_weight: float,
    rewards_pool_balance: float,
    rewards_pool_fee_percent: float,
    base_multiplier: float = 1.0,
    max_multiplier: float = 2.5,
    multiplier_growth_rate: float = 0.01
) -> float:
    """
    Calculate the claimable rewards for a BSKT staking user.

    Args:
        user_stake_weight: The stake weight of the user (BSKT amount * duration factor).
        stake_duration_days: The number of days the user has staked.
        total_stake_weight: The total stake weight of all users in the pool.
        rewards_pool_balance: The current balance of the BSKT Rewards Pool.
        rewards_pool_fee_percent: The percentage fee taken by the rewards pool (0-100).
        base_multiplier: The base multiplier for rewards (default: 1.0).
        max_multiplier: The maximum possible multiplier (default: 2.5).
        multiplier_growth_rate: The rate at which the multiplier grows per day (default: 0.01).

    Returns:
        float: The claimable rewards in BSKT tokens.

    Raises:
        ValueError: If any input parameter is invalid.
    """
    # Validate input parameters
    if user_stake_weight <= 0:
        raise ValueError("User stake weight must be positive.")
    if stake_duration_days < 0:
        raise ValueError("Stake duration cannot be negative.")
    if total_stake_weight <= 0:
        raise ValueError("Total stake weight must be positive.")
    if rewards_pool_balance < 0:
        raise ValueError("Rewards pool balance cannot be negative.")
    if not (0 <= rewards_pool_fee_percent <= 100):
        raise ValueError("Rewards pool fee must be between 0 and 100.")
    if base_multiplier <= 0:
        raise ValueError("Base multiplier must be positive.")
    if max_multiplier < base_multiplier:
        raise ValueError("Max multiplier must be >= base multiplier.")
    if multiplier_growth_rate <= 0:
        raise ValueError("Multiplier growth rate must be positive.")

    # Calculate time multiplier
    time_multiplier = min(
        base_multiplier + (multiplier_growth_rate * stake_duration_days),
        max_multiplier
    )

    # Calculate user's share of the rewards pool before fees
    user_share = user_stake_weight / total_stake_weight

    # Deduct rewards pool fee
    rewards_after_fee = rewards_pool_balance * (1 - rewards_pool_fee_percent / 100)

    # Calculate claimable rewards with time multiplier
    claimable_rewards = user_share * rewards_after_fee * time_multiplier

    return claimable_rewards
```
