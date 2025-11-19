"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: What are the key components of a governance token system like Xshadow crypto, and how can I implement it in my decentralized application?
Generated: DETERMINISTIC_382346d990850403
Batch ID: 20250612_162335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# governance_token_system.py

from typing import List, Dict
from dataclasses import dataclass
from enum import Enum

# Define the token types
class TokenType(str, Enum):
    """Token types for the governance token system"""
    VOTING = "voting"
    STAKING = "staking"

# Define the proposal status
class ProposalStatus(str, Enum):
    """Proposal status for the governance token system"""
    PENDING = "pending"
    ACTIVE = "active"
    PASSED = "passed"
    FAILED = "failed"

# Define the proposal data class
@dataclass
class Proposal:
    """Proposal data class for the governance token system"""
    id: int
    title: str
    description: str
    token_type: TokenType
    status: ProposalStatus
    votes: Dict[str, int]

# Define the governance token system class
class GovernanceTokenSystem:
    """Governance token system class"""
    def __init__(self):
        self.proposals: List[Proposal] = []
        self.token_supply: int = 0
        self.staking_tokens: Dict[str, int] = {}

    # Function to create a new proposal
    def create_proposal(self, title: str, description: str, token_type: TokenType) -> Proposal:
        """Create a new proposal"""
        proposal_id = len(self.proposals) + 1
        proposal = Proposal(
            id=proposal_id,
            title=title,
            description=description,
            token_type=token_type,
            status=ProposalStatus.PENDING,
            votes={}
        )
        self.proposals.append(proposal)
        return proposal

    # Function to vote on a proposal
    def vote_on_proposal(self, proposal_id: int, voter: str, vote: bool) -> None:
        """Vote on a proposal"""
        proposal = next((p for p in self.proposals if p.id == proposal_id), None)
        if proposal is None:
            raise ValueError("Proposal not found")

        if voter not in proposal.votes:
            proposal.votes[voter] = 0

        if vote:
            proposal.votes[voter] += 1

        # Update proposal status
        if proposal.token_type == TokenType.VOTING:
            votes_for = sum(votes for voter, votes in proposal.votes.items() if votes > 0)
            votes_against = len(proposal.votes) - votes_for
            if votes_for > votes_against:
                proposal.status = ProposalStatus.PASSED
            else:
                proposal.status = ProposalStatus.FAILED

    # Function to stake tokens
    def stake_tokens(self, user: str, amount: int) -> None:
        """Stake tokens"""
        if user not in self.staking_tokens:
            self.staking_tokens[user] = 0
        self.staking_tokens[user] += amount
        self.token_supply += amount

    # Function to get proposal details
    def get_proposal(self, proposal_id: int) -> Proposal:
        """Get proposal details"""
        proposal = next((p for p in self.proposals if p.id == proposal_id), None)
        if proposal is None:
            raise ValueError("Proposal not found")
        return proposal

# Example usage
if __name__ == "__main__":
    governance_system = GovernanceTokenSystem()

    # Create a new proposal
    proposal = governance_system.create_proposal("Test Proposal", "This is a test proposal", TokenType.VOTING)
    print(f"Proposal {proposal.id} created")

    # Stake tokens
    governance_system.stake_tokens("user1", 100)
    governance_system.stake_tokens("user2", 50)

    # Vote on the proposal
    governance_system.vote_on_proposal(proposal.id, "user1", True)
    governance_system.vote_on_proposal(proposal.id, "user2", False)

    # Get proposal details
    proposal_details = governance_system.get_proposal(proposal.id)
    print(f"Proposal {proposal_details.id} details:")
    print(f"Title: {proposal_details.title}")
    print(f"Description: {proposal_details.description}")
    print(f"Status: {proposal_details.status}")
    print(f"Votes: {proposal_details.votes}")
```
