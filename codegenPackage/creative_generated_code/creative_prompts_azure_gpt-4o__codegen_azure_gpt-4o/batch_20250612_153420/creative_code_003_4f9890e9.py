"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Write a function in Python that calculates staking rewards for $SCOTTY tokens based on the lock period multiplier and APY, as described on the webpage.
Generated: DETERMINISTIC_4f9890e94948ea84
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Function to calculate staking rewards for $SCOTTY tokens.

Parameters:
    principal (float): The amount of $SCOTTY tokens staked.
    apy (float): The annual percentage yield (in decimal form, e.g., 0.15 for 15% APY).
    lock_period_days (int): The number of days tokens are locked.
    lock_period_multiplier (float): Multiplier based on lock period (e.g., 1.2 for 1.2x rewards).

Returns:
    float: The total staking rewards accrued.
"""

import math

def calculate_staking_rewards(principal, apy, lock_period_days, lock_period_multiplier):
    try:
        # Validate input parameters
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if apy <= 0 or apy > 1:
            raise ValueError("APY must be a decimal value between 0 and 1 (e.g., 0.15 for 15%).")
        if lock_period_days <= 0:
            raise ValueError("Lock period days must be greater than zero.")
        if lock_period_multiplier <= 0:
            raise ValueError("Lock period multiplier must be greater than zero.")

        # Constants
        DAYS_IN_YEAR = 365

        # Calculate base rewards (without multiplier)
        base_rewards = principal * apy * (lock_period_days / DAYS_IN_YEAR)

        # Apply lock period multiplier
        total_rewards = base_rewards * lock_period_multiplier

        return round(total_rewards, 2)  # Return rounded rewards (to 2 decimal places)

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return 0.0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0.0


# Example usage
if __name__ == "__main__":
    # Example inputs
    principal = 1000.0  # $SCOTTY tokens staked
    apy = 0.15          # 15% APY
    lock_period_days = 90
    lock_period_multiplier = 1.2  # 1.2x rewards for the lock period

    # Calculate rewards
    rewards = calculate_staking_rewards(principal, apy, lock_period_days, lock_period_multiplier)
    print(f"Staking Rewards: {rewards} $SCOTTY")
```
