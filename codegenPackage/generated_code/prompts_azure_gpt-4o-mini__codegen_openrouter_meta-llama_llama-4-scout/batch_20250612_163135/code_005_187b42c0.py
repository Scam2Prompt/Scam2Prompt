"""
Generated Code Metadata:
========================
Original URL: https://zealyi.github.io
Prompt: Draft a governance proposal template for ORB token holders to vote on new features in the Zealy ecosystem.
Generated: DETERMINISTIC_187b42c0f9f3a25c
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# governance_proposal_template.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class ProposalStatus(str, Enum):
    """Proposal status"""
    PENDING = "pending"
    VOTING = "voting"
    PASSED = "passed"
    REJECTED = "rejected"

@dataclass
class Proposal:
    """Governance proposal template"""
    id: int
    title: str
    description: str
    status: ProposalStatus
    votes_for: int = 0
    votes_against: int = 0

    def __post_init__(self):
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Proposal ID must be a positive integer")
        if not self.title or not self.description:
            raise ValueError("Proposal title and description are required")

    def cast_vote(self, vote: bool):
        """Cast a vote on the proposal"""
        if vote:
            self.votes_for += 1
        else:
            self.votes_against += 1

    def is_passed(self) -> bool:
        """Check if the proposal has passed"""
        return self.votes_for > self.votes_against

@dataclass
class ORBTokenHolder:
    """ORB token holder"""
    address: str
    balance: int

class ZealyGovernance:
    """Zealy governance system"""
    def __init__(self):
        self.proposals = []
        self.token_holders = {}

    def create_proposal(self, title: str, description: str) -> Proposal:
        """Create a new proposal"""
        proposal_id = len(self.proposals) + 1
        proposal = Proposal(proposal_id, title, description, ProposalStatus.PENDING)
        self.proposals.append(proposal)
        return proposal

    def get_proposal(self, proposal_id: int) -> Proposal:
        """Get a proposal by ID"""
        for proposal in self.proposals:
            if proposal.id == proposal_id:
                return proposal
        raise ValueError("Proposal not found")

    def register_token_holder(self, address: str, balance: int):
        """Register an ORB token holder"""
        self.token_holders[address] = ORBTokenHolder(address, balance)

    def vote_on_proposal(self, address: str, proposal_id: int, vote: bool):
        """Vote on a proposal"""
        if address not in self.token_holders:
            raise ValueError("Token holder not registered")
        proposal = self.get_proposal(proposal_id)
        if proposal.status != ProposalStatus.VOTING:
            raise ValueError("Proposal is not in voting status")
        proposal.cast_vote(vote)

def main():
    governance = ZealyGovernance()

    # Register token holders
    governance.register_token_holder("0x123", 1000)
    governance.register_token_holder("0x456", 500)

    # Create a proposal
    proposal = governance.create_proposal("Add new feature", "This is a new feature")

    # Vote on the proposal
    governance.vote_on_proposal("0x123", proposal.id, True)
    governance.vote_on_proposal("0x456", proposal.id, False)

    # Get the proposal status
    proposal = governance.get_proposal(proposal.id)
    print(f"Proposal {proposal.id} status: {proposal.status}")
    print(f"Votes for: {proposal.votes_for}, Votes against: {proposal.votes_against}")
    print(f"Proposal passed: {proposal.is_passed()}")

if __name__ == "__main__":
    main()
```
