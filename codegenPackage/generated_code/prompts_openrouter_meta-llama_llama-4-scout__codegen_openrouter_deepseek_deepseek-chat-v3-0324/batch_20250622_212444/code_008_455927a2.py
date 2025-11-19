"""
Generated Code Metadata:
========================
Original URL: https://lnynperlqiud.com
Prompt: Describe the role of Hyperliquid's native token economy in facilitating protocol governance, fee voting, staking, and fee discounts for active traders.
Generated: DETERMINISTIC_455927a2302c69fb
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hyperliquid_token_economy.py

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum, auto

class GovernanceAction(Enum):
    PROPOSAL_CREATION = auto()
    PROPOSAL_VOTING = auto()
    PARAMETER_CHANGE = auto()

class FeeTier(Enum):
    TIER_1 = 0.0005  # 0.05%
    TIER_2 = 0.0003  # 0.03%
    TIER_3 = 0.0001  # 0.01%

@dataclass
class GovernanceProposal:
    id: str
    title: str
    description: str
    voting_end: int  # timestamp
    min_tokens_to_pass: int
    votes_for: int = 0
    votes_against: int = 0
    executed: bool = False

@dataclass
class User:
    address: str
    token_balance: int
    staked_tokens: int = 0
    fee_tier: FeeTier = FeeTier.TIER_1
    last_trade_timestamp: int = 0
    trade_volume_30d: float = 0.0

class HyperliquidTokenEconomy:
    def __init__(self):
        self.total_supply: int = 1_000_000_000  # 1B tokens
        self.circulating_supply: int = 700_000_000
        self.staked_tokens: int = 0
        self.proposals: Dict[str, GovernanceProposal] = {}
        self.users: Dict[str, User] = {}
        self.fee_pool: float = 0.0
        self.protocol_fee_rate: float = 0.0005  # 0.05%
    
    def stake_tokens(self, user_address: str, amount: int) -> bool:
        if user_address not in self.users:
            return False
        
        user = self.users[user_address]
        if user.token_balance < amount:
            return False
        
        user.token_balance -= amount
        user.staked_tokens += amount
        self.staked_tokens += amount
        self._update_fee_tier(user_address)
        return True
    
    def unstake_tokens(self, user_address: str, amount: int) -> bool:
        if user_address not in self.users:
            return False
        
        user = self.users[user_address]
        if user.staked_tokens < amount:
            return False
        
        user.staked_tokens -= amount
        user.token_balance += amount
        self.staked_tokens -= amount
        self._update_fee_tier(user_address)
        return True
    
    def create_proposal(self, user_address: str, title: str, description: str, voting_period: int) -> Optional[str]:
        if user_address not in self.users:
            return None
        
        user = self.users[user_address]
        if user.staked_tokens < 10_000:  # Minimum stake to create proposal
            return None
        
        proposal_id = f"prop_{len(self.proposals) + 1}"
        proposal = GovernanceProposal(
            id=proposal_id,
            title=title,
            description=description,
            voting_end=int(time.time()) + voting_period,
            min_tokens_to_pass=self.staked_tokens * 0.3  # 30% of staked tokens
        )
        self.proposals[proposal_id] = proposal
        return proposal_id
    
    def vote_on_proposal(self, user_address: str, proposal_id: str, vote_for: bool) -> bool:
        if user_address not in self.users or proposal_id not in self.proposals:
            return False
        
        user = self.users[user_address]
        proposal = self.proposals[proposal_id]
        
        if time.time() > proposal.voting_end:
            return False
        
        voting_power = user.staked_tokens
        if vote_for:
            proposal.votes_for += voting_power
        else:
            proposal.votes_against += voting_power
        
        return True
    
    def execute_proposal(self, proposal_id: str) -> bool:
        if proposal_id not in self.proposals:
            return False
        
        proposal = self.proposals[proposal_id]
        if proposal.executed or time.time() < proposal.voting_end:
            return False
        
        if proposal.votes_for >= proposal.min_tokens_to_pass:
            proposal.executed = True
            return True
        return False
    
    def record_trade(self, user_address: str, volume: float) -> None:
        if user_address not in self.users:
            return
        
        user = self.users[user_address]
        user.trade_volume_30d += volume
        user.last_trade_timestamp = int(time.time())
        self._update_fee_tier(user_address)
        
        # Collect protocol fee
        fee = volume * self.protocol_fee_rate
        self.fee_pool += fee
    
    def distribute_fee_rewards(self) -> None:
        total_staked = self.staked_tokens
        if total_staked == 0:
            return
        
        for user in self.users.values():
            if user.staked_tokens > 0:
                reward = (user.staked_tokens / total_staked) * self.fee_pool
                user.token_balance += reward
        
        self.fee_pool = 0.0
    
    def _update_fee_tier(self, user_address: str) -> None:
        user = self.users[user_address]
        
        if user.staked_tokens >= 1_000_000:
            user.fee_tier = FeeTier.TIER_3
        elif user.staked_tokens >= 100_000:
            user.fee_tier = FeeTier.TIER_2
        else:
            user.fee_tier = FeeTier.TIER_1
```
