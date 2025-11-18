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
import time
from datetime import datetime, timedelta

class SophonNodeRewards:
    def __init__(self, transaction_fee: float):
        """
        Initialize the SophonNodeRewards calculator.
        :param transaction_fee: Fee per transaction (in the corresponding currency).
        """
        if transaction_fee <= 0:
            raise ValueError("Transaction fee must be a positive number.")
        self.transaction_fee = transaction_fee
        self.total_rewards = 0.0  # Total rewards accumulated
        self.locked_rewards = 0.0  # Rewards currently in lock-up
        self.lockup_end_time = None  # Timestamp indicating when lock-up ends
        
    def calculate_rewards(self, num_transactions: int) -> float:
        """
        Calculate rewards based on the number of transactions processed.
        :param num_transactions: Number of transactions processed by the node.
        :return: Rewards earned from the transactions.
        """
        if num_transactions < 0:
            raise ValueError("Number of transactions cannot be negative.")
        rewards = num_transactions * self.transaction_fee
        self.total_rewards += rewards
        return rewards
    
    def claim_rewards(self) -> str:
        """
        Claim the rewards. Rewards are locked for a 3-month period.
        :return: Message indicating the status of the claim.
        """
        if self.lockup_end_time and datetime.now() < self.lockup_end_time:
            return f"Rewards are still locked until {self.lockup_end_time.strftime('%Y-%m-%d %H:%M:%S')}"
        
        self.locked_rewards = self.total_rewards
        self.total_rewards = 0.0  # Reset total rewards after claim
        self.lockup_end_time = datetime.now() + timedelta(days=90)  # Set the lock-up period
        return f"Rewards claimed successfully. Lock-up ends on {self.lockup_end_time.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def check_locked_rewards(self) -> str:
        """
        Check the status of locked rewards and the lock-up period.
        :return: Status message regarding locked rewards.
        """
        if not self.locked_rewards:
            return "No rewards are currently locked."
        
        if datetime.now() >= self.lockup_end_time:
            unlocked_rewards = self.locked_rewards
            self.locked_rewards = 0.0  # Unlock rewards
            self.lockup_end_time = None  # Reset lock-up end time
            return f"Rewards unlocked: {unlocked_rewards:.2f}"
        else:
            remaining_time = self.lockup_end_time - datetime.now()
            return f"Rewards are locked. Time remaining: {remaining_time.days} days, {remaining_time.seconds // 3600} hours, {(remaining_time.seconds // 60) % 60} minutes."
    
if __name__ == "__main__":
    try:
        # Initialize the rewards system with a transaction fee of 0.01
        node_rewards = SophonNodeRewards(transaction_fee=0.01)
        
        # Simulate processing some transactions
        print(f"Rewards earned: {node_rewards.calculate_rewards(num_transactions=100):.2f}")
        
        # Claim rewards
        print(node_rewards.claim_rewards())
        
        # Check locked rewards status
        print(node_rewards.check_locked_rewards())
        
        # Force wait to simulate unlocking (in production, this would take actual 3 months)
        time.sleep(1)  # Simulated delay for demonstration purposes
        print(node_rewards.check_locked_rewards())
    
    except Exception as e:
        print(f"Error: {e}")
```
