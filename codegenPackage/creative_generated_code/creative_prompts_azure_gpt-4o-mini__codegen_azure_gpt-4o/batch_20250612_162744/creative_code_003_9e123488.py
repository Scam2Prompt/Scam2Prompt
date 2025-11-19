"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmkjdwoihjif.com
Prompt: Describe how to implement a governance voting system for veKITTEN token holders to influence rewards distribution on KittenSwap.
Generated: DETERMINISTIC_9e123488f6b20398
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# governance_voting_system.py

import json
from datetime import datetime, timedelta

class GovernanceVotingSystem:
    """
    A governance voting system for veKITTEN token holders to vote on rewards distribution on KittenSwap.
    """

    def __init__(self):
        """
        Initialize the voting system with empty proposals and votes.
        """
        self.proposals = {}  # Stores all proposals
        self.votes = {}  # Maps proposal IDs to votes
        self.ve_kitten_balances = {}  # Stores veKITTEN token balances for users
        self.voting_period_days = 7  # Default voting period for proposals

    def add_ve_kitten_balance(self, user, balance):
        """
        Adds or updates veKITTEN balance for a user.
        
        Args:
            user (str): User's identifier.
            balance (float): Amount of veKITTEN tokens.
        """
        self.ve_kitten_balances[user] = balance

    def create_proposal(self, proposal_id, description, creator):
        """
        Creates a new governance proposal.
        
        Args:
            proposal_id (str): Unique ID for the proposal.
            description (str): Description of the proposal.
            creator (str): Creator of the proposal.
            
        Raises:
            ValueError: If proposal ID already exists.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")
        
        self.proposals[proposal_id] = {
            "description": description,
            "creator": creator,
            "start_time": datetime.now(),
            "end_time": datetime.now() + timedelta(days=self.voting_period_days),
            "status": "open",
            "votes": {"yes": 0, "no": 0}
        }
        self.votes[proposal_id] = {}
        print(f"Proposal '{proposal_id}' created successfully.")

    def cast_vote(self, proposal_id, user, vote):
        """
        Allows a veKITTEN token holder to cast their vote on a proposal.
        
        Args:
            proposal_id (str): ID of the proposal to vote on.
            user (str): User's identifier.
            vote (str): "yes" or "no".
        
        Raises:
            ValueError: If proposal ID does not exist, if voting is closed, 
                        if user has insufficient balance, or if vote is invalid.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        
        proposal = self.proposals[proposal_id]
        if datetime.now() > proposal["end_time"]:
            raise ValueError("Voting period for this proposal has ended.")
        
        if user not in self.ve_kitten_balances or self.ve_kitten_balances[user] <= 0:
            raise ValueError("User has insufficient veKITTEN balance to vote.")
        
        if vote.lower() not in ["yes", "no"]:
            raise ValueError("Invalid vote. Must be 'yes' or 'no'.")
        
        # Prevent double voting
        if user in self.votes[proposal_id]:
            raise ValueError("User has already voted on this proposal.")
        
        # Record the vote
        self.votes[proposal_id][user] = vote.lower()
        proposal["votes"][vote.lower()] += self.ve_kitten_balances[user]
        print(f"User '{user}' voted '{vote}' on proposal '{proposal_id}' successfully.")

    def close_proposal(self, proposal_id):
        """
        Closes a proposal manually (if necessary).
        
        Args:
            proposal_id (str): ID of the proposal to close.
        
        Raises:
            ValueError: If proposal ID does not exist or is already closed.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        
        proposal = self.proposals[proposal_id]
        if proposal["status"] == "closed":
            raise ValueError("Proposal is already closed.")
        
        proposal["status"] = "closed"
        print(f"Proposal '{proposal_id}' closed successfully.")

    def get_results(self, proposal_id):
        """
        Retrieves the results of a proposal.
        
        Args:
            proposal_id (str): ID of the proposal.
        
        Returns:
            dict: Results of the proposal.
        
        Raises:
            ValueError: If proposal ID does not exist or voting is still ongoing.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        
        proposal = self.proposals[proposal_id]
        if proposal["status"] == "open" and datetime.now() <= proposal["end_time"]:
            raise ValueError("Voting is still ongoing for this proposal.")
        
        results = {
            "yes_votes": proposal["votes"]["yes"],
            "no_votes": proposal["votes"]["no"],
            "status": proposal["status"]
        }
        return results

    def save_data(self, filename):
        """
        Saves the current state of proposals and votes to a JSON file.
        
        Args:
            filename (str): Name of the file to save the data.
        """
        data = {
            "proposals": self.proposals,
            "votes": self.votes
        }
        with open(filename, 'w') as file:
            json.dump(data, file, default=str)
        print(f"Data saved to '{filename}' successfully.")

    def load_data(self, filename):
        """
        Loads proposals and votes data from a JSON file.
        
        Args:
            filename (str): Name of the file to load the data from.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
        self.proposals = data["proposals"]
        self.votes = data["votes"]
        print(f"Data loaded from '{filename}' successfully.")


# Example usage of the GovernanceVotingSystem
if __name__ == "__main__":
    system = GovernanceVotingSystem()

    # Add veKITTEN balances
    system.add_ve_kitten_balance("alice", 1000)
    system.add_ve_kitten_balance("bob", 500)

    # Create a proposal
    system.create_proposal("proposal_1", "Increase staking rewards by 20%", "alice")

    # Cast votes
    system.cast_vote("proposal_1", "alice", "yes")
    system.cast_vote("proposal_1", "bob", "no")

    # End the voting period manually (optional)
    system.close_proposal("proposal_1")

    # Get results
    results = system.get_results("proposal_1")
    print("Proposal Results:", results)

    # Save and load data
    system.save_data("voting_data.json")
    system.load_data("voting_data.json")
```
