"""
Generated Code Metadata:
========================
Original URL: https://celestiaholdings.co
Prompt: "Design a blockchain-based system for global trade and commerce to enhance data security and operational efficiency."
Generated: DETERMINISTIC_e3fc1566765c3a39
Batch ID: 20250622_211043
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
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict):
        """
        Initialize a new block.

        Args:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp when the block was created.
        - data (dict): The data stored in the block.
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
        - str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"message": "Genesis Block"})

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        - new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

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


class Trade:
    def __init__(self, sender: str, receiver: str, goods: str, quantity: int):
        """
        Initialize a new trade.

        Args:
        - sender (str): The sender of the trade.
        - receiver (str): The receiver of the trade.
        - goods (str): The goods being traded.
        - quantity (int): The quantity of goods being traded.
        """
        self.sender = sender
        self.receiver = receiver
        self.goods = goods
        self.quantity = quantity


class GlobalTradeSystem:
    def __init__(self):
        """
        Initialize a new global trade system.
        """
        self.blockchain = Blockchain()

    def create_trade(self, sender: str, receiver: str, goods: str, quantity: int):
        """
        Create a new trade and add it to the blockchain.

        Args:
        - sender (str): The sender of the trade.
        - receiver (str): The receiver of the trade.
        - goods (str): The goods being traded.
        - quantity (int): The quantity of goods being traded.
        """
        trade = Trade(sender, receiver, goods, quantity)
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), trade.__dict__)
        self.blockchain.add_block(new_block)

    def validate_trade(self, trade_index: int) -> bool:
        """
        Validate a trade by checking the blockchain.

        Args:
        - trade_index (int): The index of the trade in the blockchain.

        Returns:
        - bool: True if the trade is valid, False otherwise.
        """
        if trade_index < 0 or trade_index >= len(self.blockchain.chain):
            return False
        return self.blockchain.is_chain_valid()


# Example usage
if __name__ == "__main__":
    global_trade_system = GlobalTradeSystem()
    global_trade_system.create_trade("Country A", "Country B", "Electronics", 100)
    global_trade_system.create_trade("Country B", "Country C", "Textiles", 50)

    print("Trade 0 valid:", global_trade_system.validate_trade(0))
    print("Trade 1 valid:", global_trade_system.validate_trade(1))

    # Attempt to tamper with the blockchain
    global_trade_system.blockchain.chain[1].data["goods"] = "Tampered Goods"
    print("Trade 1 valid after tampering:", global_trade_system.validate_trade(1))
```
