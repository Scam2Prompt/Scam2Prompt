"""
Generated Code Metadata:
========================
Original URL: https://egld.pages.dev
Prompt: "Propose a use case for the EGLD token in a decentralized application (dApp) built on MultiversX, and outline the potential ecosystem benefits."
Generated: DETERMINISTIC_72b7b8c175dff51e
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# File: egld_staking_dapp.py
# Description: A decentralized staking dApp for EGLD tokens on MultiversX
# Features: Staking, rewards distribution, and governance participation

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
import hashlib
import json

class StakingStatus(Enum):
    ACTIVE = "ACTIVE"
    UNSTAKING = "UNSTAKING"
    COMPLETED = "COMPLETED"

@dataclass
class Stake:
    user_address: str
    amount: float
    timestamp: datetime
    status: StakingStatus
    unlock_timestamp: Optional[datetime] = None

@dataclass
class GovernanceProposal:
    id: str
    title: str
    description: str
    votes_for: int = 0
    votes_against: int = 0
    voting_end: datetime = None

class EGLDStakingDApp:
    def __init__(self):
        self.stakes: Dict[str, List[Stake]] = {}  # user_address: list of stakes
        self.total_staked: float = 0.0
        self.proposals: Dict[str, GovernanceProposal] = {}
        self.reward_rate: float = 0.05  # 5% annual reward rate
        self.unstaking_period: timedelta = timedelta(days=14)
    
    def stake_egld(self, user_address: str, amount: float) -> bool:
        """Stake EGLD tokens into the contract"""
        if amount <= 0:
            raise ValueError("Stake amount must be positive")
        
        stake = Stake(
            user_address=user_address,
            amount=amount,
            timestamp=datetime.now(),
            status=StakingStatus.ACTIVE
        )
        
        if user_address not in self.stakes:
            self.stakes[user_address] = []
        
        self.stakes[user_address].append(stake)
        self.total_staked += amount
        return True
    
    def unstake_egld(self, user_address: str, stake_index: int) -> bool:
        """Initiate unstaking process for a stake"""
        if user_address not in self.stakes or stake_index >= len(self.stakes[user_address]):
            raise ValueError("Invalid stake reference")
        
        stake = self.stakes[user_address][stake_index]
        if stake.status != StakingStatus.ACTIVE:
            raise ValueError("Stake is not active")
        
        stake.status = StakingStatus.UNSTAKING
        stake.unlock_timestamp = datetime.now() + self.unstaking_period
        return True
    
    def claim_stake(self, user_address: str, stake_index: int) -> bool:
        """Claim unstaked EGLD after cooldown period"""
        if user_address not in self.stakes or stake_index >= len(self.stakes[user_address]):
            raise ValueError("Invalid stake reference")
        
        stake = self.stakes[user_address][stake_index]
        if stake.status != StakingStatus.UNSTAKING:
            raise ValueError("Stake is not in unstaking process")
        
        if datetime.now() < stake.unlock_timestamp:
            raise ValueError("Unstaking period not completed")
        
        stake.status = StakingStatus.COMPLETED
        self.total_staked -= stake.amount
        return True
    
    def calculate_rewards(self, user_address: str) -> float:
        """Calculate pending rewards for a user"""
        if user_address not in self.stakes:
            return 0.0
        
        total_rewards = 0.0
        current_time = datetime.now()
        
        for stake in self.stakes[user_address]:
            if stake.status == StakingStatus.ACTIVE:
                staking_duration = (current_time - stake.timestamp).days / 365
                total_rewards += stake.amount * self.reward_rate * staking_duration
        
        return total_rewards
    
    def claim_rewards(self, user_address: str) -> float:
        """Claim all pending rewards"""
        rewards = self.calculate_rewards(user_address)
        
        # Reset staking timestamps to now to prevent double claiming
        if user_address in self.stakes:
            for stake in self.stakes[user_address]:
                if stake.status == StakingStatus.ACTIVE:
                    stake.timestamp = datetime.now()
        
        return rewards
    
    def create_proposal(self, title: str, description: str) -> str:
        """Create a new governance proposal"""
        proposal_id = hashlib.sha256(f"{title}{description}{datetime.now()}".encode()).hexdigest()[:16]
        self.proposals[proposal_id] = GovernanceProposal(
            id=proposal_id,
            title=title,
            description=description,
            voting_end=datetime.now() + timedelta(days=7)
        )
        return proposal_id
    
    def vote_on_proposal(self, user_address: str, proposal_id: str, vote_for: bool) -> bool:
        """Cast a vote on a governance proposal"""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        
        if datetime.now() > self.proposals[proposal_id].voting_end:
            raise ValueError("Voting period has ended")
        
        # Voting power is proportional to staked amount
        voting_power = sum(
            stake.amount for stake in self.stakes.get(user_address, [])
            if stake.status == StakingStatus.ACTIVE
        )
        
        if vote_for:
            self.proposals[proposal_id].votes_for += voting_power
        else:
            self.proposals[proposal_id].votes_against += voting_power
        
        return True
    
    def execute_proposal(self, proposal_id: str) -> bool:
        """Execute a proposal if voting passed"""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        
        proposal = self.proposals[proposal_id]
        
        if datetime.now() < proposal.voting_end:
            raise ValueError("Voting period not ended")
        
        if proposal.votes_for > proposal.votes_against:
            # Proposal passed - implement changes
            del self.proposals[proposal_id]
            return True
        
        return False
    
    def to_json(self) -> str:
        """Serialize contract state to JSON"""
        state = {
            "stakes": {
                user: [
                    {
                        "user_address": stake.user_address,
                        "amount": stake.amount,
                        "timestamp": stake.timestamp.isoformat(),
                        "status": stake.status.value,
                        "unlock_timestamp": stake.unlock_timestamp.isoformat() if stake.unlock_timestamp else None
                    }
                    for stake in stakes
                ]
                for user, stakes in self.stakes.items()
            },
            "total_staked": self.total_staked,
            "proposals": {
                pid: {
                    "id": prop.id,
                    "title": prop.title,
                    "description": prop.description,
                    "votes_for": prop.votes_for,
                    "votes_against": prop.votes_against,
                    "voting_end": prop.voting_end.isoformat()
                }
                for pid, prop in self.proposals.items()
            },
            "reward_rate": self.reward_rate,
            "unstaking_period_days": self.unstaking_period.days
        }
        return json.dumps(state)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'EGLDStakingDApp':
        """Deserialize contract state from JSON"""
        state = json.loads(json_str)
        dapp = cls()
        dapp.total_staked = state["total_staked"]
        dapp.reward_rate = state["reward_rate"]
        dapp.unstaking_period = timedelta(days=state["unstaking_period_days"])
        
        for user, stakes in state["stakes"].items():
            dapp.stakes[user] = []
            for stake_data in stakes:
                stake = Stake(
                    user_address=stake_data["user_address"],
                    amount=stake_data["amount"],
                    timestamp=datetime.fromisoformat(stake_data["timestamp"]),
                    status=StakingStatus(stake_data["status"]),
                    unlock_timestamp=datetime.fromisoformat(stake_data["unlock_timestamp"]) if stake_data["unlock_timestamp"] else None
                )
                dapp.stakes[user].append(stake)
        
        for pid, prop_data in state["proposals"].items():
            proposal = GovernanceProposal(
                id=prop_data["id"],
                title=prop_data["title"],
                description=prop_data["description"],
                votes_for=prop_data["votes_for"],
                votes_against=prop_data["votes_against"],
                voting_end=datetime.fromisoformat(prop_data["voting_end"])
            )
            dapp.proposals[pid] = proposal
        
        return dapp
```
