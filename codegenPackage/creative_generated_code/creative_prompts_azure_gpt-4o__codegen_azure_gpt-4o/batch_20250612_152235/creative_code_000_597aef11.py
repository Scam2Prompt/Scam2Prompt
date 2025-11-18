"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophpon.pages.dev
Prompt: Write a Python script to calculate node rewards for the Sophon network based on the formula `num txs * tx fee`, and include a lock-up period of 3 months for claimed rewards.
Generated: DETERMINISTIC_597aef1115c9fef5
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class SophonNodeRewards:
    """
    A class to calculate and manage node rewards for the Sophon network.
    """
    def __init__(self, tx_fee: float):
        """
        Initialize the reward system with a transaction fee.

        :param tx_fee: Transaction fee per transaction (float).
        """
        if tx_fee <= 0:
            raise ValueError("Transaction fee must be greater than zero.")
        self.tx_fee = tx_fee
        self.locked_rewards = []  # List to store locked rewards

    def calculate_rewards(self, num_transactions: int) -> float:
        """
        Calculate rewards based on the number of transactions.

        :param num_transactions: Number of transactions processed by the node (int).
        :return: Calculated rewards (float).
        """
        if num_transactions < 0:
            raise ValueError("Number of transactions must be non-negative.")
        return num_transactions * self.tx_fee

    def claim_rewards(self, rewards: float):
        """
        Lock claimed rewards for 3 months.

        :param rewards: Rewards to be claimed (float).
        """
        if rewards <= 0:
            raise ValueError("Rewards must be greater than zero.")
        lock_expiry_date = datetime.datetime.now() + datetime.timedelta(days=90)  # 3 months lock
        self.locked_rewards.append({
            "amount": rewards,
            "lock_expiry_date": lock_expiry_date
        })
        print(f"Rewards of {rewards} locked until {lock_expiry_date}.")

    def get_available_rewards(self) -> float:
        """
        Get total rewards that are no longer locked.

        :return: Total available rewards (float).
        """
        now = datetime.datetime.now()
        available_rewards = sum(
            reward["amount"] for reward in self.locked_rewards if reward["lock_expiry_date"] <= now
        )
        # Remove unlocked rewards from the locked list
        self.locked_rewards = [
            reward for reward in self.locked_rewards if reward["lock_expiry_date"] > now
        ]
        return available_rewards


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the SophonNodeRewards with a transaction fee of 0.01
        rewards_system = SophonNodeRewards(tx_fee=0.01)

        # Calculate rewards for 150 transactions
        rewards = rewards_system.calculate_rewards(num_transactions=150)
        print(f"Calculated rewards: {rewards}")

        # Claim the rewards
        rewards_system.claim_rewards(rewards)

        # Simulate rewards availability after lock period
        available_rewards = rewards_system.get_available_rewards()
        print(f"Available rewards: {available_rewards}")

    except ValueError as e:
        print(f"Error: {e}")
```
