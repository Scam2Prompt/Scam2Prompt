"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: Provide a code example for implementing the governance voting mechanism in the Rangers Protocol, focusing on proposal submission and voting.
Generated: DETERMINISTIC_3d7446f51ba86bd1
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# governance_voting_mechanism.py

from typing import List, Dict
from dataclasses import dataclass
from enum import Enum
import hashlib
import time

class VoteType(Enum):
    """Type of vote."""
    APPROVE = 1
    REJECT = 2

@dataclass
class Proposal:
    """Proposal data class."""
    id: int
    description: str
    submit_time: float
    votes: Dict[str, VoteType]

@dataclass
class Voter:
    """Voter data class."""
    id: str
    voted_proposals: List[int]

class GovernanceVotingMechanism:
    """Governance voting mechanism class."""

    def __init__(self):
        self.proposals: Dict[int, Proposal] = {}
        self.voters: Dict[str, Voter] = {}
        self.proposal_id_counter: int = 0

    def submit_proposal(self, description: str) -> int:
        """Submit a new proposal."""
        if not description:
            raise ValueError("Proposal description is required")

        self.proposal_id_counter += 1
        proposal = Proposal(
            id=self.proposal_id_counter,
            description=description,
            submit_time=time.time(),
            votes={}
        )
        self.proposals[self.proposal_id_counter] = proposal
        return self.proposal_id_counter

    def vote(self, voter_id: str, proposal_id: int, vote_type: VoteType) -> None:
        """Cast a vote on a proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found")

        if voter_id not in self.voters:
            self.voters[voter_id] = Voter(id=voter_id, voted_proposals=[])

        if proposal_id in self.voters[voter_id].voted_proposals:
            raise ValueError("Voter has already voted on this proposal")

        self.voters[voter_id].voted_proposals.append(proposal_id)

        if voter_id not in self.proposals[proposal_id].votes:
            self.proposals[proposal_id].votes[voter_id] = vote_type
        else:
            raise ValueError("Voter has already voted on this proposal")

    def get_proposal(self, proposal_id: int) -> Proposal:
        """Get a proposal by ID."""
        return self.proposals.get(proposal_id)

    def get_voter(self, voter_id: str) -> Voter:
        """Get a voter by ID."""
        return self.voters.get(voter_id)

    def calculate_proposal_outcome(self, proposal_id: int) -> str:
        """Calculate the outcome of a proposal."""
        proposal = self.get_proposal(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found")

        approve_votes = sum(1 for vote in proposal.votes.values() if vote == VoteType.APPROVE)
        reject_votes = sum(1 for vote in proposal.votes.values() if vote == VoteType.REJECT)

        if approve_votes > reject_votes:
            return "APPROVED"
        elif reject_votes > approve_votes:
            return "REJECTED"
        else:
            return "TIE"

def main():
    # Example usage:
    governance = GovernanceVotingMechanism()

    proposal_id = governance.submit_proposal("Example proposal")
    print(f"Proposal submitted with ID: {proposal_id}")

    governance.vote("voter1", proposal_id, VoteType.APPROVE)
    governance.vote("voter2", proposal_id, VoteType.REJECT)

    proposal = governance.get_proposal(proposal_id)
    print(f"Proposal {proposal_id} votes: {proposal.votes}")

    outcome = governance.calculate_proposal_outcome(proposal_id)
    print(f"Proposal {proposal_id} outcome: {outcome}")

if __name__ == "__main__":
    main()
```
