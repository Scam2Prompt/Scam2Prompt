"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappstake.pages.dev
Prompt: Write a function to calculate staking rewards for tokens listed on DappRadar, factoring in APY rates, staking duration, and minimum amounts.
Generated: DETERMINISTIC_fc828677af7d6516
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_staking_rewards(token_name, apy_rate, staking_duration_days, staked_amount, min_stake_amount):
    """
    Calculates staking rewards for a given token based on APY rate, staking duration, and staked amount.

    Args:
        token_name (str): Name of the token.
        apy_rate (float): Annual Percentage Yield (APY) rate as a percentage (e.g., 15.0 for 15% APY).
        staking_duration_days (int): Duration of staking in days.
        staked_amount (float): Amount of tokens staked.
        min_stake_amount (float): Minimum amount required for staking.

    Returns:
        dict: A dictionary containing token name, staked amount, duration, total rewards, and error message (if any).
    """
    result = {
        "token_name": token_name,
        "staked_amount": staked_amount,
        "staking_duration_days": staking_duration_days,
        "total_rewards": 0.0,
        "error": None
    }

    try:
        # Check if staked amount meets the minimum requirement
        if staked_amount < min_stake_amount:
            result["error"] = f"Staked amount ({staked_amount}) is below the minimum required ({min_stake_amount})."
            return result
        
        # Ensure APY rate is positive
        if apy_rate <= 0:
            result["error"] = f"Invalid APY rate ({apy_rate}). APY must be greater than 0."
            return result
        
        # Ensure staking duration is valid
        if staking_duration_days <= 0:
            result["error"] = f"Invalid staking duration ({staking_duration_days} days). Duration must be greater than 0."
            return result

        # Calculate rewards
        days_in_year = 365.0
        annual_rewards = (staked_amount * apy_rate) / 100  # APY is a percentage
        daily_rewards = annual_rewards / days_in_year  # Daily rewards
        total_rewards = daily_rewards * staking_duration_days  # Rewards for staking duration

        result["total_rewards"] = round(total_rewards, 6)  # Rounded to 6 decimal places for precision
        return result

    except Exception as e:
        # Catch any unexpected errors
        result["error"] = f"An unexpected error occurred: {str(e)}"
        return result


# Example usage
if __name__ == "__main__":
    token_info = calculate_staking_rewards(
        token_name="ExampleToken",
        apy_rate=15.0,
        staking_duration_days=90,
        staked_amount=500,
        min_stake_amount=100
    )
    print(token_info)
```
