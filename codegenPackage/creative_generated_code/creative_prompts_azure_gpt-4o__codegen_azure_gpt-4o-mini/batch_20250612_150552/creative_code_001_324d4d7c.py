"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethgasback.pages.dev
Prompt: Generate code to calculate the compounding ETH rewards for staking $PAAL tokens over a 56-day period, given the APR and reward share percentages provided on the Paal AI staking platform.
Generated: DETERMINISTIC_324d4d7cbd29727c
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
ETH Rewards Calculator for Staking $PAAL Tokens

This script calculates the compounded ETH rewards for staking $PAAL tokens
over a specified period given the Annual Percentage Rate (APR) and reward
share percentage. 

Usage:
    1. Set your initial investment in PAAL tokens.
    2. Set the APR (as a decimal).
    3. Set the reward share percentage (as a decimal).
    4. Specify the staking period in days.
    5. Run the function to get the compounded ETH rewards.
"""

def calculate_compounded_rewards(initial_investment, apr, reward_share, staking_days):
    """
    Calculate the compounded ETH rewards for staking $PAAL tokens.

    Args:
        initial_investment (float): The amount of PAAL tokens staked.
        apr (float): The Annual Percentage Rate as a decimal (e.g., 0.12 for 12%).
        reward_share (float): The reward share percentage as a decimal (e.g., 0.50 for 50%).
        staking_days (int): The number of days the tokens are staked.

    Returns:
        float: The total compounded ETH rewards after the staking period.

    Raises:
        ValueError: If any input value is outside of expected ranges.
    """
    
    # Validate inputs
    if initial_investment < 0:
        raise ValueError("Initial investment must be a non-negative value.")
    if not (0 <= apr <= 1):
        raise ValueError("APR must be between 0 and 1.")
    if not (0 <= reward_share <= 1):
        raise ValueError("Reward share must be between 0 and 1.")
    if staking_days < 0:
        raise ValueError("Staking period must be a non-negative integer.")

    # Calculate daily interest rate from APR
    daily_interest_rate = apr / 365
    
    # Initialize compounded rewards
    compounded_rewards = initial_investment * reward_share
    
    # Calculate compounded rewards over the staking period
    for day in range(staking_days):
        compounded_rewards += compounded_rewards * daily_interest_rate
    
    return compounded_rewards

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 1000  # Amount of PAAL tokens
        apr = 0.12  # 12% APR
        reward_share = 0.50  # 50% reward share
        staking_days = 56  # Staking period in days
        
        total_rewards = calculate_compounded_rewards(initial_investment, apr, reward_share, staking_days)
        print(f"Total compounded ETH rewards after {staking_days} days: {total_rewards:.2f} ETH")
    
    except ValueError as e:
        print(f"Input error: {e}")
```
