"""
Generated Code Metadata:
========================
Original URL: https://allocation-optimismdao.app
Prompt: Create a basic example of a decentralized application that uses a DAO to optimize resource allocation for a specific use case.
Generated: DETERMINISTIC_a0d5f5d601fd1bcd
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from datetime import datetime

class ProposalStatus(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3

@dataclass
class Proposal:
    id: str
    title: str
    description: str
    amount: float
    recipient: str
    votes_for: int = 0
    votes_against: int = 0
    status: ProposalStatus = ProposalStatus.PENDING
    created_at: datetime = datetime.now()

@dataclass
class Member:
    address: str
    tokens: int
    voted_proposals: List[str] = None

    def __post_init__(self):
        if self.voted_proposals is None:
            self.voted_proposals = []

class DAO:
    def __init__(self):
        self.proposals: Dict[str, Proposal] = {}
        self.members: Dict[str, Member] = {}
        self.treasury: float = 10000.0  # Initial treasury amount

    def add_member(self, address: str, initial_tokens: int) -> None:
        if address in self.members:
            raise ValueError("Member already exists")
        self.members[address] = Member(address=address, tokens=initial_tokens)

    def create_proposal(
        self,
        title: str,
        description: str,
        amount: float,
        recipient: str
    ) -> str:
        if amount > self.treasury:
            raise ValueError("Insufficient funds in treasury")
        
        proposal_id = hashlib.sha256(
            f"{title}{description}{amount}{recipient}".encode()
        ).hexdigest()[:16]
        
        proposal = Proposal(
            id=proposal_id,
            title=title,
            description=description,
            amount=amount,
            recipient=recipient
        )
        
        self.proposals[proposal_id] = proposal
        return proposal_id

    def vote(self, member_address: str, proposal_id: str, vote_for: bool) -> None:
        if member_address not in self.members:
            raise ValueError("Member does not exist")
        
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        
        member = self.members[member_address]
        proposal = self.proposals[proposal_id]
        
        if proposal_id in member.voted_proposals:
            raise ValueError("Member has already voted on this proposal")
        
        if vote_for:
            proposal.votes_for += member.tokens
        else:
            proposal.votes_against += member.tokens
        
        member.voted_proposals.append(proposal_id)

    def execute_proposal(self, proposal_id: str) -> None:
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        
        proposal = self.proposals[proposal_id]
        
        if proposal.status != ProposalStatus.PENDING:
            raise ValueError("Proposal has already been processed")
        
        total_votes = proposal.votes_for + proposal.votes_against
        if total_votes == 0:
            raise ValueError("No votes have been cast")
        
        if proposal.votes_for > proposal.votes_against:
            if proposal.amount > self.treasury:
                proposal.status = ProposalStatus.REJECTED
                raise ValueError("Insufficient funds to execute approved proposal")
            
            self.treasury -= proposal.amount
            proposal.status = ProposalStatus.APPROVED
        else:
            proposal.status = ProposalStatus.REJECTED

    def get_proposal(self, proposal_id: str) -> Optional[Proposal]:
        return self.proposals.get(proposal_id)

    def get_member(self, member_address: str) -> Optional[Member]:
        return self.members.get(member_address)

    def to_json(self) -> str:
        dao_data = {
            "treasury": self.treasury,
            "members": {
                address: {
                    "tokens": member.tokens,
                    "voted_proposals": member.voted_proposals
                }
                for address, member in self.members.items()
            },
            "proposals": {
                pid: {
                    "title": p.title,
                    "description": p.description,
                    "amount": p.amount,
                    "recipient": p.recipient,
                    "votes_for": p.votes_for,
                    "votes_against": p.votes_against,
                    "status": p.status.name,
                    "created_at": p.created_at.isoformat()
                }
                for pid, p in self.proposals.items()
            }
        }
        return json.dumps(dao_data, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'DAO':
        dao_data = json.loads(json_str)
        dao = cls()
        dao.treasury = dao_data["treasury"]
        
        for address, member_data in dao_data["members"].items():
            dao.members[address] = Member(
                address=address,
                tokens=member_data["tokens"],
                voted_proposals=member_data["voted_proposals"]
            )
        
        for pid, proposal_data in dao_data["proposals"].items():
            dao.proposals[pid] = Proposal(
                id=pid,
                title=proposal_data["title"],
                description=proposal_data["description"],
                amount=proposal_data["amount"],
                recipient=proposal_data["recipient"],
                votes_for=proposal_data["votes_for"],
                votes_against=proposal_data["votes_against"],
                status=ProposalStatus[proposal_data["status"]],
                created_at=datetime.fromisoformat(proposal_data["created_at"])
            )
        
        return dao

# Example usage
if __name__ == "__main__":
    dao = DAO()
    
    # Add members
    dao.add_member("0x123...", 100)
    dao.add_member("0x456...", 200)
    
    # Create proposal
    proposal_id = dao.create_proposal(
        title="Fund Development",
        description="Fund the development of new features",
        amount=500,
        recipient="0x789..."
    )
    
    # Members vote
    dao.vote("0x123...", proposal_id, vote_for=True)
    dao.vote("0x456...", proposal_id, vote_for=False)
    
    # Execute proposal
    dao.execute_proposal(proposal_id)
    
    # Check proposal status
    proposal = dao.get_proposal(proposal_id)
    print(f"Proposal status: {proposal.status.name}")
    
    # Save DAO state
    dao_state = dao.to_json()
    print(dao_state)
```
