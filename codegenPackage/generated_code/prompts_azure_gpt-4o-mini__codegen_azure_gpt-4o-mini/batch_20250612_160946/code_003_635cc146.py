"""
Generated Code Metadata:
========================
Original URL: https://koalamemecoin.pages.dev
Prompt: Describe how to create a decentralized governance model for a cryptocurrency community like KoalaKash.
Generated: DETERMINISTIC_635cc146d8346006
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Any
import json

class GovernanceModel:
    """
    A class to represent a decentralized governance model for a cryptocurrency community.
    """

    def __init__(self):
        """
        Initializes the governance model with an empty list of proposals and members.
        """
        self.proposals: List[Dict[str, Any]] = []
        self.members: List[str] = []

    def add_member(self, member_id: str) -> None:
        """
        Adds a new member to the governance model.

        :param member_id: Unique identifier for the member
        """
        if member_id not in self.members:
            self.members.append(member_id)
        else:
            raise ValueError("Member already exists.")

    def create_proposal(self, title: str, description: str, proposer: str) -> None:
        """
        Creates a new proposal in the governance model.

        :param title: Title of the proposal
        :param description: Description of the proposal
        :param proposer: Member ID of the proposer
        """
        if proposer not in self.members:
            raise ValueError("Proposer is not a member of the community.")

        proposal = {
            "title": title,
            "description": description,
            "proposer": proposer,
            "votes": {"yes": 0, "no": 0},
            "status": "pending"
        }
        self.proposals.append(proposal)

    def vote(self, proposal_index: int, member_id: str, vote: str) -> None:
        """
        Allows a member to vote on a proposal.

        :param proposal_index: Index of the proposal in the proposals list
        :param member_id: Unique identifier for the member voting
        :param vote: Vote choice ('yes' or 'no')
        """
        if member_id not in self.members:
            raise ValueError("Member is not a part of the community.")
        
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index out of range.")

        if vote not in ['yes', 'no']:
            raise ValueError("Vote must be 'yes' or 'no'.")

        proposal = self.proposals[proposal_index]
        if proposal["status"] != "pending":
            raise ValueError("Voting is closed for this proposal.")

        proposal["votes"][vote] += 1

    def finalize_proposal(self, proposal_index: int) -> None:
        """
        Finalizes a proposal based on the votes.

        :param proposal_index: Index of the proposal to finalize
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index out of range.")

        proposal = self.proposals[proposal_index]
        if proposal["status"] != "pending":
            raise ValueError("Proposal has already been finalized.")

        # Simple majority rule
        total_votes = proposal["votes"]["yes"] + proposal["votes"]["no"]
        if total_votes == 0:
            raise ValueError("No votes have been cast.")

        if proposal["votes"]["yes"] > proposal["votes"]["no"]:
            proposal["status"] = "approved"
        else:
            proposal["status"] = "rejected"

    def get_proposals(self) -> List[Dict[str, Any]]:
        """
        Returns the list of proposals.

        :return: List of proposals
        """
        return self.proposals

    def to_json(self) -> str:
        """
        Serializes the governance model to a JSON string.

        :return: JSON representation of the governance model
        """
        return json.dumps({
            "members": self.members,
            "proposals": self.proposals
        }, indent=4)

# Example usage
if __name__ == "__main__":
    governance = GovernanceModel()
    governance.add_member("member1")
    governance.create_proposal("Increase Block Size", "Proposal to increase the block size to improve transaction throughput.", "member1")
    governance.vote(0, "member1", "yes")
    governance.finalize_proposal(0)
    print(governance.to_json())
```
