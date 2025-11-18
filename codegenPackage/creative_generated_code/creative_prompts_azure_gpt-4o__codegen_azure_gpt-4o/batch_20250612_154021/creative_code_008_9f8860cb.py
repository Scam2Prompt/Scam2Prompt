"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdx.com
Prompt: Generate code to calculate potential earnings from staking assets on Aster, factoring in APY rates and token minting rewards.
Generated: DETERMINISTIC_9f8860cbfc92e3cf
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_staking_rewards(principal, apy_rate, duration_days, token_minting_reward):
    """
    Calculate potential earnings from staking assets on Aster.

    Args:
        principal (float): The initial amount of assets staked.
        apy_rate (float): Annual Percentage Yield (APY) rate as a percentage (e.g., 5 for 5% APY).
        duration_days (int): Duration of staking in days.
        token_minting_reward (float): Additional reward from token minting.

    Returns:
        float: The total potential earnings (including APY and token minting rewards).
    """

    # Validate inputs
    if principal <= 0:
        raise ValueError("Principal amount should be greater than zero.")
    if apy_rate < 0:
        raise ValueError("APY rate cannot be negative.")
    if duration_days <= 0:
        raise ValueError("Staking duration should be greater than zero.")
    if token_minting_reward < 0:
        raise ValueError("Token minting reward cannot be negative.")

    # Calculate APY rewards (compounded daily)
    annual_interest_rate = apy_rate / 100  # Convert percentage to decimal
    daily_interest_rate = annual_interest_rate / 365  # Daily rate based on APY
    compound_multiplier = math.pow(1 + daily_interest_rate, duration_days)  # Compound multiplier
    apy_earnings = principal * (compound_multiplier - 1)  # Total earnings from APY

    # Add token minting rewards
    total_earnings = apy_earnings + token_minting_reward

    return total_earnings


if __name__ == "__main__":
    try:
        # Example usage
        principal_amount = float(input("Enter the principal amount (e.g., 1000.00): "))
        apy_rate_percentage = float(input("Enter the APY rate (e.g., 5 for 5%): "))
        staking_duration_days = int(input("Enter the staking duration in days: "))
        minting_reward = float(input("Enter the token minting reward: "))

        total_rewards = calculate_staking_rewards(
            principal=principal_amount,
            apy_rate=apy_rate_percentage,
            duration_days=staking_duration_days,
            token_minting_reward=minting_reward,
        )

        print(f"Total potential earnings from staking: {total_rewards:.2f}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
