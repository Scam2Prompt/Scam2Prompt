"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayeaye-pro.pages.dev
Prompt: Provide an example of a blockchain-based voting system that could be used to demonstrate the community power emphasized by Aye Aye Coin.
Generated: DETERMINISTIC_50a6497300460e2e
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from hashlib import sha256
from time import time
from typing import List, Dict, Any

class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Any):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Generates the hash for the block using SHA-256.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}"
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
    """
    Represents the entire blockchain and manages the voting process.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.current_votes: List[Dict[str, Any]] = []
        self.create_block(previous_hash='1')  # Create the genesis block

    def create_block(self, previous_hash: str) -> Block:
        """
        Creates a new block and adds it to the blockchain.
        """
        index = len(self.chain) + 1
        timestamp = time()
        block = Block(index, previous_hash, timestamp, self.current_votes)
        self.current_votes = []  # Reset the current votes
        self.chain.append(block)
        return block

    def add_vote(self, voter_id: str, candidate: str) -> None:
        """
        Adds a vote to the current votes.
        """
        # Ensure the voter hasn't voted before (this is a simplification)
        if any(vote['voter_id'] == voter_id for vote in self.current_votes):
            raise Exception("Voter has already voted.")
        
        self.current_votes.append({'voter_id': voter_id, 'candidate': candidate})

    def mine(self) -> Block:
        """
        Mints a new block after adding the current votes.
        """
        if not self.current_votes:
            raise Exception("No votes to mine.")
        
        last_block = self.chain[-1]
        return self.create_block(last_block.hash)

    def get_votes(self) -> Dict[str, int]:
        """
        Returns the tally of votes across the blockchain.
        """
        vote_tally = {}
        for block in self.chain:
            for vote in block.data:
                candidate = vote['candidate']
                vote_tally[candidate] = vote_tally.get(candidate, 0) + 1
        return vote_tally

# Example usage
if __name__ == "__main__":
    try:
        # Create a voting blockchain
        voting_chain = Blockchain()

        # Add votes
        voting_chain.add_vote(voter_id="Voter1", candidate="Alice")
        voting_chain.add_vote(voter_id="Voter2", candidate="Bob")

        # Mine a new block to include the votes
        voting_chain.mine()

        # Add more votes
        voting_chain.add_vote(voter_id="Voter3", candidate="Alice")
        voting_chain.add_vote(voter_id="Voter4", candidate="Bob")

        # Mine another block
        voting_chain.mine()

        # Print the voting result
        vote_results = voting_chain.get_votes()
        print("Vote Results:", vote_results)

    except Exception as e:
        print(f"An error occurred: {e}")
```
