"""
Generated Code Metadata:
========================
Original URL: https://agora-next-jlesgw0mi-voteagora.vercel.app
Prompt: "How does Optimism Agora facilitate on-chain governance for RetroPGF projects, and what are the key features of its voting system?"
Generated: DETERMINISTIC_edd88f5555e65439
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Optimism Agora Voting System Simulation

This script demonstrates how Optimism Agora facilitates on-chain governance for RetroPGF projects.
It includes a voting system with key features such as weighted voting, proposal creation, and result calculation.

Note: This is a simplified simulation and does not interact with an actual blockchain.
"""

from typing import List, Dict, Union
import json

class Proposal:
    """
    Represents a proposal in the governance system.
    """
    def __init__(self, proposal_id: int, title: str, description: str):
        self.proposal_id = proposal_id
        self.title = title
        self.description = description
        self.votes = {}  # Stores votes as {voter_address: weight}

    def add_vote(self, voter_address: str, weight: int):
        """
        Adds a vote to the proposal.
        :param voter_address: Address of the voter.
        :param weight: Voting weight of the voter.
        """
        if weight <= 0:
            raise ValueError("Voting weight must be positive.")
        self.votes[voter_address] = weight

    def calculate_results(self) -> int:
        """
        Calculates the total voting weight for the proposal.
        :return: Total weight of votes.
        """
        return sum(self.votes.values())

    def to_dict(self) -> Dict[str, Union[int, str, Dict[str, int]]]:
        """
        Converts the proposal to a dictionary for serialization.
        :return: Dictionary representation of the proposal.
        """
        return {
            "proposal_id": self.proposal_id,
            "title": self.title,
            "description": self.description,
            "votes": self.votes
        }


class GovernanceSystem:
    """
    Represents the governance system for RetroPGF projects.
    """
    def __init__(self):
        self.proposals = {}  # Stores proposals as {proposal_id: Proposal}
        self.next_proposal_id = 1

    def create_proposal(self, title: str, description: str) -> Proposal:
        """
        Creates a new proposal.
        :param title: Title of the proposal.
        :param description: Description of the proposal.
        :return: The created Proposal object.
        """
        proposal = Proposal(self.next_proposal_id, title, description)
        self.proposals[self.next_proposal_id] = proposal
        self.next_proposal_id += 1
        return proposal

    def vote_on_proposal(self, proposal_id: int, voter_address: str, weight: int):
        """
        Casts a vote on a proposal.
        :param proposal_id: ID of the proposal to vote on.
        :param voter_address: Address of the voter.
        :param weight: Voting weight of the voter.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        proposal = self.proposals[proposal_id]
        proposal.add_vote(voter_address, weight)

    def get_proposal_results(self, proposal_id: int) -> int:
        """
        Retrieves the voting results for a proposal.
        :param proposal_id: ID of the proposal.
        :return: Total voting weight for the proposal.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        proposal = self.proposals[proposal_id]
        return proposal.calculate_results()

    def serialize_proposals(self) -> str:
        """
        Serializes all proposals to a JSON string.
        :return: JSON string of all proposals.
        """
        return json.dumps([proposal.to_dict() for proposal in self.proposals.values()], indent=4)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the governance system
        governance = GovernanceSystem()

        # Create proposals
        proposal1 = governance.create_proposal("Fund Open Source Project", "Allocate funds to support open source development.")
        proposal2 = governance.create_proposal("Community Education Program", "Invest in community education initiatives.")

        # Cast votes
        governance.vote_on_proposal(proposal1.proposal_id, "0x123", 100)
        governance.vote_on_proposal(proposal1.proposal_id, "0x456", 200)
        governance.vote_on_proposal(proposal2.proposal_id, "0x789", 150)

        # Get results
        print(f"Results for Proposal 1: {governance.get_proposal_results(proposal1.proposal_id)}")
        print(f"Results for Proposal 2: {governance.get_proposal_results(proposal2.proposal_id)}")

        # Serialize proposals
        print("Serialized Proposals:")
        print(governance.serialize_proposals())

    except Exception as e:
        print(f"Error: {e}")
```
