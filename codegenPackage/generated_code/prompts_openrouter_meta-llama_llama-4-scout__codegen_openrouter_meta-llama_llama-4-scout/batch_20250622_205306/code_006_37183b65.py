"""
Generated Code Metadata:
========================
Original URL: https://layerfinance.enterprises
Prompt: How can blockchain technology be integrated into a layer finance system for secure transactions?
Generated: DETERMINISTIC_37183b65e475991a
Batch ID: 20250622_205306
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

class Block:
    """
    Represents a block in the blockchain.
    """

    def __init__(self, index: int, previous_hash: str, timestamp: float, transactions: List[dict], nonce: int = 0):
        """
        Initializes a new block.

        Args:
        - index (int): The index of the block in the chain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - transactions (List[dict]): A list of transactions in the block.
        - nonce (int): A counter for proof-of-work. Defaults to 0.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.transactions) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    """
    Represents a blockchain.
    """

    def __init__(self):
        """
        Initializes a new blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []

    def create_genesis_block(self) -> Block:
        """
        Creates the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), [])

    def get_latest_block(self) -> Block:
        """
        Gets the latest block in the chain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_transaction(self, transaction: dict):
        """
        Adds a transaction to the pending transactions.

        Args:
        - transaction (dict): The transaction to add.
        """
        self.pending_transactions.append(transaction)

    def mine_block(self, miner: str):
        """
        Mines a new block.

        Args:
        - miner (str): The miner of the block.

        Returns:
        - Block: The mined block.
        """
        if not self.pending_transactions:
            return False

        new_block_index = self.get_latest_block().index + 1
        new_block_timestamp = time.time()
        new_block = Block(new_block_index, self.get_latest_block().hash, new_block_timestamp, self.pending_transactions)

        # Proof-of-work
        while new_block.hash[: self.difficulty] != "0" * self.difficulty:
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        # Add miner reward
        new_block.transactions.append({"from": "network", "to": miner, "amount": 1})

        self.chain.append(new_block)
        self.pending_transactions = []

        return new_block

    def is_chain_valid(self) -> bool:
        """
        Checks if the chain is valid.

        Returns:
        - bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True


class LayerFinanceSystem:
    """
    Represents a layer finance system.
    """

    def __init__(self):
        """
        Initializes a new layer finance system.
        """
        self.blockchain = Blockchain()

    def make_transaction(self, from_address: str, to_address: str, amount: float):
        """
        Makes a transaction.

        Args:
        - from_address (str): The sender's address.
        - to_address (str): The recipient's address.
        - amount (float): The amount to transfer.
        """
        transaction = {"from": from_address, "to": to_address, "amount": amount}
        self.blockchain.add_transaction(transaction)

    def mine_transaction(self, miner: str):
        """
        Mines a transaction.

        Args:
        - miner (str): The miner of the block.

        Returns:
        - Block: The mined block.
        """
        return self.blockchain.mine_block(miner)

    def get_balance(self, address: str) -> float:
        """
        Gets the balance of an address.

        Args:
        - address (str): The address.

        Returns:
        - float: The balance.
        """
        balance = 0.0

        for block in self.blockchain.chain:
            for transaction in block.transactions:
                if transaction["to"] == address:
                    balance += transaction["amount"]
                elif transaction["from"] == address:
                    balance -= transaction["amount"]

        return balance


def main():
    layer_finance_system = LayerFinanceSystem()

    # Make transactions
    layer_finance_system.make_transaction("Alice", "Bob", 10.0)
    layer_finance_system.make_transaction("Bob", "Charlie", 5.0)

    # Mine transactions
    mined_block = layer_finance_system.mine_transaction("Miner")

    # Print mined block
    print("Mined Block:")
    print(f"Index: {mined_block.index}")
    print(f"Hash: {mined_block.hash}")
    print(f"Transactions: {mined_block.transactions}")

    # Get balances
    print(f"Alice's balance: {layer_finance_system.get_balance('Alice')}")
    print(f"Bob's balance: {layer_finance_system.get_balance('Bob')}")
    print(f"Charlie's balance: {layer_finance_system.get_balance('Charlie')}")

    # Check chain validity
    print(f"Is chain valid? {layer_finance_system.blockchain.is_chain_valid()}")


if __name__ == "__main__":
    main()
```
