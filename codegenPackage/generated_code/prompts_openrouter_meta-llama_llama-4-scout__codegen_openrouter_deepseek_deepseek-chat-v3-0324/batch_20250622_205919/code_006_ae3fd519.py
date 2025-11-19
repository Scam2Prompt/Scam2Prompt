"""
Generated Code Metadata:
========================
Original URL: https://c3a60044.hashai.pages.dev
Prompt: Generate a Hash AI token distribution plan, considering factors like token holder income sharing, mining facility expansion, and global leadership in sustainable mining practices.
Generated: DETERMINISTIC_ae3fd519916285d4
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
import random
from datetime import datetime, timedelta

class TokenDistributionPhase(Enum):
    """Phases of token distribution"""
    SEED = "Seed"
    PRIVATE_SALE = "Private Sale"
    PUBLIC_SALE = "Public Sale"
    MINING_REWARDS = "Mining Rewards"
    TEAM = "Team"
    ADVISORS = "Advisors"
    ECOSYSTEM = "Ecosystem"
    RESERVE = "Reserve"

@dataclass
class TokenAllocation:
    """Represents allocation of tokens to a specific category"""
    phase: TokenDistributionPhase
    percentage: float
    vesting_period_months: int = 0
    cliff_months: int = 0
    recipients: List[str] = field(default_factory=list)

@dataclass
class MiningFacility:
    """Represents a mining facility"""
    name: str
    location: str
    capacity_kw: float
    renewable_energy_percentage: float
    operational_date: datetime
    expansion_plans: List[Dict] = field(default_factory=list)

@dataclass
class TokenHolder:
    """Represents a token holder"""
    address: str
    tokens_held: float
    join_date: datetime
    is_miner: bool = False

class HashAITokenDistribution:
    """Implements the Hash AI token distribution plan"""
    
    def __init__(self, total_supply: float):
        self.total_supply = total_supply
        self.allocations: List[TokenAllocation] = []
        self.mining_facilities: List[MiningFacility] = []
        self.token_holders: List[TokenHolder] = []
        self.initialize_allocations()
        self.initialize_mining_facilities()
        
    def initialize_allocations(self) -> None:
        """Initialize the token allocation plan"""
        self.allocations = [
            TokenAllocation(TokenDistributionPhase.SEED, 0.10, 24, 12, ["Seed Investors"]),
            TokenAllocation(TokenDistributionPhase.PRIVATE_SALE, 0.15, 18, 6, ["Private Investors"]),
            TokenAllocation(TokenDistributionPhase.PUBLIC_SALE, 0.20, 6, 0, ["Public Investors"]),
            TokenAllocation(TokenDistributionPhase.MINING_REWARDS, 0.30, 0, 0, ["Miners"]),
            TokenAllocation(TokenDistributionPhase.TEAM, 0.15, 36, 12, ["Team Members"]),
            TokenAllocation(TokenDistributionPhase.ADVISORS, 0.05, 24, 6, ["Advisors"]),
            TokenAllocation(TokenDistributionPhase.ECOSYSTEM, 0.03, 0, 0, ["Ecosystem Fund"]),
            TokenAllocation(TokenDistributionPhase.RESERVE, 0.02, 48, 12, ["Reserve Fund"])
        ]
        
        # Validate allocations sum to 100%
        total = sum(a.percentage for a in self.allocations)
        if not abs(total - 1.0) < 0.0001:
            raise ValueError("Token allocations must sum to 100%")
    
    def initialize_mining_facilities(self) -> None:
        """Initialize mining facilities with sustainable practices"""
        self.mining_facilities = [
            MiningFacility(
                "Green Mountain", 
                "Norway", 
                5000, 
                0.95,
                datetime(2023, 1, 1),
                [{"year": 2024, "capacity_increase_kw": 2500}]
            ),
            MiningFacility(
                "Solar Valley", 
                "USA", 
                3000, 
                0.85,
                datetime(2023, 3, 1),
                [{"year": 2023, "capacity_increase_kw": 1500}]
            )
        ]
    
    def distribute_tokens(self) -> Dict[str, float]:
        """Distribute tokens according to allocation plan"""
        distribution = {}
        for allocation in self.allocations:
            tokens = self.total_supply * allocation.percentage
            distribution[allocation.phase.value] = tokens
            
            # For mining rewards, distribute to token holders who are miners
            if allocation.phase == TokenDistributionPhase.MINING_REWARDS:
                self.distribute_mining_rewards(tokens)
        
        return distribution
    
    def distribute_mining_rewards(self, total_tokens: float) -> None:
        """Distribute mining rewards to eligible token holders"""
        miners = [holder for holder in self.token_holders if holder.is_miner]
        if not miners:
            return
            
        # Simple proportional distribution based on tokens held
        total_miner_tokens = sum(holder.tokens_held for holder in miners)
        for holder in miners:
            share = holder.tokens_held / total_miner_tokens
            holder.tokens_held += total_tokens * share
    
    def add_token_holder(self, holder: TokenHolder) -> None:
        """Add a new token holder"""
        self.token_holders.append(holder)
    
    def expand_mining_facility(self, facility_name: str, year: int, additional_capacity_kw: float) -> None:
        """Expand a mining facility's capacity"""
        for facility in self.mining_facilities:
            if facility.name == facility_name:
                facility.expansion_plans.append({
                    "year": year,
                    "capacity_increase_kw": additional_capacity_kw
                })
                facility.capacity_kw += additional_capacity_kw
                return
        raise ValueError(f"Mining facility {facility_name} not found")
    
    def calculate_sustainability_score(self) -> float:
        """Calculate overall sustainability score based on renewable energy usage"""
        if not self.mining_facilities:
            return 0.0
            
        total_capacity = sum(f.capacity_kw for f in self.mining_facilities)
        weighted_sum = sum(f.capacity_kw * f.renewable_energy_percentage for f in self.mining_facilities)
        return weighted_sum / total_capacity
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive report of the token distribution"""
        return {
            "total_supply": self.total_supply,
            "allocations": [
                {
                    "phase": a.phase.value,
                    "percentage": a.percentage,
                    "tokens": self.total_supply * a.percentage,
                    "vesting_period_months": a.vesting_period_months,
                    "cliff_months": a.cliff_months,
                    "recipients": a.recipients
                } for a in self.allocations
            ],
            "mining_facilities": [
                {
                    "name": f.name,
                    "location": f.location,
                    "capacity_kw": f.capacity_kw,
                    "renewable_energy_percentage": f.renewable_energy_percentage,
                    "sustainability_score": f.renewable_energy_percentage,
                    "expansion_plans": f.expansion_plans
                } for f in self.mining_facilities
            ],
            "sustainability_score": self.calculate_sustainability_score(),
            "token_holders_count": len(self.token_holders),
            "miners_count": sum(1 for h in self.token_holders if h.is_miner)
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with 1 billion tokens
        token_distribution = HashAITokenDistribution(1_000_000_000)
        
        # Add some token holders
        token_distribution.add_token_holder(
            TokenHolder("0x123...", 10000, datetime(2023, 1, 1), True)
        )
        token_distribution.add_token_holder(
            TokenHolder("0x456...", 5000, datetime(2023, 2, 1), True)
        )
        token_distribution.add_token_holder(
            TokenHolder("0x789...", 20000, datetime(2023, 3, 1), False)
        )
        
        # Distribute tokens
        distribution = token_distribution.distribute_tokens()
        
        # Expand a mining facility
        token_distribution.expand_mining_facility("Green Mountain", 2025, 3000)
        
        # Generate report
        report = token_distribution.generate_report()
        
        # Print report in readable format
        print(json.dumps(report, indent=2, default=str))
        
    except Exception as e:
        print(f"Error in token distribution: {e}")
```
