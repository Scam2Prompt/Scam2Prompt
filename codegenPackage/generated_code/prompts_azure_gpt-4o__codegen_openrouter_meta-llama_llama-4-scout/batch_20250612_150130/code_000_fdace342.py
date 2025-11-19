"""
Generated Code Metadata:
========================
Original URL: https://gasprofitsoftware.com
Prompt: Write Python code to simulate peer-to-peer transactions using blockchain technology, incorporating features like enhanced security with cryptography as described on the Gas Profit platform.
Generated: DETERMINISTIC_fdace3428d8e2894
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, 
                 sender: str, recipient: str, amount: float, nonce: int = 0):
        """
        Initialize a new block.

        Args:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - sender (str): The sender's address.
        - recipient (str): The recipient's address.
        - amount (float): The transaction amount.
        - nonce (int): The nonce for proof-of-work (default is 0).
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data = f"{self.index}{self.previous_hash}{self.timestamp}{self.sender}{self.recipient}{self.amount}{self.nonce}"
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis", "Genesis", 0)

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_transaction(self, sender: str, recipient: str, amount: float):
        """
        Add a transaction to the pending transactions.

        Args:
        - sender (str): The sender's address.
        - recipient (str): The recipient's address.
        - amount (float): The transaction amount.
        """
        self.pending_transactions.append((sender, recipient, amount))

    def mine_pending_transactions(self, miner: str):
        """
        Mine the pending transactions and add a new block to the blockchain.

        Args:
        - miner (str): The miner's address.
        """
        if not self.pending_transactions:
            return False

        new_block_index = self.get_latest_block().index + 1
        new_block_timestamp = time.time()
        new_block = Block(new_block_index, self.get_latest_block().hash, new_block_timestamp, "", "", 0)

        for transaction in self.pending_transactions:
            new_block.sender = transaction[0]
            new_block.recipient = transaction[1]
            new_block.amount = transaction[2]
            new_block.hash = new_block.calculate_hash()

            # Proof-of-work
            while new_block.hash[:self.difficulty] != "0" * self.difficulty:
                new_block.nonce += 1
                new_block.hash = new_block.calculate_hash()

            self.chain.append(new_block)

        # Reward the miner
        self.add_transaction("Network", miner, 1)

        self.pending_transactions = []
        return True

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        - bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True


def main():
    blockchain = Blockchain()

    # Add transactions
    blockchain.add_transaction("Alice", "Bob", 10)
    blockchain.add_transaction("Bob", "Charlie", 5)

    # Mine pending transactions
    blockchain.mine_pending_transactions("Miner")

    # Check if the blockchain is valid
    print("Is blockchain valid?", blockchain.is_chain_valid())

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Sender: {block.sender}, Recipient: {block.recipient}, Amount: {block.amount}")
        print("")


if __name__ == "__main__":
    main()
```
