"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: "Explain how to integrate blockchain technology into a platform for transparent, secure, and instantaneous transactions in the oil and gas industry, using the Crudo Protocol as a case study."
Generated: DETERMINISTIC_a2516f7e14898864
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import time
from typing import List

# Define a class for Block
class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict):
        """
        Initialize a Block object.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        data (dict): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


# Define a class for Blockchain
class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain object.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"})

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

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


# Define a class for Transaction
class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float):
        """
        Initialize a Transaction object.

        Args:
        sender (str): The sender of the transaction.
        receiver (str): The receiver of the transaction.
        amount (float): The amount of the transaction.
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount


# Define a class for CrudoProtocol
class CrudoProtocol:
    def __init__(self):
        """
        Initialize a CrudoProtocol object.
        """
        self.blockchain = Blockchain()
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        """
        Add a transaction to the protocol.

        Args:
        transaction (Transaction): The transaction to add.
        """
        self.transactions.append(transaction)
        self.mine_block()

    def mine_block(self):
        """
        Mine a new block and add it to the blockchain.
        """
        if not self.transactions:
            return False

        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), self.transactions)
        self.blockchain.add_block(new_block)
        self.transactions = []
        return new_block

    def get_balance(self, address: str) -> float:
        """
        Get the balance of an address.

        Args:
        address (str): The address to get the balance for.

        Returns:
        float: The balance of the address.
        """
        balance = 0.0
        for block in self.blockchain.chain:
            for transaction in block.data:
                if transaction.sender == address:
                    balance -= transaction.amount
                if transaction.receiver == address:
                    balance += transaction.amount
        return balance


def main():
    # Create a CrudoProtocol object
    crudo_protocol = CrudoProtocol()

    # Create transactions
    transaction1 = Transaction("address1", "address2", 10.0)
    transaction2 = Transaction("address2", "address3", 5.0)

    # Add transactions to the protocol
    crudo_protocol.add_transaction(transaction1)
    crudo_protocol.add_transaction(transaction2)

    # Print the blockchain
    for block in crudo_protocol.blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        for transaction in block.data:
            print(f"  Transaction: {transaction.sender} -> {transaction.receiver}, Amount: {transaction.amount}")
        print()

    # Check if the blockchain is valid
    print(f"Is blockchain valid? {crudo_protocol.blockchain.is_chain_valid()}")

    # Get the balance of an address
    print(f"Balance of address2: {crudo_protocol.get_balance('address2')}")

if __name__ == "__main__":
    main()
```
