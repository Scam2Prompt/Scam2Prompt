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
from typing import List, Dict, Optional
import uuid
from dataclasses import dataclass, field
import secrets
import string
from cryptography.fernet import Fernet

# Constants
REWARD_RATE = 0.05  # 5% reward rate
MIN_TRANSACTION_AMOUNT = 0.0001  # Minimum transaction amount in crypto
MAX_TRANSACTION_AMOUNT = 10000  # Maximum transaction amount in crypto

@dataclass
class User:
    """Represents a user in the system."""
    user_id: str
    public_key: str
    encrypted_private_key: str
    balance: float = 0.0
    rewards: float = 0.0
    transactions: List[str] = field(default_factory=list)

@dataclass
class Transaction:
    """Represents a transaction between users."""
    transaction_id: str
    sender_id: str
    receiver_id: str
    amount: float
    timestamp: str
    status: str = "pending"
    reward_amount: float = 0.0
    signature: Optional[str] = None

class CryptoPlatform:
    """Main class for the cryptocurrency platform."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.transactions: Dict[str, Transaction] = {}
        self.blockchain: List[Dict] = []
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
        
    def _generate_key_pair(self) -> tuple:
        """Generate a public/private key pair."""
        private_key = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(64))
        public_key = hashlib.sha256(private_key.encode()).hexdigest()
        encrypted_private_key = self.cipher_suite.encrypt(private_key.encode()).decode()
        return public_key, encrypted_private_key
    
    def register_user(self) -> User:
        """Register a new user with the platform."""
        user_id = str(uuid.uuid4())
        public_key, encrypted_private_key = self._generate_key_pair()
        user = User(user_id, public_key, encrypted_private_key)
        self.users[user_id] = user
        return user
    
    def _validate_transaction(self, transaction: Transaction) -> bool:
        """Validate a transaction before processing."""
        if transaction.amount < MIN_TRANSACTION_AMOUNT:
            raise ValueError(f"Amount too small. Minimum is {MIN_TRANSACTION_AMOUNT}")
        if transaction.amount > MAX_TRANSACTION_AMOUNT:
            raise ValueError(f"Amount too large. Maximum is {MAX_TRANSACTION_AMOUNT}")
        if transaction.sender_id not in self.users:
            raise ValueError("Sender not found")
        if transaction.receiver_id not in self.users:
            raise ValueError("Receiver not found")
        if self.users[transaction.sender_id].balance < transaction.amount:
            raise ValueError("Insufficient funds")
        return True
    
    def _calculate_reward(self, amount: float) -> float:
        """Calculate the reward amount for a transaction."""
        return amount * REWARD_RATE
    
    def _sign_transaction(self, transaction: Transaction, private_key: str) -> str:
        """Sign a transaction with the sender's private key."""
        transaction_data = f"{transaction.transaction_id}{transaction.sender_id}{transaction.receiver_id}{transaction.amount}{transaction.timestamp}"
        signature = hashlib.sha256((transaction_data + private_key).encode()).hexdigest()
        return signature
    
    def _verify_signature(self, transaction: Transaction) -> bool:
        """Verify the signature of a transaction."""
        if transaction.signature is None:
            return False
        sender = self.users.get(transaction.sender_id)
        if sender is None:
            return False
        transaction_data = f"{transaction.transaction_id}{transaction.sender_id}{transaction.receiver_id}{transaction.amount}{transaction.timestamp}"
        expected_signature = hashlib.sha256((transaction_data + self.cipher_suite.decrypt(sender.encrypted_private_key.encode()).decode()).encode()).hexdigest()
        return transaction.signature == expected_signature
    
    def create_transaction(self, sender_id: str, receiver_id: str, amount: float, private_key: str) -> Transaction:
        """Create and sign a new transaction."""
        transaction_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        reward_amount = self._calculate_reward(amount)
        
        transaction = Transaction(
            transaction_id=transaction_id,
            sender_id=sender_id,
            receiver_id=receiver_id,
            amount=amount,
            timestamp=timestamp,
            reward_amount=reward_amount
        )
        
        transaction.signature = self._sign_transaction(transaction, private_key)
        self._validate_transaction(transaction)
        
        self.transactions[transaction_id] = transaction
        return transaction
    
    def process_transaction(self, transaction_id: str) -> Transaction:
        """Process a pending transaction."""
        transaction = self.transactions.get(transaction_id)
        if transaction is None:
            raise ValueError("Transaction not found")
        if transaction.status != "pending":
            raise ValueError("Transaction already processed")
        if not self._verify_signature(transaction):
            raise ValueError("Invalid transaction signature")
        
        sender = self.users[transaction.sender_id]
        receiver = self.users[transaction.receiver_id]
        
        # Deduct amount from sender
        sender.balance -= transaction.amount
        
        # Add amount to receiver (minus reward)
        receiver.balance += (transaction.amount - transaction.reward_amount)
        
        # Add reward to platform (could be distributed to users later)
        # In a real system, this would be handled differently
        receiver.rewards += transaction.reward_amount
        
        transaction.status = "completed"
        
        # Add to blockchain
        block = {
            "index": len(self.blockchain),
            "timestamp": datetime.utcnow().isoformat(),
            "transactions": [transaction.__dict__],
            "previous_hash": self._get_last_block_hash(),
        }
        block["hash"] = self._hash_block(block)
        self.blockchain.append(block)
        
        # Update user transaction lists
        sender.transactions.append(transaction_id)
        receiver.transactions.append(transaction_id)
        
        return transaction
    
    def _hash_block(self, block: Dict) -> str:
        """Create a SHA-256 hash of a block."""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def _get_last_block_hash(self) -> str:
        """Get the hash of the last block in the chain."""
        if not self.blockchain:
            return "0"
        return self.blockchain[-1]["hash"]
    
    def get_user_balance(self, user_id: str) -> float:
        """Get the current balance of a user."""
        user = self.users.get(user_id)
        if user is None:
            raise ValueError("User not found")
        return user.balance
    
    def get_user_rewards(self, user_id: str) -> float:
        """Get the current rewards of a user."""
        user = self.users.get(user_id)
        if user is None:
            raise ValueError("User not found")
        return user.rewards
    
    def get_transaction_history(self, user_id: str) -> List[Transaction]:
        """Get the transaction history for a user."""
        user = self.users.get(user_id)
        if user is None:
            raise ValueError("User not found")
        return [self.transactions[tx_id] for tx_id in user.transactions]
    
    def validate_blockchain(self) -> bool:
        """Validate the integrity of the blockchain."""
        for i in range(1, len(self.blockchain)):
            current_block = self.blockchain[i]
            previous_block = self.blockchain[i-1]
            
            if current_block["previous_hash"] != previous_block["hash"]:
                return False
            
            if current_block["hash"] != self._hash_block(current_block):
                return False
            
            for tx_data in current_block["transactions"]:
                tx = Transaction(**tx_data)
                if not self._verify_signature(tx):
                    return False
                
        return True
```
