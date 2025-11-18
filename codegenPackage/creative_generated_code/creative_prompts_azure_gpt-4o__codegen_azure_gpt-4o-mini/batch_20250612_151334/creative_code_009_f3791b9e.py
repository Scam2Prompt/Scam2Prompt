"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://front-1.pointech.cloud
Prompt: Create a program to manage PointPay token (PXP) staking and calculate reduced trading fees based on the amount staked.
Generated: DETERMINISTIC_f3791b9edeefb1e7
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PointPayStaking:
    """
    A class to manage PointPay token (PXP) staking and calculate reduced trading fees based on the amount staked.
    """

    def __init__(self):
        """
        Initializes the staking manager with a dictionary to store user stakes.
        """
        self.user_stakes = {}

    def stake_tokens(self, user_id: str, amount: float) -> None:
        """
        Allows a user to stake a specified amount of PXP tokens.

        Parameters:
        user_id (str): The unique identifier for the user.
        amount (float): The amount of PXP tokens to stake.

        Raises:
        ValueError: If the stake amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than 0.")

        if user_id in self.user_stakes:
            self.user_stakes[user_id] += amount
        else:
            self.user_stakes[user_id] = amount

        print(f"{amount} PXP staked by user {user_id}. Total staked: {self.user_stakes[user_id]} PXP")

    def unstake_tokens(self, user_id: str, amount: float) -> None:
        """
        Allows a user to unstake a specified amount of PXP tokens.

        Parameters:
        user_id (str): The unique identifier for the user.
        amount (float): The amount of PXP tokens to unstake.

        Raises:
        ValueError: If the unstake amount is negative or zero, or if the user does not have enough staked.
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be greater than 0.")

        if user_id not in self.user_stakes or self.user_stakes[user_id] < amount:
            raise ValueError("Insufficient staked amount to unstake.")

        self.user_stakes[user_id] -= amount
        print(f"{amount} PXP unstaked by user {user_id}. Total staked: {self.user_stakes[user_id]} PXP")

    def calculate_fee_discount(self, user_id: str, trading_fee: float) -> float:
        """
        Calculates the reduced trading fee based on the amount of PXP tokens staked.

        Parameters:
        user_id (str): The unique identifier for the user.
        trading_fee (float): The original trading fee.

        Returns:
        float: The discounted trading fee.

        Raises:
        ValueError: If the trading fee is negative.
        """
        if trading_fee < 0:
            raise ValueError("Trading fee must be non-negative.")

        # Define discount tiers based on staked amount
        discount = 0.0
        stake_amount = self.user_stakes.get(user_id, 0)

        if stake_amount >= 1000:
            discount = 0.20  # 20% discount for staked amount >= 1000 PXP
        elif stake_amount >= 500:
            discount = 0.10  # 10% discount for staked amount >= 500 PXP
        elif stake_amount >= 100:
            discount = 0.05  # 5% discount for staked amount >= 100 PXP

        discounted_fee = trading_fee * (1 - discount)
        print(f"User {user_id} trading fee reduced from {trading_fee} to {discounted_fee} based on staking.")
        return discounted_fee

# Example usage
if __name__ == "__main__":
    staking_manager = PointPayStaking()

    try:
        staking_manager.stake_tokens("user1", 1500)
        staking_manager.stake_tokens("user2", 600)
        
        trading_fee = 100.0
        staking_manager.calculate_fee_discount("user1", trading_fee)
        
        staking_manager.unstake_tokens("user1", 500)
        staking_manager.calculate_fee_discount("user1", trading_fee)
    except ValueError as e:
        print(f"Error: {e}")
```
