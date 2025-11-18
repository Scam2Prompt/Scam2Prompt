"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dee-lance.pages.dev
Prompt: Generate code for a blockchain-based dispute resolution system for freelance contracts, incorporating the decentralized features described in DeeLance's ecosystem.
Generated: DETERMINISTIC_98b03b495c47c787
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from hashlib import sha256
import json
from typing import List, Optional

class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = self._get_current_timestamp()
        self.transaction_id = self._generate_transaction_id()

    def _get_current_timestamp(self) -> str:
        from datetime import datetime
        return datetime.utcnow().isoformat()

    def _generate_transaction_id(self) -> str:
        transaction_string = f"{self.sender}{self.receiver}{self.amount}{self.timestamp}"
        return sha256(transaction_string.encode()).hexdigest()

    def to_dict(self) -> dict:
        return {
            "transaction_id": self.transaction_id,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp,
        }

class Block:
    def __init__(self, transactions: List[Transaction], previous_hash: Optional[str] = None):
        self.index = 0
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = self._get_current_timestamp()
        self.hash = self._generate_block_hash()

    def _get_current_timestamp(self) -> str:
        from datetime import datetime
        return datetime.utcnow().isoformat()

    def _generate_block_hash(self) -> str:
        block_string = json.dumps([tx.to_dict() for tx in self.transactions]) + self.previous_hash + self.timestamp
        return sha256(block_string.encode()).hexdigest()

    def to_dict(self) -> dict:
        return {
            "index": self.index,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "hash": self.hash,
        }

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(transactions=[], previous_hash='0')
        self.chain.append(genesis_block)

    def add_transaction(self, sender: str, receiver: str, amount: float):
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")
        transaction = Transaction(sender, receiver, amount)
        self.pending_transactions.append(transaction)

    def mine_block(self):
        if not self.pending_transactions:
            raise ValueError("No transactions to mine")
        
        last_block = self.chain[-1]
        new_block = Block(transactions=self.pending_transactions, previous_hash=last_block.hash)
        new_block.index = len(self.chain) + 1
        self.chain.append(new_block)
        self.pending_transactions = []  # Reset the pending transactions

    def to_dict(self) -> dict:
        return {
            "chain": [block.to_dict() for block in self.chain],
            "pending_transactions": [tx.to_dict() for tx in self.pending_transactions],
        }

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()

    # Adding transactions
    try:
        blockchain.add_transaction(sender="Alice", receiver="Bob", amount=50)
        blockchain.add_transaction(sender="Bob", receiver="Charlie", amount=30)
        
        # Mining a new block
        blockchain.mine_block()

        # Displaying the blockchain
        print(json.dumps(blockchain.to_dict(), indent=4))
    except ValueError as e:
        print(f"Error: {e}")
```
