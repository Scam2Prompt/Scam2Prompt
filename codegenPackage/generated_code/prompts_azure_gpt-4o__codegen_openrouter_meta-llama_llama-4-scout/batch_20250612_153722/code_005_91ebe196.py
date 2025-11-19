"""
Generated Code Metadata:
========================
Original URL: https://pengwu.io
Prompt: Create a voting mechanism for token holders to influence community decisions, leveraging PENGWU tokens as described in the Voting feature.
Generated: DETERMINISTIC_91ebe196da3a22dd
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# voting_mechanism.py

from typing import Dict, List
from datetime import datetime, timedelta

class VotingMechanism:
    def __init__(self):
        """
        Initialize the voting mechanism.

        Attributes:
        - proposals (Dict): Mapping of proposal IDs to their respective details.
        - votes (Dict): Mapping of proposal IDs to their respective votes.
        """
        self.proposals = {}
        self.votes = {}

    def create_proposal(self, proposal_id: str, description: str, options: List[str]):
        """
        Create a new proposal.

        Args:
        - proposal_id (str): Unique identifier for the proposal.
        - description (str): Brief description of the proposal.
        - options (List[str]): List of options for the proposal.

        Raises:
        - ValueError: If the proposal ID already exists.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists")

        self.proposals[proposal_id] = {
            "description": description,
            "options": options,
            "start_time": datetime.now(),
            "end_time": datetime.now() + timedelta(days=7),  # 7-day voting period
            "votes": {option: 0 for option in options}
        }
        self.votes[proposal_id] = {}

    def cast_vote(self, proposal_id: str, user: str, option: str):
        """
        Cast a vote for a proposal.

        Args:
        - proposal_id (str): Unique identifier for the proposal.
        - user (str): User casting the vote (PENGWU token holder).
        - option (str): Chosen option for the proposal.

        Raises:
        - ValueError: If the proposal ID does not exist or the user has already voted.
        - KeyError: If the chosen option is not valid.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist")

        if user in self.votes[proposal_id]:
            raise ValueError("User has already voted")

        if option not in self.proposals[proposal_id]["options"]:
            raise KeyError("Invalid option")

        self.proposals[proposal_id]["votes"][option] += 1
        self.votes[proposal_id][user] = option

    def get_proposal_results(self, proposal_id: str) -> Dict:
        """
        Get the results of a proposal.

        Args:
        - proposal_id (str): Unique identifier for the proposal.

        Returns:
        - Dict: Dictionary containing the proposal's description, options, and vote counts.

        Raises:
        - ValueError: If the proposal ID does not exist.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist")

        return {
            "description": self.proposals[proposal_id]["description"],
            "options": self.proposals[proposal_id]["options"],
            "votes": self.proposals[proposal_id]["votes"]
        }

    def has_voted(self, proposal_id: str, user: str) -> bool:
        """
        Check if a user has voted on a proposal.

        Args:
        - proposal_id (str): Unique identifier for the proposal.
        - user (str): User to check.

        Returns:
        - bool: True if the user has voted, False otherwise.

        Raises:
        - ValueError: If the proposal ID does not exist.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist")

        return user in self.votes.get(proposal_id, {})

def main():
    voting_mechanism = VotingMechanism()

    # Create a proposal
    proposal_id = "pengwu-001"
    description = "Proposal to update PENGWU token contract"
    options = ["Yes", "No"]
    voting_mechanism.create_proposal(proposal_id, description, options)

    # Cast votes
    users = ["user1", "user2", "user3"]
    for user in users:
        voting_mechanism.cast_vote(proposal_id, user, "Yes")

    # Get proposal results
    results = voting_mechanism.get_proposal_results(proposal_id)
    print(results)

    # Check if a user has voted
    has_voted = voting_mechanism.has_voted(proposal_id, "user1")
    print(f"Has user1 voted? {has_voted}")

if __name__ == "__main__":
    main()
```
