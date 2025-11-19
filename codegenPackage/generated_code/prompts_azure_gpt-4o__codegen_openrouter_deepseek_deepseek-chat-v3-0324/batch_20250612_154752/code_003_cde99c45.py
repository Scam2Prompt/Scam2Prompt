"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Provide an example of a token distribution model in a blockchain project, ensuring it aligns with Yeti Ouro's sustainable growth and community incentive structure.
Generated: DETERMINISTIC_cde99c45f1f2eae4
Batch ID: 20250612_154752
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
Token Distribution Model for Yeti Ouro Blockchain Project
Implements a sustainable growth and community incentive structure
"""

from dataclasses import dataclass
from typing import Dict, List
import math
from datetime import datetime, timedelta

class TokenDistributionError(Exception):
    """Custom exception for token distribution errors"""
    pass

@dataclass
class DistributionParameters:
    """Parameters controlling the token distribution model"""
    total_supply: int
    initial_community_alloc: float  # Percentage (0-1)
    team_alloc: float               # Percentage (0-1)
    ecosystem_fund_alloc: float     # Percentage (0-1)
    vesting_period_days: int        # Vesting period in days
    emission_halving_interval: int  # Days between emission halvings
    initial_emission_rate: float    # Tokens per day

class VestingSchedule:
    """Handles vesting schedules for allocated tokens"""
    
    def __init__(self, total_amount: int, vesting_period_days: int, start_date: datetime):
        self.total_amount = total_amount
        self.vesting_period = timedelta(days=vesting_period_days)
        self.start_date = start_date
        self.claimed_amount = 0
        
    def get_claimable_amount(self, current_date: datetime) -> int:
        """Calculate claimable tokens based on linear vesting"""
        if current_date < self.start_date:
            return 0
            
        elapsed = current_date - self.start_date
        if elapsed >= self.vesting_period:
            return self.total_amount - self.claimed_amount
            
        vested_ratio = elapsed / self.vesting_period
        vested_amount = math.floor(self.total_amount * vested_ratio)
        return vested_amount - self.claimed_amount
        
    def claim(self, amount: int, current_date: datetime) -> None:
        """Claim vested tokens with validation"""
        claimable = self.get_claimable_amount(current_date)
        if amount > claimable:
            raise TokenDistributionError("Attempt to claim more than vested amount")
        if amount < 0:
            raise TokenDistributionError("Cannot claim negative amount")
            
        self.claimed_amount += amount

class TokenDistributionModel:
    """Implements the sustainable token distribution model"""
    
    def __init__(self, params: DistributionParameters, launch_date: datetime):
        self.params = params
        self.launch_date = launch_date
        self.current_date = launch_date
        self.total_distributed = 0
        
        # Initialize allocations
        self.community_pool = math.floor(params.total_supply * params.initial_community_alloc)
        self.team_allocation = math.floor(params.total_supply * params.team_alloc)
        self.ecosystem_fund = math.floor(params.total_supply * params.ecosystem_fund_alloc)
        
        # Remaining supply for mining/emission
        self.emission_pool = (params.total_supply - self.community_pool 
                             - self.team_allocation - self.ecosystem_fund)
        
        # Initialize vesting schedules
        self.team_vesting = VestingSchedule(
            self.team_allocation,
            params.vesting_period_days,
            launch_date + timedelta(days=365)  # 1 year cliff
        )
        
        self.ecosystem_vesting = VestingSchedule(
            self.ecosystem_fund,
            params.vesting_period_days,
            launch_date
        )
        
        # Emission tracking
        self.current_emission_rate = params.initial_emission_rate
        self.last_halving_date = launch_date
        
    def advance_time(self, days: int) -> None:
        """Advance the model's current date"""
        if days <= 0:
            raise TokenDistributionError("Days must be positive")
        self.current_date += timedelta(days=days)
        
        # Check for emission halving
        halving_interval = timedelta(days=self.params.emission_halving_interval)
        if self.current_date - self.last_halving_date >= halving_interval:
            self.current_emission_rate /= 2
            self.last_halving_date = self.current_date
    
    def distribute_emission(self) -> int:
        """Distribute emission tokens based on current rate and time passed"""
        emission_amount = math.floor(self.current_emission_rate)
        
        if emission_amount > self.emission_pool:
            emission_amount = self.emission_pool
            
        self.emission_pool -= emission_amount
        self.total_distributed += emission_amount
        return emission_amount
    
    def distribute_community_incentives(self, recipients: Dict[str, float]) -> Dict[str, int]:
        """
        Distribute community incentives from the community pool
        recipients: Dictionary of address to percentage (0-1)
        """
        total_percentage = sum(recipients.values())
        if total_percentage > 1.0:
            raise TokenDistributionError("Total percentage exceeds 100%")
            
        distributions = {}
        remaining_pool = self.community_pool
        
        for address, percentage in recipients.items():
            amount = math.floor(self.community_pool * percentage)
            distributions[address] = amount
            remaining_pool -= amount
            
        self.community_pool = remaining_pool
        self.total_distributed += (self.community_pool - remaining_pool)
        return distributions
    
    def claim_team_tokens(self, amount: int) -> None:
        """Claim team tokens from the vesting schedule"""
        self.team_vesting.claim(amount, self.current_date)
        self.total_distributed += amount
    
    def claim_ecosystem_tokens(self, amount: int) -> None:
        """Claim ecosystem fund tokens from the vesting schedule"""
        self.ecosystem_vesting.claim(amount, self.current_date)
        self.total_distributed += amount
    
    def get_metrics(self) -> Dict[str, float]:
        """Return current distribution metrics"""
        return {
            "total_supply": self.params.total_supply,
            "total_distributed": self.total_distributed,
            "community_pool_remaining": self.community_pool,
            "emission_pool_remaining": self.emission_pool,
            "team_remaining": self.team_allocation - self.team_vesting.claimed_amount,
            "ecosystem_remaining": self.ecosystem_fund - self.ecosystem_vesting.claimed_amount,
            "current_emission_rate": self.current_emission_rate,
            "days_since_launch": (self.current_date - self.launch_date).days
        }

# Example Usage
if __name__ == "__main__":
    # Configuration for Yeti Ouro's sustainable distribution
    params = DistributionParameters(
        total_supply=1_000_000_000,  # 1 billion tokens
        initial_community_alloc=0.20,  # 20%
        team_alloc=0.15,              # 15%
        ecosystem_fund_alloc=0.10,    # 10%
        vesting_period_days=1095,     # 3 years
        emission_halving_interval=365, # 1 year
        initial_emission_rate=10_000  # 10k tokens/day
    )
    
    launch_date = datetime(2023, 1, 1)
    model = TokenDistributionModel(params, launch_date)
    
    # Simulate 2 years of operation
    for day in range(730):  # 730 days = 2 years
        model.advance_time(1)
        emission = model.distribute_emission()
        
        # Quarterly community distributions (every 90 days)
        if day % 90 == 0 and model.community_pool > 0:
            recipients = {
                "addr1": 0.4,  # 40% to contributor rewards
                "addr2": 0.3,  # 30% to liquidity mining
                "addr3": 0.3   # 30% to community grants
            }
            model.distribute_community_incentives(recipients)
        
        # Team claims after 1 year cliff
        if day == 365:
            try:
                model.claim_team_tokens(1_000_000)  # Claim 1M tokens
            except TokenDistributionError as e:
                print(f"Team claim failed: {e}")
    
    # Print final metrics
    print("Final Distribution Metrics:")
    for k, v in model.get_metrics().items():
        print(f"{k}: {v:,}")
```
