"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard0x0.com
Prompt: Write a function that calculates the estimated APY based on the total distributed and claimed rewards from the 0x0 Dashboard.
Generated: DETERMINISTIC_5951ca6d4c8f2d2b
Batch ID: 20250612_163646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_apy(total_distributed_rewards, total_claimed_rewards, staking_period_days):
    """
    Calculate the Annual Percentage Yield (APY) based on the rewards distributed and claimed.

    Args:
        total_distributed_rewards (float): Total amount of rewards distributed over the staking period.
        total_claimed_rewards (float): Total amount of rewards claimed by users.
        staking_period_days (int): The number of days in the staking period.

    Returns:
        float: The estimated APY as a percentage.
        
    Raises:
        ValueError: If total_distributed_rewards, total_claimed_rewards, or staking_period_days are invalid.
    """
    # Validate inputs
    if total_distributed_rewards <= 0:
        raise ValueError("Total distributed rewards must be greater than zero.")
    if total_claimed_rewards < 0:
        raise ValueError("Total claimed rewards cannot be negative.")
    if staking_period_days <= 0:
        raise ValueError("Staking period days must be greater than zero.")

    # Calculate the reward rate (claimed rewards as a fraction of distributed rewards)
    try:
        reward_rate = total_claimed_rewards / total_distributed_rewards
    except ZeroDivisionError:
        raise ValueError("Total distributed rewards cannot be zero.")

    # Convert staking period days to years
    staking_period_years = staking_period_days / 365.0

    # Calculate APY using the reward rate and staking period in years
    estimated_apy = (reward_rate / staking_period_years) * 100  # Convert to percentage

    return round(estimated_apy, 2)


# Example usage:
if __name__ == "__main__":
    try:
        # Example values
        distributed_rewards = 10000.0  # Total distributed rewards
        claimed_rewards = 2500.0       # Total claimed rewards
        staking_days = 30             # Staking period in days
        
        apy = calculate_apy(distributed_rewards, claimed_rewards, staking_days)
        print(f"Estimated APY: {apy}%")
    except ValueError as e:
        print(f"Error calculating APY: {e}")
```
