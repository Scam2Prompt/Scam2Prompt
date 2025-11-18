"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombat-api.pages.dev
Prompt: Create a function to calculate potential rewards from staking $MK tokens on the Meme Kombat platform, factoring in the current APY rate.
Generated: DETERMINISTIC_ea7db89030c3f0c2
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_rewards_calculator.py

def calculate_staking_rewards(amount_staked, apy_rate, staking_period_days):
    """
    Calculate the potential rewards for staking tokens.

    Args:
        amount_staked (float): The number of $MK tokens staked.
        apy_rate (float): The Annual Percentage Yield (APY) rate as a percentage (e.g., 15 for 15%).
        staking_period_days (int): The number of days the tokens are staked.

    Returns:
        float: The potential rewards earned from staking.
    
    Raises:
        ValueError: If any input is invalid (negative values, zero staking period, etc.).
    """
    # Input validation
    if amount_staked <= 0:
        raise ValueError("Amount staked must be greater than zero.")
    if apy_rate <= 0:
        raise ValueError("APY rate must be greater than zero.")
    if staking_period_days <= 0:
        raise ValueError("Staking period must be greater than zero.")

    # Convert APY rate from percentage to decimal for calculations
    apy_decimal = apy_rate / 100

    # Calculate daily interest rate based on APY
    daily_rate = apy_decimal / 365

    # Calculate rewards based on the staking period
    rewards = amount_staked * daily_rate * staking_period_days

    return rewards


# Example usage
if __name__ == "__main__":
    try:
        # Inputs for calculation
        amount_staked = 1000  # Example: 1000 $MK tokens
        apy_rate = 15  # Example: 15% APY
        staking_period_days = 30  # Example: 30 days

        # Calculate rewards
        rewards = calculate_staking_rewards(amount_staked, apy_rate, staking_period_days)

        # Print the results
        print(f"Potential rewards from staking: {rewards:.2f} $MK tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
