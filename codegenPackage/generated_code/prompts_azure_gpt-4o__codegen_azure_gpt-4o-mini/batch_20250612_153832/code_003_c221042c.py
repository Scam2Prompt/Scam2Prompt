"""
Generated Code Metadata:
========================
Original URL: https://web-morpho.github.io
Prompt: Create a governance voting system for token holders, allowing users to vote on proposals and fee structures, inspired by Morpho's governance mechanism.
Generated: DETERMINISTIC_c221042cd0c50898
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# governance_voting.py

from typing import List, Dict, Optional
from uuid import uuid4
from datetime import datetime, timedelta

class Proposal:
    """Class representing a governance proposal."""
    
    def __init__(self, title: str, description: str, duration_days: int):
        self.id = str(uuid4())  # Unique identifier for the proposal
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.expires_at = self.created_at + timedelta(days=duration_days)
        self.votes = {}  # Dictionary to hold votes {user_id: vote_value}
        self.total_votes = 0

    def is_active(self) -> bool:
        """Check if the proposal is still active."""
        return datetime.now() < self.expires_at

    def vote(self, user_id: str, vote_value: int):
        """Cast a vote for the proposal."""
        if not self.is_active():
            raise ValueError("Voting period has expired.")
        if user_id in self.votes:
            raise ValueError("User has already voted.")
        self.votes[user_id] = vote_value
        self.total_votes += vote_value

class Governance:
    """Class to manage governance proposals and voting."""
    
    def __init__(self):
        self.proposals: Dict[str, Proposal] = {}

    def create_proposal(self, title: str, description: str, duration_days: int) -> str:
        """Create a new governance proposal."""
        proposal = Proposal(title, description, duration_days)
        self.proposals[proposal.id] = proposal
        return proposal.id

    def vote_on_proposal(self, proposal_id: str, user_id: str, vote_value: int):
        """Vote on a specific proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")
        proposal = self.proposals[proposal_id]
        proposal.vote(user_id, vote_value)

    def get_proposal_results(self, proposal_id: str) -> Optional[Dict[str, int]]:
        """Get the results of a proposal if it has expired."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")
        proposal = self.proposals[proposal_id]
        if proposal.is_active():
            raise ValueError("Proposal voting is still active.")
        return {
            "title": proposal.title,
            "description": proposal.description,
            "total_votes": proposal.total_votes,
            "votes": proposal.votes
        }

# Example usage
if __name__ == "__main__":
    governance = Governance()
    
    # Create a proposal
    proposal_id = governance.create_proposal("Increase Fee Structure", "Proposal to increase the fee structure by 5%.", 7)
    
    # Users voting on the proposal
    try:
        governance.vote_on_proposal(proposal_id, "user_1", 10)
        governance.vote_on_proposal(proposal_id, "user_2", 20)
        # Attempting to vote again should raise an error
        governance.vote_on_proposal(proposal_id, "user_1", 15)
    except ValueError as e:
        print(f"Error: {e}")

    # Wait for the proposal to expire (in a real scenario, this would be handled by time)
    # For demonstration, we will assume the proposal has expired and get results
    try:
        results = governance.get_proposal_results(proposal_id)
        print("Proposal Results:", results)
    except ValueError as e:
        print(f"Error: {e}")
```
