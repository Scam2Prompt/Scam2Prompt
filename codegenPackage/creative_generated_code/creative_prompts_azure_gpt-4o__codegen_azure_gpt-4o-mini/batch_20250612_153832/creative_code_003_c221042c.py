"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-morpho.github.io
Prompt: Create a governance voting system for token holders, allowing users to vote on proposals and fee structures, inspired by Morpho's governance mechanism.
Generated: DETERMINISTIC_c221042cd0c50898
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# GovernanceVotingSystem.py

from typing import List, Dict, Optional
from dataclasses import dataclass, field
from enum import Enum
import uuid


class ProposalStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass
class Proposal:
    id: str
    description: str
    votes_for: int = 0
    votes_against: int = 0
    status: ProposalStatus = ProposalStatus.PENDING
    voters: set = field(default_factory=set)

    def vote(self, user_id: str, vote: bool) -> None:
        """Record a user's vote on the proposal."""
        if user_id in self.voters:
            raise ValueError("User has already voted.")
        
        self.voters.add(user_id)
        
        if vote:
            self.votes_for += 1
        else:
            self.votes_against += 1

    def finalize(self) -> None:
        """Finalizes the proposal based on the voting results."""
        if self.votes_for > self.votes_against:
            self.status = ProposalStatus.APPROVED
        else:
            self.status = ProposalStatus.REJECTED


class GovernanceVotingSystem:
    def __init__(self):
        """Initialize the voting system with an empty list of proposals."""
        self.proposals: Dict[str, Proposal] = {}

    def create_proposal(self, description: str) -> Proposal:
        """Creates a new proposal and adds it to the system."""
        proposal_id = str(uuid.uuid4())
        new_proposal = Proposal(id=proposal_id, description=description)
        self.proposals[proposal_id] = new_proposal
        return new_proposal

    def vote(self, proposal_id: str, user_id: str, vote: bool) -> None:
        """Allows a user to cast a vote on a proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")
        
        proposal = self.proposals[proposal_id]
        proposal.vote(user_id, vote)

    def finalize_proposal(self, proposal_id: str) -> None:
        """Finalize the voting for a proposal and update its status."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")
        
        proposal = self.proposals[proposal_id]
        proposal.finalize()

    def get_proposal(self, proposal_id: str) -> Optional[Proposal]:
        """Retrieve a proposal by its ID."""
        return self.proposals.get(proposal_id)

    def list_proposals(self) -> List[Proposal]:
        """Returns a list of all proposals."""
        return list(self.proposals.values())


# Example usage:
if __name__ == "__main__":
    try:
        voting_system = GovernanceVotingSystem()
        
        # Create a proposal
        proposal = voting_system.create_proposal("Increase the protocol fee by 2%")
        print(f"Created Proposal: {proposal}")

        # User votes
        voting_system.vote(proposal.id, "user_1", True)
        voting_system.vote(proposal.id, "user_2", False)

        # Finalize the proposal
        voting_system.finalize_proposal(proposal.id)

        # Check proposal status
        finalized_proposal = voting_system.get_proposal(proposal.id)
        print(f"Finalized Proposal: {finalized_proposal}")

    except ValueError as e:
        print(f"Error: {e}")
```
