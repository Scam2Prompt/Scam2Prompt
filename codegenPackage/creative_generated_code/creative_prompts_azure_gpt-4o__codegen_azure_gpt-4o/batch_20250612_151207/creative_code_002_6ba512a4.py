"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Generate code to calculate and display token staking rewards for a platform with fixed token supply and a profit-sharing model, as described in Blockchain Bets.
Generated: DETERMINISTIC_6ba512a42f846ab6
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Token Staking Rewards Calculation Script

This script calculates staking rewards for a platform with a fixed token
supply and a profit-sharing model.

Key Assumptions:
- Fixed token supply (`TOTAL_SUPPLY`)
- Profit-sharing from platform profits (`TOTAL_PROFITS`)
- Staking rewards are distributed proportionately based on each user's
  staked tokens relative to the total staked supply.
- Includes error handling for invalid inputs.
"""

# Import necessary libraries
from typing import Dict, Union

# Constants
TOTAL_SUPPLY = 1_000_000  # Total token supply in the platform
TOTAL_PROFITS = 50_000  # Total profits to be distributed as rewards (in tokens)

def calculate_rewards(
    staked_tokens: Dict[str, Union[int, float]], total_staked: int
) -> Dict[str, float]:
    """
    Calculate staking rewards for users based on their staked tokens.

    Args:
        staked_tokens (Dict[str, Union[int, float]]): Dictionary of user IDs and their staked token amounts.
        total_staked (int): Total number of tokens staked across all users.

    Returns:
        Dict[str, float]: Dictionary of user IDs and their calculated rewards.
    """
    # Validate inputs
    if not staked_tokens:
        raise ValueError("The `staked_tokens` dictionary cannot be empty.")
    if total_staked <= 0:
        raise ValueError("`total_staked` must be greater than zero.")
    if sum(staked_tokens.values()) != total_staked:
        raise ValueError("The sum of all staked tokens must equal `total_staked`.")

    # Calculate rewards proportionately
    rewards = {}
    for user_id, user_staked in staked_tokens.items():
        # Error check for invalid staking
        if user_staked < 0:
            raise ValueError(f"Invalid staked amount for user {user_id}: {user_staked}")
        # Calculate reward
        rewards[user_id] = (user_staked / total_staked) * TOTAL_PROFITS

    return rewards


def main():
    """
    Main function to execute staking reward calculations and display the results.
    """
    # Example data: user token staking information
    staked_tokens = {
        "user_1": 50_000,  # User 1 staked 50,000 tokens
        "user_2": 30_000,  # User 2 staked 30,000 tokens
        "user_3": 20_000,  # User 3 staked 20,000 tokens
    }

    # Calculate total staked tokens
    total_staked = sum(staked_tokens.values())

    # Validate fixed token supply is not exceeded
    if total_staked > TOTAL_SUPPLY:
        raise ValueError("Total staked tokens cannot exceed the fixed token supply.")

    try:
        # Calculate staking rewards
        rewards = calculate_rewards(staked_tokens, total_staked)

        # Display the results
        print("Staking Rewards Distribution:")
        for user_id, reward in rewards.items():
            print(f"User: {user_id}, Reward: {reward:.2f} tokens")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the main function
    main()
```
