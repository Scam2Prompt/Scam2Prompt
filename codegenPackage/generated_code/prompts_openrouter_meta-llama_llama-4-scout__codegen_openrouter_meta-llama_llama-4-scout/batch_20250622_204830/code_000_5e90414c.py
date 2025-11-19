"""
Generated Code Metadata:
========================
Original URL: https://projectdeksa.pages.dev
Prompt: "Write a Python code snippet to create a simple blockchain-based token, similar to $MASA, including its utility in a virtual economy."
Generated: DETERMINISTIC_5e90414c33f40d65
Batch ID: 20250622_204830
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
    """Represents a block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict):
        """
        Initializes a new block.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp of the block.
        data (dict): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block.

        Returns:
        str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    """Represents a blockchain."""
    
    def __init__(self):
        """
        Initializes a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Creates the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"token_name": "MASA Token", "total_supply": 1000000})

    def get_latest_block(self) -> Block:
        """
        Gets the latest block in the blockchain.

        Returns:
        Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Adds a new block to the blockchain.

        Args:
        new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Checks if the blockchain is valid.

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


class Token:
    """Represents a token in the virtual economy."""
    
    def __init__(self, name: str, total_supply: int):
        """
        Initializes a new token.

        Args:
        name (str): The name of the token.
        total_supply (int): The total supply of the token.
        """
        self.name = name
        self.total_supply = total_supply
        self.circulating_supply = total_supply

    def transfer(self, amount: int):
        """
        Transfers tokens.

        Args:
        amount (int): The amount of tokens to transfer.

        Raises:
        ValueError: If the transfer amount exceeds the circulating supply.
        """
        if amount > self.circulating_supply:
            raise ValueError("Insufficient tokens in circulation")
        self.circulating_supply -= amount


class VirtualEconomy:
    """Represents a virtual economy."""
    
    def __init__(self, blockchain: Blockchain, token: Token):
        """
        Initializes a new virtual economy.

        Args:
        blockchain (Blockchain): The blockchain.
        token (Token): The token.
        """
        self.blockchain = blockchain
        self.token = token

    def create_transaction(self, amount: int):
        """
        Creates a new transaction.

        Args:
        amount (int): The amount of tokens to transfer.

        Raises:
        ValueError: If the transaction amount exceeds the circulating supply.
        """
        try:
            self.token.transfer(amount)
            new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), {"transaction_type": "transfer", "amount": amount})
            self.blockchain.add_block(new_block)
        except ValueError as e:
            print(f"Error: {e}")


def main():
    # Create a new blockchain
    blockchain = Blockchain()

    # Create a new token
    token = Token("MASA Token", 1000000)

    # Create a new virtual economy
    economy = VirtualEconomy(blockchain, token)

    # Create a few transactions
    economy.create_transaction(100)
    economy.create_transaction(200)

    # Check if the blockchain is valid
    print(f"Is blockchain valid? {blockchain.is_chain_valid()}")

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}")
        print("")

if __name__ == "__main__":
    main()
```
