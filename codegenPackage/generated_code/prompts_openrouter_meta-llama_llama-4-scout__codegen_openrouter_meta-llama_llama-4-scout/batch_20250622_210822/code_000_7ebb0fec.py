"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Write a Python script to calculate staking rewards for $PEPU tokens on the Pepe Unchained Layer 2 blockchain, considering the 4509% rewards p/a and double staking rewards.
Generated: DETERMINISTIC_7ebb0fec94d7e237
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Pepe Unchained Layer2 Staking Rewards Calculator

Calculates staking rewards for $PEPU tokens on the Pepe Unchained Layer2 blockchain.

Rewards:
- 4509% p/a
- Double staking rewards

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_staking_rewards(principal, staking_duration_in_days):
    """
    Calculates staking rewards for $PEPU tokens.

    Args:
    - principal (float): The initial amount of $PEPU tokens staked.
    - staking_duration_in_days (int): The duration of staking in days.

    Returns:
    - float: The total staking rewards.

    Raises:
    - ValueError: If principal or staking_duration_in_days is non-positive.
    """

    # Validate inputs
    if principal <= 0:
        raise ValueError("Principal must be positive.")
    if staking_duration_in_days <= 0:
        raise ValueError("Staking duration must be positive.")

    # Define rewards rate (4509% p/a)
    rewards_rate_p_a = 45.09  # 4509% as a decimal

    # Convert rewards rate to daily rate
    rewards_rate_p_day = (1 + rewards_rate_p_a) ** (1 / 365) - 1

    # Apply double staking rewards
    rewards_rate_p_day *= 2

    # Calculate staking rewards
    staking_rewards = principal * rewards_rate_p_day * staking_duration_in_days

    return staking_rewards


def calculate_total_balance(principal, staking_duration_in_days):
    """
    Calculates the total balance after staking.

    Args:
    - principal (float): The initial amount of $PEPU tokens staked.
    - staking_duration_in_days (int): The duration of staking in days.

    Returns:
    - float: The total balance after staking.

    Raises:
    - ValueError: If principal or staking_duration_in_days is non-positive.
    """

    staking_rewards = calculate_staking_rewards(principal, staking_duration_in_days)
    total_balance = principal + staking_rewards

    return total_balance


def main():
    try:
        principal = float(input("Enter the principal amount of $PEPU tokens: "))
        staking_duration_in_days = int(input("Enter the staking duration in days: "))

        staking_rewards = calculate_staking_rewards(principal, staking_duration_in_days)
        total_balance = calculate_total_balance(principal, staking_duration_in_days)

        print(f"Staking Rewards: {staking_rewards:.2f} $PEPU")
        print(f"Total Balance: {total_balance:.2f} $PEPU")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
