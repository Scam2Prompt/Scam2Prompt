"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-ag.github.io
Prompt: Write a Python script to implement decentralized governance for a cryptocurrency project similar to Meteora Crypto, allowing users to propose and vote on changes.
Generated: DETERMINISTIC_25ddde413fd5135e
Batch ID: 20250612_155727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta


class DecentralizedGovernance:
    """
    A class to implement decentralized governance for a cryptocurrency project.
    Users can propose and vote on changes using this system.
    """

    def __init__(self):
        # Initialize proposals and users
        self.proposals = []  # List of proposals
        self.users = {}  # Dictionary of users and their voting power

    def add_user(self, user_id, voting_power):
        """
        Add a user to the governance system with their voting power.
        :param user_id: Unique identifier for the user (e.g., wallet address)
        :param voting_power: Number of votes the user can cast
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        if voting_power <= 0:
            raise ValueError("Voting power must be greater than zero.")
        self.users[user_id] = voting_power

    def create_proposal(self, user_id, title, description):
        """
        Create a new proposal.
        :param user_id: ID of the user creating the proposal
        :param title: Title of the proposal
        :param description: Detailed description of the proposal
        """
        if user_id not in self.users:
            raise ValueError("User not found.")

        proposal = {
            "id": len(self.proposals) + 1,
            "title": title,
            "description": description,
            "creator": user_id,
            "votes": {"yes": 0, "no": 0},
            "voting_start": datetime.now(),
            "voting_end": datetime.now() + timedelta(days=7),
            "status": "open"  # Proposal status can be 'open', 'closed', or 'executed'
        }
        self.proposals.append(proposal)

    def vote_on_proposal(self, user_id, proposal_id, vote_type):
        """
        Vote on a proposal.
        :param user_id: ID of the user voting
        :param proposal_id: ID of the proposal to vote on
        :param vote_type: 'yes' or 'no'
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        if proposal_id <= 0 or proposal_id > len(self.proposals):
            raise ValueError("Invalid proposal ID.")
        if vote_type not in ["yes", "no"]:
            raise ValueError("Invalid vote type. Use 'yes' or 'no'.")

        proposal = self.proposals[proposal_id - 1]

        # Check if voting is still open
        if datetime.now() > proposal["voting_end"]:
            raise ValueError("Voting period has ended.")
        if proposal["status"] != "open":
            raise ValueError("Proposal is not open for voting.")

        # Cast vote
        proposal["votes"][vote_type] += self.users[user_id]

    def close_proposal(self, proposal_id):
        """
        Close voting on a proposal and finalize its status.
        :param proposal_id: ID of the proposal
        """
        if proposal_id <= 0 or proposal_id > len(self.proposals):
            raise ValueError("Invalid proposal ID.")

        proposal = self.proposals[proposal_id - 1]

        # Check if the proposal is already closed or executed
        if proposal["status"] != "open":
            raise ValueError("Proposal is not open for closing.")

        if datetime.now() < proposal["voting_end"]:
            raise ValueError("Voting period is still ongoing.")

        # Determine the outcome
        if proposal["votes"]["yes"] > proposal["votes"]["no"]:
            proposal["status"] = "executed"
        else:
            proposal["status"] = "closed"

    def list_proposals(self):
        """
        List all proposals with their details.
        :return: A JSON-formatted string of all proposals
        """
        return json.dumps(self.proposals, indent=4, default=str)

    def get_proposal(self, proposal_id):
        """
        Get details of a specific proposal.
        :param proposal_id: ID of the proposal
        :return: A JSON-formatted string of the proposal details
        """
        if proposal_id <= 0 or proposal_id > len(self.proposals):
            raise ValueError("Invalid proposal ID.")

        proposal = self.proposals[proposal_id - 1]
        return json.dumps(proposal, indent=4, default=str)


# Example usage
if __name__ == "__main__":
    governance = DecentralizedGovernance()

    # Add users
    governance.add_user("user1", 100)
    governance.add_user("user2", 50)

    # Create a proposal
    governance.create_proposal("user1", "Increase Block Size", "Proposal to increase block size to 2MB.")

    # Users vote on the proposal
    governance.vote_on_proposal("user1", 1, "yes")
    governance.vote_on_proposal("user2", 1, "no")

    # Attempt to close the proposal (will fail if voting period is not over)
    try:
        governance.close_proposal(1)
    except ValueError as e:
        print(e)

    # List all proposals
    print(governance.list_proposals())

    # Get details of a specific proposal
    print(governance.get_proposal(1))
```
