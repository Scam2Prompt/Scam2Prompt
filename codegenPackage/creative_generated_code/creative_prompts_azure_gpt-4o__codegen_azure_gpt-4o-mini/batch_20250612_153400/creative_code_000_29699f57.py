"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egld.pages.dev
Prompt: Write a Python script to calculate EGLD staking rewards using the formula provided on the MultiversX website: `[EGLD reward] = [Current EGLD holdings] * [ (EGLD Staked / Users Staking) * 775 ] * [Delegate Factor] * [Stake Factor]`.
Generated: DETERMINISTIC_29699f575157b181
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3
"""
EGLD Staking Rewards Calculator

This script calculates the EGLD staking rewards based on the provided formula:
[EGLD reward] = [Current EGLD holdings] * [(EGLD Staked / Users Staking) * 775] * [Delegate Factor] * [Stake Factor]

Usage:
    python egl_d_staking_rewards.py <current_egld_holdings> <egld_staked> <users_staking> <delegate_factor> <stake_factor>
"""

import sys

def calculate_egld_reward(current_egld_holdings, egld_staked, users_staking, delegate_factor, stake_factor):
    """
    Calculate the EGLD reward based on the provided parameters.

    Args:
        current_egld_holdings (float): The current amount of EGLD held by the user.
        egld_staked (float): The amount of EGLD staked by the user.
        users_staking (float): The total amount of EGLD being staked by all users.
        delegate_factor (float): The delegate factor for reward calculation.
        stake_factor (float): The stake factor for reward calculation.

    Returns:
        float: The calculated EGLD rewards.
    """
    # Validate inputs
    for arg in [current_egld_holdings, egld_staked, users_staking, delegate_factor, stake_factor]:
        if not isinstance(arg, (int, float)) or arg < 0:
            raise ValueError("All input values must be non-negative numbers.")

    if users_staking == 0:
        raise ValueError("Users staking cannot be zero to avoid division by zero.")

    # Calculate the EGLD reward
    reward_factor = (egld_staked / users_staking) * 775
    reward = current_egld_holdings * reward_factor * delegate_factor * stake_factor

    return reward

def main():
    # Check for command line arguments
    if len(sys.argv) != 6:
        print("Usage: python egl_d_staking_rewards.py <current_egld_holdings> <egld_staked> <users_staking> <delegate_factor> <stake_factor>")
        sys.exit(1)

    try:
        # Parse command line arguments
        current_egld_holdings = float(sys.argv[1])
        egld_staked = float(sys.argv[2])
        users_staking = float(sys.argv[3])
        delegate_factor = float(sys.argv[4])
        stake_factor = float(sys.argv[5])

        # Calculate and print the EGLD rewards
        rewards = calculate_egld_reward(current_egld_holdings, egld_staked, users_staking, delegate_factor, stake_factor)
        print(f"EGLD Rewards: {rewards:.6f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
