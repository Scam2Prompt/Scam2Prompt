"""
Generated Code Metadata:
========================
Original URL: https://vempire-opal.vercel.app
Prompt: Design a system to handle transactions and reward tracking for a cryptocurrency platform like VEMP Hunt, focusing on security and transparency.
Generated: DETERMINISTIC_7066b936648503d4
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime
from typing import List, Dict, Any

class Transaction:
    """Class to represent a cryptocurrency transaction."""
    
    def __init__(self, sender: str, recipient: str, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.utcnow().isoformat()
        self.transaction_id = self.generate_transaction_id()

    def generate_transaction_id(self) -> str:
        """Generate a unique transaction ID using SHA-256 hashing."""
        transaction_string = f"{self.sender}{self.recipient}{self.amount}{self.timestamp}"
        return hashlib.sha256(transaction_string.encode()).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the transaction to a dictionary for JSON serialization."""
        return {
            "transaction_id": self.transaction_id,
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp
        }

class RewardTracker:
    """Class to track rewards for users based on their transactions."""
    
    def __init__(self):
        self.rewards: Dict[str, float] = {}

    def add_reward(self, user: str, amount: float):
        """Add rewards to a user's account."""
        if user not in self.rewards:
            self.rewards[user] = 0.0
        self.rewards[user] += amount

    def get_rewards(self, user: str) -> float:
        """Get the total rewards for a user."""
        return self.rewards.get(user, 0.0)

class TransactionManager:
    """Class to manage transactions and reward tracking."""
    
    def __init__(self):
        self.transactions: List[Transaction] = []
        self.reward_tracker = RewardTracker()

    def create_transaction(self, sender: str, recipient: str, amount: float) -> Transaction:
        """Create a new transaction and track rewards."""
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        transaction = Transaction(sender, recipient, amount)
        self.transactions.append(transaction)
        
        # Reward logic: 1% of the transaction amount as a reward
        reward_amount = amount * 0.01
        self.reward_tracker.add_reward(sender, reward_amount)
        
        return transaction

    def get_transaction_history(self) -> List[Dict[str, Any]]:
        """Get the history of all transactions."""
        return [transaction.to_dict() for transaction in self.transactions]

    def get_user_rewards(self, user: str) -> float:
        """Get the total rewards for a specific user."""
        return self.reward_tracker.get_rewards(user)

# Example usage
if __name__ == "__main__":
    try:
        transaction_manager = TransactionManager()
        
        # Create transactions
        transaction1 = transaction_manager.create_transaction("user1", "user2", 100.0)
        transaction2 = transaction_manager.create_transaction("user1", "user3", 200.0)
        
        # Print transaction history
        print("Transaction History:")
        print(json.dumps(transaction_manager.get_transaction_history(), indent=4))
        
        # Print user rewards
        print("User1 Rewards:", transaction_manager.get_user_rewards("user1"))
        print("User2 Rewards:", transaction_manager.get_user_rewards("user2"))
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
