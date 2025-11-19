"""
Generated Code Metadata:
========================
Original URL: https://hellohosting.pages.dev
Prompt: Design a data model to track the performance milestones and contest rules for the Wealth Coin (WEL) incentive plan, including fields for market capitalization targets, estimated price/share, and total coins in each wallet.
Generated: DETERMINISTIC_3efde5e690171808
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from enum import Enum, auto

class MilestoneStatus(Enum):
    PENDING = auto()
    ACTIVE = auto()
    COMPLETED = auto()
    FAILED = auto()

@dataclass
class Wallet:
    address: str
    total_coins: float
    owner: str
    is_team_wallet: bool
    creation_date: datetime
    last_updated: datetime

@dataclass
class ContestRule:
    rule_id: str
    description: str
    start_date: datetime
    end_date: datetime
    target_market_cap: float
    required_min_holding: float
    reward_percentage: float
    is_active: bool

@dataclass
class PerformanceMilestone:
    milestone_id: str
    name: str
    description: str
    target_market_cap: float
    estimated_price_per_coin: float
    start_date: datetime
    end_date: datetime
    status: MilestoneStatus
    wallets: List[Wallet]
    contest_rules: List[ContestRule]

@dataclass
class WealthCoinIncentivePlan:
    plan_id: str
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    total_coins_allocated: float
    milestones: List[PerformanceMilestone]
    
    def get_active_milestones(self) -> List[PerformanceMilestone]:
        return [m for m in self.milestones if m.status == MilestoneStatus.ACTIVE]
    
    def get_completed_milestones(self) -> List[PerformanceMilestone]:
        return [m for m in self.milestones if m.status == MilestoneStatus.COMPLETED]
    
    def get_wallet_by_address(self, address: str) -> Optional[Wallet]:
        for milestone in self.milestones:
            for wallet in milestone.wallets:
                if wallet.address == address:
                    return wallet
        return None
    
    def validate_milestone_dates(self) -> bool:
        for milestone in self.milestones:
            if milestone.start_date > milestone.end_date:
                return False
            if milestone.start_date < self.start_date or milestone.end_date > self.end_date:
                return False
        return True
    
    def add_milestone(self, milestone: PerformanceMilestone) -> bool:
        if not self.validate_milestone_dates():
            return False
        self.milestones.append(milestone)
        return True
```
