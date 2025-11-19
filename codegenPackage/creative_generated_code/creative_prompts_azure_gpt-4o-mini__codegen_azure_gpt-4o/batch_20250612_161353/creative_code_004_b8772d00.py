"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vlaunch-io.web.app
Prompt: Generate a script that calculates potential VPAD rewards based on different lockup durations for staking on VLaunch.
Generated: DETERMINISTIC_b8772d0097dd9405
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_vpad_rewards(stake_amount, lockup_days):
    """
    Calculate VPAD rewards based on the staking amount and lockup duration.
    Rewards are calculated based on the following example multipliers:
    - Lockup Days <= 30: 5% reward
    - Lockup Days <= 60: 12% reward
    - Lockup Days <= 90: 20% reward
    - Lockup Days > 90: 30% reward

    Parameters:
        stake_amount (float): Amount of VPAD staked.
        lockup_days (int): Number of days the stake is locked up.

    Returns:
        float: Calculated rewards in VPAD tokens.
    """
    if stake_amount <= 0:
        raise ValueError("Stake amount must be greater than 0.")
    if lockup_days <= 0:
        raise ValueError("Lockup days must be greater than 0.")

    # Define reward multipliers
    if lockup_days <= 30:
        reward_percentage = 0.05  # 5%
    elif lockup_days <= 60:
        reward_percentage = 0.12  # 12%
    elif lockup_days <= 90:
        reward_percentage = 0.20  # 20%
    else:
        reward_percentage = 0.30  # 30%

    # Calculate rewards
    rewards = stake_amount * reward_percentage
    return rewards


def main():
    """
    Main function to interact with the user, take inputs, and calculate rewards.
    """
    try:
        print("Welcome to the VPAD Rewards Calculator!")
        stake_amount = float(input("Enter the amount of VPAD tokens staked: "))
        lockup_days = int(input("Enter the number of lockup days: "))

        # Calculate rewards
        rewards = calculate_vpad_rewards(stake_amount, lockup_days)

        # Output the result
        print(f"Based on a stake of {stake_amount} VPAD for {lockup_days} days, "
              f"your potential rewards are: {rewards:.2f} VPAD.")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Ensure the script runs only when executed directly
    main()
```
