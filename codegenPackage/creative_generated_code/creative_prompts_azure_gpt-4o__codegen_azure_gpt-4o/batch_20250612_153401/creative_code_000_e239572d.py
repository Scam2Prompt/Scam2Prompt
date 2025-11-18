"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayeaye-pro.pages.dev
Prompt: Write code to simulate the "proof of community algorithm" described by the Aye Aye Coin project, ensuring it emphasizes community participation metrics.
Generated: DETERMINISTIC_e239572dcb549140
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time
from typing import List, Dict

class CommunityMember:
    """
    Represents a community member with their unique ID and participation metrics.
    """
    def __init__(self, member_id: str, participation_score: int):
        self.member_id = member_id
        self.participation_score = participation_score

class ProofOfCommunityBlock:
    """
    Represents a single block in the Proof of Community blockchain.
    """
    def __init__(self, index: int, timestamp: float, data: str, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # Encodes participation metrics
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Generates the hash for the block using its content.
        """
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_content.encode()).hexdigest()

class ProofOfCommunityChain:
    """
    Blockchain implementation for the Proof of Community algorithm.
    """
    def __init__(self):
        self.chain: List[ProofOfCommunityBlock] = [self.create_genesis_block()]
        self.community_members: Dict[str, CommunityMember] = {}

    def create_genesis_block(self) -> ProofOfCommunityBlock:
        """
        Creates the genesis block to start the blockchain.
        """
        return ProofOfCommunityBlock(0, time.time(), "Genesis Block", "0")

    def add_member(self, member_id: str, participation_score: int):
        """
        Adds a new community member to the system.
        """
        if member_id in self.community_members:
            raise ValueError(f"Member with ID {member_id} already exists.")
        self.community_members[member_id] = CommunityMember(member_id, participation_score)

    def update_participation_score(self, member_id: str, score_delta: int):
        """
        Updates the participation score of an existing community member.
        """
        if member_id not in self.community_members:
            raise ValueError(f"Member with ID {member_id} does not exist.")
        self.community_members[member_id].participation_score += score_delta

    def calculate_community_participation_metric(self) -> int:
        """
        Calculates the community participation metric, which is the sum of all participation scores.
        """
        return sum(member.participation_score for member in self.community_members.values())

    def create_block(self) -> ProofOfCommunityBlock:
        """
        Creates and adds a new block to the blockchain. The block's data encodes the community participation metric.
        """
        previous_block = self.chain[-1]
        new_index = previous_block.index + 1
        new_timestamp = time.time()
        participation_metric = self.calculate_community_participation_metric()
        new_data = f"Community Participation Metric: {participation_metric}"
        new_block = ProofOfCommunityBlock(new_index, new_timestamp, new_data, previous_block.hash)
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Validate previous hash link
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self):
        """
        Prints the blockchain in a readable format.
        """
        for block in self.chain:
            print(f"Index: {block.index}, Timestamp: {block.timestamp}, Data: {block.data}, Hash: {block.hash}")

# Example Usage:
if __name__ == "__main__":
    chain = ProofOfCommunityChain()

    # Add members
    chain.add_member("member1", 100)
    chain.add_member("member2", 200)

    # Update participation scores
    chain.update_participation_score("member1", 50)
    chain.update_participation_score("member2", -30)

    # Create blocks
    chain.create_block()
    chain.create_block()

    # Validate chain
    print("Is chain valid?", chain.is_chain_valid())

    # Display chain
    chain.display_chain()
```
