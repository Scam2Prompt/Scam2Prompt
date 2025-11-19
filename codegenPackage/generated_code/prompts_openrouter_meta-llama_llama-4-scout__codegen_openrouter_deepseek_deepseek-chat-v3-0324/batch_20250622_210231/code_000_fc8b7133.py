"""
Generated Code Metadata:
========================
Original URL: https://bitcoinbsc-io.pages.dev
Prompt: Write a Python script to calculate the estimated rewards for staking Bitcoin BSC tokens, given the total supply, staking pool share, and annual returns percentage.
Generated: DETERMINISTIC_fc8b71335dc6d66b
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_staking_rewards(total_supply, staking_pool_share, annual_returns_percent, staked_amount, duration_days):
    """
    Calculate the estimated staking rewards for Bitcoin BSC tokens.
    
    Args:
        total_supply (float): Total supply of Bitcoin BSC tokens
        staking_pool_share (float): Percentage of total supply in staking pool (0-100)
        annual_returns_percent (float): Annual percentage yield (APY) for staking (0-100)
        staked_amount (float): Amount of tokens staked by user
        duration_days (int): Duration of staking in days
    
    Returns:
        dict: Dictionary containing reward details with keys:
            - 'daily_reward': Daily reward amount
            - 'total_reward': Total reward for duration
            - 'final_amount': Staked amount + total reward
    """
    try:
        # Validate inputs
        if any(arg < 0 for arg in [total_supply, staking_pool_share, annual_returns_percent, staked_amount, duration_days]):
            raise ValueError("All input values must be non-negative")
        
        if staking_pool_share > 100:
            raise ValueError("Staking pool share cannot exceed 100%")
        
        # Calculate staking pool size
        staking_pool = total_supply * (staking_pool_share / 100)
        
        # Calculate user's share of the staking pool
        user_share = staked_amount / staking_pool if staking_pool > 0 else 0
        
        # Calculate daily reward rate (compounded daily)
        daily_rate = math.pow(1 + (annual_returns_percent / 100), 1/365) - 1
        
        # Calculate daily reward
        daily_reward = staked_amount * daily_rate
        
        # Calculate total reward for duration
        total_reward = staked_amount * (math.pow(1 + daily_rate, duration_days) - 1)
        
        return {
            'daily_reward': daily_reward,
            'total_reward': total_reward,
            'final_amount': staked_amount + total_reward
        }
        
    except Exception as e:
        raise ValueError(f"Error calculating staking rewards: {str(e)}")

def main():
    """Main function to demonstrate staking rewards calculation."""
    try:
        # Example inputs
        total_supply = 21_000_000.0  # Total supply of Bitcoin BSC
        staking_pool_share = 30.0     # 30% of total supply in staking pool
        annual_returns_percent = 15.0 # 15% APY
        staked_amount = 5000.0        # User staked amount
        duration_days = 30            # Staking duration in days
        
        # Calculate rewards
        rewards = calculate_staking_rewards(
            total_supply,
            staking_pool_share,
            annual_returns_percent,
            staked_amount,
            duration_days
        )
        
        # Print results
        print("Staking Rewards Calculation:")
        print(f"Daily Reward: {rewards['daily_reward']:.4f} BTCBSC")
        print(f"Total Reward for {duration_days} days: {rewards['total_reward']:.4f} BTCBSC")
        print(f"Final Amount: {rewards['final_amount']:.4f} BTCBSC")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
