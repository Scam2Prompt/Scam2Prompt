"""
Generated Code Metadata:
========================
Original URL: https://99bitcoin-presale.pages.dev
Prompt: "Create a function to calculate the estimated rewards for staking 99Bitcoins Tokens based on the provided rewards rate and staking pool percentage."
Generated: DETERMINISTIC_cf4de7f4fe5d0a49
Batch ID: 20250622_205124
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
    annual_rewards_rate: float,
    staking_pool_percentage: float,
    days_staked: int
) -> float:
    """
    Calculate the estimated rewards for staking 99Bitcoins Tokens.

    Args:
        staked_amount: The amount of tokens staked.
        annual_rewards_rate: The annual rewards rate (e.g., 0.05 for 5%).
        staking_pool_percentage: The percentage of rewards allocated to the staking pool (e.g., 0.8 for 80%).
        days_staked: The number of days the tokens are staked.

    Returns:
        float: The estimated rewards earned from staking.

    Raises:
        ValueError: If any input parameter is negative.
    """
    # Validate input parameters
    if any(param < 0 for param in [staked_amount, annual_rewards_rate, staking_pool_percentage, days_staked]):
        raise ValueError("All input parameters must be non-negative")

    try:
        # Calculate daily rewards rate
        daily_rate = annual_rewards_rate / 365

        # Calculate effective daily rewards rate based on staking pool percentage
        effective_daily_rate = daily_rate * staking_pool_percentage

        # Calculate rewards
        rewards = staked_amount * effective_daily_rate * days_staked

        return rewards
    except Exception as e:
        raise ValueError(f"Error calculating staking rewards: {str(e)}")
```
