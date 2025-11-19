"""
Generated Code Metadata:
========================
Original URL: https://jwzt-dashboards-inqubeta.pages.dev
Prompt: Generate a script to simulate staking $QUBE tokens for a specified number of days and calculate the total rewards earned.
Generated: DETERMINISTIC_9bd3af0fb2c05e09
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_calculator.py

import datetime

class StakingCalculator:
    """
    Calculates the total rewards earned from staking $QUBE tokens.
    """

    def __init__(self, principal_amount, staking_days, daily_interest_rate):
        """
        Initializes the staking calculator.

        Args:
        - principal_amount (float): The initial amount of $QUBE tokens staked.
        - staking_days (int): The number of days the tokens are staked.
        - daily_interest_rate (float): The daily interest rate for staking.
        """
        self.principal_amount = principal_amount
        self.staking_days = staking_days
        self.daily_interest_rate = daily_interest_rate

    def calculate_rewards(self):
        """
        Calculates the total rewards earned from staking.

        Returns:
        - float: The total rewards earned.
        """
        # Calculate the total rewards using compound interest formula
        total_rewards = self.principal_amount * ((1 + self.daily_interest_rate) ** self.staking_days - 1)
        return total_rewards

    def simulate_staking(self):
        """
        Simulates the staking process and prints the daily rewards.

        Returns:
        - None
        """
        print(f"Staking {self.principal_amount} $QUBE tokens for {self.staking_days} days.")
        print(f"Daily interest rate: {self.daily_interest_rate * 100}%")

        current_balance = self.principal_amount
        for day in range(1, self.staking_days + 1):
            daily_rewards = current_balance * self.daily_interest_rate
            current_balance += daily_rewards

            print(f"Day {day}:")
            print(f"  Balance: {current_balance:.2f} $QUBE")
            print(f"  Daily Rewards: {daily_rewards:.2f} $QUBE")

        total_rewards = current_balance - self.principal_amount
        print(f"\nTotal Rewards: {total_rewards:.2f} $QUBE")


def main():
    try:
        principal_amount = float(input("Enter the principal amount of $QUBE tokens: "))
        staking_days = int(input("Enter the number of days to stake: "))
        daily_interest_rate = float(input("Enter the daily interest rate (in decimal form, e.g., 0.05 for 5%): "))

        calculator = StakingCalculator(principal_amount, staking_days, daily_interest_rate)
        calculator.simulate_staking()

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
