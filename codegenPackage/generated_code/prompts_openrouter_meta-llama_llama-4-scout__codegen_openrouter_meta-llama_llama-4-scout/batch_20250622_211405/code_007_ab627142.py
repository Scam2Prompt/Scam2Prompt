"""
Generated Code Metadata:
========================
Original URL: https://d-510.pages.dev
Prompt: "Propose a community-driven DAO governance model for Lingo, enabling token holders to participate in decision-making processes for the RWA investment portfolio."
Generated: DETERMINISTIC_ab6271421b3d4932
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# governance_model.py

from typing import List, Dict
from dataclasses import dataclass
from enum import Enum
from datetime import datetime, timedelta

# Define the governance model enums
class ProposalStatus(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3

class VoteType(Enum):
    YES = 1
    NO = 2
    ABSTAIN = 3

# Define the proposal data class
@dataclass
class Proposal:
    id: int
    description: str
    status: ProposalStatus
    created_at: datetime
    votes: Dict[str, VoteType]

# Define the governance model class
class GovernanceModel:
    def __init__(self, token_holders: List[str], proposal_threshold: int, voting_period: timedelta):
        """
        Initialize the governance model.

        Args:
        - token_holders (List[str]): A list of token holder addresses.
        - proposal_threshold (int): The minimum number of votes required for a proposal to pass.
        - voting_period (timedelta): The duration of the voting period.
        """
        self.token_holders = token_holders
        self.proposal_threshold = proposal_threshold
        self.voting_period = voting_period
        self.proposals = {}

    def create_proposal(self, description: str) -> Proposal:
        """
        Create a new proposal.

        Args:
        - description (str): The proposal description.

        Returns:
        - Proposal: The created proposal.
        """
        proposal_id = len(self.proposals) + 1
        proposal = Proposal(proposal_id, description, ProposalStatus.PENDING, datetime.now(), {})
        self.proposals[proposal_id] = proposal
        return proposal

    def vote(self, proposal_id: int, token_holder: str, vote_type: VoteType) -> None:
        """
        Cast a vote on a proposal.

        Args:
        - proposal_id (int): The ID of the proposal to vote on.
        - token_holder (str): The address of the token holder casting the vote.
        - vote_type (VoteType): The type of vote (YES, NO, or ABSTAIN).
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found")

        proposal = self.proposals[proposal_id]
        if proposal.status != ProposalStatus.PENDING:
            raise ValueError("Proposal is not in a pending state")

        if token_holder not in self.token_holders:
            raise ValueError("Token holder not found")

        if token_holder in proposal.votes:
            raise ValueError("Token holder has already voted")

        proposal.votes[token_holder] = vote_type

    def finalize_proposal(self, proposal_id: int) -> None:
        """
        Finalize a proposal based on the votes cast.

        Args:
        - proposal_id (int): The ID of the proposal to finalize.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found")

        proposal = self.proposals[proposal_id]
        if proposal.status != ProposalStatus.PENDING:
            raise ValueError("Proposal is not in a pending state")

        yes_votes = sum(1 for vote in proposal.votes.values() if vote == VoteType.YES)
        no_votes = sum(1 for vote in proposal.votes.values() if vote == VoteType.NO)

        if yes_votes >= self.proposal_threshold:
            proposal.status = ProposalStatus.APPROVED
        else:
            proposal.status = ProposalStatus.REJECTED

    def get_proposal(self, proposal_id: int) -> Proposal:
        """
        Get a proposal by ID.

        Args:
        - proposal_id (int): The ID of the proposal to retrieve.

        Returns:
        - Proposal: The proposal with the given ID.
        """
        return self.proposals.get(proposal_id)

# Example usage
if __name__ == "__main__":
    token_holders = ["holder1", "holder2", "holder3"]
    governance_model = GovernanceModel(token_holders, 2, timedelta(days=3))

    proposal = governance_model.create_proposal("Invest in RWA portfolio")
    print(proposal)

    governance_model.vote(proposal.id, "holder1", VoteType.YES)
    governance_model.vote(proposal.id, "holder2", VoteType.YES)
    governance_model.vote(proposal.id, "holder3", VoteType.NO)

    governance_model.finalize_proposal(proposal.id)

    finalized_proposal = governance_model.get_proposal(proposal.id)
    print(finalized_proposal)
```
