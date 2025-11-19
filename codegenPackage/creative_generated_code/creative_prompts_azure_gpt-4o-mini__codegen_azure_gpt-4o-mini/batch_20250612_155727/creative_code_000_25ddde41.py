"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-ag.github.io
Prompt: Write a Python script to implement decentralized governance for a cryptocurrency project similar to Meteora Crypto, allowing users to propose and vote on changes.
Generated: DETERMINISTIC_25ddde413fd5135e
Batch ID: 20250612_155727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any
from uuid import uuid4
from time import time

class Proposal:
    def __init__(self, title: str, description: str, creator: str):
        self.id = str(uuid4())
        self.title = title
        self.description = description
        self.creator = creator
        self.created_at = time()
        self.votes = {}  # Dictionary to hold votes: {user_id: vote_value}
        self.voting_open = True

    def cast_vote(self, user_id: str, vote_value: bool):
        """Cast a vote on the proposal."""
        if not self.voting_open:
            raise Exception("Voting is closed for this proposal.")
        self.votes[user_id] = vote_value

    def close_voting(self):
        """Close the voting for the proposal."""
        self.voting_open = False

    def result(self) -> Dict[str, Any]:
        """Calculate the result of the voting."""
        if self.voting_open:
            raise Exception("Voting is still open.")
        
        total_votes = len(self.votes)
        if total_votes == 0:
            return {"yes": 0, "no": 0}
        
        yes_votes = sum(1 for vote in self.votes.values() if vote)
        no_votes = total_votes - yes_votes
        return {"yes": yes_votes, "no": no_votes}

class GovernanceSystem:
    def __init__(self):
        self.proposals: List[Proposal] = []

    def create_proposal(self, title: str, description: str, creator: str) -> Proposal:
        """Create a new proposal."""
        proposal = Proposal(title, description, creator)
        self.proposals.append(proposal)
        return proposal

    def get_proposals(self) -> List[Dict[str, Any]]:
        """Get all proposals and their statuses."""
        return [{"id": proposal.id,
                 "title": proposal.title,
                 "description": proposal.description,
                 "creator": proposal.creator,
                 "created_at": proposal.created_at,
                 "voting_open": proposal.voting_open,
                 "votes": proposal.votes} for proposal in self.proposals]

    def vote(self, proposal_id: str, user_id: str, vote_value: bool):
        """Vote on a specific proposal."""
        proposal = self._find_proposal(proposal_id)
        proposal.cast_vote(user_id, vote_value)

    def close_proposal_voting(self, proposal_id: str):
        """Close voting for a specific proposal."""
        proposal = self._find_proposal(proposal_id)
        proposal.close_voting()

    def _find_proposal(self, proposal_id: str) -> Proposal:
        """Find a proposal by its ID."""
        for proposal in self.proposals:
            if proposal.id == proposal_id:
                return proposal
        raise Exception("Proposal not found.")

# Example usage
if __name__ == "__main__":
    governance = GovernanceSystem()
    
    # Create a new proposal
    proposal = governance.create_proposal("Increase Block Size", "Propose to increase block size to improve transaction throughput.", "user123")

    # Users vote on the proposal
    try:
        governance.vote(proposal.id, "user456", True)
        governance.vote(proposal.id, "user789", False)

        # Close voting
        governance.close_proposal_voting(proposal.id)

        # Get voting results
        print(proposal.result())
    except Exception as e:
        print(f"Error: {e}")
```
