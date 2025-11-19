"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdoge20live.pages.dev
Prompt: Generate a code snippet to calculate the estimated rewards for DOGE20 staking based on a dynamic annual return percentage.
Generated: DETERMINISTIC_9338d6f7983dcc6c
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# DOGE20 Staking Rewards Calculator
# This script calculates the estimated staking rewards for DOGE20 based on a dynamic annual return percentage.

def calculate_staking_rewards(principal, annual_percentage_rate, staking_duration_days):
    """
    Calculates the estimated staking rewards for DOGE20.

    Parameters:
        principal (float): The amount of DOGE20 staked.
        annual_percentage_rate (float): The annual return percentage (APR) as a decimal (e.g., 0.05 for 5%).
        staking_duration_days (int): The number of days the funds are staked.

    Returns:
        float: The estimated staking rewards.
    """
    try:
        # Validate input types
        if not isinstance(principal, (int, float)) or principal <= 0:
            raise ValueError("Principal must be a positive number.")
        if not isinstance(annual_percentage_rate, (int, float)) or annual_percentage_rate < 0:
            raise ValueError("Annual percentage rate must be a non-negative number.")
        if not isinstance(staking_duration_days, int) or staking_duration_days <= 0:
            raise ValueError("Staking duration must be a positive integer.")

        # Calculate staking rewards
        daily_rate = annual_percentage_rate / 365  # Convert annual rate to daily rate
        rewards = principal * daily_rate * staking_duration_days

        return rewards
    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # User-provided values
    principal_amount = 1000  # Staked amount in DOGE20
    annual_rate = 0.075      # 7.5% annual return
    staking_days = 30        # Staking duration in days

    # Calculate rewards
    estimated_rewards = calculate_staking_rewards(principal_amount, annual_rate, staking_days)

    if estimated_rewards is not None:
        print(f"Estimated staking rewards for {staking_days} days: {estimated_rewards:.6f} DOGE20")
```
