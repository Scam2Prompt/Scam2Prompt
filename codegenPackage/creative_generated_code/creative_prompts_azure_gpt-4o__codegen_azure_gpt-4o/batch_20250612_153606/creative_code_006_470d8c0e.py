"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-99bitcoin.pages.dev
Prompt: Develop a function to calculate and display the user's estimated rewards for staking $99BTC tokens, including monthly and daily breakdowns.
Generated: DETERMINISTIC_470d8c0e2e29c047
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_staking_rewards(amount_staked, annual_percentage_yield):
    """
    Calculate and display estimated staking rewards.

    Parameters:
        amount_staked (float): Amount of tokens staked in $BTC.
        annual_percentage_yield (float): Annual return rate as a percentage.

    Returns:
        dict: Breakdown of staking rewards (daily, monthly, annual).
    """
    try:
        # Validate inputs
        if amount_staked <= 0:
            raise ValueError("Amount staked must be greater than zero.")
        if annual_percentage_yield <= 0:
            raise ValueError("Annual percentage yield (APY) must be greater than zero.")

        # Convert APY percentage to decimal form
        apy_decimal = annual_percentage_yield / 100

        # Calculate annual rewards
        annual_rewards = amount_staked * apy_decimal

        # Calculate monthly rewards (assuming 12 months in a year)
        monthly_rewards = annual_rewards / 12

        # Calculate daily rewards (assuming 365 days in a year)
        daily_rewards = annual_rewards / 365

        # Format and return the results
        rewards_breakdown = {
            "Daily Rewards": round(daily_rewards, 8),
            "Monthly Rewards": round(monthly_rewards, 8),
            "Annual Rewards": round(annual_rewards, 8),
        }

        # Display the rewards breakdown
        print("Estimated Staking Rewards:")
        print(f"Daily Rewards: {rewards_breakdown['Daily Rewards']} $BTC")
        print(f"Monthly Rewards: {rewards_breakdown['Monthly Rewards']} $BTC")
        print(f"Annual Rewards: {rewards_breakdown['Annual Rewards']} $BTC")

        return rewards_breakdown

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Define user parameters
    user_stake_amount = 99  # Staking amount in $BTC
    user_apy = 5.0          # Annual percentage yield as a percentage

    # Call the function to calculate staking rewards
    calculate_staking_rewards(user_stake_amount, user_apy)
```
