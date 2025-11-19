"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Write a code snippet that demonstrates how to stake $EMT tokens in the EarthMeta ecosystem and calculate potential rewards based on the staking calculator.
Generated: DETERMINISTIC_483b16562ba16519
Batch ID: 20250612_155926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from decimal import Decimal

# Constants
TOKEN_NAME = "EMT"
ANNUAL_REWARD_RATE = Decimal('0.12')  # Annual reward rate for staking (12%)
DAYS_IN_YEAR = 365

# Function for staking tokens
def stake_tokens(user_balance, stake_amount):
    """
    Function to stake $EMT tokens in the EarthMeta ecosystem.
    
    Parameters:
        user_balance (Decimal): The user's current balance of $EMT tokens.
        stake_amount (Decimal): The amount of $EMT tokens the user wants to stake.
    
    Returns:
        dict: A dictionary containing updated balance and staked amount.
    """
    if stake_amount <= 0:
        raise ValueError("Stake amount must be greater than 0.")
    if stake_amount > user_balance:
        raise ValueError("Insufficient balance to stake the specified amount.")
    
    user_balance -= stake_amount
    staked_amount = stake_amount
    return {
        "updated_balance": user_balance,
        "staked_amount": staked_amount
    }

# Function to calculate potential rewards
def calculate_rewards(staked_amount, staking_days):
    """
    Function to calculate potential rewards based on the staking calculator.
    
    Parameters:
        staked_amount (Decimal): The amount of $EMT tokens staked.
        staking_days (int): The number of days the tokens are staked for.
    
    Returns:
        Decimal: The calculated reward amount.
    """
    if staking_days <= 0:
        raise ValueError("Staking days must be greater than 0.")
    
    daily_reward_rate = ANNUAL_REWARD_RATE / DAYS_IN_YEAR
    reward = staked_amount * daily_reward_rate * Decimal(staking_days)
    return reward

# Example usage
try:
    # User's initial balance
    user_balance = Decimal('1000')  # User has 1000 EMT tokens
    
    # Amount to stake
    stake_amount = Decimal('500')  # User wants to stake 500 EMT tokens
    
    # Stake tokens
    stake_result = stake_tokens(user_balance, stake_amount)
    print(f"Updated Balance: {stake_result['updated_balance']} {TOKEN_NAME}")
    print(f"Staked Amount: {stake_result['staked_amount']} {TOKEN_NAME}")
    
    # Calculate potential rewards after staking for 90 days
    staking_days = 90
    rewards = calculate_rewards(stake_result['staked_amount'], staking_days)
    print(f"Potential Rewards after {staking_days} days: {rewards:.2f} {TOKEN_NAME}")
    
except ValueError as e:
    # Handle invalid input errors
    print(f"Error: {e}")
except Exception as e:
    # Handle unexpected errors
    print(f"An unexpected error occurred: {e}")
```
