"""
Generated Code Metadata:
========================
Original URL: https://bananagunn.io
Prompt: Write a script to calculate rewards for holding $BANANA tokens based on the APR and epoch duration, including separate calculations for EVM and Solana rewards as described on the Bananagun Rewards page.
Generated: DETERMINISTIC_61e8ea65122281a0
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bananagun_rewards_calculator.py

from datetime import timedelta

class BananagunRewardsCalculator:
    """
    Calculates rewards for holding $BANANA tokens based on APR and epoch duration.
    """

    def __init__(self, apr: float, epoch_duration: int):
        """
        Initializes the calculator with APR and epoch duration.

        Args:
        - apr (float): The annual percentage rate.
        - epoch_duration (int): The duration of an epoch in seconds.
        """
        self.apr = apr / 100  # Convert APR to decimal
        self.epoch_duration = epoch_duration

    def calculate_evm_rewards(self, banana_balance: float, seconds_in_year: int = 31536000) -> float:
        """
        Calculates EVM rewards for holding $BANANA tokens.

        Args:
        - banana_balance (float): The user's $BANANA token balance.
        - seconds_in_year (int): The number of seconds in a year. Defaults to 31536000.

        Returns:
        - float: The EVM rewards.
        """
        # Calculate the total seconds in an epoch
        epoch_seconds = self.epoch_duration

        # Calculate the reward per second
        reward_per_second = (self.apr / seconds_in_year) * banana_balance

        # Calculate the EVM rewards for the epoch
        evm_rewards = reward_per_second * epoch_seconds

        return evm_rewards

    def calculate_solana_rewards(self, banana_balance: float, seconds_in_year: int = 31536000) -> float:
        """
        Calculates Solana rewards for holding $BANANA tokens.

        Args:
        - banana_balance (float): The user's $BANANA token balance.
        - seconds_in_year (int): The number of seconds in a year. Defaults to 31536000.

        Returns:
        - float: The Solana rewards.
        """
        # For Solana, assume a 1:1 ratio with EVM rewards for simplicity
        # In a real-world scenario, this would be a more complex calculation
        # based on the actual Solana staking mechanics
        solana_rewards = self.calculate_evm_rewards(banana_balance, seconds_in_year) * 0.8

        return solana_rewards


def main():
    try:
        # Example usage
        apr = 20.0  # 20% APR
        epoch_duration = timedelta(hours=1).total_seconds()  # 1 hour epoch duration
        banana_balance = 1000.0  # $1000 $BANANA tokens

        calculator = BananagunRewardsCalculator(apr, epoch_duration)

        evm_rewards = calculator.calculate_evm_rewards(banana_balance)
        solana_rewards = calculator.calculate_solana_rewards(banana_balance)

        print(f"EVM Rewards: {evm_rewards:.2f} $BANANA")
        print(f"Solana Rewards: {solana_rewards:.2f} $BANANA")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
