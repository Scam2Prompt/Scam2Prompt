"""
Generated Code Metadata:
========================
Original URL: https://app-explorer.pages.dev
Prompt: How does Dapp Protocol ensure the safety and security of transactions within its decentralized architecture?
Generated: DETERMINISTIC_d4bb48a69cb60cd8
Batch ID: 20250612_155442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a simplified decentralized application (DApp) protocol that ensures the safety and security of transactions using cryptographic techniques and blockchain principles.

```python
import hashlib
import json
import time
from typing import List, Dict, Any


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains a timestamp, a list of transactions, the previous block's hash, and its own hash.
    """
    def __init__(self, index: int, transactions: List[Dict[str, Any]], previous_hash: str):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # Used for proof-of-work
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using its contents.
        Ensures immutability and security of the block.
        """
        block_content = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
        }
        block_string = json.dumps(block_content, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty: int):
        """
        Implements proof-of-work by finding a hash that starts with a certain number of zeros.
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    Ensures security and immutability of transactions.
    """
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.difficulty = 4  # Adjustable difficulty for proof-of-work
        self.pending_transactions: List[Dict[str, Any]] = []
        self.mining_reward = 50  # Reward for mining a block

    def create_genesis_block(self) -> Block:
        """
        Creates the first block in the blockchain, known as the genesis block.
        """
        return Block(index=0, transactions=[], previous_hash="0")

    def get_latest_block(self) -> Block:
        """
        Returns the latest block in the blockchain.
        """
        return self.chain[-1]

    def add_transaction(self, sender: str, recipient: str, amount: float):
        """
        Adds a new transaction to the list of pending transactions.
        """
        if not sender or not recipient or amount <= 0:
            raise ValueError("Invalid transaction data.")
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
        }
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address: str):
        """
        Mines a new block containing all pending transactions and rewards the miner.
        """
        if not self.pending_transactions:
            raise ValueError("No transactions to mine.")

        # Create a new block with pending transactions
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash,
        )
        new_block.mine_block(self.difficulty)

        # Add the mined block to the chain
        self.chain.append(new_block)

        # Reward the miner
        self.pending_transactions = [
            {"sender": "Network", "recipient": miner_address, "amount": self.mining_reward}
        ]

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.
        Ensures that all blocks are correctly linked and their hashes are valid.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    dapp_blockchain = Blockchain()

    # Add transactions
    dapp_blockchain.add_transaction(sender="Alice", recipient="Bob", amount=100)
    dapp_blockchain.add_transaction(sender="Bob", recipient="Charlie", amount=50)

    # Mine the transactions
    print("Mining pending transactions...")
    dapp_blockchain.mine_pending_transactions(miner_address="Miner1")

    # Display the blockchain
    for block in dapp_blockchain.chain:
        print(f"Block {block.index}:")
        print(f"  Timestamp: {block.timestamp}")
        print(f"  Transactions: {block.transactions}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Hash: {block.hash}")
        print()

    # Validate the blockchain
    print("Is blockchain valid?", dapp_blockchain.is_chain_valid())
```

This code implements a basic blockchain protocol with transaction safety and security features, including proof-of-work, cryptographic hashing, and chain validation.
