"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://srrv2oldmtlx.pages.dev
Prompt: Create a Python script that calculates the daily MTLX rewards for the "Steel Rebar V2" market based on the provided APY and liquidity data.
Generated: DETERMINISTIC_d84769a1ad08bb55
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_daily_rewards(apy, total_liquidity, reward_pool_percentage):
    """
    Calculates the daily MTLX rewards for the "Steel Rebar V2" market.

    Parameters:
        apy (float): Annual Percentage Yield (APY) as a percentage (e.g., 12.5 for 12.5%).
        total_liquidity (float): Total liquidity in the market.
        reward_pool_percentage (float): Percentage of total liquidity allocated to the reward pool.

    Returns:
        float: Daily rewards in MTLX tokens.
    """
    try:
        # Validate inputs
        if apy <= 0 or total_liquidity <= 0 or reward_pool_percentage <= 0:
            raise ValueError("APY, total liquidity, and reward pool percentage must be positive values.")

        # Convert APY percentage to a decimal
        apy_decimal = apy / 100

        # Calculate annual rewards based on APY and reward pool allocation
        annual_rewards = total_liquidity * apy_decimal * reward_pool_percentage / 100

        # Calculate daily rewards (365 days in a year)
        daily_rewards = annual_rewards / 365

        return daily_rewards
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    """
    Entry point for the script. Accepts input from the user and calculates the daily MTLX rewards.
    """
    try:
        # Collect user inputs
        apy = float(input("Enter APY (in %): "))
        total_liquidity = float(input("Enter total liquidity: "))
        reward_pool_percentage = float(input("Enter reward pool percentage (in %): "))

        # Calculate daily rewards
        daily_rewards = calculate_daily_rewards(apy, total_liquidity, reward_pool_percentage)

        if daily_rewards is not None:
            print(f"Daily MTLX Rewards: {daily_rewards:.6f} tokens")
    except ValueError:
        print("Invalid input. Please enter numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
```
