"""
Generated Code Metadata:
========================
Original URL: https://ststoned.pages.dev
Prompt: Generate a function that calculates the potential rewards for locking LP tokens with STONE based on a given APY of 2.93%.
Generated: DETERMINISTIC_5c7cdc67e9e0e91a
Batch ID: 20250612_163443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Union

def calculate_rewards(lp_tokens: Union[int, float], days_locked: int, apy: float = 2.93) -> float:
    """
    Calculate the potential rewards for locking LP tokens with STONE based on a given APY.

    Args:
        lp_tokens (Union[int, float]): The number of LP tokens locked.
        days_locked (int): The number of days the tokens are locked.
        apy (float): The annual percentage yield (APY) in percentage. Default is 2.93%.

    Returns:
        float: The potential rewards earned.
    """
    try:
        # Validate inputs
        if lp_tokens <= 0:
            raise ValueError("LP tokens must be greater than zero.")
        if days_locked <= 0:
            raise ValueError("Days locked must be greater than zero.")
        if apy <= 0:
            raise ValueError("APY must be greater than zero.")

        # Convert APY from percentage to decimal
        apy_decimal = apy / 100

        # Calculate daily yield rate
        daily_yield_rate = apy_decimal / 365

        # Calculate rewards
        rewards = lp_tokens * daily_yield_rate * days_locked

        return rewards

    except ValueError as e:
        # Handle invalid input errors
        print(f"Input Error: {e}")
        return 0.0
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return 0.0

# Example usage:
# Calculate rewards for locking 1000 LP tokens for 30 days with the default APY of 2.93%
if __name__ == "__main__":
    lp_tokens = 1000
    days_locked = 30
    rewards = calculate_rewards(lp_tokens, days_locked)
    print(f"Potential rewards for locking {lp_tokens} LP tokens for {days_locked} days: {rewards:.6f}")
```
