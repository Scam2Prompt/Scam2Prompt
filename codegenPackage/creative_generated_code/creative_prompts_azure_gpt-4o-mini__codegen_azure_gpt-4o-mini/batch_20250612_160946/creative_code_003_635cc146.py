"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koalamemecoin.pages.dev
Prompt: Describe how to create a decentralized governance model for a cryptocurrency community like KoalaKash.
Generated: DETERMINISTIC_635cc146d8346006
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict, Any
import json

class Proposal:
    """
    Class representing a governance proposal in the decentralized model.
    """

    def __init__(self, title: str, description: str, proposer: str):
        """
        Initialize a new proposal.

        :param title: Title of the proposal
        :param description: Description of the proposal
        :param proposer: The proposer of the proposal
        """
        self.title = title
        self.description = description
        self.proposer = proposer
        self.votes = {'for': 0, 'against': 0}
        self.status = 'pending'  # possible statuses: pending, approved, rejected

    def vote(self, vote: str):
        """
        Cast a vote on the proposal.

        :param vote: 'for' or 'against'
        """
        if vote not in self.votes:
            raise ValueError("Vote must be either 'for' or 'against'")
        self.votes[vote] += 1

    def finalize(self):
        """
        Finalize the proposal and update the status based on the votes.
        """
        if self.votes['for'] > self.votes['against']:
            self.status = 'approved'
        else:
            self.status = 'rejected'


class GovernanceModel:
    """
    Class representing the decentralized governance model for the cryptocurrency community.
    """

    def __init__(self):
        """
        Initialize the governance model with storage for proposals.
        """
        self.proposals: List[Proposal] = []

    def create_proposal(self, title: str, description: str, proposer: str) -> Proposal:
        """
        Create a new governance proposal.

        :param title: Title of the proposal
        :param description: Description of the proposal
        :param proposer: The proposer of the proposal
        :return: The created Proposal object
        """
        new_proposal = Proposal(title, description, proposer)
        self.proposals.append(new_proposal)
        return new_proposal

    def vote_on_proposal(self, proposal_index: int, vote: str):
        """
        Vote on a specific proposal by index.

        :param proposal_index: The index of the proposal in the proposals list
        :param vote: 'for' or 'against'
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index out of range.")
        self.proposals[proposal_index].vote(vote)

    def finalize_proposal(self, proposal_index: int):
        """
        Finalize a specific proposal by index.

        :param proposal_index: The index of the proposal to finalize
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index out of range.")
        self.proposals[proposal_index].finalize()

    def export_proposals(self) -> str:
        """
        Export the proposals to a JSON string.

        :return: JSON string representation of proposals
        """
        try:
            return json.dumps([{
                'title': p.title,
                'description': p.description,
                'proposer': p.proposer,
                'votes': p.votes,
                'status': p.status
            } for p in self.proposals])
        except Exception as e:
            raise RuntimeError(f"Failed to export proposals: {str(e)}")


# Example usage:
if __name__ == "__main__":
    governance = GovernanceModel()

    # Create a proposal
    proposal = governance.create_proposal("Increase Block Size", "Increase the block size to improve transaction throughput.", "Alice")

    # Vote on the proposal
    governance.vote_on_proposal(0, 'for')
    governance.vote_on_proposal(0, 'against')
    
    # Finalize the proposal
    governance.finalize_proposal(0)

    # Export all proposals
    proposals_json = governance.export_proposals()
    print(proposals_json)  # Output the proposals in JSON format
```
