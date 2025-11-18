"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-morpho.github.io
Prompt: Create a governance voting system for token holders, allowing users to vote on proposals and fee structures, inspired by Morpho's governance mechanism.
Generated: DETERMINISTIC_c221042cd0c50898
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready governance voting system for token holders:

```python
import json
from datetime import datetime, timedelta


class GovernanceVotingSystem:
    def __init__(self):
        # Initialize the governance system with empty proposals and votes
        self.proposals = {}  # Stores proposals: {proposal_id: {"title": str, "description": str, "deadline": datetime, "votes": {address: vote}}}
        self.token_holders = {}  # Stores token holders: {address: token_balance}

    def add_token_holder(self, address, token_balance):
        """
        Adds a new token holder to the system.
        :param address: Unique identifier (address) for the token holder.
        :param token_balance: Balance of governance tokens held by the user.
        """
        if address in self.token_holders:
            raise ValueError("Token holder already exists.")
        self.token_holders[address] = token_balance

    def create_proposal(self, title, description, duration_days):
        """
        Creates a new proposal for voting.
        :param title: Title of the proposal.
        :param description: Description of the proposal.
        :param duration_days: Number of days the proposal will be open for voting.
        :return: Unique proposal ID.
        """
        proposal_id = len(self.proposals) + 1
        self.proposals[proposal_id] = {
            "title": title,
            "description": description,
            "deadline": datetime.now() + timedelta(days=duration_days),
            "votes": {}  # Votes will be stored as {address: vote}
        }
        return proposal_id

    def cast_vote(self, proposal_id, address, vote):
        """
        Casts a vote on a proposal.
        :param proposal_id: ID of the proposal to vote on.
        :param address: Address of the token holder casting the vote.
        :param vote: Vote cast by the user ('yes', 'no', or 'abstain').
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        if address not in self.token_holders:
            raise ValueError("Invalid token holder address.")
        if vote not in ['yes', 'no', 'abstain']:
            raise ValueError("Invalid vote. Allowed values: 'yes', 'no', 'abstain'.")
        proposal = self.proposals[proposal_id]
        if datetime.now() > proposal["deadline"]:
            raise ValueError("Voting period has ended for this proposal.")
        proposal["votes"][address] = vote

    def tally_votes(self, proposal_id):
        """
        Tallies the votes for a proposal.
        :param proposal_id: ID of the proposal.
        :return: Dictionary with vote totals.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        proposal = self.proposals[proposal_id]
        if datetime.now() <= proposal["deadline"]:
            raise ValueError("Voting period is still ongoing.")

        # Tally votes taking token balances into account
        vote_totals = {"yes": 0, "no": 0, "abstain": 0}
        for address, vote in proposal["votes"].items():
            token_balance = self.token_holders[address]
            vote_totals[vote] += token_balance
        return vote_totals

    def get_proposals(self):
        """
        Retrieves all proposals and their details.
        :return: List of all proposals.
        """
        return self.proposals

    def save_to_file(self, filename):
        """
        Saves the current state of the governance system to a file.
        :param filename: Name of the file to save the data to.
        """
        data = {
            "proposals": self.proposals,
            "token_holders": self.token_holders
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        """
        Loads the governance system state from a file.
        :param filename: Name of the file to load the data from.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            self.proposals = data["proposals"]
            self.token_holders = data["token_holders"]


# Example usage:
if __name__ == "__main__":
    system = GovernanceVotingSystem()
    system.add_token_holder("holder1", 100)
    system.add_token_holder("holder2", 200)
    proposal_id = system.create_proposal("Proposal 1", "Increase fees by 1%", 7)
    system.cast_vote(proposal_id, "holder1", "yes")
    system.cast_vote(proposal_id, "holder2", "no")
    print(system.tally_votes(proposal_id))
    system.save_to_file("governance_data.json")
```

This code provides a complete governance voting system for token holders, including proposal creation, voting, and vote tallying. Proper error handling is implemented, and the system state can be saved to/loaded from a file.
