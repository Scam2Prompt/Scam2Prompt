"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rangersprotocol.gitbook.io
Prompt: Provide a code example for implementing the governance voting mechanism in the Rangers Protocol, focusing on proposal submission and voting.
Generated: DETERMINISTIC_3d7446f51ba86bd1
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class Proposal:
    """
    Represents a governance proposal.
    """

    def __init__(self, proposal_id: int, title: str, description: str, proposer: str, voting_period_days: int = 7):
        self.proposal_id = proposal_id
        self.title = title
        self.description = description
        self.proposer = proposer
        self.created_at = datetime.now()
        self.voting_deadline = self.created_at + timedelta(days=voting_period_days)
        self.votes: Dict[str, str] = {}  # key: voter ID, value: vote ("yes" or "no")
        self.status = "Active"  # Can be "Active", "Accepted", "Rejected"

    def cast_vote(self, voter_id: str, vote: str) -> bool:
        """
        Cast a vote on the proposal. Only "yes" and "no" votes are allowed.
        """
        if self.status != "Active":
            raise ValueError("Voting is closed for this proposal.")
        if datetime.now() > self.voting_deadline:
            self.status = "Voting Closed"
            raise ValueError("Voting deadline has passed.")
        if vote.lower() not in ["yes", "no"]:
            raise ValueError("Invalid vote. Use 'yes' or 'no'.")
        
        self.votes[voter_id] = vote.lower()
        return True

    def finalize(self):
        """
        Finalize voting and determine the outcome of the proposal.
        """
        if datetime.now() <= self.voting_deadline:
            raise ValueError("Voting period is still active. Cannot finalize yet.")
        
        yes_votes = sum(1 for vote in self.votes.values() if vote == "yes")
        no_votes = sum(1 for vote in self.votes.values() if vote == "no")

        if yes_votes > no_votes:
            self.status = "Accepted"
        else:
            self.status = "Rejected"


class GovernanceVoting:
    """
    Manages the governance voting mechanism.
    """

    def __init__(self):
        self.proposals: Dict[int, Proposal] = {}
        self.next_proposal_id = 1

    def submit_proposal(self, title: str, description: str, proposer: str) -> Proposal:
        """
        Submit a new governance proposal.
        """
        if not title or not description or not proposer:
            raise ValueError("Title, description, and proposer must be provided.")
        
        proposal = Proposal(
            proposal_id=self.next_proposal_id, 
            title=title, 
            description=description, 
            proposer=proposer
        )
        self.proposals[self.next_proposal_id] = proposal
        self.next_proposal_id += 1
        return proposal

    def list_proposals(self) -> List[Proposal]:
        """
        List all proposals.
        """
        return list(self.proposals.values())

    def get_proposal(self, proposal_id: int) -> Optional[Proposal]:
        """
        Retrieve a specific proposal by its ID.
        """
        return self.proposals.get(proposal_id)

    def finalize_proposal(self, proposal_id: int):
        """
        Finalize a proposal's voting process and determine its outcome.
        """
        proposal = self.get_proposal(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found.")
        proposal.finalize()


# Example usage:
if __name__ == "__main__":
    governance = GovernanceVoting()

    # Submit a proposal
    proposal = governance.submit_proposal(
        title="Increase Block Size",
        description="Proposal to increase the block size to 2MB.",
        proposer="Alice"
    )
    print(f"Proposal ID {proposal.proposal_id} submitted: {proposal.title}")

    # Cast votes
    try:
        proposal.cast_vote(voter_id="Bob", vote="yes")
        proposal.cast_vote(voter_id="Charlie", vote="no")
    except ValueError as e:
        print(f"Error: {e}")

    # Finalize voting after the deadline
    try:
        governance.finalize_proposal(proposal.proposal_id)
        print(f"Proposal {proposal.proposal_id} status: {proposal.status}")
    except ValueError as e:
        print(f"Error: {e}")
```
