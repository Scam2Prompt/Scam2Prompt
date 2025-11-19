"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paal-ai.pages.dev
Prompt: Generate a function to calculate compounded ETH rewards for staking $PAAL tokens based on the APR and pool size mentioned on the Paal AI website.
Generated: DETERMINISTIC_72ca3abbd5663f84
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_compounded_rewards(initial_stake, apr, duration_years, pool_size):
    """
    Calculates compounded ETH rewards for staking PAAL tokens.

    Args:
        initial_stake (float): The amount of PAAL tokens staked by the user.
        apr (float): Annual Percentage Rate (APR) in percentage (e.g., 10 for 10% APR).
        duration_years (float): Duration of staking in years.
        pool_size (float): Total size of the staking pool in PAAL tokens.

    Returns:
        float: The estimated ETH rewards earned from staking.
    """
    try:
        # Validate inputs
        if initial_stake <= 0 or apr <= 0 or duration_years <= 0 or pool_size <= 0:
            raise ValueError("All input values must be positive numbers.")
        if initial_stake > pool_size:
            raise ValueError("Initial stake cannot exceed the pool size.")

        # Convert APR from percentage to a decimal value
        apr_decimal = apr / 100

        # Calculate rewards based on compound interest formula
        # Compound interest formula: A = P * (1 + r/n)^(n*t)
        # For this calculation, we assume continuous compounding (n → ∞)
        # Continuous compounding formula: A = P * e^(r * t)
        rewards = initial_stake * (math.exp(apr_decimal * duration_years) - 1)

        # Adjust rewards based on the proportion of the pool size
        proportional_rewards = rewards * (initial_stake / pool_size)

        return proportional_rewards

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0

# Example usage
if __name__ == "__main__":
    # Inputs for the calculation
    initial_stake = 1000  # User's stake in PAAL tokens
    apr = 12.0           # APR in percentage
    duration_years = 3    # Staking duration in years
    pool_size = 50000     # Total pool size in PAAL tokens

    # Calculate compounded ETH rewards
    rewards = calculate_compounded_rewards(initial_stake, apr, duration_years, pool_size)
    print(f"Estimated ETH Rewards: {rewards:.6f}")
```
