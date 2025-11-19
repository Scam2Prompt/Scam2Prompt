"""
Generated Code Metadata:
========================
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Generate code to implement a voting mechanism that supports partial delegation for Optimism token holders, as described on the Agora platform.
Generated: DETERMINISTIC_f1770d7805708b6f
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# voting_mechanism.py

from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Voter:
    """Represents a voter with their Optimism token holdings."""
    address: str
    tokens: int

class VotingMechanism:
    """Implements a voting mechanism with partial delegation for Optimism token holders."""

    def __init__(self, voters: List[Voter], delegates: Dict[str, str]):
        """
        Initializes the voting mechanism.

        Args:
        - voters (List[Voter]): A list of voters with their Optimism token holdings.
        - delegates (Dict[str, str]): A dictionary mapping voter addresses to their delegates.
        """
        self.voters = {voter.address: voter for voter in voters}
        self.delegates = delegates
        self.vote_cast: Dict[str, int] = {}  # Maps voter addresses to their vote weights

    def delegate(self, voter_address: str, delegate_address: str):
        """
        Sets a delegate for a voter.

        Args:
        - voter_address (str): The address of the voter.
        - delegate_address (str): The address of the delegate.
        """
        if voter_address not in self.voters:
            raise ValueError("Voter not found")

        self.delegates[voter_address] = delegate_address

    def cast_vote(self, voter_address: str, vote_weight: int):
        """
        Casts a vote with partial delegation.

        Args:
        - voter_address (str): The address of the voter.
        - vote_weight (int): The weight of the vote.

        Raises:
        - ValueError: If the voter has not enough tokens or if the vote weight is invalid.
        """
        voter = self.voters.get(voter_address)
        if not voter:
            raise ValueError("Voter not found")

        if vote_weight < 0 or vote_weight > voter.tokens:
            raise ValueError("Invalid vote weight")

        delegate_address = self.delegates.get(voter_address)
        if delegate_address:
            # Partial delegation: add vote weight to delegate's vote
            self.vote_cast[delegate_address] = self.vote_cast.get(delegate_address, 0) + vote_weight
        else:
            # Direct vote: add vote weight to voter's vote
            self.vote_cast[voter_address] = self.vote_cast.get(voter_address, 0) + vote_weight

        # Update voter's remaining tokens
        voter.tokens -= vote_weight

    def get_votes(self) -> Dict[str, int]:
        """
        Returns a dictionary of votes cast.

        Returns:
        - Dict[str, int]: A dictionary mapping voter addresses to their vote weights.
        """
        return self.vote_cast


# Example usage:
if __name__ == "__main__":
    voters = [
        Voter("0x123", 100),
        Voter("0x456", 50),
    ]

    delegates = {
        "0x123": "0x789",
    }

    voting_mechanism = VotingMechanism(voters, delegates)

    voting_mechanism.cast_vote("0x123", 50)
    voting_mechanism.cast_vote("0x456", 20)

    votes = voting_mechanism.get_votes()
    print(votes)
```
