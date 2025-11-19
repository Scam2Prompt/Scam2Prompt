"""
Generated Code Metadata:
========================
Original URL: https://cryptolinknet.com
Prompt: Design a blockchain-based system for secure cross-border payments.
Generated: DETERMINISTIC_6004df8f650dfc1a
Batch ID: 20250622_204844
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
                 sender: str, recipient: str, amount: float, 
                 transaction_id: str):
        """
        Initialize a new block.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp of the block.
        sender (str): The sender's address.
        recipient (str): The recipient's address.
        amount (float): The amount transferred.
        transaction_id (str): The unique transaction ID.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.transaction_id = transaction_id
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        str: The hash of the block.
        """
        data = f"{self.index}{self.previous_hash}{self.timestamp}{self.sender}{self.recipient}{self.amount}{self.transaction_id}"
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_difficulty = 2
        self.mining_reward = 10.0

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis", "Genesis", 0.0, "Genesis")

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        Block: The latest block.
        """
        return self.chain[-1]

    def add_transaction(self, sender: str, recipient: str, amount: float) -> str:
        """
        Add a new transaction to the pending transactions.

        Args:
        sender (str): The sender's address.
        recipient (str): The recipient's address.
        amount (float): The amount transferred.

        Returns:
        str: The unique transaction ID.
        """
        transaction_id = hashlib.sha256(f"{sender}{recipient}{amount}".encode()).hexdigest()
        self.pending_transactions.append((sender, recipient, amount, transaction_id))
        return transaction_id

    def mine_block(self, miner: str) -> Block:
        """
        Mine a new block.

        Args:
        miner (str): The miner's address.

        Returns:
        Block: The new block.
        """
        if not self.pending_transactions:
            raise Exception("No pending transactions")

        latest_block = self.get_latest_block()
        index = latest_block.index + 1
        timestamp = time.time()
        sender = "Network"
        recipient = miner
        amount = self.mining_reward
        transaction_id = hashlib.sha256(f"{sender}{recipient}{amount}".encode()).hexdigest()

        new_block = Block(index, latest_block.hash, timestamp, sender, recipient, amount, transaction_id)

        for transaction in self.pending_transactions:
            new_block = Block(index, latest_block.hash, timestamp, transaction[0], transaction[1], transaction[2], transaction[3])
            self.chain.append(new_block)
            index += 1
            timestamp = time.time()
            latest_block = new_block

        self.pending_transactions = []
        self.chain.append(new_block)
        return new_block

    def validate_chain(self) -> bool:
        """
        Validate the blockchain.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class CrossBorderPaymentSystem:
    def __init__(self):
        """
        Initialize a new cross-border payment system.
        """
        self.blockchain = Blockchain()

    def make_payment(self, sender: str, recipient: str, amount: float) -> str:
        """
        Make a payment.

        Args:
        sender (str): The sender's address.
        recipient (str): The recipient's address.
        amount (float): The amount transferred.

        Returns:
        str: The unique transaction ID.
        """
        transaction_id = self.blockchain.add_transaction(sender, recipient, amount)
        return transaction_id

    def mine_block(self, miner: str) -> Block:
        """
        Mine a new block.

        Args:
        miner (str): The miner's address.

        Returns:
        Block: The new block.
        """
        return self.blockchain.mine_block(miner)

    def validate_chain(self) -> bool:
        """
        Validate the blockchain.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        return self.blockchain.validate_chain()


def main():
    payment_system = CrossBorderPaymentSystem()

    # Make a payment
    transaction_id = payment_system.make_payment("Alice", "Bob", 100.0)
    print(f"Transaction ID: {transaction_id}")

    # Mine a block
    new_block = payment_system.mine_block("Miner")
    print(f"New Block Hash: {new_block.hash}")

    # Validate the chain
    is_valid = payment_system.validate_chain()
    print(f"Is chain valid? {is_valid}")


if __name__ == "__main__":
    main()
```
