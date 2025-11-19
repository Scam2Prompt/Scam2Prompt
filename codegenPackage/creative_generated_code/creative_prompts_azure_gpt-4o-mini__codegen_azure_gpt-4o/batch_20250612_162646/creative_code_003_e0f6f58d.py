"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: What unique features does the Demo-DAO offer for proposal management in the MetaDAO ecosystem?
Generated: DETERMINISTIC_e0f6f58dc46f21a7
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a production-ready implementation of a `DemoDAO` class in Python that can be integrated into a MetaDAO ecosystem, showcasing unique features for proposal management:

```python
import uuid
from datetime import datetime


class ProposalStatus:
    """Enum-like class to manage proposal statuses."""
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    CANCELLED = "Cancelled"


class Proposal:
    """Represents a proposal in the DemoDAO."""
    
    def __init__(self, title: str, description: str, creator: str):
        """
        Initializes a new proposal.

        :param title: The title of the proposal.
        :param description: The detailed description of the proposal.
        :param creator: The user ID of the proposal creator.
        """
        self.proposal_id = str(uuid.uuid4())  # Unique identifier for each proposal
        self.title = title
        self.description = description
        self.creator = creator
        self.created_at = datetime.now()
        self.status = ProposalStatus.PENDING
        self.votes = {"yes": 0, "no": 0, "abstain": 0}  # Voting tallies

    def __str__(self):
        return f"Proposal({self.proposal_id}, {self.title}, {self.status})"


class DemoDAO:
    """Manages proposals and voting within the MetaDAO ecosystem."""

    def __init__(self):
        """
        Initializes the DemoDAO with an empty proposal list.
        """
        self.proposals = {}  # Dictionary to store proposals by their ID

    def create_proposal(self, title: str, description: str, creator: str) -> str:
        """
        Creates a new proposal and adds it to the DAO.

        :param title: The title of the proposal.
        :param description: The detailed description of the proposal.
        :param creator: The user ID of the proposal creator.
        :return: The unique ID of the created proposal.
        """
        proposal = Proposal(title, description, creator)
        self.proposals[proposal.proposal_id] = proposal
        return proposal.proposal_id

    def get_proposal(self, proposal_id: str) -> Proposal:
        """
        Retrieves a proposal by its ID.

        :param proposal_id: The unique ID of the proposal.
        :return: The Proposal object.
        :raises KeyError: If the proposal ID doesn't exist.
        """
        if proposal_id not in self.proposals:
            raise KeyError(f"Proposal with ID '{proposal_id}' not found.")
        return self.proposals[proposal_id]

    def vote_on_proposal(self, proposal_id: str, vote_type: str) -> None:
        """
        Casts a vote on a proposal.

        :param proposal_id: The unique ID of the proposal.
        :param vote_type: Type of vote ('yes', 'no', or 'abstain').
        :raises KeyError: If the proposal ID doesn't exist.
        :raises ValueError: If the vote type is invalid.
        """
        if proposal_id not in self.proposals:
            raise KeyError(f"Proposal with ID '{proposal_id}' not found.")
        if vote_type not in ["yes", "no", "abstain"]:
            raise ValueError("Vote type must be 'yes', 'no', or 'abstain'.")

        self.proposals[proposal_id].votes[vote_type] += 1

    def finalize_proposal(self, proposal_id: str) -> str:
        """
        Finalizes the voting process and updates the proposal status.

        :param proposal_id: The unique ID of the proposal.
        :return: The updated status of the proposal.
        :raises KeyError: If the proposal ID doesn't exist.
        """
        proposal = self.get_proposal(proposal_id)
        if proposal.status != ProposalStatus.PENDING:
            raise ValueError("Proposal has already been finalized or cancelled.")
        
        # Calculate results
        if proposal.votes["yes"] > proposal.votes["no"]:
            proposal.status = ProposalStatus.APPROVED
        else:
            proposal.status = ProposalStatus.REJECTED
        
        return proposal.status

    def cancel_proposal(self, proposal_id: str) -> None:
        """
        Cancels a proposal, making it inactive.

        :param proposal_id: The unique ID of the proposal.
        :raises KeyError: If the proposal ID doesn't exist.
        """
        proposal = self.get_proposal(proposal_id)
        proposal.status = ProposalStatus.CANCELLED

    def list_proposals(self, status_filter: str = None) -> list:
        """
        Lists all proposals, optionally filtered by status.

        :param status_filter: Filter proposals by status (optional).
        :return: A list of Proposal objects.
        """
        if status_filter:
            return [p for p in self.proposals.values() if p.status == status_filter]
        return list(self.proposals.values())


# Example usage:
if __name__ == "__main__":
    dao = DemoDAO()

    # Create a proposal
    proposal_id = dao.create_proposal(
        title="Implement Staking Rewards",
        description="Proposal to introduce staking rewards for MetaDAO participants.",
        creator="user123"
    )
    print(f"Created Proposal ID: {proposal_id}")

    # Cast votes
    dao.vote_on_proposal(proposal_id, "yes")
    dao.vote_on_proposal(proposal_id, "yes")
    dao.vote_on_proposal(proposal_id, "no")

    # Finalize proposal
    status = dao.finalize_proposal(proposal_id)
    print(f"Proposal status: {status}")

    # List all proposals
    proposals = dao.list_proposals()
    for proposal in proposals:
        print(proposal)
```

This code snippet provides a clean, efficient, and production-ready implementation for managing proposals in the MetaDAO ecosystem. It includes features like proposal creation, voting, status management, and filtering, along with error handling and proper documentation.
