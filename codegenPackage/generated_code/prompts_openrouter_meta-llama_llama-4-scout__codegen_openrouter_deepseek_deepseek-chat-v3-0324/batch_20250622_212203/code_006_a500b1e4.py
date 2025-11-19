"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Design a tokenomics structure for a new cryptocurrency project, aiming for sustainable growth, community participation, and long-term value for stakeholders.
Generated: DETERMINISTIC_a500b1e4d0f970dd
Batch ID: 20250622_212203
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
Tokenomics Structure Implementation

This module implements a comprehensive tokenomics model for a cryptocurrency project.
It includes mechanisms for distribution, vesting, staking rewards, and governance.
"""

from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime, timedelta
import math

class TokenomicsError(Exception):
    """Base exception for tokenomics-related errors"""
    pass

@dataclass
class VestingSchedule:
    """Represents a vesting schedule for token allocation"""
    beneficiary: str
    total_amount: float
    start_date: datetime
    cliff_duration: timedelta
    vesting_duration: timedelta
    claimed_amount: float = 0.0

    def available_tokens(self, current_date: datetime) -> float:
        """Calculate available tokens based on vesting schedule"""
        if current_date < self.start_date + self.cliff_duration:
            return 0.0
        
        elapsed = current_date - (self.start_date + self.cliff_duration)
        if elapsed.total_seconds() <= 0:
            return 0.0
            
        vested_ratio = min(elapsed / self.vesting_duration, 1.0)
        vested_amount = self.total_amount * vested_ratio
        return vested_amount - self.claimed_amount

    def claim(self, amount: float, current_date: datetime) -> None:
        """Claim vested tokens"""
        available = self.available_tokens(current_date)
        if amount > available:
            raise TokenomicsError("Attempt to claim more than available tokens")
        self.claimed_amount += amount

class TokenAllocation:
    """Manages token distribution across different categories"""
    def __init__(self, total_supply: float):
        self.total_supply = total_supply
        self.allocations: Dict[str, float] = {
            'community': 0.40 * total_supply,
            'team': 0.20 * total_supply,
            'investors': 0.15 * total_supply,
            'treasury': 0.15 * total_supply,
            'liquidity': 0.10 * total_supply
        }
        self.validate_allocations()

    def validate_allocations(self) -> None:
        """Ensure allocations sum to total supply"""
        total = sum(self.allocations.values())
        if not math.isclose(total, self.total_supply, rel_tol=1e-5):
            raise TokenomicsError("Allocations do not sum to total supply")

class StakingRewards:
    """Manages staking rewards distribution"""
    def __init__(self, reward_pool: float, annual_rate: float = 0.10):
        self.reward_pool = reward_pool
        self.annual_rate = annual_rate
        self.stakers: Dict[str, float] = {}  # address: staked_amount

    def stake(self, address: str, amount: float) -> None:
        """Stake tokens to earn rewards"""
        if amount <= 0:
            raise TokenomicsError("Stake amount must be positive")
        self.stakers[address] = self.stakers.get(address, 0.0) + amount

    def calculate_rewards(self, address: str, days_staked: int) -> float:
        """Calculate rewards for a staker"""
        staked_amount = self.stakers.get(address, 0.0)
        if staked_amount <= 0:
            return 0.0
        daily_rate = self.annual_rate / 365
        return staked_amount * daily_rate * days_staked

class Governance:
    """Handles token-based governance"""
    def __init__(self, token_holders: Dict[str, float]):
        self.token_holders = token_holders
        self.proposals: List[Dict] = []
        self.votes: Dict[int, Dict[str, bool]] = {}  # proposal_id: {voter: vote}

    def create_proposal(self, description: str) -> int:
        """Create a new governance proposal"""
        proposal_id = len(self.proposals)
        self.proposals.append({
            'id': proposal_id,
            'description': description,
            'created_at': datetime.now()
        })
        return proposal_id

    def vote(self, proposal_id: int, voter: str, support: bool) -> None:
        """Cast a vote on a proposal"""
        if proposal_id >= len(self.proposals):
            raise TokenomicsError("Invalid proposal ID")
        if voter not in self.token_holders:
            raise TokenomicsError("Only token holders can vote")
        
        if proposal_id not in self.votes:
            self.votes[proposal_id] = {}
        self.votes[proposal_id][voter] = support

    def get_voting_power(self, voter: str) -> float:
        """Get voting power based on token balance"""
        return self.token_holders.get(voter, 0.0)

class Tokenomics:
    """Comprehensive tokenomics implementation"""
    def __init__(self, total_supply: float):
        self.total_supply = total_supply
        self.allocation = TokenAllocation(total_supply)
        self.vesting_schedules: List[VestingSchedule] = []
        self.staking = StakingRewards(self.allocation.allocations['community'])
        self.governance = Governance({})

    def add_vesting_schedule(self, schedule: VestingSchedule) -> None:
        """Add a new vesting schedule"""
        self.vesting_schedules.append(schedule)

    def distribute_tokens(self, category: str, recipient: str, amount: float) -> None:
        """Distribute tokens from a specific allocation category"""
        if category not in self.allocation.allocations:
            raise TokenomicsError("Invalid allocation category")
        if amount > self.allocation.allocations[category]:
            raise TokenomicsError("Insufficient tokens in allocation")
        
        self.allocation.allocations[category] -= amount
        self.governance.token_holders[recipient] = \
            self.governance.token_holders.get(recipient, 0.0) + amount

    def burn_tokens(self, amount: float) -> None:
        """Burn tokens to reduce total supply"""
        if amount <= 0:
            raise TokenomicsError("Burn amount must be positive")
        self.total_supply -= amount

    def update_governance_participants(self) -> None:
        """Update governance participants based on current token holders"""
        self.governance = Governance(self.governance.token_holders.copy())
```
