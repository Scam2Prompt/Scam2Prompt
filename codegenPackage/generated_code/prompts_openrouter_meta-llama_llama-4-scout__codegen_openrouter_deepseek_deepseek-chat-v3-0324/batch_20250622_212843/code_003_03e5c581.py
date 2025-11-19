"""
Generated Code Metadata:
========================
Original URL: https://binance.wallet.consulting
Prompt: What are the benefits and challenges of using decentralized structures like DAO for community-driven projects, and how can they be applied to social impact initiatives?
Generated: DETERMINISTIC_03e5c581ba82d5af
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates a basic DAO (Decentralized Autonomous Organization) structure
# for managing community-driven social impact projects.

from typing import List, Dict, Optional
from dataclasses import dataclass
import hashlib
import json
from datetime import datetime

class DAOException(Exception):
    """Base exception for DAO-related errors"""
    pass

class InsufficientVotesException(DAOException):
    """Raised when a proposal doesn't get enough votes"""
    pass

class InsufficientFundsException(DAOException):
    """Raised when the DAO doesn't have enough funds"""
    pass

class UnauthorizedAccessException(DAOException):
    """Raised when a member tries to perform unauthorized action"""
    pass

@dataclass
class Member:
    """Represents a DAO member with voting rights"""
    address: str
    name: str
    join_date: datetime
    voting_power: int = 1
    tokens: float = 0.0

    def __post_init__(self):
        if self.voting_power < 0:
            raise ValueError("Voting power cannot be negative")

@dataclass
class Proposal:
    """Represents a proposal in the DAO"""
    id: str
    title: str
    description: str
    creator: str  # member address
    creation_date: datetime
    requested_funds: float
    beneficiary: str
    status: str = "pending"  # pending, approved, rejected, executed
    votes_for: int = 0
    votes_against: int = 0

    def vote(self, in_favor: bool, voting_power: int = 1):
        """Record a vote for this proposal"""
        if in_favor:
            self.votes_for += voting_power
        else:
            self.votes_against += voting_power

    def execute(self):
        """Mark proposal as executed"""
        if self.status != "approved":
            raise DAOException("Only approved proposals can be executed")
        self.status = "executed"

class DAO:
    """Basic implementation of a Decentralized Autonomous Organization"""
    
    def __init__(self, name: str, initial_funds: float = 0.0):
        self.name = name
        self.funds = initial_funds
        self.members: Dict[str, Member] = {}
        self.proposals: Dict[str, Proposal] = {}
        self.voting_threshold = 0.5  # 50% of votes needed to pass
        self.min_votes = 3  # minimum number of votes required
        
    def add_member(self, member: Member) -> None:
        """Add a new member to the DAO"""
        if member.address in self.members:
            raise DAOException("Member already exists")
        self.members[member.address] = member
    
    def create_proposal(
        self,
        title: str,
        description: str,
        creator_address: str,
        requested_funds: float,
        beneficiary: str
    ) -> Proposal:
        """Create a new proposal for the DAO to vote on"""
        if creator_address not in self.members:
            raise UnauthorizedAccessException("Only members can create proposals")
        
        if requested_funds > self.funds:
            raise InsufficientFundsException("DAO doesn't have enough funds")
        
        proposal_id = hashlib.sha256(
            f"{title}{description}{creator_address}{datetime.now().isoformat()}".encode()
        ).hexdigest()[:16]
        
        proposal = Proposal(
            id=proposal_id,
            title=title,
            description=description,
            creator=creator_address,
            creation_date=datetime.now(),
            requested_funds=requested_funds,
            beneficiary=beneficiary
        )
        
        self.proposals[proposal_id] = proposal
        return proposal
    
    def vote_on_proposal(
        self,
        proposal_id: str,
        member_address: str,
        in_favor: bool
    ) -> None:
        """Cast a vote on a proposal"""
        if member_address not in self.members:
            raise UnauthorizedAccessException("Only members can vote")
        
        if proposal_id not in self.proposals:
            raise DAOException("Proposal not found")
        
        proposal = self.proposals[proposal_id]
        member = self.members[member_address]
        
        proposal.vote(in_favor, member.voting_power)
    
    def process_proposal(self, proposal_id: str) -> None:
        """Process a proposal after voting period ends"""
        if proposal_id not in self.proposals:
            raise DAOException("Proposal not found")
        
        proposal = self.proposals[proposal_id]
        
        total_votes = proposal.votes_for + proposal.votes_against
        if total_votes < self.min_votes:
            proposal.status = "rejected"
            raise InsufficientVotesException("Not enough votes cast")
        
        approval_ratio = proposal.votes_for / total_votes
        if approval_ratio >= self.voting_threshold:
            proposal.status = "approved"
        else:
            proposal.status = "rejected"
    
    def execute_proposal(self, proposal_id: str) -> None:
        """Execute an approved proposal"""
        if proposal_id not in self.proposals:
            raise DAOException("Proposal not found")
        
        proposal = self.proposals[proposal_id]
        
        if proposal.status != "approved":
            raise DAOException("Only approved proposals can be executed")
        
        if proposal.requested_funds > self.funds:
            raise InsufficientFundsException("DAO doesn't have enough funds")
        
        self.funds -= proposal.requested_funds
        proposal.execute()
    
    def add_funds(self, amount: float) -> None:
        """Add funds to the DAO treasury"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.funds += amount
    
    def get_proposal_status(self, proposal_id: str) -> Optional[str]:
        """Get the status of a proposal"""
        if proposal_id in self.proposals:
            return self.proposals[proposal_id].status
        return None
    
    def to_json(self) -> str:
        """Serialize the DAO state to JSON"""
        state = {
            "name": self.name,
            "funds": self.funds,
            "members": {addr: vars(m) for addr, m in self.members.items()},
            "proposals": {pid: vars(p) for pid, p in self.proposals.items()},
            "voting_threshold": self.voting_threshold,
            "min_votes": self.min_votes
        }
        return json.dumps(state, default=str)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'DAO':
        """Deserialize a DAO from JSON"""
        data = json.loads(json_str)
        dao = cls(data["name"], data["funds"])
        dao.voting_threshold = data["voting_threshold"]
        dao.min_votes = data["min_votes"]
        
        for addr, member_data in data["members"].items():
            member_data["join_date"] = datetime.fromisoformat(member_data["join_date"])
            dao.members[addr] = Member(**member_data)
        
        for pid, proposal_data in data["proposals"].items():
            proposal_data["creation_date"] = datetime.fromisoformat(proposal_data["creation_date"])
            dao.proposals[pid] = Proposal(**proposal_data)
        
        return dao

# Example usage for a social impact initiative
def example_social_impact_dao():
    """Demonstrate how a DAO can be used for social impact initiatives"""
    try:
        # Create a DAO for community projects
        community_dao = DAO("Green Neighborhood Initiative", initial_funds=10000.0)
        
        # Add members
        alice = Member(
            address="0xAlice123",
            name="Alice",
            join_date=datetime.now(),
            voting_power=1,
            tokens=100.0
        )
        bob = Member(
            address="0xBob456",
            name="Bob",
            join_date=datetime.now(),
            voting_power=1,
            tokens=150.0
        )
        community_dao.add_member(alice)
        community_dao.add_member(bob)
        
        # Create a proposal for a community garden
        garden_proposal = community_dao.create_proposal(
            title="Community Garden Project",
            description="Create a shared garden space in the vacant lot on 5th street",
            creator_address="0xAlice123",
            requested_funds=2000.0,
            beneficiary="Community Garden Fund"
        )
        
        # Members vote on the proposal
        community_dao.vote_on_proposal(garden_proposal.id, "0xAlice123", True)
        community_dao.vote_on_proposal(garden_proposal.id, "0xBob456", True)
        
        # Process the proposal
        community_dao.process_proposal(garden_proposal.id)
        
        # Execute if approved
        if community_dao.get_proposal_status(garden_proposal.id) == "approved":
            community_dao.execute_proposal(garden_proposal.id)
            print("Community garden project
