"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20-claimyourdoge20.pages.dev
Prompt: Create a function that calculates the percentage of staking rewards for a user based on their contribution to the DOGE20 staking pool.
Generated: DETERMINISTIC_6e1be7607b3fe074
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_rewards(user_contribution, total_pool_contribution, total_rewards):
    """
    Calculate the percentage of staking rewards for a user based on their contribution to the staking pool.

    Parameters:
        user_contribution (float): The amount contributed by the user to the staking pool.
        total_pool_contribution (float): The total amount of contributions in the staking pool.
        total_rewards (float): The total rewards distributed in the staking pool.

    Returns:
        float: The rewards allocated to the user, based on their contribution to the pool.
    
    Raises:
        ValueError: If any input is negative or if total_pool_contribution is zero.
    """
    # Input validation
    if user_contribution < 0 or total_pool_contribution <= 0 or total_rewards < 0:
        raise ValueError("Invalid input: contributions and rewards must be non-negative, and total_pool_contribution must be greater than zero.")
    
    # Calculate the user's percentage contribution to the pool
    user_percentage = user_contribution / total_pool_contribution
    
    # Calculate the user's reward based on their percentage contribution
    user_rewards = user_percentage * total_rewards
    
    return user_rewards

# Example usage:
try:
    user_rewards = calculate_staking_rewards(user_contribution=500, total_pool_contribution=10000, total_rewards=1000)
    print(f"User's staking rewards: {user_rewards:.2f} DOGE")
except ValueError as e:
    print(f"Error: {e}")
```
