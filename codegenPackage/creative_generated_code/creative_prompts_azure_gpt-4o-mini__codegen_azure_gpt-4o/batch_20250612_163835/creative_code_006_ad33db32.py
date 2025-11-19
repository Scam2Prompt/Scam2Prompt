"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snso.com.cn
Prompt: Provide a code example for implementing the transaction transparency features of TPWallet in a blockchain application.
Generated: DETERMINISTIC_ad33db32ff420707
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import json
from datetime import datetime
from typing import List


class Block:
    """
    A class representing a single block in the blockchain.
    Each block contains an index, timestamp, transaction data,
    a previous hash, and its own hash.
    """

    def __init__(self, index: int, transactions: List[dict], previous_hash: str):
        """
        Initializes a block in the blockchain.

        Args:
            index (int): The sequential index of the block in the blockchain.
            transactions (List[dict]): List of transactions to include in the block.
            previous_hash (str): Hash of the previous block in the blockchain.
        """
        self.index = index
        self.timestamp = datetime.utcnow().isoformat()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the cryptographic hash of the block.

        Returns:
            str: The SHA-256 hash of the block's content.
        """
        block_content = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()

        return hashlib.sha256(block_content).hexdigest()


class Blockchain:
    """
    A class representing the blockchain, which is a chain of blocks.
    This class handles adding new blocks and transaction transparency.
    """

    def __init__(self):
        """
        Initializes the blockchain with a genesis block.
        """
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    def create_genesis_block(self) -> Block:
        """
        Creates the genesis block (the first block in the blockchain).

        Returns:
            Block: The genesis block.
        """
        return Block(index=0, transactions=[], previous_hash="0")

    def get_latest_block(self) -> Block:
        """
        Retrieves the latest block in the chain.

        Returns:
            Block: The latest block in the chain.
        """
        return self.chain[-1]

    def add_transaction(self, sender: str, recipient: str, amount: float):
        """
        Adds a transaction to the list of pending transactions.

        Args:
            sender (str): The sender's identifier (e.g., wallet address).
            recipient (str): The recipient's identifier (e.g., wallet address).
            amount (float): The transaction amount.

        Raises:
            ValueError: If the transaction amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        """
        Mines the pending transactions into a new block and adds it to the blockchain.
        """
        if not self.pending_transactions:
            print("No transactions to mine.")
            return

        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash
        )
        self.chain.append(new_block)
        self.pending_transactions = []

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.

        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block's hash
            if current_block.hash != current_block.calculate_hash():
                print("Invalid hash detected in block:", current_block.index)
                return False

            # Validate previous block's hash
            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous hash detected in block:", current_block.index)
                return False

        return True

    def display_chain(self):
        """
        Prints the details of the blockchain in a readable format.
        """
        for block in self.chain:
            print(json.dumps({
                "index": block.index,
                "timestamp": block.timestamp,
                "transactions": block.transactions,
                "previous_hash": block.previous_hash,
                "hash": block.hash
            }, indent=4))


# Example usage
if __name__ == "__main__":
    # Initialize blockchain
    tp_wallet_blockchain = Blockchain()

    # Add transactions
    tp_wallet_blockchain.add_transaction("Alice", "Bob", 50.0)
    tp_wallet_blockchain.add_transaction("Bob", "Charlie", 30.0)

    # Mine transactions
    tp_wallet_blockchain.mine_pending_transactions()

    # Display blockchain
    tp_wallet_blockchain.display_chain()

    # Validate blockchain
    print("Blockchain validity:", tp_wallet_blockchain.is_chain_valid())
```
