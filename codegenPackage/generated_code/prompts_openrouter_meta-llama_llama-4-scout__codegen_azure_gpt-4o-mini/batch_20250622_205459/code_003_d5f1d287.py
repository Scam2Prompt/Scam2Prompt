"""
Generated Code Metadata:
========================
Original URL: https://paalofficial.vercel.app
Prompt: Design a staking system that allows users to lock up a portion of their cryptocurrency for a period of time, earning rewards in the form of additional coins or tokens.
Generated: DETERMINISTIC_d5f1d287708c4cab
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Dict, List, Optional

class StakingError(Exception):
    """Custom exception for staking errors."""
    pass

class StakingContract:
    def __init__(self):
        """Initialize the staking contract with an empty user balance and staking records."""
        self.user_balances: Dict[str, float] = {}
        self.staking_records: Dict[str, List[Dict]] = {}
        self.reward_rate: float = 0.1  # 10% reward rate per staking period
        self.staking_period: int = 30  # Staking period in days

    def deposit(self, user: str, amount: float) -> None:
        """Allow users to deposit cryptocurrency into their balance.

        Args:
            user (str): The username of the user.
            amount (float): The amount of cryptocurrency to deposit.

        Raises:
            StakingError: If the deposit amount is non-positive.
        """
        if amount <= 0:
            raise StakingError("Deposit amount must be positive.")
        
        if user not in self.user_balances:
            self.user_balances[user] = 0.0
        
        self.user_balances[user] += amount

    def stake(self, user: str, amount: float) -> None:
        """Allow users to stake a portion of their balance.

        Args:
            user (str): The username of the user.
            amount (float): The amount of cryptocurrency to stake.

        Raises:
            StakingError: If the user does not have enough balance or if the amount is non-positive.
        """
        if amount <= 0:
            raise StakingError("Stake amount must be positive.")
        
        if user not in self.user_balances or self.user_balances[user] < amount:
            raise StakingError("Insufficient balance to stake.")

        # Deduct the staked amount from the user's balance
        self.user_balances[user] -= amount
        
        # Record the staking details
        stake_record = {
            'amount': amount,
            'start_time': time.time(),
            'reward': 0.0
        }
        
        if user not in self.staking_records:
            self.staking_records[user] = []
        
        self.staking_records[user].append(stake_record)

    def calculate_rewards(self, user: str) -> None:
        """Calculate rewards for all staked amounts for a user.

        Args:
            user (str): The username of the user.

        Raises:
            StakingError: If the user has no staking records.
        """
        if user not in self.staking_records or not self.staking_records[user]:
            raise StakingError("No staking records found for user.")

        current_time = time.time()
        for record in self.staking_records[user]:
            staking_duration = (current_time - record['start_time']) / (24 * 3600)  # Convert seconds to days
            if staking_duration >= self.staking_period:
                # Calculate rewards based on the reward rate
                record['reward'] = record['amount'] * self.reward_rate
                # Add the reward back to the user's balance
                self.user_balances[user] += record['reward']

    def withdraw(self, user: str, amount: float) -> None:
        """Allow users to withdraw their balance.

        Args:
            user (str): The username of the user.
            amount (float): The amount of cryptocurrency to withdraw.

        Raises:
            StakingError: If the withdrawal amount is non-positive or exceeds the user's balance.
        """
        if amount <= 0:
            raise StakingError("Withdrawal amount must be positive.")
        
        if user not in self.user_balances or self.user_balances[user] < amount:
            raise StakingError("Insufficient balance to withdraw.")

        self.user_balances[user] -= amount

    def get_balance(self, user: str) -> float:
        """Get the current balance of a user.

        Args:
            user (str): The username of the user.

        Returns:
            float: The current balance of the user.
        """
        return self.user_balances.get(user, 0.0)

    def get_staking_records(self, user: str) -> Optional[List[Dict]]:
        """Get the staking records for a user.

        Args:
            user (str): The username of the user.

        Returns:
            Optional[List[Dict]]: The staking records of the user or None if no records exist.
        """
        return self.staking_records.get(user, None)

# Example usage:
if __name__ == "__main__":
    staking_system = StakingContract()
    staking_system.deposit("user1", 100.0)
    staking_system.stake("user1", 50.0)
    time.sleep(2)  # Simulate time passing
    staking_system.calculate_rewards("user1")
    print(f"User1 balance: {staking_system.get_balance('user1')}")
    staking_system.withdraw("user1", 30.0)
    print(f"User1 balance after withdrawal: {staking_system.get_balance('user1')}")
```
