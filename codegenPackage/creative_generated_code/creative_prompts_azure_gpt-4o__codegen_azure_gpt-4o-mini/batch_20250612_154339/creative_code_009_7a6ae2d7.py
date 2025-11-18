"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hemi.host
Prompt: Explain how to use Hemi’s extensibility features to incorporate Bitcoin’s security into a custom blockchain network.
Generated: DETERMINISTIC_7a6ae2d737cca168
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Custom Blockchain Network with Bitcoin's Security Features

This script demonstrates how to utilize Hemi's extensibility features to
integrate Bitcoin's security mechanisms into a custom blockchain network.
"""

import hashlib
import json
from time import time

class Block:
    """
    Represents a single block in the blockchain.

    Attributes:
        index (int): The index of the block in the blockchain.
        timestamp (float): The time when the block was created.
        transactions (list): The list of transactions included in the block.
        previous_hash (str): The hash of the previous block.
        nonce (int): The nonce used for mining the block.
    """

    def __init__(self, index, transactions, previous_hash, nonce):
        self.index = index
        self.timestamp = time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        """
        Computes the SHA-256 hash of the block.

        Returns:
            str: The hexadecimal representation of the block's hash.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    """
    Represents the entire blockchain.

    Attributes:
        chain (list): The list of blocks in the blockchain.
        current_transactions (list): The list of transactions to be added in the next block.
        difficulty (int): The difficulty level for mining blocks.
    """

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.difficulty = 4  # Bitcoin-like difficulty
        # Create the genesis block
        self.create_block(previous_hash='1', nonce=0)

    def create_block(self, previous_hash, nonce):
        """
        Creates a new block and adds it to the blockchain.

        Args:
            previous_hash (str): The hash of the previous block.
            nonce (int): The nonce used for mining the block.

        Returns:
            Block: The newly created block.
        """
        index = len(self.chain) + 1
        block = Block(index, self.current_transactions, previous_hash, nonce)
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of transactions.

        Args:
            sender (str): The address of the sender.
            recipient (str): The address of the recipient.
            amount (float): The amount to be transferred.

        Returns:
            int: The index of the block that will hold this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block.index + 1

    @property
    def last_block(self):
        """
        Returns the last block in the blockchain.

        Returns:
            Block: The last block in the chain.
        """
        return self.chain[-1]

    def proof_of_work(self, last_nonce):
        """
        Simple Proof of Work algorithm.

        Args:
            last_nonce (int): The nonce from the last block.

        Returns:
            int: The nonce that solves the proof of work.
        """
        nonce = 0
        while not self.valid_proof(nonce, last_nonce):
            nonce += 1
        return nonce

    def valid_proof(self, nonce, last_hash):
        """
        Validates the Proof of Work.

        Args:
            nonce (int): The nonce to validate.
            last_hash (str): The hash of the last block.

        Returns:
            bool: True if valid, False otherwise.
        """
        guess = f'{last_hash}{nonce}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:self.difficulty] == '0' * self.difficulty


def main():
    """
    Main function to create a blockchain and add transactions.
    """
    try:
        # Create a blockchain instance
        blockchain = Blockchain()

        # Example transactions
        blockchain.add_transaction(sender="Alice", recipient="Bob", amount=10)
        blockchain.add_transaction(sender="Bob", recipient="Charlie", amount=5)

        # Mining the block with a proof of work
        last_block = blockchain.last_block
        last_nonce = last_block.nonce
        nonce = blockchain.proof_of_work(last_nonce)

        # Create a new block in the blockchain
        previous_hash = last_block.compute_hash()
        block = blockchain.create_block(previous_hash, nonce)

        # Output the blockchain
        print("Blockchain:")
        for b in blockchain.chain:
            print(f"Block {b.index} Hash: {b.compute_hash()} - Nonce: {b.nonce} - Transactions: {b.transactions}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
