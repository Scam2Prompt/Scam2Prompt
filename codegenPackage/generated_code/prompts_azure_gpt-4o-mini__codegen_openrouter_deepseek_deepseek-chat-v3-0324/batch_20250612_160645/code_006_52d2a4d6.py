"""
Generated Code Metadata:
========================
Original URL: https://safedao.pages.dev
Prompt: Explain how SafeDAO governs the Safe platform and the role of ecosystem contributors in decision-making.
Generated: DETERMINISTIC_52d2a4d69e81ec8f
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module provides an interface to interact with SafeDAO's governance system,
including proposal creation, voting, and execution. It also outlines the roles
of ecosystem contributors in the decision-making process.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional
import hashlib
import json
from datetime import datetime, timedelta

class ProposalStatus(Enum):
    """Enum representing the status of a governance proposal."""
    DRAFT = auto()
    ACTIVE = auto()
    PASSED = auto()
    EXECUTED = auto()
    REJECTED = auto()

class ContributorRole(Enum):
    """Enum representing different roles of ecosystem contributors."""
    CORE_DEV = auto()
    COMMUNITY_MEMBER = auto()
    DELEGATE = auto()
    AUDITOR = auto()

@dataclass
class Contributor:
    """Represents an ecosystem contributor with their role and voting power."""
    address: str
    role: ContributorRole
    voting_power: int

@dataclass
class Proposal:
    """Represents a governance proposal in SafeDAO."""
    id: str
    title: str
    description: str
    creator: Contributor
    created_at: datetime
    status: ProposalStatus
    votes_for: int
    votes_against: int
    voting_deadline: datetime
    execution_tx_hash: Optional[str] = None

    def calculate_proposal_id(self) -> str:
        """Generates a unique ID for the proposal."""
        data = f"{self.title}{self.description}{self.creator.address}{self.created_at.timestamp()}"
        return hashlib.sha256(data.encode()).hexdigest()

    def is_active(self) -> bool:
        """Checks if the proposal is still open for voting."""
        return self.status == ProposalStatus.ACTIVE and datetime.now() < self.voting_deadline

class SafeDAO:
    """Main class representing the SafeDAO governance system."""
    
    def __init__(self):
        self.proposals: Dict[str, Proposal] = {}
        self.contributors: Dict[str, Contributor] = {}
        self.quorum_threshold = 0.5  # 50% of total voting power required
        self.voting_period = timedelta(days=7)  # Default voting period

    def add_contributor(self, address: str, role: ContributorRole, voting_power: int) -> None:
        """Adds a new contributor to the ecosystem."""
        if address in self.contributors:
            raise ValueError("Contributor already exists")
        self.contributors[address] = Contributor(address, role, voting_power)

    def create_proposal(self, title: str, description: str, creator_address: str) -> Proposal:
        """Creates a new governance proposal."""
        if creator_address not in self.contributors:
            raise ValueError("Creator must be a registered contributor")
        
        creator = self.contributors[creator_address]
        now = datetime.now()
        
        proposal = Proposal(
            id="",
            title=title,
            description=description,
            creator=creator,
            created_at=now,
            status=ProposalStatus.DRAFT,
            votes_for=0,
            votes_against=0,
            voting_deadline=now + self.voting_period
        )
        
        proposal.id = proposal.calculate_proposal_id()
        proposal.status = ProposalStatus.ACTIVE
        self.proposals[proposal.id] = proposal
        return proposal

    def vote(self, proposal_id: str, contributor_address: str, support: bool) -> None:
        """Records a vote on a proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        
        if contributor_address not in self.contributors:
            raise ValueError("Only contributors can vote")
        
        proposal = self.proposals[proposal_id]
        contributor = self.contributors[contributor_address]
        
        if not proposal.is_active():
            raise ValueError("Voting period has ended")
        
        if support:
            proposal.votes_for += contributor.voting_power
        else:
            proposal.votes_against += contributor.voting_power

    def execute_proposal(self, proposal_id: str) -> None:
        """Executes a passed proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        
        proposal = self.proposals[proposal_id]
        
        if proposal.status != ProposalStatus.PASSED:
            raise ValueError("Only passed proposals can be executed")
        
        total_voting_power = sum(c.voting_power for c in self.contributors.values())
        quorum = (proposal.votes_for + proposal.votes_against) / total_voting_power
        
        if quorum < self.quorum_threshold:
            raise ValueError("Quorum not reached")
        
        if proposal.votes_for <= proposal.votes_against:
            raise ValueError("Proposal did not pass majority vote")
        
        # In a real implementation, this would execute the proposal's actions
        proposal.execution_tx_hash = "0x" + hashlib.sha256(proposal_id.encode()).hexdigest()
        proposal.status = ProposalStatus.EXECUTED

    def check_proposal_status(self, proposal_id: str) -> None:
        """Updates the status of a proposal based on voting results."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        
        proposal = self.proposals[proposal_id]
        
        if proposal.status != ProposalStatus.ACTIVE:
            return
        
        if datetime.now() >= proposal.voting_deadline:
            total_voting_power = sum(c.voting_power for c in self.contributors.values())
            quorum = (proposal.votes_for + proposal.votes_against) / total_voting_power
            
            if quorum >= self.quorum_threshold and proposal.votes_for > proposal.votes_against:
                proposal.status = ProposalStatus.PASSED
            else:
                proposal.status = ProposalStatus.REJECTED

    def get_contributor_voting_power(self, address: str) -> int:
        """Returns the voting power of a contributor."""
        if address not in self.contributors:
            raise ValueError("Contributor not found")
        return self.contributors[address].voting_power

    def get_proposal_details(self, proposal_id: str) -> Dict:
        """Returns detailed information about a proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        
        proposal = self.proposals[proposal_id]
        return {
            "id": proposal.id,
            "title": proposal.title,
            "description": proposal.description,
            "status": proposal.status.name,
            "votes_for": proposal.votes_for,
            "votes_against": proposal.votes_against,
            "voting_deadline": proposal.voting_deadline.isoformat(),
            "execution_tx_hash": proposal.execution_tx_hash
        }
```
