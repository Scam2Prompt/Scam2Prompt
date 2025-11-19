"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Write a Python code snippet to implement a basic slashing mechanism for a DAO, where members can vote to redistribute staked assets from non-compliant participants to charitable causes.
Generated: DETERMINISTIC_ab445b9071a7aa8b
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum, auto

class VoteOutcome(Enum):
    """Enum representing possible vote outcomes."""
    PASSED = auto()
    FAILED = auto()
    PENDING = auto()

@dataclass
class Proposal:
    """Data class representing a slashing proposal."""
    id: str
    target_member: str
    amount: float
    charity_address: str
    votes_for: int = 0
    votes_against: int = 0
    status: VoteOutcome = VoteOutcome.PENDING

class DAO:
    """Class representing a Decentralized Autonomous Organization with slashing mechanism."""
    
    def __init__(self, min_votes: int, majority_threshold: float):
        """
        Initialize the DAO with voting parameters.
        
        Args:
            min_votes: Minimum number of votes required for a proposal to pass
            majority_threshold: Percentage of votes needed to pass (0.0 to 1.0)
        """
        self.min_votes = min_votes
        self.majority_threshold = majority_threshold
        self.proposals: Dict[str, Proposal] = {}
        self.member_stakes: Dict[str, float] = {}
        self.voted_members: Dict[str, List[str]] = {}  # proposal_id -> list of voters
        
    def stake(self, member: str, amount: float) -> None:
        """Stake tokens for a member."""
        if amount <= 0:
            raise ValueError("Stake amount must be positive")
        self.member_stakes[member] = self.member_stakes.get(member, 0.0) + amount
    
    def create_proposal(self, target_member: str, amount: float, charity_address: str) -> str:
        """
        Create a new slashing proposal.
        
        Args:
            target_member: Member to potentially slash
            amount: Amount to slash
            charity_address: Address to send slashed funds
            
        Returns:
            Proposal ID
        """
        if target_member not in self.member_stakes:
            raise ValueError("Target member does not exist")
        if amount <= 0:
            raise ValueError("Slash amount must be positive")
        if amount > self.member_stakes[target_member]:
            raise ValueError("Cannot slash more than member's stake")
            
        proposal_id = hashlib.sha256(f"{target_member}{amount}{charity_address}".encode()).hexdigest()
        self.proposals[proposal_id] = Proposal(
            id=proposal_id,
            target_member=target_member,
            amount=amount,
            charity_address=charity_address
        )
        self.voted_members[proposal_id] = []
        return proposal_id
    
    def vote(self, proposal_id: str, member: str, in_favor: bool) -> None:
        """
        Vote on a slashing proposal.
        
        Args:
            proposal_id: ID of the proposal to vote on
            member: Member casting the vote
            in_favor: Whether the vote is in favor of the proposal
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        if member not in self.member_stakes:
            raise ValueError("Member does not exist")
        if member in self.voted_members[proposal_id]:
            raise ValueError("Member has already voted")
            
        proposal = self.proposals[proposal_id]
        if in_favor:
            proposal.votes_for += 1
        else:
            proposal.votes_against += 1
            
        self.voted_members[proposal_id].append(member)
        
        # Check if proposal can be resolved
        self._check_proposal_outcome(proposal_id)
    
    def _check_proposal_outcome(self, proposal_id: str) -> None:
        """Check if a proposal has reached a decision."""
        proposal = self.proposals[proposal_id]
        total_votes = proposal.votes_for + proposal.votes_against
        
        if total_votes < self.min_votes:
            return
            
        if proposal.votes_for / total_votes >= self.majority_threshold:
            proposal.status = VoteOutcome.PASSED
            self._execute_slash(proposal)
        else:
            proposal.status = VoteOutcome.FAILED
    
    def _execute_slash(self, proposal: Proposal) -> None:
        """Execute the slashing of funds."""
        if proposal.target_member in self.member_stakes:
            self.member_stakes[proposal.target_member] -= proposal.amount
            # In a real implementation, funds would be transferred to charity here
            # For this example, we just track the slash
    
    def get_proposal_status(self, proposal_id: str) -> VoteOutcome:
        """Get the current status of a proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        return self.proposals[proposal_id].status
```
