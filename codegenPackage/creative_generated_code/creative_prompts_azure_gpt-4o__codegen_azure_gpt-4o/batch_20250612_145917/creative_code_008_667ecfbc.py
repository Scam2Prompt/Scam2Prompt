"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-labs.vercel.app
Prompt: Design a blockchain-based payment system using Sonic's infrastructure that supports real-time payments with sub-second confirmation times and low transaction costs.
Generated: DETERMINISTIC_667ecfbc6959016d
Batch ID: 20250612_145917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a simplified blockchain-based payment system using Python. Note that for real-world applications, you would need to integrate with Sonic's infrastructure, which may include API calls, cryptographic libraries, and real-time networking protocols. Here, we'll simulate sub-second confirmation using a lightweight blockchain model.

```python
import hashlib
import time
import json
from typing import List

class Block:
    """
    Represents a single block in the blockchain.
    Each block contains transaction data, a timestamp, and a hash linking it to the previous block.
    """
    def __init__(self, index: int, transactions: List[dict], previous_hash: str):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        Computes the hash of the block using SHA-256.
        The hash includes the index, timestamp, transactions, previous hash, and nonce.
        """
        block_data = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_data).hexdigest()

    def mine_block(self, difficulty: int):
        """
        Mines the block by finding a hash that starts with a specific number of zeros (difficulty).
        """
        target = '0' * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()

class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    This class handles the creation, validation, and management of blocks.
    """
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = 2  # Adjustable mining difficulty for real-time confirmations
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the initial block in the blockchain.
        """
        genesis_block = Block(0, [], "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_transaction(self, sender: str, receiver: str, amount: float):
        """
        Adds a transaction to the list of pending transactions.
        """
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        }
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        """
        Mines all pending transactions and adds a new block to the blockchain.
        """
        if not self.pending_transactions:
            print("No transactions to mine.")
            return

        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions.copy(),
            previous_hash=self.chain[-1].hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []  # Clear the list of pending transactions

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain by checking hashes and links between blocks.
        """
        for i in range(1, len(self.chain)):
            previous_block = self.chain[i - 1]
            current_block = self.chain[i]

            if current_block.hash != current_block.compute_hash():
                print(f"Block {current_block.index} has invalid hash.")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} has invalid previous hash.")
                return False

        return True

    def display_chain(self):
        """
        Displays the blockchain in a readable format.
        """
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print("-" * 30)

# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Add transactions and mine blocks
    blockchain.add_transaction("Alice", "Bob", 50.0)
    blockchain.add_transaction("Bob", "Charlie", 25.0)
    blockchain.mine_pending_transactions()

    blockchain.add_transaction("Charlie", "David", 40.0)
    blockchain.mine_pending_transactions()

    # Display the blockchain
    blockchain.display_chain()

    # Validate the blockchain
    if blockchain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid.")
```

This implementation uses a simple proof-of-work mechanism with adjustable difficulty, allowing for sub-second confirmation times. However, integrating Sonic's infrastructure for real-time payments and low transaction costs would require additional APIs or libraries tailored to their system. Always ensure proper security and scalability before deploying such systems in production.
