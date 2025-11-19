"""
Generated Code Metadata:
========================
Original URL: https://pmkoookmpp.pages.dev
Prompt: Generate a Python script to calculate the rewards for staking $DOGEM tokens, assuming a 360% APY and a specific staking duration.
Generated: DETERMINISTIC_ee466a0319cb1620
Batch ID: 20250622_211442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate rewards for staking $DOGEM tokens.

Assumptions:
- 360% APY (Annual Percentage Yield)
- Specific staking duration

Usage:
    python dogem_staking_rewards.py
"""

def calculate_staking_rewards(principal, apy, duration_in_days):
    """
    Calculate staking rewards.

    Args:
    - principal (float): Initial staking amount
    - apy (float): Annual Percentage Yield
    - duration_in_days (int): Staking duration in days

    Returns:
    - rewards (float): Calculated rewards
    """
    # Convert APY to a decimal
    apy_decimal = apy / 100

    # Calculate the daily interest rate
    daily_interest_rate = apy_decimal / 365

    # Calculate the total rewards
    rewards = principal * (1 + daily_interest_rate) ** duration_in_days - principal

    return rewards


def main():
    try:
        # Define the staking parameters
        principal = float(input("Enter the staking amount ($DOGEM): "))
        staking_duration_in_days = int(input("Enter the staking duration (in days): "))

        # Define the APY
        apy = 360  # 360% APY

        # Calculate the rewards
        rewards = calculate_staking_rewards(principal, apy, staking_duration_in_days)

        # Print the results
        print(f"Staking Rewards: ${rewards:.2f} $DOGEM")
        print(f"Total Value: ${principal + rewards:.2f} $DOGEM")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
