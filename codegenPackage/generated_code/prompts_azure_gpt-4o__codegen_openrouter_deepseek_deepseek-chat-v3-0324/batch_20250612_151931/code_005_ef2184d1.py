"""
Generated Code Metadata:
========================
Original URL: https://bananagunn.io
Prompt: Create a system that tracks reward forfeiture when a user sells or transfers more than 300 $BANANA tokens during an epoch, redistributing forfeited rewards among other holders.
Generated: DETERMINISTIC_ef2184d103ef70a7
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class User:
    address: str
    balance: float
    rewards: float = 0.0
    forfeited_rewards: float = 0.0

@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: float
    timestamp: float

class RewardForfeitureSystem:
    def __init__(self, epoch_duration: int = 604800):  # Default: 1 week in seconds
        self.users: Dict[str, User] = {}
        self.transactions: List[Transaction] = []
        self.epoch_start_time: float = time.time()
        self.epoch_duration: int = epoch_duration
        self.forfeiture_threshold: float = 300.0  # 300 BANANA tokens

    def add_user(self, address: str, initial_balance: float = 0.0) -> None:
        """Add a new user to the system with an initial balance."""
        if address not in self.users:
            self.users[address] = User(address=address, balance=initial_balance)

    def record_transaction(self, sender: str, receiver: str, amount: float) -> None:
        """Record a transaction between users."""
        if sender not in self.users or receiver not in self.users:
            raise ValueError("Sender or receiver not found in system")
        
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")
            
        if self.users[sender].balance < amount:
            raise ValueError("Insufficient balance")
            
        transaction = Transaction(
            sender=sender,
            receiver=receiver,
            amount=amount,
            timestamp=time.time()
        )
        self.transactions.append(transaction)
        
        # Update balances
        self.users[sender].balance -= amount
        self.users[receiver].balance += amount

    def _is_new_epoch(self) -> bool:
        """Check if a new epoch has started."""
        return time.time() >= self.epoch_start_time + self.epoch_duration

    def _start_new_epoch(self) -> None:
        """Initialize a new epoch."""
        self.epoch_start_time = time.time()
        self.transactions = []  # Clear transactions for new epoch

    def calculate_forfeitures(self) -> Tuple[Dict[str, float], float]:
        """
        Calculate forfeited rewards for users who exceeded the threshold.
        Returns tuple of (forfeited_users, total_forfeited)
        """
        if not self._is_new_epoch():
            return {}, 0.0

        # Calculate total transfers per user in this epoch
        user_transfers: Dict[str, float] = {}
        for tx in self.transactions:
            if tx.sender not in user_transfers:
                user_transfers[tx.sender] = 0.0
            user_transfers[tx.sender] += tx.amount

        # Identify users who exceeded threshold
        forfeited_users = {}
        total_forfeited = 0.0
        for address, amount in user_transfers.items():
            if amount > self.forfeiture_threshold:
                forfeited_amount = self.users[address].rewards
                forfeited_users[address] = forfeited_amount
                total_forfeited += forfeited_amount
                self.users[address].forfeited_rewards += forfeited_amount
                self.users[address].rewards = 0.0

        self._start_new_epoch()
        return forfeited_users, total_forfeited

    def redistribute_forfeited_rewards(self, total_forfeited: float) -> None:
        """Redistribute forfeited rewards proportionally to all other holders."""
        if total_forfeited <= 0:
            return

        # Calculate total balance of all non-forfeiting users
        total_balance = sum(
            user.balance for address, user in self.users.items() 
            if user.forfeited_rewards == 0
        )

        if total_balance == 0:
            return  # No one to redistribute to

        # Redistribute proportionally
        for address, user in self.users.items():
            if user.forfeited_rewards == 0 and user.balance > 0:
                share = user.balance / total_balance
                additional_reward = total_forfeited * share
                user.rewards += additional_reward

    def process_epoch(self) -> None:
        """Process the current epoch: calculate and redistribute forfeitures."""
        forfeited_users, total_forfeited = self.calculate_forfeitures()
        self.redistribute_forfeited_rewards(total_forfeited)

    def distribute_rewards(self, reward_pool: float) -> None:
        """Distribute rewards proportionally to all users based on their balance."""
        if reward_pool <= 0:
            raise ValueError("Reward pool must be positive")

        total_balance = sum(user.balance for user in self.users.values())
        if total_balance == 0:
            return  # No one to distribute to

        for user in self.users.values():
            share = user.balance / total_balance
            user.rewards += reward_pool * share

    def get_user_info(self, address: str) -> Dict[str, float]:
        """Get user information including balance and rewards."""
        if address not in self.users:
            raise ValueError("User not found")
        
        user = self.users[address]
        return {
            "balance": user.balance,
            "rewards": user.rewards,
            "forfeited_rewards": user.forfeited_rewards
        }
```
