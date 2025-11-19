"""
Generated Code Metadata:
========================
Original URL: https://pre-mpeppe-live.pages.dev
Prompt: Propose a community-driven governance model for the Mpeppe project, incorporating decentralized decision-making and token-based voting mechanisms.
Generated: DETERMINISTIC_e44bafec9bf30684
Batch ID: 20250622_210249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Community-Driven Governance Model for the Mpeppe Project

This script implements a decentralized decision-making model using token-based voting mechanisms.
Participants can propose changes, vote on proposals, and the system calculates the results based on token weight.
"""

from typing import Dict, List, Optional
import uuid

class Proposal:
    """
    Represents a proposal in the governance system.
    """
    def __init__(self, title: str, description: str, proposer: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the proposal
        self.title = title
        self.description = description
        self.proposer = proposer
        self.votes = {}  # Dictionary to store votes {voter_address: vote_weight}
        self.status = "Active"  # Status can be "Active", "Approved", or "Rejected"

    def add_vote(self, voter_address: str, vote_weight: int):
        """
        Adds a vote to the proposal.
        :param voter_address: Address of the voter
        :param vote_weight: Weight of the vote based on tokens held
        """
        if voter_address in self.votes:
            raise ValueError("Voter has already voted on this proposal.")
        self.votes[voter_address] = vote_weight

    def calculate_result(self, total_tokens: int) -> str:
        """
        Calculates the result of the proposal based on votes.
        :param total_tokens: Total number of tokens in circulation
        :return: Status of the proposal ("Approved" or "Rejected")
        """
        total_vote_weight = sum(self.votes.values())
        if total_vote_weight > total_tokens / 2:  # Majority rule
            self.status = "Approved"
        else:
            self.status = "Rejected"
        return self.status


class GovernanceSystem:
    """
    Represents the governance system for the Mpeppe project.
    """
    def __init__(self, total_tokens: int):
        self.total_tokens = total_tokens  # Total tokens in circulation
        self.proposals: Dict[str, Proposal] = {}  # Dictionary to store proposals {proposal_id: Proposal}

    def create_proposal(self, title: str, description: str, proposer: str) -> str:
        """
        Creates a new proposal.
        :param title: Title of the proposal
        :param description: Description of the proposal
        :param proposer: Address of the proposer
        :return: ID of the created proposal
        """
        proposal = Proposal(title, description, proposer)
        self.proposals[proposal.id] = proposal
        return proposal.id

    def vote_on_proposal(self, proposal_id: str, voter_address: str, vote_weight: int):
        """
        Casts a vote on a proposal.
        :param proposal_id: ID of the proposal
        :param voter_address: Address of the voter
        :param vote_weight: Weight of the vote based on tokens held
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found.")
        proposal = self.proposals[proposal_id]
        if proposal.status != "Active":
            raise ValueError("Proposal is no longer active.")
        proposal.add_vote(voter_address, vote_weight)

    def finalize_proposal(self, proposal_id: str) -> str:
        """
        Finalizes a proposal by calculating the result.
        :param proposal_id: ID of the proposal
        :return: Final status of the proposal ("Approved" or "Rejected")
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found.")
        proposal = self.proposals[proposal_id]
        if proposal.status != "Active":
            raise ValueError("Proposal is already finalized.")
        return proposal.calculate_result(self.total_tokens)

    def get_proposal(self, proposal_id: str) -> Optional[Proposal]:
        """
        Retrieves a proposal by ID.
        :param proposal_id: ID of the proposal
        :return: Proposal object or None if not found
        """
        return self.proposals.get(proposal_id)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize governance system with 1000 tokens in circulation
        governance = GovernanceSystem(total_tokens=1000)

        # Create a new proposal
        proposal_id = governance.create_proposal(
            title="Increase Staking Rewards",
            description="Proposal to increase staking rewards by 10%.",
            proposer="0xProposerAddress"
        )
        print(f"Proposal created with ID: {proposal_id}")

        # Cast votes
        governance.vote_on_proposal(proposal_id, voter_address="0xVoter1", vote_weight=300)
        governance.vote_on_proposal(proposal_id, voter_address="0xVoter2", vote_weight=400)

        # Finalize proposal
        final_status = governance.finalize_proposal(proposal_id)
        print(f"Proposal {proposal_id} has been {final_status}.")

        # Retrieve proposal details
        proposal = governance.get_proposal(proposal_id)
        if proposal:
            print(f"Proposal Details: {proposal.title}, Status: {proposal.status}, Votes: {proposal.votes}")

    except Exception as e:
        print(f"Error: {e}")
```
