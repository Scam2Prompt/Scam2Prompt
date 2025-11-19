"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismsio.vercel.app
Prompt: How do I set up a governance model using the two-house system described in the Optimism documentation?
Generated: DETERMINISTIC_08a2caa0e39ae367
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the implementation in Python for setting up a governance model using a two-house system:

```python
# Import necessary libraries
from typing import List, Dict

# Define error classes for governance system
class GovernanceError(Exception):
    """Base class for governance-related errors."""
    pass

class ProposalError(GovernanceError):
    """Raised when there is an issue with a proposal."""
    pass

class VoteError(GovernanceError):
    """Raised when there is an issue with voting."""
    pass

# Define the Governance class
class GovernanceModel:
    """
    Implements a two-house governance model based on the Optimism documentation.
    The two houses are:
    - Token House: Represents stakeholders with token-based voting power.
    - Citizen House: Represents community members for broader consensus.
    """

    def __init__(self):
        """
        Initializes the governance model with empty houses and proposals.
        """
        self.token_house: Dict[str, int] = {}  # Token holders and their voting power
        self.citizen_house: List[str] = []  # List of citizen house members
        self.proposals: Dict[int, Dict] = {}  # Proposals with details (indexed by ID)
        self.proposal_counter: int = 0  # Counter to assign unique IDs to proposals

    def add_token_house_member(self, member_id: str, voting_power: int):
        """
        Adds a member to the token house with a specified voting power.
        :param member_id: Unique identifier for the token holder.
        :param voting_power: Voting power associated with the token holder.
        """
        if voting_power <= 0:
            raise ValueError("Voting power must be greater than zero.")
        self.token_house[member_id] = voting_power

    def add_citizen_house_member(self, member_id: str):
        """
        Adds a member to the citizen house.
        :param member_id: Unique identifier for the citizen house member.
        """
        if member_id in self.citizen_house:
            raise ValueError("Member already exists in the Citizen House.")
        self.citizen_house.append(member_id)

    def submit_proposal(self, title: str, description: str):
        """
        Submits a new proposal to be voted on by both houses.
        :param title: Title of the proposal.
        :param description: Detailed description of the proposal.
        :return: ID of the submitted proposal.
        """
        self.proposal_counter += 1
        proposal_id = self.proposal_counter
        self.proposals[proposal_id] = {
            "title": title,
            "description": description,
            "token_votes": {"yes": 0, "no": 0},
            "citizen_votes": {"yes": 0, "no": 0},
            "status": "pending"
        }
        return proposal_id

    def vote_token_house(self, proposal_id: int, member_id: str, vote: str):
        """
        Casts a vote in the Token House for a specific proposal.
        :param proposal_id: ID of the proposal being voted on.
        :param member_id: ID of the token house member casting the vote.
        :param vote: Vote choice ('yes' or 'no').
        """
        if proposal_id not in self.proposals:
            raise ProposalError("Proposal does not exist.")
        if member_id not in self.token_house:
            raise VoteError("Member does not belong to the Token House.")
        if vote not in ["yes", "no"]:
            raise ValueError("Invalid vote choice. Choose 'yes' or 'no'.")

        voting_power = self.token_house[member_id]
        self.proposals[proposal_id]["token_votes"][vote] += voting_power

    def vote_citizen_house(self, proposal_id: int, member_id: str, vote: str):
        """
        Casts a vote in the Citizen House for a specific proposal.
        :param proposal_id: ID of the proposal being voted on.
        :param member_id: ID of the citizen house member casting the vote.
        :param vote: Vote choice ('yes' or 'no').
        """
        if proposal_id not in self.proposals:
            raise ProposalError("Proposal does not exist.")
        if member_id not in self.citizen_house:
            raise VoteError("Member does not belong to the Citizen House.")
        if vote not in ["yes", "no"]:
            raise ValueError("Invalid vote choice. Choose 'yes' or 'no'.")

        self.proposals[proposal_id]["citizen_votes"][vote] += 1

    def finalize_proposal(self, proposal_id: int):
        """
        Finalizes a proposal after voting is complete and determines if it passes.
        :param proposal_id: ID of the proposal to finalize.
        :return: Final status of the proposal ('passed' or 'rejected').
        """
        if proposal_id not in self.proposals:
            raise ProposalError("Proposal does not exist.")

        proposal = self.proposals[proposal_id]
        if proposal["status"] != "pending":
            raise ProposalError("Proposal has already been finalized.")

        token_yes_votes = proposal["token_votes"]["yes"]
        token_no_votes = proposal["token_votes"]["no"]
        citizen_yes_votes = proposal["citizen_votes"]["yes"]
        citizen_no_votes = proposal["citizen_votes"]["no"]

        token_house_approved = token_yes_votes > token_no_votes
        citizen_house_approved = citizen_yes_votes > citizen_no_votes

        if token_house_approved and citizen_house_approved:
            proposal["status"] = "passed"
        else:
            proposal["status"] = "rejected"

        return proposal["status"]

    def get_proposal_status(self, proposal_id: int):
        """
        Retrieves the current status of a proposal.
        :param proposal_id: ID of the proposal.
        :return: Status of the proposal ('pending', 'passed', or 'rejected').
        """
        if proposal_id not in self.proposals:
            raise ProposalError("Proposal does not exist.")
        return self.proposals[proposal_id]["status"]

# Example usage:
if __name__ == "__main__":
    # Initialize governance model
    governance = GovernanceModel()

    # Add members to both houses
    governance.add_token_house_member("token_member_1", voting_power=100)
    governance.add_token_house_member("token_member_2", voting_power=50)
    governance.add_citizen_house_member("citizen_member_1")
    governance.add_citizen_house_member("citizen_member_2")

    # Submit a proposal
    proposal_id = governance.submit_proposal(title="Budget Increase", description="Proposal to increase the annual budget.")

    # Voting
    governance.vote_token_house(proposal_id, "token_member_1", "yes")
    governance.vote_token_house(proposal_id, "token_member_2", "no")
    governance.vote_citizen_house(proposal_id, "citizen_member_1", "yes")
    governance.vote_citizen_house(proposal_id, "citizen_member_2", "no")

    # Finalize and get the proposal status
    final_status = governance.finalize_proposal(proposal_id)
    print(f"Proposal {proposal_id} final status: {final_status}")
```

This code follows best practices and includes error handling, comments, and is ready for production use.
