"""
Generated Code Metadata:
========================
Original URL: https://scottyweb.pages.dev
Prompt: Write a Python script to calculate staking rewards for the Scotty AI token, using the dynamic reward rate of 82.5 $SCOTTY per ETH block and an annual return percentage of 24%. Include calculations for monthly and daily rewards.
Generated: DETERMINISTIC_4fdecb536537c752
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_staking_rewards(staked_amount, days_staked, blocks_per_day=7200, reward_rate=82.5, annual_return=0.24):
    """
    Calculate staking rewards for Scotty AI token based on dynamic reward rate and annual return.
    
    Args:
        staked_amount (float): Amount of SCOTTY tokens staked
        days_staked (int): Number of days tokens are staked
        blocks_per_day (int, optional): ETH blocks per day. Defaults to 7200.
        reward_rate (float, optional): SCOTTY reward per ETH block. Defaults to 82.5.
        annual_return (float, optional): Annual return percentage. Defaults to 0.24 (24%).
    
    Returns:
        dict: Dictionary containing daily, monthly, and total rewards
    """
    try:
        if staked_amount <= 0 or days_staked <= 0:
            raise ValueError("Staked amount and days staked must be positive values")
        
        # Calculate daily rewards based on block rewards
        daily_block_rewards = blocks_per_day * reward_rate
        
        # Calculate daily rewards based on annual return
        daily_percentage_rewards = staked_amount * (annual_return / 365)
        
        # Use the more conservative estimate (minimum of both methods)
        daily_rewards = min(daily_block_rewards, daily_percentage_rewards)
        
        monthly_rewards = daily_rewards * 30
        total_rewards = daily_rewards * days_staked
        
        return {
            'daily_rewards': daily_rewards,
            'monthly_rewards': monthly_rewards,
            'total_rewards': total_rewards,
            'annual_percentage': annual_return * 100
        }
        
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    staked_amount = 10000  # Example: 10,000 SCOTTY tokens staked
    days_staked = 30       # Example: 30 days staking period
    
    rewards = calculate_staking_rewards(staked_amount, days_staked)
    
    if rewards:
        print(f"Staking Rewards for {staked_amount} SCOTTY over {days_staked} days:")
        print(f"Daily Rewards: {rewards['daily_rewards']:.2f} SCOTTY")
        print(f"Monthly Rewards: {rewards['monthly_rewards']:.2f} SCOTTY")
        print(f"Total Rewards: {rewards['total_rewards']:.2f} SCOTTY")
        print(f"Annual Percentage: {rewards['annual_percentage']:.2f}%")
```
