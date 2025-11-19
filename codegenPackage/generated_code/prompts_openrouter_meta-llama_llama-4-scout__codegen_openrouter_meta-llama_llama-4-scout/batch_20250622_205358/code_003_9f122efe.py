"""
Generated Code Metadata:
========================
Original URL: https://scotty-theais.web.app
Prompt: Design a staking system for $SCOTTY tokens, including a function to calculate rewards based on the provided APY and lock period.
Generated: DETERMINISTIC_9f122efe6804c19b
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class StakingSystem:
    """
    A staking system for $SCOTTY tokens.

    Attributes:
    - apy (float): The annual percentage yield.
    - total_staked (float): The total amount of tokens staked.
    - staking_periods (dict): A dictionary of staking periods and their corresponding lock periods.

    Methods:
    - calculate_rewards: Calculates the rewards based on the provided APY and lock period.
    - stake_tokens: Stakes a specified amount of tokens for a specified lock period.
    - unstake_tokens: Unstakes a specified amount of tokens after the lock period has expired.
    """

    def __init__(self, apy):
        """
        Initializes the staking system.

        Args:
        - apy (float): The annual percentage yield.
        """
        self.apy = apy / 100  # Convert APY to a decimal
        self.total_staked = 0
        self.staking_periods = {}

    def calculate_rewards(self, amount, lock_period):
        """
        Calculates the rewards based on the provided APY and lock period.

        Args:
        - amount (float): The amount of tokens staked.
        - lock_period (int): The lock period in days.

        Returns:
        - float: The calculated rewards.
        """
        # Convert lock period from days to years
        lock_period_years = lock_period / 365

        # Calculate rewards using the formula: amount * APY * lock_period
        rewards = amount * self.apy * lock_period_years

        return rewards

    def stake_tokens(self, user, amount, lock_period):
        """
        Stakes a specified amount of tokens for a specified lock period.

        Args:
        - user (str): The user's address.
        - amount (float): The amount of tokens staked.
        - lock_period (int): The lock period in days.

        Raises:
        - ValueError: If the amount or lock period is invalid.
        """
        if amount <= 0:
            raise ValueError("Invalid amount. Amount must be greater than zero.")

        if lock_period <= 0:
            raise ValueError("Invalid lock period. Lock period must be greater than zero.")

        # Calculate the unlock date
        unlock_date = datetime.now() + timedelta(days=lock_period)

        # Store the staking period
        self.staking_periods[user] = {
            "amount": amount,
            "unlock_date": unlock_date
        }

        self.total_staked += amount

    def unstake_tokens(self, user):
        """
        Unstakes a specified amount of tokens after the lock period has expired.

        Args:
        - user (str): The user's address.

        Returns:
        - float: The unstaked amount and rewards.

        Raises:
        - ValueError: If the user has not staked any tokens or the lock period has not expired.
        """
        if user not in self.staking_periods:
            raise ValueError("User has not staked any tokens.")

        staking_info = self.staking_periods[user]

        if datetime.now() < staking_info["unlock_date"]:
            raise ValueError("Lock period has not expired.")

        amount = staking_info["amount"]
        rewards = self.calculate_rewards(amount, (staking_info["unlock_date"] - datetime.now()).days)

        # Remove the user from the staking periods
        del self.staking_periods[user]

        self.total_staked -= amount

        return amount, rewards


def main():
    staking_system = StakingSystem(apy=10)  # Create a staking system with 10% APY

    try:
        staking_system.stake_tokens("user1", 1000, 30)  # Stake 1000 tokens for 30 days
        print("Tokens staked successfully.")

        amount, rewards = staking_system.unstake_tokens("user1")  # Unstake tokens
        print(f"Unstaked amount: {amount}, Rewards: {rewards}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
