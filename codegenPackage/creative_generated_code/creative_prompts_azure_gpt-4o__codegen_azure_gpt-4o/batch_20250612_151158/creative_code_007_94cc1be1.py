"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zivoe.pages.dev
Prompt: Create a program to automate the governance voting process on the Zivoe platform, allowing users to cast votes based on their staked ZVE tokens.
Generated: DETERMINISTIC_94cc1be17c18bd56
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict

class ZivoeGovernanceVotingSystem:
    def __init__(self):
        # Store votes and user stake information
        self.votes = {}  # Example: {'proposal_id': {'yes': 0, 'no': 0}}
        self.user_stakes = {}  # Example: {'user_id': amount_of_stake}
        self.proposals = {}  # Example: {'proposal_id': 'Proposal Description'}

    def add_proposal(self, proposal_id: str, description: str):
        """
        Add a new proposal to the system.
        :param proposal_id: Unique identifier for the proposal.
        :param description: Description of the proposal.
        """
        if proposal_id in self.proposals:
            raise ValueError(f"Proposal ID '{proposal_id}' already exists.")
        self.proposals[proposal_id] = description
        self.votes[proposal_id] = {"yes": 0, "no": 0}

    def cast_vote(self, user_id: str, proposal_id: str, vote: str):
        """
        Cast a vote on a proposal.
        :param user_id: ID of the user casting the vote.
        :param proposal_id: ID of the proposal being voted on.
        :param vote: Vote type ('yes' or 'no').
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal ID '{proposal_id}' does not exist.")
        if vote not in ['yes', 'no']:
            raise ValueError("Invalid vote type. Please vote 'yes' or 'no'.")
        if user_id not in self.user_stakes or self.user_stakes[user_id] <= 0:
            raise ValueError("User must have staked ZVE tokens to vote.")

        # Weight the vote based on the user's staked tokens
        vote_weight = self.user_stakes[user_id]
        self.votes[proposal_id][vote] += vote_weight
        print(f"User {user_id} successfully cast '{vote}' vote for proposal '{proposal_id}'.")

    def set_user_stake(self, user_id: str, stake: int):
        """
        Set or update the amount of ZVE tokens staked by a user.
        :param user_id: ID of the user.
        :param stake: Amount of ZVE tokens staked.
        """
        if stake < 0:
            raise ValueError("Stake amount cannot be negative.")
        self.user_stakes[user_id] = stake
        print(f"User {user_id} stake set to {stake} ZVE tokens.")

    def get_proposal_results(self, proposal_id: str) -> Dict[str, int]:
        """
        Retrieve the results for a specific proposal.
        :param proposal_id: ID of the proposal.
        :return: Dictionary containing vote counts for 'yes' and 'no'.
        """
        if proposal_id not in self.votes:
            raise ValueError(f"Proposal ID '{proposal_id}' does not exist.")
        return self.votes[proposal_id]

    def save_state_to_file(self, file_path: str):
        """
        Save the current state of the governance system to a file.
        :param file_path: Path to the file where the state will be saved.
        """
        state = {
            'proposals': self.proposals,
            'votes': self.votes,
            'user_stakes': self.user_stakes
        }
        try:
            with open(file_path, 'w') as file:
                json.dump(state, file, indent=4)
            print(f"State successfully saved to '{file_path}'.")
        except Exception as e:
            print(f"Error saving state to file: {e}")

    def load_state_from_file(self, file_path: str):
        """
        Load the governance system state from a file.
        :param file_path: Path to the file containing the saved state.
        """
        try:
            with open(file_path, 'r') as file:
                state = json.load(file)
            self.proposals = state['proposals']
            self.votes = state['votes']
            self.user_stakes = state['user_stakes']
            print(f"State successfully loaded from '{file_path}'.")
        except Exception as e:
            print(f"Error loading state from file: {e}")

# Example usage of the system:
if __name__ == "__main__":
    # Initialize the governance system
    governance_system = ZivoeGovernanceVotingSystem()

    # Add proposals
    governance_system.add_proposal("proposal_1", "Increase staking rewards by 5%")
    governance_system.add_proposal("proposal_2", "Reduce transaction fees by 10%")

    # Set user stakes
    governance_system.set_user_stake("user_123", 100)
    governance_system.set_user_stake("user_456", 200)

    # Cast votes
    governance_system.cast_vote("user_123", "proposal_1", "yes")
    governance_system.cast_vote("user_456", "proposal_1", "no")

    # Retrieve proposal results
    results = governance_system.get_proposal_results("proposal_1")
    print("Proposal 1 results:", results)

    # Save and load system state
    governance_system.save_state_to_file("governance_state.json")
    governance_system.load_state_from_file("governance_state.json")
```
