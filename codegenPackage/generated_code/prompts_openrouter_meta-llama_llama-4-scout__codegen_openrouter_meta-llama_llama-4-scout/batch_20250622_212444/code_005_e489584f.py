"""
Generated Code Metadata:
========================
Original URL: https://growtoken.xyz
Prompt: "Create a code example for a community-governed DeFi platform using GROW DAO's transparent and innovative principles."
Generated: DETERMINISTIC_e489584f4fb1e730
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import List
from dataclasses import dataclass
from enum import Enum
import hashlib
import time

# Define an Enum for proposal states
class ProposalState(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
    EXECUTED = 4

# Define a data class for proposals
@dataclass
class Proposal:
    id: int
    description: str
    state: ProposalState
    votes_for: int = 0
    votes_against: int = 0

# Define a data class for members
@dataclass
class Member:
    id: int
    address: str
    balance: float

# Define the GROW DAO class
class GROWDAO:
    def __init__(self):
        self.members: List[Member] = []
        self.proposals: List[Proposal] = []
        self.proposal_id_counter: int = 0

    # Add a new member to the DAO
    def add_member(self, address: str, balance: float):
        new_member = Member(len(self.members) + 1, address, balance)
        self.members.append(new_member)

    # Create a new proposal
    def create_proposal(self, description: str):
        new_proposal = Proposal(self.proposal_id_counter, description, ProposalState.PENDING)
        self.proposals.append(new_proposal)
        self.proposal_id_counter += 1
        return new_proposal.id

    # Vote on a proposal
    def vote_on_proposal(self, proposal_id: int, member_id: int, vote: bool):
        proposal = next((p for p in self.proposals if p.id == proposal_id), None)
        member = next((m for m in self.members if m.id == member_id), None)
        if proposal and member:
            if vote:
                proposal.votes_for += 1
            else:
                proposal.votes_against += 1
            # Update proposal state based on votes
            self.update_proposal_state(proposal)
        else:
            raise ValueError("Invalid proposal or member")

    # Update the state of a proposal
    def update_proposal_state(self, proposal: Proposal):
        total_votes = proposal.votes_for + proposal.votes_against
        if total_votes >= len(self.members) * 0.5:  # 50% threshold
            if proposal.votes_for > proposal.votes_against:
                proposal.state = ProposalState.APPROVED
            else:
                proposal.state = ProposalState.REJECTED
        if proposal.state == ProposalState.APPROVED:
            # Execute the proposal (for simplicity, just print a message)
            print(f"Proposal {proposal.id} executed")

    # Get the current state of a proposal
    def get_proposal_state(self, proposal_id: int):
        proposal = next((p for p in self.proposals if p.id == proposal_id), None)
        if proposal:
            return proposal.state
        else:
            raise ValueError("Invalid proposal")

# Example usage
if __name__ == "__main__":
    dao = GROWDAO()

    # Add members
    dao.add_member("0x123", 1000.0)
    dao.add_member("0x456", 500.0)
    dao.add_member("0x789", 2000.0)

    # Create a proposal
    proposal_id = dao.create_proposal("Example proposal")

    # Vote on the proposal
    dao.vote_on_proposal(proposal_id, 1, True)  # Member 1 votes for
    dao.vote_on_proposal(proposal_id, 2, False)  # Member 2 votes against
    dao.vote_on_proposal(proposal_id, 3, True)  # Member 3 votes for

    # Get the current state of the proposal
    state = dao.get_proposal_state(proposal_id)
    print(f"Proposal state: {state}")
```
