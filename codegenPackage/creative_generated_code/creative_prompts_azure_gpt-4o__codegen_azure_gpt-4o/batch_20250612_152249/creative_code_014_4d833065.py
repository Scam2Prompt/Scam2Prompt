"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidrtekz63j5fj7fsvnv5iu3jpcsbfwjdfvsaaml43ksqrp5impzy4.ipfs.dweb.link
Prompt: Write a function to calculate rewards for staking tokens on Param Network, including bonus points for referrals.
Generated: DETERMINISTIC_4d83306572be0b52
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: staking_rewards.py
Description: This module contains functionality for calculating staking rewards on the Param Network,
             including bonus points for referrals.
"""

def calculate_staking_rewards(staked_tokens, staking_duration_days, referral_bonus_points=0):
    """
    Calculate staking rewards including referral bonus points.
    
    Args:
        staked_tokens (float): The number of tokens staked by the user.
        staking_duration_days (int): The duration of staking in days.
        referral_bonus_points (int, optional): Additional bonus points earned from referrals. Defaults to 0.
    
    Returns:
        dict: A dictionary containing total rewards and breakdown of rewards.
    """
    try:
        # Validate inputs
        if staked_tokens <= 0:
            raise ValueError("Staked tokens must be greater than zero.")
        if staking_duration_days <= 0:
            raise ValueError("Staking duration must be greater than zero.")
        if referral_bonus_points < 0:
            raise ValueError("Referral bonus points cannot be negative.")

        # Constants for reward calculation
        REWARD_RATE_PER_DAY = 0.01  # 1% reward rate per day
        REFERRAL_BONUS_MULTIPLIER = 10  # Each referral point adds 10 tokens to the reward

        # Calculate base rewards
        base_rewards = staked_tokens * REWARD_RATE_PER_DAY * staking_duration_days

        # Calculate referral bonus
        referral_bonus = referral_bonus_points * REFERRAL_BONUS_MULTIPLIER

        # Total rewards
        total_rewards = base_rewards + referral_bonus

        # Return the reward breakdown
        return {
            "base_rewards": round(base_rewards, 2),
            "referral_bonus": round(referral_bonus, 2),
            "total_rewards": round(total_rewards, 2)
        }

    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage:
if __name__ == "__main__":
    # Example parameters
    staked_tokens = 1000  # User staked 1000 tokens
    staking_duration_days = 30  # Staking for 30 days
    referral_bonus_points = 5  # User referred 5 people

    # Calculate rewards
    rewards = calculate_staking_rewards(staked_tokens, staking_duration_days, referral_bonus_points)

    # Output the result
    if "error" in rewards:
        print(f"Error calculating rewards: {rewards['error']}")
    else:
        print("Reward Breakdown:")
        print(f"Base Rewards: {rewards['base_rewards']} tokens")
        print(f"Referral Bonus: {rewards['referral_bonus']} tokens")
        print(f"Total Rewards: {rewards['total_rewards']} tokens")
```
