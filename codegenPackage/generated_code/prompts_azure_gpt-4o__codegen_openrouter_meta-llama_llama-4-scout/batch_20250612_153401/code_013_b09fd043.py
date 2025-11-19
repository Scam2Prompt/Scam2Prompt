"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: Write code to implement a blockchain-based referral program, inspired by Masa's "Refer a friend" feature.
Generated: DETERMINISTIC_b09fd043e484cf57
Batch ID: 20250612_153401
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
from typing import List, Dict

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict, nonce: int = 0):
        """
        Initialize a new block.

        Args:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - data (Dict): The data stored in the block.
        - nonce (int): The nonce for proof-of-work. Defaults to 0.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
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

    def add_pending_data(self, data: Dict):
        """
        Add pending data to be included in the next block.

        Args:
        - data (Dict): The pending data.
        """
        self.pending_data.append(data)

    def mine_pending_data(self):
        """
        Mine the pending data and add it to the blockchain.
        """
        if not self.pending_data:
            return False

        new_block_index = len(self.chain)
        new_block_timestamp = time.time()
        new_block = Block(new_block_index, self.get_latest_block().hash, new_block_timestamp, self.pending_data)

        # Proof-of-work
        while new_block.hash[: self.difficulty] != "0" * self.difficulty:
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        self.add_block(new_block)
        self.pending_data = []
        return True


class ReferralProgram:
    def __init__(self, blockchain: Blockchain):
        """
        Initialize a new referral program.

        Args:
        - blockchain (Blockchain): The blockchain to use.
        """
        self.blockchain = blockchain
        self.referrals = {}

    def refer_friend(self, referrer: str, friend: str):
        """
        Record a referral.

        Args:
        - referrer (str): The referrer's ID.
        - friend (str): The friend's ID.
        """
        referral_data = {"referrer": referrer, "friend": friend}
        self.blockchain.add_pending_data(referral_data)
        self.blockchain.mine_pending_data()

        # Update referrals
        if referrer not in self.referrals:
            self.referrals[referrer] = []
        self.referrals[referrer].append(friend)

    def get_referrals(self, referrer: str) -> List[str]:
        """
        Get the referrals for a given referrer.

        Args:
        - referrer (str): The referrer's ID.

        Returns:
        - List[str]: The referrals.
        """
        return self.referrals.get(referrer, [])


def main():
    blockchain = Blockchain()
    referral_program = ReferralProgram(blockchain)

    referral_program.refer_friend("user1", "user2")
    referral_program.refer_friend("user1", "user3")
    referral_program.refer_friend("user2", "user4")

    print(referral_program.get_referrals("user1"))  # Output: ['user2', 'user3']
    print(referral_program.get_referrals("user2"))  # Output: ['user4']

    # Print blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}")
        print("")


if __name__ == "__main__":
    main()
```
