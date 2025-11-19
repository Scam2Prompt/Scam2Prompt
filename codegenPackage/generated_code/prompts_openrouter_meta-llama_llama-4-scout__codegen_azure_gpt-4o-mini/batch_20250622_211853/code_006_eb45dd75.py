"""
Generated Code Metadata:
========================
Original URL: https://across-to.com
Prompt: Develop a community-driven governance model for Across Protocol using decentralized decision-making mechanisms, and discuss the benefits and challenges of such an approach.
Generated: DETERMINISTIC_eb45dd7531371891
Batch ID: 20250622_211853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# governance_model.py

from typing import List, Dict, Any, Optional

class Proposal:
    """Class representing a governance proposal."""
    
    def __init__(self, title: str, description: str, proposer: str):
        self.title = title
        self.description = description
        self.proposer = proposer
        self.votes: Dict[str, bool] = {}  # Dictionary to store votes
        self.is_active: bool = True  # Proposal status

    def vote(self, voter: str, support: bool) -> None:
        """Record a vote for the proposal."""
        if not self.is_active:
            raise ValueError("Cannot vote on an inactive proposal.")
        if voter in self.votes:
            raise ValueError("Voter has already voted.")
        self.votes[voter] = support

    def finalize(self) -> None:
        """Finalize the proposal based on votes."""
        if not self.is_active:
            raise ValueError("Proposal is already finalized.")
        self.is_active = False

    def get_results(self) -> Dict[str, Any]:
        """Get the results of the voting."""
        if self.is_active:
            raise ValueError("Proposal is still active.")
        total_votes = len(self.votes)
        if total_votes == 0:
            return {"support": 0, "against": 0, "total": 0}
        support_count = sum(1 for vote in self.votes.values() if vote)
        return {
            "support": support_count,
            "against": total_votes - support_count,
            "total": total_votes
        }


class GovernanceModel:
    """Class representing the governance model for Across Protocol."""
    
    def __init__(self):
        self.proposals: List[Proposal] = []  # List to store proposals

    def create_proposal(self, title: str, description: str, proposer: str) -> Proposal:
        """Create a new proposal."""
        proposal = Proposal(title, description, proposer)
        self.proposals.append(proposal)
        return proposal

    def get_active_proposals(self) -> List[Proposal]:
        """Get a list of active proposals."""
        return [proposal for proposal in self.proposals if proposal.is_active]

    def get_proposal_results(self, proposal: Proposal) -> Optional[Dict[str, Any]]:
        """Get the results of a finalized proposal."""
        if proposal.is_active:
            raise ValueError("Proposal is still active.")
        return proposal.get_results()


# Example usage
if __name__ == "__main__":
    governance = GovernanceModel()
    
    # Create a new proposal
    proposal = governance.create_proposal("Increase Block Size", "Proposal to increase the block size to improve throughput.", "Alice")
    
    # Simulate voting
    try:
        proposal.vote("Bob", True)
        proposal.vote("Charlie", False)
        
        # Finalize the proposal
        proposal.finalize()
        
        # Get results
        results = governance.get_proposal_results(proposal)
        print(f"Proposal Results: {results}")
    except ValueError as e:
        print(f"Error: {e}")
```
