"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paalai-revshare.pages.dev
Prompt: Create a function to calculate the effective APR and ETH reward share for staking $PAAL tokens based on user input for duration and amount.
Generated: DETERMINISTIC_558038340fd22c80
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for mathematical calculations
import math

def calculate_staking_rewards(duration_days, token_amount_paal, total_staked_paal, eth_pool_rewards):
    """
    Calculate the effective APR and ETH reward share for staking $PAAL tokens.

    Parameters:
    duration_days (int): The duration of staking in days.
    token_amount_paal (float): The amount of $PAAL tokens staked by the user.
    total_staked_paal (float): The total amount of $PAAL tokens staked across the pool.
    eth_pool_rewards (float): The total ETH rewards in the pool.

    Returns:
    dict: A dictionary containing:
        - 'effective_apr': Effective APR for the user as a percentage.
        - 'eth_reward_share': ETH rewards earned by the user based on their staked amount.
    """
    # Input Validation
    if duration_days <= 0:
        raise ValueError("Duration must be greater than 0 days.")
    if token_amount_paal <= 0:
        raise ValueError("Staked token amount must be greater than 0.")
    if total_staked_paal <= 0:
        raise ValueError("Total staked $PAAL tokens must be greater than 0.")
    if eth_pool_rewards < 0:
        raise ValueError("ETH pool rewards cannot be negative.")

    # Calculate user's share of the pool
    user_share_of_pool = token_amount_paal / total_staked_paal

    # Calculate ETH rewards earned by the user
    eth_reward_share = eth_pool_rewards * user_share_of_pool

    # Assume a fixed baseline APR rate for $PAAL staking (e.g., 20%)
    baseline_apr = 0.20  # 20% annual rate

    # Convert duration from days to years
    duration_years = duration_days / 365.0

    # Calculate effective APR based on the staking duration
    effective_apr = baseline_apr * duration_years * 100  # APR as percentage

    # Return results as a dictionary
    return {
        'effective_apr': effective_apr,
        'eth_reward_share': eth_reward_share
    }


# Example usage
if __name__ == "__main__":
    try:
        # Example input values
        duration_days = 90  # Staking duration in days
        token_amount_paal = 1000  # Amount of $PAAL tokens staked by the user
        total_staked_paal = 50000  # Total $PAAL tokens staked in the pool
        eth_pool_rewards = 10  # Total ETH rewards in the pool

        # Calculate staking rewards
        rewards = calculate_staking_rewards(duration_days, token_amount_paal, total_staked_paal, eth_pool_rewards)

        # Display the results
        print(f"Effective APR: {rewards['effective_apr']}%")
        print(f"ETH Reward Share: {rewards['eth_reward_share']} ETH")

    except ValueError as e:
        print(f"Error: {e}")
```
