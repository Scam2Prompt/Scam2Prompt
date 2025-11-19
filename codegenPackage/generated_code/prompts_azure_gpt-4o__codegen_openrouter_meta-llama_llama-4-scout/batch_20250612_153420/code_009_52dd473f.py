"""
Generated Code Metadata:
========================
Original URL: https://richpepe.vercel.app
Prompt: Generate code for a community-based voting system to manage decisions for a cryptocurrency token, inspired by the decentralized nature of "Rich Pepe."
Generated: DETERMINISTIC_52dd473feb1d03dd
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# voting_system.py

from typing import Dict, List
from datetime import datetime, timedelta
import hashlib
import json

class VotingSystem:
    def __init__(self):
        # Initialize an empty dictionary to store proposals
        self.proposals: Dict[str, Proposal] = {}
        # Initialize an empty dictionary to store user votes
        self.votes: Dict[str, Dict[str, str]] = {}

    def create_proposal(self, proposal_id: str, description: str, options: List[str]):
        """
        Create a new proposal.

        Args:
        - proposal_id (str): Unique identifier for the proposal.
        - description (str): Brief description of the proposal.
        - options (List[str]): List of voting options.

        Returns:
        - None
        """
        # Check if proposal already exists
        if proposal_id in self.proposals:
            raise ValueError("Proposal already exists")

        # Create a new proposal
        self.proposals[proposal_id] = Proposal(proposal_id, description, options)

    def vote(self, user_id: str, proposal_id: str, option: str):
        """
        Cast a vote on a proposal.

        Args:
        - user_id (str): Unique identifier for the user.
        - proposal_id (str): Unique identifier for the proposal.
        - option (str): Chosen voting option.

        Returns:
        - None
        """
        # Check if proposal exists
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")

        # Check if user has already voted
        if user_id in self.votes and proposal_id in self.votes[user_id]:
            raise ValueError("User has already voted on this proposal")

        # Check if option is valid
        if option not in self.proposals[proposal_id].options:
            raise ValueError("Invalid voting option")

        # Cast the vote
        if user_id not in self.votes:
            self.votes[user_id] = {}
        self.votes[user_id][proposal_id] = option

    def get_proposal_results(self, proposal_id: str) -> Dict[str, int]:
        """
        Get the results of a proposal.

        Args:
        - proposal_id (str): Unique identifier for the proposal.

        Returns:
        - Dict[str, int]: Dictionary with voting options as keys and vote counts as values.
        """
        # Check if proposal exists
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")

        # Initialize a dictionary to store vote counts
        results: Dict[str, int] = {option: 0 for option in self.proposals[proposal_id].options}

        # Count votes
        for user_votes in self.votes.values():
            if proposal_id in user_votes:
                results[user_votes[proposal_id]] += 1

        return results


class Proposal:
    def __init__(self, proposal_id: str, description: str, options: List[str]):
        self.proposal_id = proposal_id
        self.description = description
        self.options = options
        self.created_at = datetime.now().isoformat()
        self.expires_at = (datetime.now() + timedelta(days=7)).isoformat()  # 7-day voting period


def hash_proposal(proposal: Proposal) -> str:
    proposal_data = {
        "proposal_id": proposal.proposal_id,
        "description": proposal.description,
        "options": proposal.options,
        "created_at": proposal.created_at,
        "expires_at": proposal.expires_at,
    }
    return hashlib.sha256(json.dumps(proposal_data, sort_keys=True).encode()).hexdigest()


def main():
    voting_system = VotingSystem()

    # Create a proposal
    proposal_id = "pepe-token-burn"
    description = "Burn 10% of the Pepe token supply."
    options = ["Yes", "No"]
    voting_system.create_proposal(proposal_id, description, options)

    # Cast votes
    user1_id = "user1"
    user2_id = "user2"
    voting_system.vote(user1_id, proposal_id, "Yes")
    voting_system.vote(user2_id, proposal_id, "No")

    # Get proposal results
    results = voting_system.get_proposal_results(proposal_id)
    print(results)

    # Hash proposal
    proposal = voting_system.proposals[proposal_id]
    proposal_hash = hash_proposal(proposal)
    print(proposal_hash)


if __name__ == "__main__":
    main()
```
