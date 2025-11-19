"""
Generated Code Metadata:
========================
Original URL: https://dorgbglgn.pages.dev
Prompt: Suggest tools or frameworks for building a blockchain-based application similar to Ord.io, focusing on features like inscriptions and snapshots.
Generated: DETERMINISTIC_a3a5814cc25e7c92
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_app.py

import hashlib
import json
from typing import List, Dict

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict):
        """
        Initialize a new block.

        Args:
        - index (int): The block's index in the chain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The block's timestamp.
        - data (Dict): The block's data.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block's hash.

        Returns:
        - str: The block's hash.
        """
        data_string = json.dumps(self.data, sort_keys=True)
        block_data = f"{self.index}{self.previous_hash}{self.timestamp}{data_string}"
        return hashlib.sha256(block_data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.pending_data = []

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", 1643723400, {"inscriptions": [], "snapshots": []})

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the chain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the chain.

        Args:
        - new_block (Block): The new block.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def add_inscription(self, inscription: str):
        """
        Add an inscription to the pending data.

        Args:
        - inscription (str): The inscription.
        """
        self.pending_data.append({"inscription": inscription})

    def add_snapshot(self, snapshot: str):
        """
        Add a snapshot to the pending data.

        Args:
        - snapshot (str): The snapshot.
        """
        self.pending_data.append({"snapshot": snapshot})

    def mine_pending_data(self):
        """
        Mine the pending data and add it to the chain.
        """
        if not self.pending_data:
            return False

        new_block = Block(
            len(self.chain),
            self.get_latest_block().hash,
            1643723400,
            {"inscriptions": [], "snapshots": []},
        )

        for data in self.pending_data:
            if "inscription" in data:
                new_block.data["inscriptions"].append(data["inscription"])
            elif "snapshot" in data:
                new_block.data["snapshots"].append(data["snapshot"])

        self.add_block(new_block)
        self.pending_data = []
        return True


def main():
    blockchain = Blockchain()

    # Add inscriptions and snapshots
    blockchain.add_inscription("Inscription 1")
    blockchain.add_snapshot("Snapshot 1")
    blockchain.add_inscription("Inscription 2")
    blockchain.add_snapshot("Snapshot 2")

    # Mine pending data
    blockchain.mine_pending_data()

    # Print blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print("")


if __name__ == "__main__":
    main()
```
