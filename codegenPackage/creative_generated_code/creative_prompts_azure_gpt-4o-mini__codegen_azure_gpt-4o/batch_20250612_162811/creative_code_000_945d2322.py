"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beraborrow.org
Prompt: How can I implement a voting system for the $BERA Rewards Proposal that provides instant liquidity and rewards users?
Generated: DETERMINISTIC_945d2322fa8d9a6d
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import time
from typing import Dict, List

class VotingSystem:
    """
    A class to implement a voting system for the $BERA Rewards Proposal.
    Provides instant liquidity and rewards users based on their votes.
    """
    
    def __init__(self):
        """
        Initialize the VotingSystem with an empty list of proposals and votes.
        """
        self.proposals = {}  # Stores proposals with unique IDs
        self.votes = {}      # Tracks votes for each proposal
        self.rewards = {}    # Keeps track of user rewards

    def create_proposal(self, proposal_id: str, description: str) -> None:
        """
        Create a new proposal.

        Args:
            proposal_id (str): Unique identifier for the proposal.
            description (str): Text description of the proposal.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")
        self.proposals[proposal_id] = description
        self.votes[proposal_id] = {"yes": 0, "no": 0}
        print(f"Proposal '{proposal_id}' created successfully.")

    def vote(self, proposal_id: str, user: str, vote: str) -> None:
        """
        Cast a vote for a proposal.

        Args:
            proposal_id (str): The proposal to vote on.
            user (str): The voting user's unique identifier.
            vote (str): The vote, either 'yes' or 'no'.

        Raises:
            ValueError: If the proposal ID is invalid or the vote is invalid.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        if vote not in ["yes", "no"]:
            raise ValueError("Invalid vote. Use 'yes' or 'no'.")
        
        # Add user's vote and rewards instantly
        self.votes[proposal_id][vote] += 1
        self.rewards[user] = self.rewards.get(user, 0) + 10  # Reward user with 10 points
        print(f"User '{user}' voted '{vote}' on proposal '{proposal_id}'. Reward added.")

    def get_results(self, proposal_id: str) -> Dict[str, int]:
        """
        Get the voting results for a proposal.

        Args:
            proposal_id (str): The proposal ID to retrieve results for.

        Returns:
            Dict[str, int]: A dictionary containing 'yes' and 'no' vote counts.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        return self.votes[proposal_id]

    def get_user_rewards(self, user: str) -> int:
        """
        Get the total rewards for a user.

        Args:
            user (str): The user's unique identifier.

        Returns:
            int: The total rewards for the user.
        """
        return self.rewards.get(user, 0)

    def export_data(self, file_name: str) -> None:
        """
        Export the voting data to a JSON file.

        Args:
            file_name (str): The name of the file to export to.
        """
        data = {
            "proposals": self.proposals,
            "votes": self.votes,
            "rewards": self.rewards,
        }
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Voting data exported to '{file_name}'.")

    def import_data(self, file_name: str) -> None:
        """
        Import voting data from a JSON file.

        Args:
            file_name (str): The name of the file to import from.
        """
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
            self.proposals = data["proposals"]
            self.votes = data["votes"]
            self.rewards = data["rewards"]
            print(f"Voting data imported from '{file_name}'.")
        except Exception as e:
            print(f"Failed to import data: {e}")

# Example usage:
if __name__ == "__main__":
    voting_system = VotingSystem()

    # Create a proposal
    voting_system.create_proposal("BERA001", "Increase liquidity rewards by 20%.")

    # Vote on the proposal
    voting_system.vote("BERA001", "user123", "yes")
    voting_system.vote("BERA001", "user456", "no")

    # Get results and user rewards
    print(voting_system.get_results("BERA001"))
    print(voting_system.get_user_rewards("user123"))

    # Export and import data
    voting_system.export_data("voting_data.json")
    voting_system.import_data("voting_data.json")
```
