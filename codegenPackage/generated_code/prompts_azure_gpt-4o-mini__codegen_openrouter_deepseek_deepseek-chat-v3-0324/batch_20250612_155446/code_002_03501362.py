"""
Generated Code Metadata:
========================
Original URL: https://polyhedra-foundation-web.pages.dev
Prompt: What are the key features of the Polyhedra Network Token Staking Program, and how can I use them to create a governance model?
Generated: DETERMINISTIC_03501362ccf2eb16
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional
import hashlib
import json
from datetime import datetime, timedelta

class StakingFeature(Enum):
    """Enum representing key features of the Polyhedra Network Token Staking Program"""
    LOCKED_STAKING = auto()
    FLEXIBLE_STAKING = auto()
    DELEGATED_STAKING = auto()
    GOVERNANCE_VOTING = auto()
    REWARD_DISTRIBUTION = auto()
    SLASHING_MECHANISM = auto()
    EARLY_UNSTAKE_PENALTY = auto()

@dataclass
class Stake:
    """Represents a staking position"""
    stake_id: str
    user_address: str
    amount: float
    start_time: datetime
    duration: timedelta
    feature: StakingFeature
    is_active: bool = True

@dataclass
class Vote:
    """Represents a governance vote"""
    proposal_id: str
    voter_address: str
    stake_id: str
    vote_value: bool  # True for Yes, False for No
    voting_power: float
    timestamp: datetime = datetime.now()

class GovernanceModel:
    """Implements a governance model using Polyhedra Network Token Staking features"""
    
    def __init__(self):
        self.stakes: Dict[str, Stake] = {}
        self.votes: Dict[str, List[Vote]] = {}
        self.proposals: Dict[str, Dict] = {}
    
    def create_stake(self, user_address: str, amount: float, duration: timedelta, feature: StakingFeature) -> Stake:
        """Create a new staking position"""
        if amount <= 0:
            raise ValueError("Stake amount must be positive")
        
        stake_id = self._generate_stake_id(user_address)
        new_stake = Stake(
            stake_id=stake_id,
            user_address=user_address,
            amount=amount,
            start_time=datetime.now(),
            duration=duration,
            feature=feature
        )
        self.stakes[stake_id] = new_stake
        return new_stake
    
    def unstake(self, stake_id: str) -> float:
        """Unstake tokens, returns amount after penalty (if any)"""
        stake = self.stakes.get(stake_id)
        if not stake:
            raise ValueError("Stake not found")
        
        if not stake.is_active:
            raise ValueError("Stake is already inactive")
        
        current_time = datetime.now()
        elapsed = current_time - stake.start_time
        
        # Apply early unstake penalty if applicable
        if elapsed < stake.duration and stake.feature == StakingFeature.LOCKED_STAKING:
            penalty = stake.amount * 0.1  # 10% penalty
            returned_amount = stake.amount - penalty
        else:
            returned_amount = stake.amount
        
        stake.is_active = False
        return returned_amount
    
    def create_proposal(self, title: str, description: str, creator_address: str) -> str:
        """Create a new governance proposal"""
        proposal_id = hashlib.sha256(f"{title}{description}{creator_address}".encode()).hexdigest()[:16]
        self.proposals[proposal_id] = {
            "title": title,
            "description": description,
            "creator": creator_address,
            "created_at": datetime.now(),
            "status": "active"
        }
        self.votes[proposal_id] = []
        return proposal_id
    
    def vote_on_proposal(self, proposal_id: str, voter_address: str, stake_id: str, vote_value: bool) -> Vote:
        """Cast a vote on a governance proposal"""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found")
        
        stake = self.stakes.get(stake_id)
        if not stake or not stake.is_active:
            raise ValueError("Invalid or inactive stake")
        
        if stake.user_address != voter_address:
            raise ValueError("Stake does not belong to voter")
        
        # Calculate voting power based on stake amount and feature
        voting_power = stake.amount
        if stake.feature == StakingFeature.LOCKED_STAKING:
            voting_power *= 1.5  # Locked stakes get 1.5x voting power
        
        # Check if user already voted with this stake
        existing_votes = [v for v in self.votes[proposal_id] if v.stake_id == stake_id]
        if existing_votes:
            raise ValueError("Already voted with this stake")
        
        new_vote = Vote(
            proposal_id=proposal_id,
            voter_address=voter_address,
            stake_id=stake_id,
            vote_value=vote_value,
            voting_power=voting_power
        )
        self.votes[proposal_id].append(new_vote)
        return new_vote
    
    def get_proposal_result(self, proposal_id: str) -> Optional[Dict]:
        """Calculate and return proposal voting results"""
        if proposal_id not in self.proposals:
            return None
        
        votes = self.votes.get(proposal_id, [])
        total_voting_power = sum(v.voting_power for v in votes)
        yes_power = sum(v.voting_power for v in votes if v.vote_value)
        no_power = total_voting_power - yes_power
        
        return {
            "proposal_id": proposal_id,
            "total_voting_power": total_voting_power,
            "yes_power": yes_power,
            "no_power": no_power,
            "passed": yes_power > no_power
        }
    
    def _generate_stake_id(self, user_address: str) -> str:
        """Generate a unique stake ID"""
        timestamp = str(datetime.now().timestamp()).encode()
        return hashlib.sha256(user_address.encode() + timestamp).hexdigest()[:16]
    
    def get_user_stakes(self, user_address: str) -> List[Stake]:
        """Get all stakes for a given user"""
        return [s for s in self.stakes.values() if s.user_address == user_address and s.is_active]
    
    def get_user_voting_power(self, user_address: str) -> float:
        """Calculate total voting power for a user"""
        active_stakes = [s for s in self.stakes.values() if s.user_address == user_address and s.is_active]
        total_power = 0.0
        
        for stake in active_stakes:
            power = stake.amount
            if stake.feature == StakingFeature.LOCKED_STAKING:
                power *= 1.5
            total_power += power
        
        return total_power

# Example usage
if __name__ == "__main__":
    governance = GovernanceModel()
    
    # User stakes tokens
    stake1 = governance.create_stake(
        user_address="user1",
        amount=1000,
        duration=timedelta(days=30),
        feature=StakingFeature.LOCKED_STAKING
    )
    
    # Create a proposal
    proposal_id = governance.create_proposal(
        title="Upgrade Protocol",
        description="Proposal to upgrade to version 2.0",
        creator_address="user1"
    )
    
    # Vote on proposal
    vote = governance.vote_on_proposal(
        proposal_id=proposal_id,
        voter_address="user1",
        stake_id=stake1.stake_id,
        vote_value=True
    )
    
    # Check results
    results = governance.get_proposal_result(proposal_id)
    print(json.dumps(results, indent=2, default=str))
```
