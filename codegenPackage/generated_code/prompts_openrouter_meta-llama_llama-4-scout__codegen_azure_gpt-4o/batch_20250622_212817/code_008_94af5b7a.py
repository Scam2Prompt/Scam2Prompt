"""
Generated Code Metadata:
========================
Original URL: https://polkadot.org
Prompt: How does Polkadot's decentralized autonomous organization (DAO) function, and what are its implications for community governance?
Generated: DETERMINISTIC_94af5b7aed1652a8
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a Python script that simulates a simplified version of Polkadot's DAO functionality, focusing on community governance. This code is designed to demonstrate how proposals can be created, voted on, and executed within a DAO framework.

```python
import json
from typing import List, Dict, Union

class DAO:
    """
    A class representing a Decentralized Autonomous Organization (DAO).
    This implementation simulates proposal creation, voting, and execution.
    """

    def __init__(self):
        """
        Initializes the DAO with an empty list of proposals and members.
        """
        self.proposals = []  # List to store proposals
        self.members = {}    # Dictionary to store members and their voting power

    def add_member(self, member_id: str, voting_power: int):
        """
        Adds a new member to the DAO with a specified voting power.

        :param member_id: Unique identifier for the member (e.g., wallet address).
        :param voting_power: The voting power assigned to the member.
        """
        if member_id in self.members:
            raise ValueError("Member already exists.")
        self.members[member_id] = voting_power

    def create_proposal(self, title: str, description: str) -> int:
        """
        Creates a new proposal and adds it to the list of proposals.

        :param title: Title of the proposal.
        :param description: Detailed description of the proposal.
        :return: The ID of the newly created proposal.
        """
        proposal_id = len(self.proposals) + 1
        proposal = {
            "id": proposal_id,
            "title": title,
            "description": description,
            "votes": {},  # Dictionary to store votes (member_id -> vote)
            "status": "Pending"  # Status can be "Pending", "Approved", or "Rejected"
        }
        self.proposals.append(proposal)
        return proposal_id

    def vote_on_proposal(self, member_id: str, proposal_id: int, vote: str):
        """
        Allows a member to vote on a proposal.

        :param member_id: Unique identifier for the member.
        :param proposal_id: ID of the proposal to vote on.
        :param vote: The vote ("Yes" or "No").
        """
        if member_id not in self.members:
            raise ValueError("Member not found.")
        if proposal_id < 1 or proposal_id > len(self.proposals):
            raise ValueError("Invalid proposal ID.")
        if vote not in ["Yes", "No"]:
            raise ValueError("Invalid vote. Use 'Yes' or 'No'.")

        proposal = self.proposals[proposal_id - 1]
        if member_id in proposal["votes"]:
            raise ValueError("Member has already voted on this proposal.")

        # Record the vote
        proposal["votes"][member_id] = {"vote": vote, "voting_power": self.members[member_id]}

    def tally_votes(self, proposal_id: int):
        """
        Tallies the votes for a proposal and updates its status.

        :param proposal_id: ID of the proposal to tally votes for.
        """
        if proposal_id < 1 or proposal_id > len(self.proposals):
            raise ValueError("Invalid proposal ID.")

        proposal = self.proposals[proposal_id - 1]
        if proposal["status"] != "Pending":
            raise ValueError("Proposal has already been finalized.")

        yes_votes = sum(v["voting_power"] for v in proposal["votes"].values() if v["vote"] == "Yes")
        no_votes = sum(v["voting_power"] for v in proposal["votes"].values() if v["vote"] == "No")

        # Update proposal status based on vote tally
        if yes_votes > no_votes:
            proposal["status"] = "Approved"
        else:
            proposal["status"] = "Rejected"

    def get_proposals(self) -> List[Dict[str, Union[int, str, Dict]]]:
        """
        Returns the list of all proposals.

        :return: List of proposals.
        """
        return self.proposals

    def save_to_file(self, filename: str):
        """
        Saves the DAO state (members and proposals) to a JSON file.

        :param filename: Name of the file to save the data to.
        """
        dao_state = {
            "members": self.members,
            "proposals": self.proposals
        }
        with open(filename, "w") as file:
            json.dump(dao_state, file, indent=4)

    def load_from_file(self, filename: str):
        """
        Loads the DAO state (members and proposals) from a JSON file.

        :param filename: Name of the file to load the data from.
        """
        with open(filename, "r") as file:
            dao_state = json.load(file)
            self.members = dao_state["members"]
            self.proposals = dao_state["proposals"]


# Example usage
if __name__ == "__main__":
    dao = DAO()

    # Add members
    dao.add_member("member1", 10)
    dao.add_member("member2", 20)

    # Create a proposal
    proposal_id = dao.create_proposal("Increase Treasury Budget", "Proposal to increase the treasury budget by 10%.")

    # Members vote on the proposal
    dao.vote_on_proposal("member1", proposal_id, "Yes")
    dao.vote_on_proposal("member2", proposal_id, "No")

    # Tally votes and finalize the proposal
    dao.tally_votes(proposal_id)

    # Print all proposals
    print(json.dumps(dao.get_proposals(), indent=4))

    # Save DAO state to a file
    dao.save_to_file("dao_state.json")

    # Load DAO state from a file
    dao.load_from_file("dao_state.json")
```

This code provides a basic framework for a DAO, including member management, proposal creation, voting, and vote tallying. It also includes functionality to save and load the DAO state to/from a file for persistence.
