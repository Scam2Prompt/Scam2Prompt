"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bzreards.top
Prompt: Generate code for a decentralized voting system to allow community contributions to anime lore, inspired by Azuki's community-driven model.
Generated: DETERMINISTIC_c310bbc0d5bbb6d1
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from datetime import datetime
from typing import List

class Block:
    """
    A Block represents a single unit in the blockchain.
    Each block contains data about a voting event.
    """
    def __init__(self, index: int, timestamp: str, data: dict, previous_hash: str):
        self.index = index  # Index of the block in the chain
        self.timestamp = timestamp  # Timestamp when the block was created
        self.data = data  # Data contained in the block (e.g., lore contributions)
        self.previous_hash = previous_hash  # Hash of the previous block
        self.hash = self.calculate_hash()  # Hash of the current block

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using its contents.
        Returns:
            str: The computed hash of the block.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """
    A Blockchain represents the entire chain for decentralized voting and lore contributions.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize chain with a genesis block

    def create_genesis_block(self) -> Block:
        """
        Creates the genesis (first) block in the blockchain.
        Returns:
            Block: The genesis block.
        """
        return Block(0, datetime.utcnow().isoformat(), {"message": "Genesis Block"}, "0")

    def get_latest_block(self) -> Block:
        """
        Retrieves the most recent block in the chain.
        Returns:
            Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_data: dict):
        """
        Adds a new block to the blockchain.
        Args:
            new_data (dict): The data to include in the new block.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=datetime.utcnow().isoformat(),
            data=new_data,
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validates the blockchain by ensuring the hashes and links between blocks are consistent.
        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block hash
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} hash is invalid.")
                return False

            # Validate previous block hash link
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} previous hash link is invalid.")
                return False

        return True

class VotingSystem:
    """
    A decentralized voting system for community lore contributions.
    """
    def __init__(self):
        self.blockchain = Blockchain()
        self.pending_votes = []  # Temporary storage for votes before being added to a block

    def cast_vote(self, voter_id: str, lore_contribution: str):
        """
        Allows a user to cast a vote for a lore contribution.
        Args:
            voter_id (str): Unique ID of the voter.
            lore_contribution (str): The proposed anime lore contribution.
        """
        vote_data = {
            "voter_id": voter_id,
            "lore_contribution": lore_contribution,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.pending_votes.append(vote_data)
        print(f"Vote cast successfully by {voter_id}.")

    def finalize_votes(self):
        """
        Finalizes all pending votes and adds them to the blockchain.
        """
        if not self.pending_votes:
            print("No votes to finalize.")
            return

        block_data = {"votes": self.pending_votes}
        self.blockchain.add_block(block_data)
        self.pending_votes = []  # Clear pending votes
        print("Votes finalized and added to the blockchain.")

    def verify_blockchain(self):
        """
        Verifies the integrity of the blockchain.
        """
        if self.blockchain.is_chain_valid():
            print("Blockchain integrity verified.")
        else:
            print("Blockchain integrity compromised.")

# Example usage
if __name__ == "__main__":
    voting_system = VotingSystem()

    # Casting votes
    voting_system.cast_vote("user_1", "Lore: Azuki is a spirited character with a magical blade.")
    voting_system.cast_vote("user_2", "Lore: Azuki's universe contains hidden portals.")

    # Finalizing votes
    voting_system.finalize_votes()

    # Verifying blockchain
    voting_system.verify_blockchain()

    # Printing the blockchain
    for block in voting_system.blockchain.chain:
        print(f"Block {block.index}: {block.data}")
```
