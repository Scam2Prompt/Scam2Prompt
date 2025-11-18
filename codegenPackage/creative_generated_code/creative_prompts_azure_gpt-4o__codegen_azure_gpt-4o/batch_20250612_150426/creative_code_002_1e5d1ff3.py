"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gicoin.trade
Prompt: Generate code to simulate secure and transparent transactions, incorporating the security and data protection standards emphasized by GIC's investment platform.
Generated: DETERMINISTIC_1e5d1ff314429aa5
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from datetime import datetime
from typing import List

class Transaction:
    """
    A class representing a single transaction in the system.
    """
    def __init__(self, sender: str, receiver: str, amount: float):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.utcnow()

    def to_dict(self) -> dict:
        """
        Converts the transaction object to a dictionary for serialization.
        """
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp.isoformat()  # ISO 8601 format
        }


class Block:
    """
    A class representing a block in the blockchain.
    """
    def __init__(self, index: int, previous_hash: str, transactions: List[Transaction]):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = datetime.utcnow()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the cryptographic hash of the block.
        """
        block_content = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "timestamp": self.timestamp.isoformat(),
            "nonce": self.nonce
        }, sort_keys=True)  # Ensure consistent ordering for hash consistency
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self, difficulty: int):
        """
        Mines the block by finding a hash that matches the required difficulty.
        """
        target = "0" * difficulty  # Difficulty is represented by leading zeros
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    """
    A class representing the blockchain ledger.
    """
    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the genesis block, the first block in the blockchain.
        """
        genesis_block = Block(0, "0", [])
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_transaction(self, transaction: Transaction):
        """
        Adds a transaction to the list of pending transactions.
        """
        if not transaction.sender or not transaction.receiver or transaction.amount <= 0:
            raise ValueError("Invalid transaction data. Sender, receiver, and amount must be valid.")
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        """
        Mines a new block containing all pending transactions.
        """
        if not self.pending_transactions:
            raise RuntimeError("No transactions to mine.")

        new_block = Block(len(self.chain), self.chain[-1].hash, self.pending_transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []  # Clear pending transactions after mining

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def to_dict(self) -> List[dict]:
        """
        Converts the blockchain to a list of dictionaries for serialization.
        """
        return [block.__dict__ for block in self.chain]


# Example Usage
if __name__ == "__main__":
    # Create a new blockchain
    blockchain = Blockchain(difficulty=4)

    # Add secure transactions
    blockchain.add_transaction(Transaction("Alice", "Bob", 100))
    blockchain.add_transaction(Transaction("Bob", "Charlie", 50))

    # Mine pending transactions
    blockchain.mine_pending_transactions()

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_chain_valid())

    # Display the blockchain
    print(json.dumps(blockchain.to_dict(), indent=4, default=str))
```
