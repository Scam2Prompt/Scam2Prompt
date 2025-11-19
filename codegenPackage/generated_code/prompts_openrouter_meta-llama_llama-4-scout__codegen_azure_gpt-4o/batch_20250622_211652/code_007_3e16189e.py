"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Develop a code example for a basic blockchain-based voting system, including data structures, consensus mechanisms, and security considerations.
Generated: DETERMINISTIC_3e16189ee65091ef
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
import time
from typing import List, Dict, Any

class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index: int, timestamp: float, data: Dict[str, Any], previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using SHA-256.
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
    Represents the blockchain, which is a chain of blocks.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (genesis block).
        """
        genesis_block = Block(index=0, timestamp=time.time(), data={"message": "Genesis Block"}, previous_hash="0")
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data: Dict[str, Any]):
        """
        Adds a new block to the blockchain.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


class VotingSystem:
    """
    Implements a basic blockchain-based voting system.
    """
    def __init__(self):
        self.blockchain = Blockchain()
        self.votes: Dict[str, int] = {}  # Stores vote counts for candidates

    def cast_vote(self, voter_id: str, candidate: str):
        """
        Casts a vote for a candidate. Each vote is recorded as a block in the blockchain.
        """
        if not voter_id or not candidate:
            raise ValueError("Voter ID and candidate name must be provided.")

        # Record the vote in the blockchain
        vote_data = {"voter_id": voter_id, "candidate": candidate}
        self.blockchain.add_block(vote_data)

        # Update the vote count
        if candidate not in self.votes:
            self.votes[candidate] = 0
        self.votes[candidate] += 1

    def get_results(self) -> Dict[str, int]:
        """
        Returns the current voting results.
        """
        return self.votes

    def validate_votes(self) -> bool:
        """
        Validates the integrity of the blockchain to ensure votes are not tampered with.
        """
        return self.blockchain.is_chain_valid()


# Example usage
if __name__ == "__main__":
    voting_system = VotingSystem()

    try:
        # Cast votes
        voting_system.cast_vote(voter_id="Voter1", candidate="Alice")
        voting_system.cast_vote(voter_id="Voter2", candidate="Bob")
        voting_system.cast_vote(voter_id="Voter3", candidate="Alice")

        # Display results
        print("Voting Results:", voting_system.get_results())

        # Validate blockchain integrity
        print("Is blockchain valid?", voting_system.validate_votes())

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
