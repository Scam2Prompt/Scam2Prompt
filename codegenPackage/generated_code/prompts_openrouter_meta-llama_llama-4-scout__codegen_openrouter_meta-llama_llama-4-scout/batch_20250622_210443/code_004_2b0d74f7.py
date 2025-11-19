"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Generate a staking pool rewards calculator for Meme Moguls, taking into account the user's stake amount, annual returns percentage, and the total pool share.
Generated: DETERMINISTIC_2b0d74f7f9131d24
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingPoolRewardsCalculator:
    """
    A class used to calculate staking pool rewards for Meme Moguls.

    Attributes:
    ----------
    stake_amount : float
        The user's stake amount.
    annual_returns_percentage : float
        The annual returns percentage.
    total_pool_share : float
        The total pool share.

    Methods:
    -------
    calculate_rewards()
        Calculates the staking pool rewards.
    """

    def __init__(self, stake_amount: float, annual_returns_percentage: float, total_pool_share: float):
        """
        Initializes the StakingPoolRewardsCalculator.

        Args:
        ----
        stake_amount (float): The user's stake amount.
        annual_returns_percentage (float): The annual returns percentage.
        total_pool_share (float): The total pool share.

        Raises:
        ------
        ValueError: If stake_amount, annual_returns_percentage, or total_pool_share is not a positive number.
        """
        if stake_amount <= 0 or annual_returns_percentage <= 0 or total_pool_share <= 0:
            raise ValueError("Stake amount, annual returns percentage, and total pool share must be positive numbers.")

        self.stake_amount = stake_amount
        self.annual_returns_percentage = annual_returns_percentage / 100  # Convert to decimal
        self.total_pool_share = total_pool_share

    def calculate_rewards(self) -> float:
        """
        Calculates the staking pool rewards.

        Returns:
        -------
        float: The staking pool rewards.

        Raises:
        ------
        ValueError: If the stake amount or total pool share is zero or negative.
        """
        try:
            # Calculate the user's pool share
            user_pool_share = self.stake_amount / self.total_pool_share

            # Calculate the annual rewards
            annual_rewards = self.annual_returns_percentage * self.total_pool_share

            # Calculate the user's rewards
            user_rewards = annual_rewards * user_pool_share

            return user_rewards

        except ZeroDivisionError:
            raise ValueError("Total pool share cannot be zero.")

def main():
    try:
        stake_amount = float(input("Enter your stake amount: "))
        annual_returns_percentage = float(input("Enter the annual returns percentage: "))
        total_pool_share = float(input("Enter the total pool share: "))

        calculator = StakingPoolRewardsCalculator(stake_amount, annual_returns_percentage, total_pool_share)
        rewards = calculator.calculate_rewards()

        print(f"Your staking pool rewards are: {rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
