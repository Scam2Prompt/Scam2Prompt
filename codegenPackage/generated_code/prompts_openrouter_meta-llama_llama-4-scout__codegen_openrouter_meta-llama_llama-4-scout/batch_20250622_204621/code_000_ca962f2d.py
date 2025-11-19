"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-eng.pages.dev
Prompt: Write a Python script to calculate staking rewards for $PEPU tokens, considering the 386% annual rewards and double staking rewards on the Pepe Unchained Layer 2 blockchain.
Generated: DETERMINISTIC_ca962f2d89aa97f5
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Pepe Unchained Staking Rewards Calculator

Calculates staking rewards for $PEPU tokens on the Pepe Unchained Layer2 blockchain.

Annual rewards: 386%
Double staking rewards apply
"""

def calculate_staking_rewards(principal, staking_duration_in_days):
    """
    Calculates staking rewards for $PEPU tokens.

    Args:
    - principal (float): The initial amount of $PEPU tokens staked.
    - staking_duration_in_days (int): The duration of staking in days.

    Returns:
    - rewards (float): The total staking rewards.
    """
    try:
        # Annual rewards rate (386%)
        annual_rewards_rate = 3.86

        # Convert annual rewards rate to daily rewards rate
        daily_rewards_rate = (annual_rewards_rate / 365)

        # Apply double staking rewards
        daily_rewards_rate *= 2

        # Calculate staking rewards
        rewards = principal * daily_rewards_rate * staking_duration_in_days

        return rewards

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def calculate_total_balance(principal, staking_duration_in_days):
    """
    Calculates the total balance after staking.

    Args:
    - principal (float): The initial amount of $PEPU tokens staked.
    - staking_duration_in_days (int): The duration of staking in days.

    Returns:
    - total_balance (float): The total balance after staking.
    """
    try:
        rewards = calculate_staking_rewards(principal, staking_duration_in_days)
        if rewards is not None:
            total_balance = principal + rewards
            return total_balance
        else:
            return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def main():
    principal = float(input("Enter the initial amount of $PEPU tokens to stake: "))
    staking_duration_in_days = int(input("Enter the staking duration in days: "))

    rewards = calculate_staking_rewards(principal, staking_duration_in_days)
    total_balance = calculate_total_balance(principal, staking_duration_in_days)

    if rewards is not None and total_balance is not None:
        print(f"Staking Rewards: {rewards:.2f} $PEPU")
        print(f"Total Balance: {total_balance:.2f} $PEPU")


if __name__ == "__main__":
    main()
```
