"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfinanciallabs.com
Prompt: Illustrate how to integrate community-driven governance features into a financial application using the principles outlined by the People's World Liberty Financial DAO.
Generated: DETERMINISTIC_e3f2eb3703555075
Batch ID: 20250612_162711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Community-Driven Governance Module for Financial Application

This module demonstrates the integration of community-driven governance features
into a financial application using DAO (Decentralized Autonomous Organization) principles.
The example leverages blockchain-based voting for proposal management.
"""

import json
import hashlib


class DAO:
    """
    A class that represents a simplified DAO for financial governance.
    """

    def __init__(self):
        self.proposals = {}  # Stores proposals with unique IDs
        self.votes = {}      # Stores votes per proposal
        self.members = set()  # Members of the DAO

    def add_member(self, member_id):
        """
        Adds a new member to the DAO.
        
        :param member_id: Unique identifier for the member (e.g., wallet address)
        :return: None
        """
        if member_id in self.members:
            raise ValueError("Member already exists.")
        self.members.add(member_id)

    def create_proposal(self, creator, title, description):
        """
        Creates a new proposal for community voting.
        
        :param creator: ID of the creator (must be a DAO member)
        :param title: Title of the proposal
        :param description: Detailed description of the proposal
        :return: Proposal ID
        """
        if creator not in self.members:
            raise PermissionError("Only DAO members can create proposals.")

        proposal_id = hashlib.sha256(f"{creator}-{title}".encode()).hexdigest()
        self.proposals[proposal_id] = {
            "title": title,
            "description": description,
            "creator": creator,
            "votes": {"yes": 0, "no": 0},
            "status": "active"  # Proposal can be active, approved, or rejected
        }
        self.votes[proposal_id] = set()  # Keeps track of members who voted
        return proposal_id

    def vote_on_proposal(self, member_id, proposal_id, vote_choice):
        """
        Allows a DAO member to vote on a proposal.
        
        :param member_id: ID of the voting member (must be a DAO member)
        :param proposal_id: ID of the proposal to vote on
        :param vote_choice: 'yes' or 'no'
        :return: None
        """
        if member_id not in self.members:
            raise PermissionError("Only DAO members can vote.")
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        if vote_choice not in ["yes", "no"]:
            raise ValueError("Invalid vote choice. Choose 'yes' or 'no'.")
        if member_id in self.votes[proposal_id]:
            raise PermissionError("Member has already voted on this proposal.")
        if self.proposals[proposal_id]["status"] != "active":
            raise ValueError("Proposal is no longer active.")

        self.proposals[proposal_id]["votes"][vote_choice] += 1
        self.votes[proposal_id].add(member_id)

    def finalize_proposal(self, proposal_id):
        """
        Finalizes voting on a proposal and determines the outcome.
        
        :param proposal_id: ID of the proposal to finalize
        :return: None
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        if self.proposals[proposal_id]["status"] != "active":
            raise ValueError("Proposal is already finalized.")

        votes = self.proposals[proposal_id]["votes"]
        if votes["yes"] > votes["no"]:
            self.proposals[proposal_id]["status"] = "approved"
        else:
            self.proposals[proposal_id]["status"] = "rejected"

    def view_proposals(self):
        """
        Returns all proposals with details.
        
        :return: Dictionary of proposals
        """
        return self.proposals

    def view_members(self):
        """
        Returns all DAO members.
        
        :return: Set of members
        """
        return self.members


# Example usage
if __name__ == "__main__":
    # Initialize the DAO
    dao = DAO()

    # Add DAO members
    try:
        dao.add_member("member1")
        dao.add_member("member2")
    except ValueError as e:
        print(f"Error adding member: {e}")

    # Create a proposal
    try:
        proposal_id = dao.create_proposal(
            creator="member1",
            title="Reduce transaction fees",
            description="Proposal to reduce transaction fees by 10% for all users."
        )
        print(f"Proposal created with ID: {proposal_id}")
    except Exception as e:
        print(f"Error creating proposal: {e}")

    # Vote on the proposal
    try:
        dao.vote_on_proposal(member_id="member1", proposal_id=proposal_id, vote_choice="yes")
        dao.vote_on_proposal(member_id="member2", proposal_id=proposal_id, vote_choice="no")
    except Exception as e:
        print(f"Error voting on proposal: {e}")

    # Finalize the proposal
    try:
        dao.finalize_proposal(proposal_id)
    except Exception as e:
        print(f"Error finalizing proposal: {e}")

    # View proposals
    print("Proposals:")
    print(json.dumps(dao.view_proposals(), indent=4))

    # View members
    print("Members:")
    print(dao.view_members())
```
