"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibpiht7izgwflj7ruju4tcwrl7b45xmoifhhch7hi47n5ip5du4c4.ipfs.dweb.link
Prompt: Illustrate how to implement a community voting system for a cryptocurrency project, taking cues from the SharkCat community ownership model.
Generated: DETERMINISTIC_d28eb38d48f1e1df
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

# Define a class for the Community Voting System
class CommunityVotingSystem:
    def __init__(self):
        """Initialize the voting system with an empty list of proposals and votes."""
        self.proposals = {}
        self.votes = {}

    def create_proposal(self, proposal_id, description, deadline):
        """
        Create a new proposal.
        
        :param proposal_id: Unique identifier for the proposal
        :param description: Text describing the proposal
        :param deadline: Deadline for voting (ISO format string, e.g., "2023-12-31T23:59:59")
        :raises ValueError: If the proposal_id already exists or the deadline is invalid
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")
        
        try:
            deadline_dt = datetime.fromisoformat(deadline)
        except ValueError:
            raise ValueError("Invalid deadline format. Use ISO format (YYYY-MM-DDTHH:MM:SS).")
        
        if deadline_dt <= datetime.now():
            raise ValueError("Deadline must be in the future.")

        self.proposals[proposal_id] = {
            "description": description,
            "deadline": deadline,
            "votes": {"yes": 0, "no": 0},
        }
        self.votes[proposal_id] = set()  # Track users who have voted

    def cast_vote(self, proposal_id, user_id, vote):
        """
        Cast a vote on a proposal.
        
        :param proposal_id: Identifier of the proposal to vote on
        :param user_id: Unique identifier of the voter
        :param vote: Either "yes" or "no"
        :raises ValueError: If the proposal doesn't exist, the vote is invalid, or the user has already voted
        :raises RuntimeError: If the voting deadline has passed
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        
        if vote not in ("yes", "no"):
            raise ValueError("Invalid vote option. Use 'yes' or 'no'.")
        
        if user_id in self.votes[proposal_id]:
            raise ValueError("User has already voted on this proposal.")
        
        deadline_dt = datetime.fromisoformat(self.proposals[proposal_id]["deadline"])
        if datetime.now() > deadline_dt:
            raise RuntimeError("Voting deadline has passed for this proposal.")
        
        self.proposals[proposal_id]["votes"][vote] += 1
        self.votes[proposal_id].add(user_id)

    def get_results(self, proposal_id):
        """
        Get the results of a proposal's voting.
        
        :param proposal_id: Identifier of the proposal
        :return: Dictionary containing the vote counts
        :raises ValueError: If the proposal doesn't exist
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        
        return self.proposals[proposal_id]["votes"]

    def save_to_file(self, filename):
        """
        Save the proposals and votes to a JSON file.
        
        :param filename: Name of the file to save the data
        :raises IOError: If there is a problem writing to the file
        """
        try:
            data = {
                "proposals": self.proposals,
                "votes": {k: list(v) for k, v in self.votes.items()},  # Serialize sets as lists
            }
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save data to file: {e}")

    def load_from_file(self, filename):
        """
        Load proposals and votes from a JSON file.
        
        :param filename: Name of the file to load the data from
        :raises IOError: If there is a problem reading the file
        :raises ValueError: If the file contains invalid data
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            
            self.proposals = data["proposals"]
            self.votes = {k: set(v) for k, v in data["votes"].items()}  # Deserialize lists as sets
        except IOError as e:
            raise IOError(f"Failed to load data from file: {e}")
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid data in file: {e}")


# Example usage (uncomment to test locally):
# voting_system = CommunityVotingSystem()
# voting_system.create_proposal("proposal1", "Increase staking rewards.", "2023-12-31T23:59:59")
# voting_system.cast_vote("proposal1", "user123", "yes")
# voting_system.cast_vote("proposal1", "user456", "no")
# print(voting_system.get_results("proposal1"))
# voting_system.save_to_file("voting_data.json")
# voting_system.load_from_file("voting_data.json")
```
