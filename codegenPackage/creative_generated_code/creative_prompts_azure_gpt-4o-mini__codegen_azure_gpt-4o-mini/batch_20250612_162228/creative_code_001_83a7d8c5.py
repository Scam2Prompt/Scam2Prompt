"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elephantrewards.pages.dev
Prompt: Write a function to calculate the daily rewards from purchasing TRUNK at the Farmers' Depot, given a specific amount in BUSD.
Generated: DETERMINISTIC_83a7d8c5f48d6428
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_daily_rewards(busd_amount: float, reward_rate: float = 0.05) -> float:
    """
    Calculate the daily rewards from purchasing TRUNK at the Farmers' Depot.

    Parameters:
    busd_amount (float): The amount in BUSD that is used to purchase TRUNK.
    reward_rate (float): The daily reward rate, default is 5% (0.05).

    Returns:
    float: The daily rewards generated from the BUSD amount.

    Raises:
    ValueError: If busd_amount is negative or if reward_rate is outside the range [0, 1].

    Example:
    >>> calculate_daily_rewards(100)
    5.0
    """
    
    # Validate input parameters
    if busd_amount < 0:
        raise ValueError("BUSD amount must be non-negative.")
    if not (0 <= reward_rate <= 1):
        raise ValueError("Reward rate must be between 0 and 1 inclusive.")

    # Calculate daily rewards
    daily_rewards = busd_amount * reward_rate

    return daily_rewards

# Example usage:
if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount in BUSD: "))
        rewards = calculate_daily_rewards(amount)
        print(f"Daily rewards from purchasing TRUNK: {rewards:.2f} BUSD")
    except ValueError as e:
        print(f"Error: {e}")
```
