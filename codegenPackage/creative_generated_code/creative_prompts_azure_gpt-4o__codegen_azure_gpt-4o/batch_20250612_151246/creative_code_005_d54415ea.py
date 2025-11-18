"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olliivveemmaaiinn12893891bndjdbiqw.pages.dev
Prompt: Write a script to calculate staking rewards dynamically based on deposit amounts and referral bonuses, incorporating features like "Olive Boost."
Generated: DETERMINISTIC_d54415ea6511bdc6
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_staking_rewards(deposit_amount, referral_bonus=0, olive_boost=False):
    """
    Calculate staking rewards dynamically based on deposit, referral bonus, and Olive Boost.

    Parameters:
    deposit_amount (float): The amount deposited for staking.
    referral_bonus (float): The bonus for referrals (default is 0).
    olive_boost (bool): Whether Olive Boost is applied (default is False).

    Returns:
    float: The total staking reward.
    """
    try:
        # Validate input
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        if referral_bonus < 0:
            raise ValueError("Referral bonus cannot be negative.")

        # Base reward rate (e.g., 5% annual yield)
        base_reward_rate = 0.05

        # Olive Boost multiplier (e.g., increases yield by 20%)
        olive_boost_multiplier = 1.2 if olive_boost else 1.0

        # Calculate base rewards
        base_rewards = deposit_amount * base_reward_rate

        # Apply Olive Boost
        adjusted_rewards = base_rewards * olive_boost_multiplier

        # Add referral bonus
        total_rewards = adjusted_rewards + referral_bonus

        return total_rewards

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    try:
        # Get user input
        deposit = float(input("Enter your deposit amount: "))
        referral = float(input("Enter the referral bonus amount (optional, default is 0): ") or 0)
        olive_boost_input = input("Enable Olive Boost? (yes/no, default is no): ").strip().lower()
        olive_boost_flag = olive_boost_input in ['yes', 'y']

        # Calculate rewards
        rewards = calculate_staking_rewards(deposit, referral, olive_boost_flag)
        if rewards is not None:
            print(f"Your total staking rewards: {rewards:.2f}")
        else:
            print("Failed to calculate rewards due to an error.")

    except ValueError:
        print("Invalid input. Please enter numeric values for deposit and referral bonus.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
