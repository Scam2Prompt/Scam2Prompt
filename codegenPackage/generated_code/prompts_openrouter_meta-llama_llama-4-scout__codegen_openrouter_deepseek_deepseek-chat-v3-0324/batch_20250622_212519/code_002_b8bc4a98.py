"""
Generated Code Metadata:
========================
Original URL: https://gitcoins.com
Prompt: Design a step-by-step framework for launching a Gitcoin-style grants program, incorporating community engagement and governance.
Generated: DETERMINISTIC_b8bc4a985749a6af
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Gitcoin-style Grants Program Framework
This script outlines a step-by-step framework for launching a community-driven grants program.
"""

import json
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum, auto
import hashlib
import uuid

class GrantStatus(Enum):
    DRAFT = auto()
    ACTIVE = auto()
    CLOSED = auto()
    FUNDED = auto()

class VoteType(Enum):
    YES = auto()
    NO = auto()
    ABSTAIN = auto()

class Grant:
    def __init__(self, title: str, description: str, owner: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.owner = owner
        self.status = GrantStatus.DRAFT
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.funds_raised = 0.0
        self.votes = {"yes": 0, "no": 0, "abstain": 0}
        self.contributors = set()

    def update_status(self, new_status: GrantStatus) -> None:
        self.status = new_status
        self.updated_at = datetime.now()

    def add_vote(self, vote_type: VoteType, voter: str) -> None:
        if vote_type == VoteType.YES:
            self.votes["yes"] += 1
        elif vote_type == VoteType.NO:
            self.votes["no"] += 1
        else:
            self.votes["abstain"] += 1
        self.contributors.add(voter)

    def add_funds(self, amount: float, contributor: str) -> None:
        self.funds_raised += amount
        self.contributors.add(contributor)

class GrantsProgram:
    def __init__(self, name: str, admin: str):
        self.name = name
        self.admin = admin
        self.grants = {}
        self.created_at = datetime.now()
        self.rounds = []
        self.community_members = set()
        self.community_members.add(admin)

    def create_grant(self, title: str, description: str, owner: str) -> Grant:
        grant = Grant(title, description, owner)
        self.grants[grant.id] = grant
        self.community_members.add(owner)
        return grant

    def start_funding_round(self, name: str, start_date: datetime, end_date: datetime) -> Dict:
        round_id = hashlib.sha256(name.encode()).hexdigest()
        funding_round = {
            "id": round_id,
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "active": True,
            "grants": set()
        }
        self.rounds.append(funding_round)
        return funding_round

    def add_grant_to_round(self, round_id: str, grant_id: str) -> None:
        for funding_round in self.rounds:
            if funding_round["id"] == round_id:
                funding_round["grants"].add(grant_id)
                self.grants[grant_id].update_status(GrantStatus.ACTIVE)
                break

    def end_funding_round(self, round_id: str) -> None:
        for funding_round in self.rounds:
            if funding_round["id"] == round_id:
                funding_round["active"] = False
                funding_round["end_date"] = datetime.now()
                for grant_id in funding_round["grants"]:
                    self.grants[grant_id].update_status(GrantStatus.CLOSED)
                break

    def add_community_member(self, member: str) -> None:
        self.community_members.add(member)

    def get_grant(self, grant_id: str) -> Optional[Grant]:
        return self.grants.get(grant_id)

    def vote_on_grant(self, grant_id: str, vote_type: VoteType, voter: str) -> bool:
        if voter not in self.community_members:
            return False
        grant = self.grants.get(grant_id)
        if grant and grant.status == GrantStatus.ACTIVE:
            grant.add_vote(vote_type, voter)
            return True
        return False

    def contribute_to_grant(self, grant_id: str, amount: float, contributor: str) -> bool:
        if contributor not in self.community_members:
            return False
        grant = self.grants.get(grant_id)
        if grant and grant.status == GrantStatus.ACTIVE:
            grant.add_funds(amount, contributor)
            return True
        return False

    def get_active_grants(self) -> List[Grant]:
        return [grant for grant in self.grants.values() if grant.status == GrantStatus.ACTIVE]

    def to_json(self) -> str:
        program_data = {
            "name": self.name,
            "admin": self.admin,
            "created_at": self.created_at.isoformat(),
            "grants": [vars(grant) for grant in self.grants.values()],
            "rounds": self.rounds,
            "community_members": list(self.community_members)
        }
        return json.dumps(program_data, indent=2)

class GovernanceProposal:
    def __init__(self, title: str, description: str, proposer: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.proposer = proposer
        self.created_at = datetime.now()
        self.votes = {"yes": 0, "no": 0, "abstain": 0}
        self.voters = set()
        self.executed = False

    def add_vote(self, vote_type: VoteType, voter: str) -> None:
        if vote_type == VoteType.YES:
            self.votes["yes"] += 1
        elif vote_type == VoteType.NO:
            self.votes["no"] += 1
        else:
            self.votes["abstain"] += 1
        self.voters.add(voter)

class Governance:
    def __init__(self, grants_program: GrantsProgram):
        self.proposals = {}
        self.grants_program = grants_program

    def create_proposal(self, title: str, description: str, proposer: str) -> GovernanceProposal:
        if proposer not in self.grants_program.community_members:
            raise ValueError("Only community members can create proposals")
        proposal = GovernanceProposal(title, description, proposer)
        self.proposals[proposal.id] = proposal
        return proposal

    def vote_on_proposal(self, proposal_id: str, vote_type: VoteType, voter: str) -> bool:
        if voter not in self.grants_program.community_members:
            return False
        proposal = self.proposals.get(proposal_id)
        if proposal:
            proposal.add_vote(vote_type, voter)
            return True
        return False

    def execute_proposal(self, proposal_id: str) -> bool:
        proposal = self.proposals.get(proposal_id)
        if not proposal or proposal.executed:
            return False
        
        total_votes = sum(proposal.votes.values())
        if total_votes > 0 and proposal.votes["yes"] / total_votes > 0.5:
            proposal.executed = True
            return True
        return False

def main():
    # Example usage
    program = GrantsProgram("Ecosystem Grants", "admin@example.com")
    
    # Community engagement
    program.add_community_member("user1@example.com")
    program.add_community_member("user2@example.com")
    
    # Grant creation
    grant1 = program.create_grant("Web3 Education", "Educational content for Web3", "creator1@example.com")
    
    # Funding round
    round1 = program.start_funding_round("Q1 2023", datetime(2023, 1, 1), datetime(2023, 3, 31))
    program.add_grant_to_round(round1["id"], grant1.id)
    
    # Community participation
    program.vote_on_grant(grant1.id, VoteType.YES, "user1@example.com")
    program.contribute_to_grant(grant1.id, 100.0, "user2@example.com")
    
    # Governance
    governance = Governance(program)
    proposal = governance.create_proposal("Increase Grant Size", "Double the max grant amount", "user1@example.com")
    governance.vote_on_proposal(proposal.id, VoteType.YES, "user2@example.com")
    governance.execute_proposal(proposal.id)
    
    # End round
    program.end_funding_round(round1["id"])
    
    print(program.to_json())

if __name__ == "__main__":
    main()
```
