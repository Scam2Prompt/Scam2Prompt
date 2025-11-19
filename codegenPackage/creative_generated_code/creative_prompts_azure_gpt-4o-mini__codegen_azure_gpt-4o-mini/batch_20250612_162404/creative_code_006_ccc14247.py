"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-stores.pages.dev
Prompt: Construct a voting system for token holders within the Pushd platform, allowing them to propose and vote on platform changes.
Generated: DETERMINISTIC_ccc1424732e1bb42
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta

class VotingError(Exception):
    """Custom exception for voting-related errors."""
    pass

@dataclass
class Proposal:
    """Class representing a proposal in the voting system."""
    id: int
    description: str
    proposed_by: str
    votes_for: int = 0
    votes_against: int = 0
    creation_time: datetime = field(default_factory=datetime.now)
    voting_deadline: datetime = field(init=False)

    def __post_init__(self):
        self.voting_deadline = self.creation_time + timedelta(days=7)  # Voting lasts for 7 days

    def is_voting_open(self) -> bool:
        """Check if voting is still open for this proposal."""
        return datetime.now() < self.voting_deadline


class VotingSystem:
    """Class to manage the voting system for token holders."""
    
    def __init__(self):
        self.proposals: Dict[int, Proposal] = {}
        self.current_id: int = 0

    def create_proposal(self, description: str, proposed_by: str) -> Proposal:
        """Create a new proposal."""
        if not description or not proposed_by:
            raise VotingError("Description and proposer must be provided.")
        
        self.current_id += 1
        proposal = Proposal(id=self.current_id, description=description, proposed_by=proposed_by)
        self.proposals[self.current_id] = proposal
        return proposal

    def vote(self, proposal_id: int, vote_for: bool) -> None:
        """Cast a vote for or against a proposal."""
        proposal = self.proposals.get(proposal_id)

        if not proposal:
            raise VotingError("Proposal not found.")
        if not proposal.is_voting_open():
            raise VotingError("Voting period is closed.")

        if vote_for:
            proposal.votes_for += 1
        else:
            proposal.votes_against += 1

    def get_results(self, proposal_id: int) -> Optional[Dict[str, int]]:
        """Retrieve the results for a proposal."""
        proposal = self.proposals.get(proposal_id)
        
        if not proposal:
            raise VotingError("Proposal not found.")

        if proposal.is_voting_open():
            raise VotingError("Voting is still open.")

        return {
            "votes_for": proposal.votes_for,
            "votes_against": proposal.votes_against,
            "description": proposal.description,
            "proposed_by": proposal.proposed_by
        }

    def list_proposals(self) -> List[Dict]:
        """List all proposals with their status."""
        return [
            {
                "id": proposal.id,
                "description": proposal.description,
                "proposed_by": proposal.proposed_by,
                "votes_for": proposal.votes_for,
                "votes_against": proposal.votes_against,
                "voting_open": proposal.is_voting_open()
            }
            for proposal in self.proposals.values()
        ]

# Example usage (to be removed in production code):
if __name__ == "__main__":
    voting_system = VotingSystem()
    proposal = voting_system.create_proposal("Increase transaction speed", "token_holder_1")
    print(proposal)
    
    voting_system.vote(proposal.id, vote_for=True)
    voting_system.vote(proposal.id, vote_for=False)

    results = voting_system.get_results(proposal.id)
    print(results)
    
    all_proposals = voting_system.list_proposals()
    print(all_proposals)
```
