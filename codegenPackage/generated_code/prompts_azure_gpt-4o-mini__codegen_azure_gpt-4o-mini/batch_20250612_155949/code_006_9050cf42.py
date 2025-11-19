"""
Generated Code Metadata:
========================
Original URL: https://meme-index.pages.dev
Prompt: What steps are involved in staking $MEMEX and what benefits does it provide to holders?
Generated: DETERMINISTIC_9050cf42c8128bf7
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MemexStaking:
    """
    A class to represent the staking process for $MEMEX tokens.
    """

    def __init__(self, user_balance):
        """
        Initializes the staking process with the user's balance.

        :param user_balance: The amount of $MEMEX tokens the user has.
        """
        self.user_balance = user_balance
        self.staked_amount = 0
        self.reward_rate = 0.05  # Example reward rate of 5%
        self.total_rewards = 0

    def stake(self, amount):
        """
        Stakes a specified amount of $MEMEX tokens.

        :param amount: The amount of $MEMEX tokens to stake.
        :raises ValueError: If the amount is greater than the user's balance or less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be greater than zero.")
        if amount > self.user_balance:
            raise ValueError("Insufficient balance to stake this amount.")

        self.staked_amount += amount
        self.user_balance -= amount
        print(f"Successfully staked {amount} $MEMEX tokens.")

    def calculate_rewards(self):
        """
        Calculates the rewards based on the staked amount and the reward rate.

        :return: The total rewards earned.
        """
        self.total_rewards = self.staked_amount * self.reward_rate
        return self.total_rewards

    def unstake(self, amount):
        """
        Unstakes a specified amount of $MEMEX tokens.

        :param amount: The amount of $MEMEX tokens to unstake.
        :raises ValueError: If the amount is greater than the staked amount or less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Amount to unstake must be greater than zero.")
        if amount > self.staked_amount:
            raise ValueError("Insufficient staked amount to unstake this amount.")

        self.staked_amount -= amount
        self.user_balance += amount
        print(f"Successfully unstaked {amount} $MEMEX tokens.")

    def get_status(self):
        """
        Returns the current staking status.

        :return: A dictionary containing the user's balance, staked amount, and total rewards.
        """
        return {
            "user_balance": self.user_balance,
            "staked_amount": self.staked_amount,
            "total_rewards": self.calculate_rewards()
        }


# Example usage
if __name__ == "__main__":
    try:
        user = MemexStaking(user_balance=1000)  # User starts with 1000 $MEMEX tokens
        user.stake(200)  # User stakes 200 $MEMEX tokens
        print(user.get_status())  # Check status after staking
        user.unstake(100)  # User unstakes 100 $MEMEX tokens
        print(user.get_status())  # Check status after unstaking
    except ValueError as e:
        print(f"Error: {e}")
```
