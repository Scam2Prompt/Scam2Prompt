"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Write a script to calculate the rewards for operating a Sophon node based on the formula `num txs * tx fee`, and include logic for the 3-month lock-up period for claimed rewards.
Generated: DETERMINISTIC_72afb738c80021ac
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# sophon_rewards.py
"""
Sophon Node Reward Calculator

This script calculates the rewards for operating a Sophon node based on the 
number of transactions (num_txs) and the transaction fee (tx_fee). Rewards 
are subject to a 3-month lock-up period before they can be claimed.
"""

from datetime import datetime, timedelta

class SophonNode:
    def __init__(self):
        self.total_rewards = 0
        self.locked_rewards = 0
        self.reward_claim_date = None

    def calculate_rewards(self, num_txs: int, tx_fee: float) -> float:
        """
        Calculate the rewards based on the number of transactions and the transaction fee.

        :param num_txs: Number of transactions processed
        :param tx_fee: Fee earned per transaction
        :return: Total calculated rewards
        """
        if num_txs < 0 or tx_fee < 0:
            raise ValueError("Number of transactions and transaction fee must be non-negative")
        
        return num_txs * tx_fee

    def claim_rewards(self):
        """
        Claim the locked rewards only if the 3-month lock-up period has passed.
        
        Raises:
            Exception: If rewards are still locked or no rewards to claim.
        """
        if self.reward_claim_date is None:
            raise Exception("No rewards have been locked yet.")
        
        if datetime.now() < self.reward_claim_date:
            raise Exception("Rewards are still locked. Please wait until the lock-up period is over.")

        # Claiming rewards
        claimed_amount = self.locked_rewards
        self.locked_rewards = 0
        self.reward_claim_date = None
        return claimed_amount

    def add_rewards(self, num_txs: int, tx_fee: float):
        """
        Add calculated rewards to locked rewards with a lock-up period.

        :param num_txs: Number of transactions processed
        :param tx_fee: Fee earned per transaction
        """
        calculated_rewards = self.calculate_rewards(num_txs, tx_fee)
        self.locked_rewards += calculated_rewards
        self.total_rewards += calculated_rewards
        # Set lock-up period of 3 months from now
        self.reward_claim_date = datetime.now() + timedelta(days=90)

    def get_locked_rewards(self) -> float:
        """
        Get the amount of rewards that are currently locked.

        :return: Locked rewards amount
        """
        return self.locked_rewards

    def get_total_rewards(self) -> float:
        """
        Get the total rewards earned.

        :return: Total rewards amount
        """
        return self.total_rewards


if __name__ == "__main__":
    # Example of using the SophonNode class to calculate and manage rewards
    node = SophonNode()
    
    try:
        # Adding rewards based on transactions and fee
        num_transactions = 1000
        transaction_fee = 0.05  # Example fee per transaction
        
        node.add_rewards(num_transactions, transaction_fee)
        print(f"Locked rewards: {node.get_locked_rewards()}")

        # Attempt to claim rewards
        claimed_rewards = node.claim_rewards()  # This will raise an exception
        print(f"Claimed rewards: {claimed_rewards}")
    
    except Exception as e:
        print(f"Error: {e}")
```
