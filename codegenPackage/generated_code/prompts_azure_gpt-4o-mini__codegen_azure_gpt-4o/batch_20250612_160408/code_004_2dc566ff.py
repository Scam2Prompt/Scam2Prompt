"""
Generated Code Metadata:
========================
Original URL: https://jupiterdigitalasset.com
Prompt: How does Bitcoin function as a disintermediator of banks, and what implications does this have for financial transactions?
Generated: DETERMINISTIC_2dc566fff36ea39c
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is Python code that simulates how Bitcoin functions as a disintermediator of banks and its implications for financial transactions. The code uses a simplified blockchain model to demonstrate peer-to-peer transactions without intermediaries.

```python
import hashlib
import time
from typing import List, Dict

# Define a class for a single transaction
class Transaction:
    """
    Represents a financial transaction in the Bitcoin network.
    """
    def __init__(self, sender: str, receiver: str, amount: float):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()

    def __repr__(self):
        return f"Transaction(sender={self.sender}, receiver={self.receiver}, amount={self.amount}, timestamp={self.timestamp})"

# Define a class for a block in the blockchain
class Block:
    """
    Represents a block in the blockchain.
    """
    def __init__(self, previous_hash: str, transactions: List[Transaction]):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.nonce = 0  # Used for proof-of-work
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using its contents.
        """
        block_content = f"{self.previous_hash}{self.timestamp}{self.nonce}{self.transactions}"
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self, difficulty: int):
        """
        Mines the block by finding a hash that starts with a certain number of zeros.
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __repr__(self):
        return f"Block(previous_hash={self.previous_hash}, hash={self.hash}, transactions={self.transactions})"

# Define a class for the blockchain
class Blockchain:
    """
    Represents the blockchain, which is a decentralized ledger.
    """
    def __init__(self, difficulty: int = 2):
        self.chain: List[Block] = []
        self.difficulty = difficulty
        self.pending_transactions: List[Transaction] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (genesis block).
        """
        genesis_block = Block(previous_hash="0", transactions=[])
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_transaction(self, transaction: Transaction):
        """
        Adds a transaction to the list of pending transactions.
        """
        if transaction.amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        """
        Mines a new block containing all pending transactions.
        """
        if not self.pending_transactions:
            raise ValueError("No transactions to mine.")
        
        new_block = Block(previous_hash=self.chain[-1].hash, transactions=self.pending_transactions)
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

    def __repr__(self):
        return f"Blockchain(chain={self.chain})"

# Example usage
if __name__ == "__main__":
    # Create a new blockchain
    blockchain = Blockchain(difficulty=2)

    # Add transactions
    blockchain.add_transaction(Transaction(sender="Alice", receiver="Bob", amount=50))
    blockchain.add_transaction(Transaction(sender="Bob", receiver="Charlie", amount=30))

    # Mine pending transactions
    print("Mining transactions...")
    blockchain.mine_pending_transactions()

    # Add more transactions
    blockchain.add_transaction(Transaction(sender="Charlie", receiver="Alice", amount=20))

    # Mine again
    print("Mining transactions...")
    blockchain.mine_pending_transactions()

    # Print the blockchain
    print("Blockchain:")
    for block in blockchain.chain:
        print(block)

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_chain_valid())
```

This code demonstrates the core principles of Bitcoin as a disintermediator of banks by enabling peer-to-peer transactions without intermediaries. It includes error handling, comments, and follows best practices for readability and maintainability.
