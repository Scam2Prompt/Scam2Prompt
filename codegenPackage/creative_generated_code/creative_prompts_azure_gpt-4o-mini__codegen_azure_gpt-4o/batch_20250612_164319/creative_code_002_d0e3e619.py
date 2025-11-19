"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presale.pages.dev
Prompt: Generate a function to calculate the staking rewards for the 99Bitcoins token based on the dynamic rate provided.
Generated: DETERMINISTIC_d0e3e619b86fcdb5
Batch ID: 20250612_164319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_rewards.py

def calculate_staking_rewards(principal: float, rate: float, duration_days: int) -> float:
    """
    Calculate staking rewards for the 99Bitcoins token based on a dynamic rate and duration.

    Args:
        principal (float): The amount of tokens staked (must be greater than zero).
        rate (float): The daily staking reward rate as a percentage (e.g., 0.5 for 0.5% daily).
        duration_days (int): The number of days the tokens are staked for.

    Returns:
        float: The total staking rewards accumulated over the given duration.
    
    Raises:
        ValueError: If principal, rate, or duration_days are invalid (negative values or zero).
    """
    # Input validation
    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if rate <= 0:
        raise ValueError("Rate must be greater than zero.")
    if duration_days <= 0:
        raise ValueError("Duration must be greater than zero.")
    
    # Calculate rewards using simple interest formula
    # Staking reward = Principal * (Rate / 100) * Duration (in days)
    staking_rewards = principal * (rate / 100) * duration_days
    
    return staking_rewards


# Example of how to use the function:
if __name__ == "__main__":
    try:
        # Example values
        principal_amount = 1000.0  # Tokens staked
        daily_rate = 0.5           # Daily rate in percentage (e.g., 0.5%)
        staking_duration = 30      # Duration in days

        rewards = calculate_staking_rewards(principal_amount, daily_rate, staking_duration)
        print(f"Staking Rewards: {rewards:.2f} tokens")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
