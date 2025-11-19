"""
Generated Code Metadata:
========================
Original URL: https://e-mainnet.pages.dev
Prompt: Design a blockchain-based system for minting and distributing digital assets, incorporating a quick start guide and recovery mechanisms.
Generated: DETERMINISTIC_248b9220ef2b155a
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_asset_manager.py

import hashlib
import time
import json
from typing import List, Dict

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict, nonce: int = 0):
        """
        Initialize a new block.

        :param index: The block's index in the chain.
        :param previous_hash: The hash of the previous block.
        :param timestamp: The block's timestamp.
        :param data: The block's data (transactions).
        :param nonce: The block's nonce (for mining).
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block's hash.

        :return: The block's hash.
        """
        data_string = json.dumps(self.data)
        block_data = f"{self.index}{self.previous_hash}{self.timestamp}{data_string}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        :return: The genesis block.
        """
        return Block(0, "0", time.time(), {"message": "Genesis Block"})

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the chain.

        :return: The latest block.
        """
        return self.chain[-1]

    def add_transaction(self, transaction: Dict):
        """
        Add a transaction to the pending transactions.

        :param transaction: The transaction to add.
        """
        self.pending_transactions.append(transaction)

    def mine_block(self, miner: str):
        """
        Mine a new block.

        :param miner: The miner's address.
        """
        if not self.pending_transactions:
            return False

        new_block_index = len(self.chain)
        new_block_timestamp = time.time()
        new_block_previous_hash = self.get_latest_block().hash
        new_block_data = self.pending_transactions

        new_block = Block(new_block_index, new_block_previous_hash, new_block_timestamp, new_block_data)

        self.proof_of_work(new_block)

        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

        # Reward the miner
        self.add_transaction({"type": "reward", "amount": 10, "to": miner})

        self.pending_transactions = []

        return new_block

    def proof_of_work(self, block: Block):
        """
        Perform proof of work for a block.

        :param block: The block to mine.
        """
        while block.hash[: self.difficulty] != "0" * self.difficulty:
            block.nonce += 1
            block.hash = block.calculate_hash()

    def is_chain_valid(self) -> bool:
        """
        Check if the chain is valid.

        :return: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True


class DigitalAssetManager:
    def __init__(self):
        """
        Initialize a new digital asset manager.
        """
        self.blockchain = Blockchain()
        self.assets = {}

    def mint_asset(self, asset_id: str, amount: int):
        """
        Mint a new digital asset.

        :param asset_id: The asset's ID.
        :param amount: The asset's amount.
        """
        if asset_id in self.assets:
            print("Asset already exists.")
            return

        self.assets[asset_id] = amount
        self.blockchain.add_transaction({"type": "mint", "asset_id": asset_id, "amount": amount})

        new_block = self.blockchain.mine_block("system")
        if new_block:
            print(f"Asset {asset_id} minted successfully.")

    def distribute_asset(self, asset_id: str, amount: int, recipient: str):
        """
        Distribute a digital asset.

        :param asset_id: The asset's ID.
        :param amount: The amount to distribute.
        :param recipient: The recipient's address.
        """
        if asset_id not in self.assets:
            print("Asset does not exist.")
            return

        if self.assets[asset_id] < amount:
            print("Insufficient asset amount.")
            return

        self.assets[asset_id] -= amount
        self.blockchain.add_transaction({"type": "distribute", "asset_id": asset_id, "amount": amount, "to": recipient})

        new_block = self.blockchain.mine_block("system")
        if new_block:
            print(f"Asset {asset_id} distributed successfully.")

    def recover_chain(self):
        """
        Recover the blockchain in case of a failure.
        """
        # Load the blockchain from a backup or a node
        pass

def main():
    asset_manager = DigitalAssetManager()

    while True:
        print("1. Mint Asset")
        print("2. Distribute Asset")
        print("3. Check Chain Validity")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            asset_id = input("Enter asset ID: ")
            amount = int(input("Enter asset amount: "))
            asset_manager.mint_asset(asset_id, amount)
        elif choice == "2":
            asset_id = input("Enter asset ID: ")
            amount = int(input("Enter amount to distribute: "))
            recipient = input("Enter recipient's address: ")
            asset_manager.distribute_asset(asset_id, amount, recipient)
        elif choice == "3":
            print(asset_manager.blockchain.is_chain_valid())
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
```
