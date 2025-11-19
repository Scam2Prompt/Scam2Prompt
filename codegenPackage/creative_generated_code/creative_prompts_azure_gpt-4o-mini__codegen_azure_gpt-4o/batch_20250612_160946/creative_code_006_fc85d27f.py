"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-inqubeta.pages.dev
Prompt: How can token holders participate in governance decisions on the InQubeta platform using $QUBE?
Generated: DETERMINISTIC_fc85d27f7592a054
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, List

# Define a class for InQubeta Governance
class InQubetaGovernance:
    """
    A class to represent the governance system of the InQubeta platform.
    Token holders can use $QUBE tokens to vote on proposals.
    """

    def __init__(self):
        # Initialize an empty list for proposals
        self.proposals: Dict[int, Dict] = {}
        self.votes: Dict[int, Dict[str, int]] = {}
        self.proposal_count = 0  # Unique ID for proposals

    def create_proposal(self, title: str, description: str) -> int:
        """
        Create a new governance proposal.

        Args:
            title (str): Title of the proposal.
            description (str): Description of the proposal.

        Returns:
            int: Proposal ID of the newly created proposal.
        """
        # Increment proposal count to create a unique ID
        self.proposal_count += 1
        
        # Store proposal details
        self.proposals[self.proposal_count] = {
            "title": title,
            "description": description,
            "votes_for": 0,
            "votes_against": 0,
            "status": "Open"
        }
        self.votes[self.proposal_count] = {}
        
        return self.proposal_count

    def vote_on_proposal(self, proposal_id: int, voter_address: str, vote: str, token_balance: int) -> str:
        """
        Allow token holders to vote on a proposal.

        Args:
            proposal_id (int): ID of the proposal to vote on.
            voter_address (str): Address of the voter.
            vote (str): Choice of the vote ("for" or "against").
            token_balance (int): The balance of $QUBE tokens the voter holds.

        Returns:
            str: Result of the voting process.
        """
        # Validate proposal ID
        if proposal_id not in self.proposals:
            return "Proposal ID not found."

        # Validate vote choice
        if vote not in ["for", "against"]:
            return "Invalid vote choice. Use 'for' or 'against'."

        # Check if voter has already voted on the proposal
        if voter_address in self.votes[proposal_id]:
            return "Voter has already cast their vote on this proposal."

        # Ensure the proposal is still open for voting
        if self.proposals[proposal_id]["status"] != "Open":
            return "Voting on this proposal is closed."

        # Register the vote
        self.votes[proposal_id][voter_address] = token_balance
        if vote == "for":
            self.proposals[proposal_id]["votes_for"] += token_balance
        elif vote == "against":
            self.proposals[proposal_id]["votes_against"] += token_balance
        
        return "Vote successfully registered."

    def close_voting(self, proposal_id: int) -> str:
        """
        Close the voting for a proposal and finalize the decision.

        Args:
            proposal_id (int): ID of the proposal to close voting for.

        Returns:
            str: Result of the proposal.
        """
        # Validate proposal ID
        if proposal_id not in self.proposals:
            return "Proposal ID not found."

        # Ensure the proposal is open
        if self.proposals[proposal_id]["status"] != "Open":
            return "Voting on this proposal has already been closed."

        # Finalize the voting and close the proposal
        self.proposals[proposal_id]["status"] = "Closed"
        votes_for = self.proposals[proposal_id]["votes_for"]
        votes_against = self.proposals[proposal_id]["votes_against"]

        if votes_for > votes_against:
            self.proposals[proposal_id]["result"] = "Accepted"
            return f"Proposal {proposal_id} has been accepted."
        else:
            self.proposals[proposal_id]["result"] = "Rejected"
            return f"Proposal {proposal_id} has been rejected."

# Example usage
if __name__ == "__main__":
    # Initialize the governance system
    governance = InQubetaGovernance()

    # Create a new proposal
    proposal_id = governance.create_proposal(
        title="Increase Staking Rewards",
        description="Proposal to increase staking rewards for $QUBE token holders."
    )
    print(f"Proposal {proposal_id} created.")

    # Token holders vote on the proposal
    print(governance.vote_on_proposal(proposal_id, "0x123", "for", 100))
    print(governance.vote_on_proposal(proposal_id, "0x456", "against", 50))

    # Close the voting and finalize the proposal
    print(governance.close_voting(proposal_id))
```
