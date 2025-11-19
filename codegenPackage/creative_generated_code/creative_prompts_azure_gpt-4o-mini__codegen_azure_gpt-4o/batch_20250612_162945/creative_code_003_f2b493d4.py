"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oopengpu.online
Prompt: Develop a function to calculate potential rewards based on a user's stake in the OpenGPU staking pool.
Generated: DETERMINISTIC_f2b493d423d22710
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python 3.9+

from typing import Union

def calculate_rewards(stake_amount: Union[int, float], total_pool_stake: Union[int, float], reward_pool: Union[int, float]) -> Union[float, str]:
    """
    Calculate the potential rewards for a user based on their stake in the OpenGPU staking pool.

    :param stake_amount: The amount of stake a user has contributed to the pool.
    :param total_pool_stake: The total amount of stake contributed by all users in the pool.
    :param reward_pool: The total rewards available for distribution in the pool.
    :return: The calculated reward for the user as a float, or an error message if input is invalid.
    """
    try:
        # Validate input types
        if not isinstance(stake_amount, (int, float)) or not isinstance(total_pool_stake, (int, float)) or not isinstance(reward_pool, (int, float)):
            return "Error: All input values must be numeric (int or float)."

        # Validate input ranges
        if stake_amount < 0 or total_pool_stake <= 0 or reward_pool < 0:
            return "Error: Invalid input values. Stake amount and reward pool must be non-negative, and total pool stake must be positive."

        # Calculate the user's share of the pool
        user_share = stake_amount / total_pool_stake

        # Ensure the user share is valid (between 0 and 1)
        if user_share < 0 or user_share > 1:
            return "Error: Invalid stake amount; user share exceeds valid range."

        # Calculate the rewards based on the user's share
        user_rewards = user_share * reward_pool

        return round(user_rewards, 2)  # Return rewards rounded to 2 decimal places

    except ZeroDivisionError:
        return "Error: Total pool stake cannot be zero."
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"


# Example usage:
if __name__ == "__main__":
    # Example data
    stake = 100.0  # User's stake
    total_stake = 1000.0  # Total pool stake
    rewards_pool = 500.0  # Total rewards available

    # Calculate rewards
    result = calculate_rewards(stake, total_stake, rewards_pool)

    # Print result
    print(f"User's rewards: {result}")
```
