"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Develop a blockchain-based application that supports Universal Health Coverage (UHC) and Universal Basic Income (UBI) principles, as described in BitDoctor's mission.
Generated: DETERMINISTIC_0cd6c013660ee241
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_uhc_ubi.py

import hashlib
import time
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
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


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
        return Block(0, "0", time.time(), {"genesis": "block"})

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

    def add_pending_data(self, data: Dict):
        """
        Add pending data to be included in the next block.

        Args:
        - data (Dict): The pending data.
        """
        self.pending_data.append(data)

    def mine_pending_data(self):
        """
        Mine the pending data and add it to the chain.
        """
        if not self.pending_data:
            return False

        new_block = Block(self.get_latest_block().index + 1, self.get_latest_block().hash, time.time(), self.pending_data)
        self.add_block(new_block)
        self.pending_data = []
        return new_block


class UHC_UBI_System:
    def __init__(self, blockchain: Blockchain):
        """
        Initialize a new UHC-UBI system.

        Args:
        - blockchain (Blockchain): The blockchain.
        """
        self.blockchain = blockchain
        self.users = {}

    def add_user(self, user_id: str, balance: float):
        """
        Add a new user to the system.

        Args:
        - user_id (str): The user's ID.
        - balance (float): The user's initial balance.
        """
        self.users[user_id] = balance

    def provide_ubi(self, user_id: str, amount: float):
        """
        Provide UBI to a user.

        Args:
        - user_id (str): The user's ID.
        - amount (float): The UBI amount.
        """
        if user_id not in self.users:
            raise ValueError("User not found")

        self.users[user_id] += amount
        self.blockchain.add_pending_data({"user_id": user_id, "ubi_amount": amount})

    def provide_uhc(self, user_id: str, service_cost: float):
        """
        Provide UHC to a user.

        Args:
        - user_id (str): The user's ID.
        - service_cost (float): The service cost.
        """
        if user_id not in self.users:
            raise ValueError("User not found")

        if self.users[user_id] < service_cost:
            raise ValueError("Insufficient balance")

        self.users[user_id] -= service_cost
        self.blockchain.add_pending_data({"user_id": user_id, "service_cost": service_cost})


def main():
    blockchain = Blockchain()
    uhc_ubi_system = UHC_UBI_System(blockchain)

    uhc_ubi_system.add_user("user1", 1000.0)
    uhc_ubi_system.provide_ubi("user1", 100.0)
    uhc_ubi_system.provide_uhc("user1", 50.0)

    blockchain.mine_pending_data()

    print("Blockchain:")
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}")
        print("")

    print("UHC-UBI System:")
    print(f"User balance: {uhc_ubi_system.users['user1']}")


if __name__ == "__main__":
    main()
```
