"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundkation.com
Prompt: Generate a governance voting system for a DAO that oversees tokenized financial products, inspired by Ondo DAO's governance structure.
Generated: DETERMINISTIC_8ad8adac77ff4ba6
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import Dict, List, Union

class DAOGovernance:
    """
    A governance voting system for a DAO that oversees tokenized financial products.
    """

    def __init__(self):
        """
        Initializes the DAO governance system.
        """
        self.proposals = {}  # Store proposals as a dictionary with proposal IDs as keys
        self.votes = {}  # Store votes with proposal IDs as keys
        self.token_holders = {}  # Store token holders with their voting power
        self.proposal_counter = 0  # Unique ID counter for proposals

    def register_token_holder(self, holder_address: str, voting_power: int):
        """
        Register or update a token holder and their voting power.

        :param holder_address: Unique identifier for the token holder
        :param voting_power: The voting power, typically based on tokens held
        """
        if voting_power <= 0:
            raise ValueError("Voting power must be greater than zero.")
        self.token_holders[holder_address] = voting_power

    def submit_proposal(self, title: str, description: str, duration_days: int) -> int:
        """
        Submit a new proposal for voting.

        :param title: Title of the proposal
        :param description: Detailed description of the proposal
        :param duration_days: Voting duration in days
        :return: Proposal ID of the newly submitted proposal
        """
        if duration_days <= 0:
            raise ValueError("Voting duration must be greater than zero.")

        self.proposal_counter += 1
        proposal_id = self.proposal_counter
        expiration_date = datetime.now() + timedelta(days=duration_days)

        self.proposals[proposal_id] = {
            "title": title,
            "description": description,
            "expiration_date": expiration_date,
            "votes_for": 0,
            "votes_against": 0
        }
        self.votes[proposal_id] = {}  # Initialize vote tracking for the proposal

        return proposal_id

    def cast_vote(self, proposal_id: int, voter_address: str, vote: Union["FOR", "AGAINST"]):
        """
        Cast a vote on a proposal.

        :param proposal_id: ID of the proposal being voted on
        :param voter_address: Unique identifier for the voter
        :param vote: "FOR" or "AGAINST" vote
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID not found.")

        if voter_address not in self.token_holders:
            raise ValueError("Voter is not a registered token holder.")

        if vote not in ["FOR", "AGAINST"]:
            raise ValueError("Vote must be either 'FOR' or 'AGAINST'.")

        proposal = self.proposals[proposal_id]

        # Check if the proposal is still active
        if datetime.now() > proposal["expiration_date"]:
            raise ValueError("Voting period for this proposal has expired.")

        # Prevent double voting
        if voter_address in self.votes[proposal_id]:
            raise ValueError("Voter has already cast a vote for this proposal.")

        # Cast the vote
        voting_power = self.token_holders[voter_address]
        if vote == "FOR":
            proposal["votes_for"] += voting_power
        else:  # vote == "AGAINST"
            proposal["votes_against"] += voting_power

        # Record the vote
        self.votes[proposal_id][voter_address] = vote

    def get_proposal_result(self, proposal_id: int) -> Dict[str, Union[str, int]]:
        """
        Get the result of a proposal.

        :param proposal_id: ID of the proposal
        :return: Dictionary containing the result of the proposal
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID not found.")

        proposal = self.proposals[proposal_id]

        result = "ONGOING"
        if datetime.now() > proposal["expiration_date"]:
            result = "APPROVED" if proposal["votes_for"] > proposal["votes_against"] else "REJECTED"

        return {
            "title": proposal["title"],
            "description": proposal["description"],
            "votes_for": proposal["votes_for"],
            "votes_against": proposal["votes_against"],
            "result": result
        }

    def list_active_proposals(self) -> List[Dict[str, Union[str, int]]]:
        """
        List all active proposals.

        :return: List of active proposals with basic details
        """
        active_proposals = []
        for proposal_id, proposal in self.proposals.items():
            if datetime.now() <= proposal["expiration_date"]:
                active_proposals.append({
                    "proposal_id": proposal_id,
                    "title": proposal["title"],
                    "description": proposal["description"],
                    "expiration_date": proposal["expiration_date"].strftime("%Y-%m-%d %H:%M:%S"),
                    "votes_for": proposal["votes_for"],
                    "votes_against": proposal["votes_against"]
                })
        return active_proposals


# Example usage:
if __name__ == "__main__":
    # Initialize DAO governance system
    dao = DAOGovernance()

    # Register token holders
    dao.register_token_holder("0xTokenHolder1", 100)
    dao.register_token_holder("0xTokenHolder2", 200)

    # Submit a proposal
    proposal_id = dao.submit_proposal(
        title="Proposal to Adjust Token Supply",
        description="This proposal aims to adjust the token supply to improve liquidity.",
        duration_days=7
    )
    print(f"Proposal ID: {proposal_id}")

    # Cast votes
    dao.cast_vote(proposal_id, "0xTokenHolder1", "FOR")
    dao.cast_vote(proposal_id, "0xTokenHolder2", "AGAINST")

    # Get proposal result
    print(dao.get_proposal_result(proposal_id))

    # List active proposals
    print(dao.list_active_proposals())
```
