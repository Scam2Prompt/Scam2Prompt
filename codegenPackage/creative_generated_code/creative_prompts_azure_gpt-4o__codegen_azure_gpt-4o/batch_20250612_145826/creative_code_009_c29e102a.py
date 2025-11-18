"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogg.pages.dev
Prompt: Write code to implement a community voting system for a cryptocurrency project, allowing members to make decisions collectively, as described in Popo's community-backed project model.
Generated: DETERMINISTIC_c29e102acdb73c0b
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# community_voting_system.py

import json
from datetime import datetime, timedelta

class VotingSystem:
    """
    A class for implementing a community voting system for a cryptocurrency project.
    """

    def __init__(self):
        """
        Initializes the voting system with an empty proposal list and results dictionary.
        """
        self.proposals = {}  # Stores proposals with their details
        self.votes = {}  # Stores votes cast by community members
        self.results = {}  # Stores final voting results

    def create_proposal(self, proposal_id, description, voting_duration_days):
        """
        Creates a new proposal.

        Args:
            proposal_id (str): Unique ID for the proposal.
            description (str): Description of the proposal.
            voting_duration_days (int): Duration in days for voting on the proposal.

        Returns:
            str: Confirmation message.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")
        
        end_date = datetime.now() + timedelta(days=voting_duration_days)
        self.proposals[proposal_id] = {
            "description": description,
            "end_date": end_date,
            "votes": {"yes": 0, "no": 0}
        }
        return f"Proposal '{proposal_id}' created successfully."

    def cast_vote(self, proposal_id, voter_id, vote):
        """
        Casts a vote for a given proposal.

        Args:
            proposal_id (str): ID of the proposal to vote on.
            voter_id (str): ID of the community member voting.
            vote (str): The vote ('yes' or 'no').

        Returns:
            str: Confirmation message.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        
        if datetime.now() > self.proposals[proposal_id]["end_date"]:
            raise ValueError("Voting period for this proposal has ended.")
        
        if voter_id in self.votes.get(proposal_id, {}):
            raise ValueError("Voter has already cast a vote for this proposal.")
        
        # Validate vote input
        if vote.lower() not in ["yes", "no"]:
            raise ValueError("Invalid vote. Use 'yes' or 'no'.")
        
        # Record the vote
        self.proposals[proposal_id]["votes"][vote.lower()] += 1
        self.votes.setdefault(proposal_id, {})[voter_id] = vote.lower()
        return f"Vote cast successfully for proposal '{proposal_id}' by voter '{voter_id}'."

    def get_results(self, proposal_id):
        """
        Retrieves the results of a proposal.

        Args:
            proposal_id (str): ID of the proposal to retrieve results for.

        Returns:
            dict: Results of the proposal.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        
        if datetime.now() <= self.proposals[proposal_id]["end_date"]:
            raise ValueError("Voting is still ongoing for this proposal.")
        
        # Retrieve results
        votes = self.proposals[proposal_id]["votes"]
        result = {
            "proposal_id": proposal_id,
            "description": self.proposals[proposal_id]["description"],
            "votes_yes": votes["yes"],
            "votes_no": votes["no"],
            "result": "Approved" if votes["yes"] > votes["no"] else "Rejected"
        }
        self.results[proposal_id] = result
        return result

    def save_data(self, file_path):
        """
        Saves the current state of proposals and results to a JSON file.

        Args:
            file_path (str): Path to the file to save data.

        Returns:
            str: Confirmation message.
        """
        data = {
            "proposals": self.proposals,
            "results": self.results
        }
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, default=str, indent=4)
            return "Data saved successfully."
        except Exception as e:
            raise IOError(f"Error saving data: {e}")

    def load_data(self, file_path):
        """
        Loads proposals and results from a JSON file.

        Args:
            file_path (str): Path to the file to load data.

        Returns:
            str: Confirmation message.
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.proposals = data.get("proposals", {})
                self.results = data.get("results", {})
            return "Data loaded successfully."
        except Exception as e:
            raise IOError(f"Error loading data: {e}")


# Example usage:
if __name__ == "__main__":
    voting_system = VotingSystem()
    
    # Create a proposal
    print(voting_system.create_proposal("Proposal1", "Increase staking rewards", 7))
    
    # Cast votes
    print(voting_system.cast_vote("Proposal1", "User1", "yes"))
    print(voting_system.cast_vote("Proposal1", "User2", "no"))
    
    # Wait for voting to end and get results
    try:
        print(voting_system.get_results("Proposal1"))
    except ValueError as e:
        print(e)  # Voting is still ongoing
    
    # Save data to file
    print(voting_system.save_data("voting_data.json"))
    
    # Load data from file
    print(voting_system.load_data("voting_data.json"))
```
