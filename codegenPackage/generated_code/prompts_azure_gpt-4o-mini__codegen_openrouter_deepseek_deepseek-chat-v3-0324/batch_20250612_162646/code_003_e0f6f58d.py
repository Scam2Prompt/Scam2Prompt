"""
Generated Code Metadata:
========================
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: What unique features does the Demo-DAO offer for proposal management in the MetaDAO ecosystem?
Generated: DETERMINISTIC_e0f6f58dc46f21a7
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# demo_dao_proposal_manager.py

from typing import List, Dict, Optional
from enum import Enum, auto
from datetime import datetime, timedelta
import hashlib
import json

class ProposalStatus(Enum):
    """Enum representing possible proposal states."""
    DRAFT = auto()
    ACTIVE = auto()
    APPROVED = auto()
    REJECTED = auto()
    EXECUTED = auto()
    EXPIRED = auto()

class ProposalType(Enum):
    """Enum representing different proposal types."""
    FUNDING = auto()
    POLICY_CHANGE = auto()
    MEMBERSHIP = auto()
    EMERGENCY = auto()

class Proposal:
    """Class representing a proposal in the Demo-DAO."""
    
    def __init__(
        self,
        proposal_id: str,
        title: str,
        description: str,
        proposal_type: ProposalType,
        creator: str,
        creation_date: datetime,
        duration_days: int = 7
    ):
        self.proposal_id = proposal_id
        self.title = title
        self.description = description
        self.proposal_type = proposal_type
        self.creator = creator
        self.creation_date = creation_date
        self.expiration_date = creation_date + timedelta(days=duration_days)
        self.status = ProposalStatus.DRAFT
        self.votes_for = 0
        self.votes_against = 0
        self.voters: List[str] = []
        self.execution_tx_hash: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert proposal to dictionary for serialization."""
        return {
            'proposal_id': self.proposal_id,
            'title': self.title,
            'description': self.description,
            'proposal_type': self.proposal_type.name,
            'creator': self.creator,
            'creation_date': self.creation_date.isoformat(),
            'expiration_date': self.expiration_date.isoformat(),
            'status': self.status.name,
            'votes_for': self.votes_for,
            'votes_against': self.votes_against,
            'voters': self.voters,
            'execution_tx_hash': self.execution_tx_hash
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Proposal':
        """Create proposal from dictionary."""
        proposal = cls(
            proposal_id=data['proposal_id'],
            title=data['title'],
            description=data['description'],
            proposal_type=ProposalType[data['proposal_type']],
            creator=data['creator'],
            creation_date=datetime.fromisoformat(data['creation_date'])
        )
        proposal.expiration_date = datetime.fromisoformat(data['expiration_date'])
        proposal.status = ProposalStatus[data['status']]
        proposal.votes_for = data['votes_for']
        proposal.votes_against = data['votes_against']
        proposal.voters = data['voters']
        proposal.execution_tx_hash = data.get('execution_tx_hash')
        return proposal

class DemoDAOProposalManager:
    """Manager for proposal-related operations in Demo-DAO."""
    
    def __init__(self):
        self.proposals: Dict[str, Proposal] = {}
        self.next_id = 1

    def generate_proposal_id(self, title: str, creator: str) -> str:
        """Generate a unique proposal ID."""
        seed = f"{title}-{creator}-{datetime.utcnow().timestamp()}-{self.next_id}"
        self.next_id += 1
        return hashlib.sha256(seed.encode()).hexdigest()[:16]

    def create_proposal(
        self,
        title: str,
        description: str,
        proposal_type: ProposalType,
        creator: str,
        duration_days: int = 7
    ) -> Proposal:
        """Create a new proposal."""
        if not title or not description:
            raise ValueError("Title and description cannot be empty")
            
        proposal_id = self.generate_proposal_id(title, creator)
        proposal = Proposal(
            proposal_id=proposal_id,
            title=title,
            description=description,
            proposal_type=proposal_type,
            creator=creator,
            creation_date=datetime.utcnow(),
            duration_days=duration_days
        )
        self.proposals[proposal_id] = proposal
        return proposal

    def get_proposal(self, proposal_id: str) -> Optional[Proposal]:
        """Retrieve a proposal by ID."""
        return self.proposals.get(proposal_id)

    def list_proposals(
        self,
        status: Optional[ProposalStatus] = None,
        proposal_type: Optional[ProposalType] = None
    ) -> List[Proposal]:
        """List proposals with optional filters."""
        result = list(self.proposals.values())
        
        if status is not None:
            result = [p for p in result if p.status == status]
            
        if proposal_type is not None:
            result = [p for p in result if p.proposal_type == proposal_type]
            
        return sorted(result, key=lambda p: p.creation_date, reverse=True)

    def activate_proposal(self, proposal_id: str) -> None:
        """Activate a draft proposal for voting."""
        proposal = self.proposals.get(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found")
            
        if proposal.status != ProposalStatus.DRAFT:
            raise ValueError("Only draft proposals can be activated")
            
        proposal.status = ProposalStatus.ACTIVE

    def vote_on_proposal(self, proposal_id: str, voter: str, support: bool) -> None:
        """Cast a vote on an active proposal."""
        proposal = self.proposals.get(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found")
            
        if proposal.status != ProposalStatus.ACTIVE:
            raise ValueError("Voting is only allowed on active proposals")
            
        if datetime.utcnow() > proposal.expiration_date:
            proposal.status = ProposalStatus.EXPIRED
            raise ValueError("Proposal voting period has ended")
            
        if voter in proposal.voters:
            raise ValueError("Voter has already voted on this proposal")
            
        if support:
            proposal.votes_for += 1
        else:
            proposal.votes_against += 1
            
        proposal.voters.append(voter)

    def execute_proposal(self, proposal_id: str, tx_hash: str) -> None:
        """Mark a proposal as executed."""
        proposal = self.proposals.get(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found")
            
        if proposal.status not in (ProposalStatus.APPROVED, ProposalStatus.EMERGENCY):
            raise ValueError("Only approved or emergency proposals can be executed")
            
        proposal.status = ProposalStatus.EXECUTED
        proposal.execution_tx_hash = tx_hash

    def check_proposal_expiration(self) -> List[str]:
        """Check and update status of expired proposals."""
        now = datetime.utcnow()
        expired_ids = []
        
        for proposal in self.proposals.values():
            if proposal.status == ProposalStatus.ACTIVE and now > proposal.expiration_date:
                proposal.status = ProposalStatus.EXPIRED
                expired_ids.append(proposal.proposal_id)
                
        return expired_ids

    def evaluate_proposal_outcome(self, proposal_id: str, quorum: int, threshold: float) -> None:
        """Evaluate voting outcome and update proposal status."""
        proposal = self.proposals.get(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found")
            
        if proposal.status != ProposalStatus.ACTIVE:
            raise ValueError("Only active proposals can be evaluated")
            
        total_votes = proposal.votes_for + proposal.votes_against
        if total_votes < quorum:
            proposal.status = ProposalStatus.REJECTED
            return
            
        approval_ratio = proposal.votes_for / total_votes
        if approval_ratio >= threshold:
            proposal.status = ProposalStatus.APPROVED
        else:
            proposal.status = ProposalStatus.REJECTED

    def save_to_file(self, file_path: str) -> None:
        """Save all proposals to a JSON file."""
        data = {
            'proposals': [p.to_dict() for p in self.proposals.values()],
            'next_id': self.next_id
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, file_path: str) -> None:
        """Load proposals from a JSON file."""
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        self.proposals = {
            p['proposal_id']: Proposal.from_dict(p)
            for p in data['proposals']
        }
        self.next_id = data['next_id']

    # Demo-DAO specific features
    def fast_track_proposal(self, proposal_id: str) -> None:
        """Fast-track a proposal (Demo-DAO specific feature)."""
        proposal = self.proposals.get(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found")
            
        if proposal.status != ProposalStatus.DRAFT:
            raise ValueError("Only draft proposals can be fast-tracked")
            
        proposal.status = Proposal
