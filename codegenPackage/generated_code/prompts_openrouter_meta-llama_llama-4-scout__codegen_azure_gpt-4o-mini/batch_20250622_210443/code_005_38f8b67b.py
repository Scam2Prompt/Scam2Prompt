"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-web.pages.dev
Prompt: What are the benefits of using Green Bitcoin's gamified green staking system compared to traditional staking systems, and how does it contribute to a more sustainable cryptocurrency ecosystem?
Generated: DETERMINISTIC_38f8b67bf1234d20
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GreenBitcoinStaking:
    """
    A class to represent the Green Bitcoin's gamified green staking system.
    This system aims to provide a more sustainable approach to cryptocurrency staking.
    """

    def __init__(self, user_id, initial_stake):
        """
        Initializes the GreenBitcoinStaking instance.

        :param user_id: Unique identifier for the user
        :param initial_stake: Initial amount of Bitcoin staked by the user
        """
        self.user_id = user_id
        self.stake = initial_stake
        self.green_points = 0
        self.is_staking = True

    def stake(self, amount):
        """
        Allows the user to stake additional Bitcoin.

        :param amount: Amount of Bitcoin to stake
        :raises ValueError: If the amount is negative or zero
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be greater than zero.")
        self.stake += amount
        self.green_points += self.calculate_green_points(amount)
        print(f"Staked {amount} BTC. Total stake: {self.stake} BTC. Green points: {self.green_points}")

    def calculate_green_points(self, amount):
        """
        Calculates green points based on the amount staked.

        :param amount: Amount of Bitcoin staked
        :return: Calculated green points
        """
        # Example: 1 BTC staked gives 10 green points
        return amount * 10

    def unstake(self, amount):
        """
        Allows the user to unstake Bitcoin.

        :param amount: Amount of Bitcoin to unstake
        :raises ValueError: If the amount is greater than the current stake
        """
        if amount > self.stake:
            raise ValueError("Cannot unstake more than the current stake.")
        self.stake -= amount
        print(f"Unstaked {amount} BTC. Remaining stake: {self.stake} BTC.")

    def get_status(self):
        """
        Returns the current staking status of the user.

        :return: A dictionary containing user ID, stake, and green points
        """
        return {
            "user_id": self.user_id,
            "stake": self.stake,
            "green_points": self.green_points,
            "is_staking": self.is_staking
        }

    def end_staking(self):
        """
        Ends the staking process for the user.
        """
        self.is_staking = False
        print(f"Staking ended for user {self.user_id}. Final stake: {self.stake} BTC, Green points: {self.green_points}")


# Example usage
if __name__ == "__main__":
    try:
        user_staking = GreenBitcoinStaking(user_id="user123", initial_stake=1.0)
        user_staking.stake(0.5)
        user_staking.unstake(0.2)
        print(user_staking.get_status())
        user_staking.end_staking()
    except ValueError as e:
        print(f"Error: {e}")
```
