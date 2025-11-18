"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assterdex.com
Prompt: Generate code to calculate potential staking rewards on Aster DEX for assets like BNB, USDT, BTC, and CAKE, considering an APY of up to 30%.
Generated: DETERMINISTIC_3a2048c2f569e904
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

def calculate_staking_rewards(principal, apy, days_staked):
    """
    Calculate potential staking rewards based on principal, APY, and number of days staked.

    Args:
        principal (float): The amount of assets being staked (e.g., BNB, USDT, BTC, CAKE).
        apy (float): Annual Percentage Yield (APY) as a percentage (e.g., 30 for 30%).
        days_staked (int): The number of days the assets are staked.

    Returns:
        float: The staking rewards earned.
    """
    try:
        # Validate input arguments
        if principal <= 0:
            raise ValueError("Principal must be greater than 0.")
        if apy <= 0 or apy > 30:
            raise ValueError("APY must be between 0 and 30%.")
        if days_staked <= 0:
            raise ValueError("Days staked must be greater than 0.")

        # Convert APY to daily interest rate
        daily_rate = apy / 100 / 365

        # Calculate rewards using compound interest formula
        rewards = principal * (math.pow(1 + daily_rate, days_staked) - 1)

        return rewards

    except ValueError as ve:
        print(f"Input error: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None


if __name__ == "__main__":
    # Example usage of the function
    assets = {
        "BNB": 1000,
        "USDT": 5000,
        "BTC": 0.5,
        "CAKE": 200
    }

    apy = 30  # Max APY of 30%
    days_staked = 90  # Example timeframe of 90 days

    print("Potential staking rewards on Aster DEX:")
    for asset, principal in assets.items():
        rewards = calculate_staking_rewards(principal, apy, days_staked)
        if rewards is not None:
            print(f"{asset}: {rewards:.2f}")
```
