"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aimigrateapp.pages.dev
Prompt: Generate code to calculate potential rewards for staking AIT tokens for 14, 28, and 56 days based on the APR provided.
Generated: DETERMINISTIC_79a20de681b7cfd3
Batch ID: 20250612_163627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def calculate_staking_rewards(amount: float, apr: float, staking_days: List[int]) -> Dict[int, float]:
    """
    Calculate potential rewards for staking tokens over specified periods based on APR.
    
    Parameters:
        amount (float): The amount of AIT tokens staked.
        apr (float): The Annual Percentage Rate (APR) as a percentage (e.g., 12.5 for 12.5% APR).
        staking_days (List[int]): List of staking periods in days (e.g., [14, 28, 56]).
    
    Returns:
        Dict[int, float]: A dictionary with staking days as keys and potential rewards as values.
    """
    try:
        if amount <= 0 or apr <= 0:
            raise ValueError("Amount and APR must be greater than zero.")
        
        if not all(isinstance(days, int) and days > 0 for days in staking_days):
            raise ValueError("Staking days must be a list of positive integers.")
        
        # Convert APR from percentage to decimal
        apr_decimal = apr / 100
        
        # Calculate daily rate based on APR
        daily_rate = apr_decimal / 365
        
        rewards = {}
        for days in staking_days:
            # Calculate rewards for each staking period
            reward = amount * daily_rate * days
            rewards[days] = reward
        
        return rewards

    except Exception as e:
        print(f"Error calculating staking rewards: {e}")
        return {}

# Example usage:
if __name__ == "__main__":
    # Input values
    staked_amount = 1000  # Amount of AIT tokens
    annual_apr = 12.5     # APR in percentage
    staking_periods = [14, 28, 56]  # Staking periods in days
    
    # Calculate rewards
    rewards = calculate_staking_rewards(staked_amount, annual_apr, staking_periods)
    
    # Output the results
    if rewards:
        print("Potential rewards for staking:")
        for days, reward in rewards.items():
            print(f"{days} days: {reward:.2f} AIT tokens")
```
