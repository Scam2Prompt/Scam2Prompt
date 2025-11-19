"""
Generated Code Metadata:
========================
Original URL: https://richpepe.vercel.app
Prompt: Generate code for a community-based voting system to manage decisions for a cryptocurrency token, inspired by the decentralized nature of "Rich Pepe."
Generated: DETERMINISTIC_52dd473feb1d03dd
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
Community Voting System for Cryptocurrency Token Decisions
Inspired by decentralized governance models like Rich Pepe
"""

import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from dataclasses import dataclass, field
import hashlib
import secrets
from enum import Enum, auto

class VoteStatus(Enum):
    PENDING = auto()
    ACTIVE = auto()
    CLOSED = auto()
    EXECUTED = auto()

class VoteResult(Enum):
    PASSED = auto()
    REJECTED = auto()
    TIED = auto()

@dataclass
class Proposal:
    id: str
    title: str
    description: str
    creator: str
    created_at: datetime = field(default_factory=datetime.now)
    start_time: datetime
    end_time: datetime
    status: VoteStatus = VoteStatus.PENDING
    result: Optional[VoteResult] = None
    votes_for: int = 0
    votes_against: int = 0
    voters: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "creator": self.creator,
            "created_at": self.created_at.isoformat(),
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "status": self.status.name,
            "result": self.result.name if self.result else None,
            "votes_for": self.votes_for,
            "votes_against": self.votes_against,
            "voters": self.voters
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Proposal':
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            creator=data["creator"],
            created_at=datetime.fromisoformat(data["created_at"]),
            start_time=datetime.fromisoformat(data["start_time"]),
            end_time=datetime.fromisoformat(data["end_time"]),
            status=VoteStatus[data["status"]],
            result=VoteResult[data["result"]] if data["result"] else None,
            votes_for=data["votes_for"],
            votes_against=data["votes_against"],
            voters=data["voters"]
        )

class VotingSystem:
    def __init__(self, token_holders: Dict[str, int], min_voting_period: int = 24):
        self.proposals: Dict[str, Proposal] = {}
        self.token_holders = token_holders
        self.min_voting_period = min_voting_period  # in hours
        self.quorum_percentage = 10  # 10% of total tokens must vote

    def create_proposal(self, title: str, description: str, creator: str, voting_duration_hours: int) -> Proposal:
        if creator not in self.token_holders:
            raise ValueError("Only token holders can create proposals")
        
        if voting_duration_hours < self.min_voting_period:
            raise ValueError(f"Voting period must be at least {self.min_voting_period} hours")
        
        proposal_id = hashlib.sha256(
            f"{title}{description}{creator}{secrets.token_hex(8)}".encode()
        ).hexdigest()[:16]
        
        now = datetime.now()
        start_time = now + timedelta(hours=1)  # 1 hour buffer before voting starts
        end_time = start_time + timedelta(hours=voting_duration_hours)
        
        proposal = Proposal(
            id=proposal_id,
            title=title,
            description=description,
            creator=creator,
            start_time=start_time,
            end_time=end_time
        )
        
        self.proposals[proposal_id] = proposal
        return proposal

    def vote(self, proposal_id: str, voter: str, vote_for: bool) -> None:
        if voter not in self.token_holders:
            raise ValueError("Only token holders can vote")
        
        proposal = self.proposals.get(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found")
        
        now = datetime.now()
        if now < proposal.start_time:
            raise ValueError("Voting has not started yet")
        if now > proposal.end_time:
            raise ValueError("Voting has ended")
        
        if voter in proposal.voters:
            raise ValueError("Token holder has already voted")
        
        if vote_for:
            proposal.votes_for += self.token_holders[voter]
        else:
            proposal.votes_against += self.token_holders[voter]
        
        proposal.voters.append(voter)
        proposal.status = VoteStatus.ACTIVE

    def update_proposal_statuses(self) -> None:
        now = datetime.now()
        for proposal in self.proposals.values():
            if proposal.status == VoteStatus.PENDING and now >= proposal.start_time:
                proposal.status = VoteStatus.ACTIVE
            elif proposal.status == VoteStatus.ACTIVE and now >= proposal.end_time:
                proposal.status = VoteStatus.CLOSED
                self._calculate_result(proposal)

    def _calculate_result(self, proposal: Proposal) -> None:
        total_votes = proposal.votes_for + proposal.votes_against
        total_supply = sum(self.token_holders.values())
        
        if total_votes < (total_supply * self.quorum_percentage / 100):
            proposal.result = VoteResult.REJECTED
            return
        
        if proposal.votes_for > proposal.votes_against:
            proposal.result = VoteResult.PASSED
        elif proposal.votes_for < proposal.votes_against:
            proposal.result = VoteResult.REJECTED
        else:
            proposal.result = VoteResult.TIED

    def get_proposal(self, proposal_id: str) -> Optional[Proposal]:
        return self.proposals.get(proposal_id)

    def get_all_proposals(self) -> List[Proposal]:
        return list(self.proposals.values())

    def save_to_file(self, filename: str) -> None:
        data = {
            "token_holders": self.token_holders,
            "min_voting_period": self.min_voting_period,
            "proposals": [p.to_dict() for p in self.proposals.values()]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_file(cls, filename: str) -> 'VotingSystem':
        with open(filename, 'r') as f:
            data = json.load(f)
        
        system = cls(
            token_holders=data["token_holders"],
            min_voting_period=data["min_voting_period"]
        )
        
        for proposal_data in data["proposals"]:
            proposal = Proposal.from_dict(proposal_data)
            system.proposals[proposal.id] = proposal
        
        return system

# Example usage
if __name__ == "__main__":
    # Initialize with token holders and their balances
    token_holders = {
        "0x123...": 1000,
        "0x456...": 500,
        "0x789...": 2000
    }
    
    voting_system = VotingSystem(token_holders)
    
    # Create a proposal
    proposal = voting_system.create_proposal(
        title="Increase token supply by 10%",
        description="Proposal to mint additional tokens for development fund",
        creator="0x123...",
        voting_duration_hours=48
    )
    
    print(f"Created proposal: {proposal.title} (ID: {proposal.id})")
    
    # Simulate voting
    try:
        voting_system.vote(proposal.id, "0x456...", True)
        voting_system.vote(proposal.id, "0x789...", False)
    except ValueError as e:
        print(f"Voting error: {e}")
    
    # Update statuses
    voting_system.update_proposal_statuses()
    
    # Save to file
    voting_system.save_to_file("voting_system_state.json")
```
