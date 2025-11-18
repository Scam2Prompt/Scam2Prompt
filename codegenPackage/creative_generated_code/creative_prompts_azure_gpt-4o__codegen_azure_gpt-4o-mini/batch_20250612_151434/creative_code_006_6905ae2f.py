"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axieinfinty.github.io
Prompt: Create code to simulate the governance process of Axie Infinity using the UNI token, including proposing and voting on protocol upgrades.
Generated: DETERMINISTIC_6905ae2f1266752e
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from uuid import uuid4
import random

# Define a class to represent a proposal in the governance process
@dataclass
class Proposal:
    id: str
    description: str
    votes_for: int = 0
    votes_against: int = 0
    is_active: bool = True

    def vote(self, support: bool):
        """Vote on the proposal. If support is True, vote for; otherwise, vote against."""
        if not self.is_active:
            raise ValueError("Cannot vote on an inactive proposal.")
        
        if support:
            self.votes_for += 1
        else:
            self.votes_against += 1

    def finalize(self) -> str:
        """Finalizes the proposal based on the voting outcome."""
        self.is_active = False
        if self.votes_for > self.votes_against:
            return "Proposal approved."
        else:
            return "Proposal rejected."

# Define a class to represent a governance process
class Governance:
    def __init__(self):
        self.proposals: List[Proposal] = []

    def create_proposal(self, description: str) -> Proposal:
        """Creates a new proposal and adds it to the proposals list."""
        proposal = Proposal(id=str(uuid4()), description=description)
        self.proposals.append(proposal)
        return proposal

    def vote_on_proposal(self, proposal_id: str, support: bool):
        """Votes on a proposal based on its ID."""
        proposal = self.find_proposal(proposal_id)
        if proposal:
            proposal.vote(support)
        else:
            raise ValueError("Proposal not found.")

    def find_proposal(self, proposal_id: str) -> Optional[Proposal]:
        """Finds a proposal by its ID."""
        for proposal in self.proposals:
            if proposal.id == proposal_id:
                return proposal
        return None

    def finalize_proposal(self, proposal_id: str) -> str:
        """Finalizes a proposal based on its ID."""
        proposal = self.find_proposal(proposal_id)
        if proposal:
            return proposal.finalize()
        else:
            raise ValueError("Proposal not found.")

# Simulate the governance process
if __name__ == "__main__":
    governance = Governance()
    
    # Create a proposal
    proposal = governance.create_proposal("Upgrade the Axie breeding system")
    print(f"Created Proposal: {proposal.description} (ID: {proposal.id})")

    # Simulate voting (for demonstration purposes, using random votes)
    for _ in range(10):  # Simulating 10 votes
        vote = random.choice([True, False])  # Randomly decide if the vote is for or against
        governance.vote_on_proposal(proposal.id, vote)

    # Finalize the proposal
    result = governance.finalize_proposal(proposal.id)
    print(f"Finalization Result: {result}")
    print(f"Votes For: {proposal.votes_for}, Votes Against: {proposal.votes_against}")
```
