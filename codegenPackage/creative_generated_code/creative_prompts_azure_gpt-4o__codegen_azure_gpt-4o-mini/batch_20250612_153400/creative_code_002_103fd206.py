"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-live.pages.dev
Prompt: Create a function in Python to calculate daily and monthly staking rewards for DOGE20 tokens based on the provided annual percentage returns and the user's percentage of the staking pool.
Generated: DETERMINISTIC_103fd2062520ca3f
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_rewards(annual_percentage_rate: float, user_stake_percentage: float, total_staked: float) -> dict:
    """
    Calculate daily and monthly staking rewards for DOGE20 tokens based on the annual percentage returns
    and the user's percentage of the staking pool.

    Parameters:
        annual_percentage_rate (float): The annual percentage rate (APR) for staking rewards (as a percentage).
        user_stake_percentage (float): The percentage of the total staking pool that the user owns (as a percentage).
        total_staked (float): The total amount of tokens staked in the pool.

    Returns:
        dict: A dictionary containing daily and monthly rewards in DOGE20 tokens.
    """
    
    # Validate inputs
    if annual_percentage_rate < 0 or user_stake_percentage < 0 or total_staked <= 0:
        raise ValueError("Annual percentage rate, user stake percentage, and total staked must be positive values.")
    
    if user_stake_percentage > 100:
        raise ValueError("User stake percentage cannot exceed 100.")

    # Calculate the user's stake amount in the total staked pool
    user_stake_amount = (user_stake_percentage / 100) * total_staked

    # Convert annual percentage rate to a decimal
    apr_decimal = annual_percentage_rate / 100

    # Calculate daily and monthly rewards
    daily_reward = user_stake_amount * (apr_decimal / 365)
    monthly_reward = user_stake_amount * (apr_decimal / 12)

    # Return the rewards as a dictionary
    return {
        "daily_reward": daily_reward,
        "monthly_reward": monthly_reward
    }

# Example usage
if __name__ == "__main__":
    try:
        rewards = calculate_staking_rewards(5.0, 10.0, 10000)
        print(f"Daily Reward: {rewards['daily_reward']:.4f} DOGE20")
        print(f"Monthly Reward: {rewards['monthly_reward']:.4f} DOGE20")
    except ValueError as e:
        print(f"Error: {e}")
```
