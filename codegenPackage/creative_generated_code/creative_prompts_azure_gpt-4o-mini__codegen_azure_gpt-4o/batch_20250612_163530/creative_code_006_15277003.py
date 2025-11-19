"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shib-army.pages.dev
Prompt: Describe the governance role of the BONE token in the Shiba ecosystem and how it allows community voting.
Generated: DETERMINISTIC_152770036bf52b59
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script describes the governance role of the BONE token in the Shiba ecosystem.
It explains how BONE allows community members to vote on proposals within the ecosystem.
The code simulates a decentralized governance system using Python.
"""

# Import necessary libraries
from typing import Dict, List


class BoneTokenGovernance:
    """
    A class to represent the governance system for the Shiba ecosystem using BONE tokens.
    """

    def __init__(self):
        """
        Initialize the governance system with no proposals and an empty voter registry.
        """
        self.proposals: Dict[int, Dict[str, any]] = {}  # Stores proposals
        self.votes: Dict[int, List[str]] = {}  # Tracks votes against proposal IDs
        self.voter_registry: Dict[str, int] = {}  # Tracks voter addresses and their BONE balance

    def register_voter(self, voter_address: str, bone_balance: int) -> None:
        """
        Registers a voter with their address and BONE token balance.

        :param voter_address: The address of the voter.
        :param bone_balance: The balance of BONE tokens for the voter.
        :raises ValueError: If the voter is already registered or balance is invalid.
        """
        if voter_address in self.voter_registry:
            raise ValueError("Voter is already registered.")
        if bone_balance <= 0:
            raise ValueError("BONE balance must be greater than zero.")

        self.voter_registry[voter_address] = bone_balance

    def create_proposal(self, proposal_id: int, description: str) -> None:
        """
        Allows community members to create a new governance proposal.

        :param proposal_id: The unique ID of the proposal.
        :param description: A short description of the proposal.
        :raises ValueError: If the proposal ID already exists.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")

        self.proposals[proposal_id] = {"description": description, "votes": {"yes": 0, "no": 0}}
        self.votes[proposal_id] = []

    def vote(self, voter_address: str, proposal_id: int, vote_choice: str) -> None:
        """
        Allows a registered voter to cast their vote on a proposal.

        :param voter_address: The address of the voter.
        :param proposal_id: The ID of the proposal to vote on.
        :param vote_choice: The voter's choice ('yes' or 'no').
        :raises ValueError: If the voter is not registered, proposal ID is invalid, or vote choice is invalid.
        """
        if voter_address not in self.voter_registry:
            raise ValueError("Voter is not registered.")
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        if vote_choice not in ["yes", "no"]:
            raise ValueError("Vote choice must be 'yes' or 'no'.")
        if voter_address in self.votes[proposal_id]:
            raise ValueError("Voter has already cast a vote for this proposal.")

        bone_balance = self.voter_registry[voter_address]
        self.proposals[proposal_id]["votes"][vote_choice] += bone_balance
        self.votes[proposal_id].append(voter_address)

    def get_proposal_result(self, proposal_id: int) -> Dict[str, any]:
        """
        Retrieves the voting results of a specific proposal.

        :param proposal_id: The ID of the proposal.
        :return: A dictionary containing the proposal description and vote counts.
        :raises ValueError: If the proposal ID is invalid.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")

        return {
            "description": self.proposals[proposal_id]["description"],
            "votes": self.proposals[proposal_id]["votes"],
        }

    def show_all_proposals(self) -> Dict[int, str]:
        """
        Returns a list of all proposals with their IDs and descriptions.

        :return: A dictionary with proposal IDs and descriptions.
        """
        return {pid: self.proposals[pid]["description"] for pid in self.proposals}


# Example usage
if __name__ == "__main__":
    # Initialize governance system
    governance = BoneTokenGovernance()

    # Register voters
    try:
        governance.register_voter("voter1", 100)
        governance.register_voter("voter2", 200)
    except ValueError as e:
        print(f"Error registering voter: {e}")

    # Create proposals
    try:
        governance.create_proposal(1, "Proposal to add new features to the Shiba ecosystem.")
        governance.create_proposal(2, "Proposal to implement staking rewards.")
    except ValueError as e:
        print(f"Error creating proposal: {e}")

    # Cast votes
    try:
        governance.vote("voter1", 1, "yes")
        governance.vote("voter2", 1, "no")
        governance.vote("voter1", 2, "yes")
    except ValueError as e:
        print(f"Error voting: {e}")

    # Retrieve proposal results
    try:
        result = governance.get_proposal_result(1)
        print(f"Proposal 1 results: {result}")
    except ValueError as e:
        print(f"Error retrieving proposal results: {e}")

    # Show all proposals
    print("All proposals:")
    print(governance.show_all_proposals())
```
