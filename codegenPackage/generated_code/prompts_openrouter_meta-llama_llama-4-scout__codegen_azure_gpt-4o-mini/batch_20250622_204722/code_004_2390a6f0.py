"""
Generated Code Metadata:
========================
Original URL: https://mantle-xyz.pages.dev
Prompt: "Design a simple governance proposal for the Mantle ecosystem using the $MNT token, including a voting mechanism and decision-making process."
Generated: DETERMINISTIC_2390a6f0e33e19c7
Batch ID: 20250622_204722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# governance_proposal.py

from typing import List, Dict, Optional
from dataclasses import dataclass, field
from collections import defaultdict

@dataclass
class Proposal:
    """Class representing a governance proposal."""
    id: int
    title: str
    description: str
    votes_for: int = 0
    votes_against: int = 0
    total_votes: int = 0
    is_active: bool = True

    def vote(self, in_favor: bool):
        """Record a vote for or against the proposal."""
        if not self.is_active:
            raise ValueError("Voting has ended for this proposal.")
        
        if in_favor:
            self.votes_for += 1
        else:
            self.votes_against += 1
        
        self.total_votes += 1

    def finalize(self):
        """Finalize the proposal and determine the outcome."""
        self.is_active = False
        if self.votes_for > self.votes_against:
            return "Proposal Passed"
        else:
            return "Proposal Rejected"

class Governance:
    """Class to manage governance proposals and voting."""
    def __init__(self):
        self.proposals: Dict[int, Proposal] = {}
        self.next_proposal_id: int = 1

    def create_proposal(self, title: str, description: str) -> Proposal:
        """Create a new governance proposal."""
        proposal = Proposal(id=self.next_proposal_id, title=title, description=description)
        self.proposals[self.next_proposal_id] = proposal
        self.next_proposal_id += 1
        return proposal

    def vote_on_proposal(self, proposal_id: int, in_favor: bool):
        """Vote on a specific proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        
        proposal = self.proposals[proposal_id]
        proposal.vote(in_favor)

    def finalize_proposal(self, proposal_id: int) -> Optional[str]:
        """Finalize a proposal and return the outcome."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        
        proposal = self.proposals[proposal_id]
        return proposal.finalize()

    def get_proposal(self, proposal_id: int) -> Optional[Proposal]:
        """Retrieve a proposal by its ID."""
        return self.proposals.get(proposal_id)

# Example usage
if __name__ == "__main__":
    governance = Governance()
    
    # Create a new proposal
    proposal = governance.create_proposal("Increase Block Size", "Proposal to increase the block size to improve transaction throughput.")
    
    # Simulate voting
    try:
        governance.vote_on_proposal(proposal.id, in_favor=True)
        governance.vote_on_proposal(proposal.id, in_favor=False)
        
        # Finalize the proposal
        outcome = governance.finalize_proposal(proposal.id)
        print(f"Proposal Outcome: {outcome}")
    except ValueError as e:
        print(f"Error: {e}")
```
