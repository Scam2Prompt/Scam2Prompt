"""
Generated Code Metadata:
========================
Original URL: https://paal-ai.pages.dev
Prompt: Create a function to calculate the total ETH rewarded for staking $PAAL tokens, given a pool size and rewards share percentage.
Generated: DETERMINISTIC_9d71d3b6b96c7def
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_staking_rewards(
    staked_amount: float,
    total_pool_size: float,
    rewards_percentage: float,
    eth_price: float
) -> float:
    """
    Calculate the total ETH rewarded for staking PAAL tokens.

    Args:
        staked_amount (float): Amount of PAAL tokens staked by the user
        total_pool_size (float): Total amount of PAAL tokens in the staking pool
        rewards_percentage (float): Percentage of total rewards allocated to the pool (0-100)
        eth_price (float): Current price of ETH in USD

    Returns:
        float: Total ETH rewards earned

    Raises:
        ValueError: If any input parameter is invalid (negative values, zero pool size, etc.)
    """
    # Validate input parameters
    if staked_amount <= 0:
        raise ValueError("Staked amount must be positive")
    if total_pool_size <= 0:
        raise ValueError("Total pool size must be positive")
    if rewards_percentage < 0 or rewards_percentage > 100:
        raise ValueError("Rewards percentage must be between 0 and 100")
    if eth_price <= 0:
        raise ValueError("ETH price must be positive")

    # Calculate user's share of the pool
    user_share = staked_amount / total_pool_size

    # Calculate total rewards in ETH (assuming rewards_percentage is of total ETH rewards)
    total_eth_rewards = rewards_percentage / 100

    # Calculate user's ETH rewards
    user_eth_rewards = user_share * total_eth_rewards

    return user_eth_rewards
```
