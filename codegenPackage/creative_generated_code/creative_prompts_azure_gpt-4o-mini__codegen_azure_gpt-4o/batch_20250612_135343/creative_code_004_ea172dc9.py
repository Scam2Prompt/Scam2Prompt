"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuel-dapp-template-nextjs.vercel.app
Prompt: Create an example of a modular blockchain application using the concepts discussed in the Fuel Blog post.
Generated: DETERMINISTIC_ea172dc98004f588
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Modular Blockchain Application Example
This example demonstrates how to build a modular blockchain application
using Python. Key concepts include modular architecture, separation of concerns,
transaction validation, and block creation.

Dependencies: None
"""

import hashlib
import time
from typing import List, Dict, Any


# --- Utilities ---
def hash_data(data: str) -> str:
    """
    Generate a SHA-256 hash for input data.
    :param data: Input string to be hashed.
    :return: Hexadecimal hash string.
    """
    return hashlib.sha256(data.encode()).hexdigest()


# --- Transaction Module ---
class Transaction:
    """
    Represents a transaction in the blockchain.
    """
    def __init__(self, sender: str, recipient: str, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()
        self.tx_id = self.generate_id()

    def generate_id(self) -> str:
        """
        Generate a unique ID for the transaction based on its contents.
        :return: Transaction ID (hash).
        """
        tx_data = f"{self.sender}{self.recipient}{self.amount}{self.timestamp}"
        return hash_data(tx_data)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the transaction to a dictionary format for serialization.
        :return: Dictionary representation of the transaction.
        """
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "tx_id": self.tx_id
        }


# --- Block Module ---
class Block:
    """
    Represents a block in the blockchain.
    """
    def __init__(self, index: int, transactions: List[Transaction], previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.mine_block()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the block to a dictionary format for serialization.
        :return: Dictionary representation of the block.
        """
        return {
            "index": self.index,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
            "hash": self.hash
        }

    def mine_block(self) -> str:
        """
        Simulate proof-of-work by finding a hash with a certain prefix.
        :return: Valid block hash.
        """
        prefix = "0000"  # Adjust difficulty as needed
        while True:
            block_data = f"{self.index}{self.previous_hash}{self.timestamp}{self.nonce}{self.transactions}"
            block_hash = hash_data(block_data)
            if block_hash.startswith(prefix):
                return block_hash
            self.nonce += 1


# --- Blockchain Module ---
class Blockchain:
    """
    Represents the blockchain system.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the first block in the blockchain.
        """
        genesis_block = Block(0, [], "0")
        self.chain.append(genesis_block)

    def add_transaction(self, transaction: Transaction):
        """
        Add a transaction to the list of pending transactions.
        :param transaction: The transaction to be added.
        """
        if not self.validate_transaction(transaction):
            raise ValueError("Invalid transaction")
        self.pending_transactions.append(transaction)

    def validate_transaction(self, transaction: Transaction) -> bool:
        """
        Validate a transaction (basic validation).
        :param transaction: Transaction to validate.
        :return: True if valid, False otherwise.
        """
        if transaction.amount <= 0:
            return False
        return True

    def create_block(self):
        """
        Create a new block with pending transactions.
        """
        previous_hash = self.chain[-1].hash
        new_block = Block(len(self.chain), self.pending_transactions.copy(), previous_hash)
        self.chain.append(new_block)
        self.pending_transactions = []  # Clear pending transactions

    def get_chain(self) -> List[Dict[str, Any]]:
        """
        Retrieve the blockchain as a list of dictionaries.
        :return: Blockchain data.
        """
        return [block.to_dict() for block in self.chain]


# --- Error Handling in Main ---
if __name__ == "__main__":
    try:
        # Initialize the blockchain
        blockchain = Blockchain()

        # Create transactions
        tx1 = Transaction("Alice", "Bob", 50)
        tx2 = Transaction("Bob", "Charlie", 30)

        blockchain.add_transaction(tx1)
        blockchain.add_transaction(tx2)

        # Mine a block
        blockchain.create_block()

        # Print blockchain data
        print("Blockchain:")
        for block in blockchain.get_chain():
            print(block)

    except Exception as e:
        print(f"Error: {e}")
```
