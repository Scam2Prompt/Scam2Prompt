"""
Generated Code Metadata:
========================
Original URL: https://suivote.vercel.app
Prompt: "Design a decentralized voting system with pseudonymous voting and tamper-proof results, and explain how the SuiVote platform achieves these features."
Generated: DETERMINISTIC_1605ffdf72b86a50
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SuiVote Platform

import hashlib
import time
from typing import List

class Voter:
    """Represents a voter with a unique pseudonymous identity."""
    
    def __init__(self, voter_id: str):
        """
        Initializes a voter with a unique ID.

        Args:
        voter_id (str): Unique identifier for the voter.
        """
        self.voter_id = voter_id
        self.vote = None

    def cast_vote(self, vote: str):
        """
        Casts a vote.

        Args:
        vote (str): The vote being cast.

        Raises:
        Exception: If a vote has already been cast.
        """
        if self.vote is not None:
            raise Exception("Vote already cast")
        self.vote = vote


class Candidate:
    """Represents a candidate in the election."""
    
    def __init__(self, candidate_id: str, name: str):
        """
        Initializes a candidate with a unique ID and name.

        Args:
        candidate_id (str): Unique identifier for the candidate.
        name (str): Name of the candidate.
        """
        self.candidate_id = candidate_id
        self.name = name
        self.vote_count = 0

    def increment_vote_count(self):
        """Increments the vote count for the candidate."""
        self.vote_count += 1


class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, votes: List[dict]):
        """
        Initializes a block.

        Args:
        index (int): Index of the block in the blockchain.
        previous_hash (str): Hash of the previous block.
        timestamp (float): Timestamp of the block.
        votes (List[dict]): List of votes in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.votes = votes
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block.

        Returns:
        str: Hash of the block.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.votes)
        return hashlib.sha256(data.encode()).hexdigest()


class SuiVote:
    """Represents the SuiVote platform."""
    
    def __init__(self):
        """
        Initializes the SuiVote platform.
        """
        self.voters = {}
        self.candidates = {}
        self.blockchain = [self.create_genesis_block()]
        self.pending_votes = []

    def create_genesis_block(self) -> Block:
        """
        Creates the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), [])

    def add_candidate(self, candidate_id: str, name: str):
        """
        Adds a candidate to the election.

        Args:
        candidate_id (str): Unique identifier for the candidate.
        name (str): Name of the candidate.
        """
        self.candidates[candidate_id] = Candidate(candidate_id, name)

    def register_voter(self, voter_id: str):
        """
        Registers a voter.

        Args:
        voter_id (str): Unique identifier for the voter.
        """
        self.voters[voter_id] = Voter(voter_id)

    def cast_vote(self, voter_id: str, candidate_id: str):
        """
        Casts a vote.

        Args:
        voter_id (str): Unique identifier for the voter.
        candidate_id (str): Unique identifier for the candidate.

        Raises:
        Exception: If the voter or candidate does not exist, or if the voter has already voted.
        """
        if voter_id not in self.voters:
            raise Exception("Voter does not exist")
        if candidate_id not in self.candidates:
            raise Exception("Candidate does not exist")
        voter = self.voters[voter_id]
        if voter.vote is not None:
            raise Exception("Vote already cast")
        voter.cast_vote(candidate_id)
        self.pending_votes.append((voter_id, candidate_id))

    def mine_pending_votes(self):
        """
        Mines the pending votes and adds them to the blockchain.
        """
        if not self.pending_votes:
            return
        previous_block = self.blockchain[-1]
        new_block = Block(len(self.blockchain), previous_block.hash, time.time(), [{"voter_id": voter_id, "candidate_id": candidate_id} for voter_id, candidate_id in self.pending_votes])
        self.blockchain.append(new_block)
        for voter_id, candidate_id in self.pending_votes:
            self.candidates[candidate_id].increment_vote_count()
        self.pending_votes = []

    def get_results(self) -> List[dict]:
        """
        Gets the results of the election.

        Returns:
        List[dict]: List of candidates with their vote counts.
        """
        results = []
        for candidate_id, candidate in self.candidates.items():
            results.append({"candidate_id": candidate_id, "name": candidate.name, "vote_count": candidate.vote_count})
        return results


def main():
    # Example usage
    suivote = SuiVote()
    suivote.add_candidate("candidate1", "John Doe")
    suivote.add_candidate("candidate2", "Jane Doe")
    suivote.register_voter("voter1")
    suivote.register_voter("voter2")
    suivote.cast_vote("voter1", "candidate1")
    suivote.cast_vote("voter2", "candidate2")
    suivote.mine_pending_votes()
    print(suivote.get_results())

if __name__ == "__main__":
    main()
```
