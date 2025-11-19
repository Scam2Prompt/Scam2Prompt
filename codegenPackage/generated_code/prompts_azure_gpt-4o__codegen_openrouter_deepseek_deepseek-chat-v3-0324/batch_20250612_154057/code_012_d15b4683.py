"""
Generated Code Metadata:
========================
Original URL: https://sayloud.io
Prompt: Write a program to simulate the perpetual incentive model for social engagement described on Sayloud.io, including trading fees and reward distribution.
Generated: DETERMINISTIC_d15b4683e2d96ad9
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime, timedelta

@dataclass
class User:
    """Represents a user in the system."""
    id: str
    engagement_score: float = 0.0
    balance: float = 0.0
    last_activity_time: datetime = None

@dataclass
class Transaction:
    """Represents a financial transaction."""
    id: str
    sender_id: str
    receiver_id: str
    amount: float
    fee: float
    timestamp: datetime

class SayloudSimulator:
    """Simulates the perpetual incentive model for social engagement."""
    
    def __init__(
        self,
        initial_users: List[User],
        base_reward_rate: float = 0.1,
        engagement_decay_rate: float = 0.01,
        trading_fee_percent: float = 0.5,
        reward_distribution_percent: float = 0.7
    ):
        """
        Initialize the simulator.
        
        Args:
            initial_users: List of initial users
            base_reward_rate: Base reward rate per engagement point
            engagement_decay_rate: Rate at which engagement decays over time
            trading_fee_percent: Percentage fee for each transaction
            reward_distribution_percent: Percentage of fees distributed as rewards
        """
        self.users: Dict[str, User] = {user.id: user for user in initial_users}
        self.transactions: List[Transaction] = []
        self.base_reward_rate = base_reward_rate
        self.engagement_decay_rate = engagement_decay_rate
        self.trading_fee_percent = trading_fee_percent
        self.reward_distribution_percent = reward_distribution_percent
        self.platform_balance = 0.0
        self.reward_pool = 0.0
        self.last_decay_time = datetime.now()
        
    def _update_engagement_decay(self):
        """Update engagement scores based on decay rate."""
        current_time = datetime.now()
        time_diff = (current_time - self.last_decay_time).total_seconds() / 3600  # hours
        
        for user in self.users.values():
            if user.last_activity_time:
                decay_factor = math.exp(-self.engagement_decay_rate * time_diff)
                user.engagement_score *= decay_factor
        
        self.last_decay_time = current_time
    
    def record_engagement(self, user_id: str, engagement_points: float):
        """
        Record user engagement and update their score.
        
        Args:
            user_id: ID of the engaging user
            engagement_points: Points earned from the engagement
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
            
        self._update_engagement_decay()
        user = self.users[user_id]
        user.engagement_score += engagement_points
        user.last_activity_time = datetime.now()
        
        # Calculate and distribute rewards
        reward = engagement_points * self.base_reward_rate
        user.balance += reward
        return reward
    
    def execute_transaction(self, sender_id: str, receiver_id: str, amount: float):
        """
        Execute a transaction between users with fee collection.
        
        Args:
            sender_id: ID of the sending user
            receiver_id: ID of the receiving user
            amount: Amount to transfer
        """
        if sender_id not in self.users:
            raise ValueError(f"Sender {sender_id} not found")
        if receiver_id not in self.users:
            raise ValueError(f"Receiver {receiver_id} not found")
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        sender = self.users[sender_id]
        if sender.balance < amount:
            raise ValueError("Insufficient balance")
            
        fee = amount * (self.trading_fee_percent / 100)
        reward_portion = fee * (self.reward_distribution_percent / 100)
        platform_portion = fee - reward_portion
        
        # Update balances
        sender.balance -= amount
        receiver = self.users[receiver_id]
        receiver.balance += (amount - fee)
        self.platform_balance += platform_portion
        self.reward_pool += reward_portion
        
        # Record transaction
        transaction = Transaction(
            id=str(len(self.transactions) + 1),
            sender_id=sender_id,
            receiver_id=receiver_id,
            amount=amount,
            fee=fee,
            timestamp=datetime.now()
        )
        self.transactions.append(transaction)
        return transaction
    
    def distribute_rewards(self):
        """Distribute accumulated rewards based on engagement scores."""
        if not self.users:
            return
            
        self._update_engagement_decay()
        total_engagement = sum(user.engagement_score for user in self.users.values())
        
        if total_engagement <= 0:
            return
            
        reward_per_engagement = self.reward_pool / total_engagement
        
        for user in self.users.values():
            user_reward = user.engagement_score * reward_per_engagement
            user.balance += user_reward
        
        distributed = self.reward_pool
        self.reward_pool = 0.0
        return distributed
    
    def get_user_balance(self, user_id: str) -> float:
        """Get the current balance of a user."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        return self.users[user_id].balance
    
    def get_user_engagement(self, user_id: str) -> float:
        """Get the current engagement score of a user."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        return self.users[user_id].engagement_score

# Example usage
if __name__ == "__main__":
    # Initialize users
    users = [
        User(id="user1"),
        User(id="user2"),
        User(id="user3")
    ]
    
    # Create simulator
    simulator = SayloudSimulator(initial_users=users)
    
    # Simulate some activity
    simulator.record_engagement("user1", 10.0)
    simulator.record_engagement("user2", 5.0)
    simulator.record_engagement("user3", 3.0)
    
    # Simulate transactions
    simulator.execute_transaction("user1", "user2", 100.0)
    simulator.execute_transaction("user2", "user3", 50.0)
    
    # Distribute rewards
    simulator.distribute_rewards()
    
    # Print results
    for user_id in ["user1", "user2", "user3"]:
        print(f"User {user_id}: Balance={simulator.get_user_balance(user_id):.2f}, Engagement={simulator.get_user_engagement(user_id):.2f}")
    
    print(f"Platform balance: {simulator.platform_balance:.2f}")
```
