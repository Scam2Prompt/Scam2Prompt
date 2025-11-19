"""
Generated Code Metadata:
========================
Original URL: https://blockchainguild.pages.dev
Prompt: Provide code for creating a blockchain-based sales category leaderboard, similar to the Guild Pins leaderboard described on the Guildhall Guild webpage.
Generated: DETERMINISTIC_59e04fa9d027f2d7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_sales_leaderboard.py

import hashlib
import time
from typing import List, Dict

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, sales_data: Dict[str, int]):
        """
        Initialize a new block.

        Args:
        - index (int): The block's index in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The block's timestamp.
        - sales_data (Dict[str, int]): A dictionary of sales categories and their corresponding sales amounts.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.sales_data = sales_data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block's hash.

        Returns:
        - str: The block's hash.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.sales_data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.sales_leaderboard = {}

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), {})

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
        self.update_sales_leaderboard(new_block.sales_data)

    def update_sales_leaderboard(self, sales_data: Dict[str, int]):
        """
        Update the sales leaderboard.

        Args:
        - sales_data (Dict[str, int]): A dictionary of sales categories and their corresponding sales amounts.
        """
        for category, amount in sales_data.items():
            if category in self.sales_leaderboard:
                self.sales_leaderboard[category] += amount
            else:
                self.sales_leaderboard[category] = amount

    def get_sales_leaderboard(self) -> List[tuple]:
        """
        Get the sales leaderboard.

        Returns:
        - List[tuple]: A list of tuples containing the sales categories and their corresponding sales amounts, sorted in descending order.
        """
        return sorted(self.sales_leaderboard.items(), key=lambda x: x[1], reverse=True)


def main():
    blockchain = Blockchain()

    # Add some blocks to the blockchain
    blockchain.add_block(Block(1, blockchain.get_latest_block().hash, time.time(), {"Category A": 100}))
    blockchain.add_block(Block(2, blockchain.get_latest_block().hash, time.time(), {"Category B": 200}))
    blockchain.add_block(Block(3, blockchain.get_latest_block().hash, time.time(), {"Category A": 50}))

    # Get and print the sales leaderboard
    leaderboard = blockchain.get_sales_leaderboard()
    print("Sales Leaderboard:")
    for i, (category, amount) in enumerate(leaderboard):
        print(f"{i+1}. {category}: {amount}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
