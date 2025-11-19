"""
Generated Code Metadata:
========================
Original URL: https://projectdeksa.pages.dev
Prompt: "Design a basic virtual economy system using $MASA token, allowing users to earn, trade, and contribute to the ecosystem."
Generated: DETERMINISTIC_29cd110bf16e8999
Batch ID: 20250622_204830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
Basic Virtual Economy System for $MASA Token
Features:
- Token minting/burning
- User balances
- Basic trading functionality
- Contribution rewards
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
import hashlib
import json
from datetime import datetime

class VirtualEconomyError(Exception):
    """Base exception for virtual economy system errors"""
    pass

class InsufficientBalanceError(VirtualEconomyError):
    """Raised when user doesn't have enough tokens"""
    pass

class InvalidTransactionError(VirtualEconomyError):
    """Raised for invalid transaction attempts"""
    pass

@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: float
    timestamp: str
    tx_hash: str
    description: Optional[str] = None

    def to_dict(self) -> Dict:
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "tx_hash": self.tx_hash,
            "description": self.description
        }

class MASATokenEconomy:
    def __init__(self):
        self.balances: Dict[str, float] = {}
        self.transactions: List[Transaction] = []
        self.total_supply: float = 0.0
        self.contribution_rewards: Dict[str, float] = {
            "content_creation": 10.0,
            "bug_report": 5.0,
            "community_moderation": 7.5
        }

    def _generate_tx_hash(self, sender: str, receiver: str, amount: float) -> str:
        """Generate a unique transaction hash"""
        tx_string = f"{sender}{receiver}{amount}{datetime.now().isoformat()}"
        return hashlib.sha256(tx_string.encode()).hexdigest()

    def create_user(self, user_id: str) -> None:
        """Initialize a new user with zero balance"""
        if user_id in self.balances:
            raise VirtualEconomyError(f"User {user_id} already exists")
        self.balances[user_id] = 0.0

    def get_balance(self, user_id: str) -> float:
        """Get user's current balance"""
        if user_id not in self.balances:
            raise VirtualEconomyError(f"User {user_id} not found")
        return self.balances[user_id]

    def mint(self, user_id: str, amount: float) -> Transaction:
        """Mint new tokens to a user"""
        if user_id not in self.balances:
            raise VirtualEconomyError(f"User {user_id} not found")
        if amount <= 0:
            raise InvalidTransactionError("Amount must be positive")

        self.balances[user_id] += amount
        self.total_supply += amount

        tx = Transaction(
            sender="system",
            receiver=user_id,
            amount=amount,
            timestamp=datetime.now().isoformat(),
            tx_hash=self._generate_tx_hash("system", user_id, amount),
            description="Token mint"
        )
        self.transactions.append(tx)
        return tx

    def burn(self, user_id: str, amount: float) -> Transaction:
        """Burn tokens from a user's balance"""
        if user_id not in self.balances:
            raise VirtualEconomyError(f"User {user_id} not found")
        if amount <= 0:
            raise InvalidTransactionError("Amount must be positive")
        if self.balances[user_id] < amount:
            raise InsufficientBalanceError(f"Insufficient balance for {user_id}")

        self.balances[user_id] -= amount
        self.total_supply -= amount

        tx = Transaction(
            sender=user_id,
            receiver="system",
            amount=amount,
            timestamp=datetime.now().isoformat(),
            tx_hash=self._generate_tx_hash(user_id, "system", amount),
            description="Token burn"
        )
        self.transactions.append(tx)
        return tx

    def transfer(
        self,
        sender: str,
        receiver: str,
        amount: float,
        description: Optional[str] = None
    ) -> Transaction:
        """Transfer tokens between users"""
        if sender not in self.balances:
            raise VirtualEconomyError(f"Sender {sender} not found")
        if receiver not in self.balances:
            raise VirtualEconomyError(f"Receiver {receiver} not found")
        if amount <= 0:
            raise InvalidTransactionError("Amount must be positive")
        if self.balances[sender] < amount:
            raise InsufficientBalanceError(f"Insufficient balance for {sender}")

        self.balances[sender] -= amount
        self.balances[receiver] += amount

        tx = Transaction(
            sender=sender,
            receiver=receiver,
            amount=amount,
            timestamp=datetime.now().isoformat(),
            tx_hash=self._generate_tx_hash(sender, receiver, amount),
            description=description
        )
        self.transactions.append(tx)
        return tx

    def reward_contribution(self, user_id: str, contribution_type: str) -> Transaction:
        """Reward user for ecosystem contributions"""
        if user_id not in self.balances:
            raise VirtualEconomyError(f"User {user_id} not found")
        if contribution_type not in self.contribution_rewards:
            raise InvalidTransactionError(f"Invalid contribution type: {contribution_type}")

        reward_amount = self.contribution_rewards[contribution_type]
        return self.mint(user_id, reward_amount)

    def get_transaction_history(self, user_id: str) -> List[Dict]:
        """Get transaction history for a user"""
        return [
            tx.to_dict() for tx in self.transactions
            if tx.sender == user_id or tx.receiver == user_id
        ]

    def save_state(self, filepath: str) -> None:
        """Save economy state to file"""
        state = {
            "balances": self.balances,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "total_supply": self.total_supply
        }
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)

    def load_state(self, filepath: str) -> None:
        """Load economy state from file"""
        with open(filepath, 'r') as f:
            state = json.load(f)
        
        self.balances = state["balances"]
        self.total_supply = state["total_supply"]
        self.transactions = [
            Transaction(
                tx["sender"],
                tx["receiver"],
                tx["amount"],
                tx["timestamp"],
                tx["tx_hash"],
                tx.get("description")
            ) for tx in state["transactions"]
        ]

# Example usage
if __name__ == "__main__":
    economy = MASATokenEconomy()
    
    # Create users
    economy.create_user("alice")
    economy.create_user("bob")
    
    # Mint initial tokens
    economy.mint("alice", 100.0)
    economy.mint("bob", 50.0)
    
    # Transfer between users
    economy.transfer("alice", "bob", 25.0, "Payment for services")
    
    # Reward contributions
    economy.reward_contribution("bob", "content_creation")
    
    # Check balances
    print("Alice balance:", economy.get_balance("alice"))
    print("Bob balance:", economy.get_balance("bob"))
    
    # Save state
    economy.save_state("economy_state.json")
```
