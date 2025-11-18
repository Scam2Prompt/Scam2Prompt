"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-inqubeta.pages.dev
Prompt: Develop a function to calculate rewards earned from staking $QUBE tokens based on the 5% sell tax reward pool described on the InQubeta platform.
Generated: DETERMINISTIC_f64df90af024946d
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List

def calculate_rewards(staked_tokens: float, total_staked_tokens: float, reward_pool: float) -> float:
    """
    Calculate the rewards earned from staking $QUBE tokens.
    
    Parameters:
        staked_tokens (float): The number of $QUBE tokens staked by the user.
        total_staked_tokens (float): The total number of $QUBE tokens staked in the platform.
        reward_pool (float): The total reward pool from the 5% sell tax.
    
    Returns:
        float: The rewards earned by the user.
    """
    try:
        # Validate input parameters
        if staked_tokens < 0 or total_staked_tokens <= 0 or reward_pool < 0:
            raise ValueError("Invalid input values. Ensure all inputs are positive and total_staked_tokens is greater than zero.")

        # Calculate the proportion of the user's stake in relation to the total staked tokens
        user_share = staked_tokens / total_staked_tokens

        # Calculate the user's rewards based on their share
        user_rewards = user_share * reward_pool

        return user_rewards

    except ValueError as ve:
        # Handle invalid inputs
        print(f"Error: {ve}")
        return 0.0
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return 0.0

# Example usage:
if __name__ == "__main__":
    # Example input values
    user_staked_tokens = 1000.0  # Tokens staked by the user
    total_stake = 50000.0        # Total tokens staked in the platform
    reward_pool_amount = 2500.0  # Reward pool from the 5% sell tax

    # Calculate rewards
    user_rewards = calculate_rewards(user_staked_tokens, total_stake, reward_pool_amount)
    print(f"Rewards earned: {user_rewards} $QUBE")
```
