"""
Generated Code Metadata:
========================
Original URL: https://blastup-en.pages.dev
Prompt: "Design a tokenomics model for a new project launching on BlastUP, incorporating the platform's tiered IDO launch system and token buy-back mechanism."
Generated: DETERMINISTIC_03fca1f2b4caf8db
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics Model for BlastUP IDO Project

from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum, auto
import math

class Tier(Enum):
    """IDO Participation Tiers"""
    TIER1 = auto()  # Lowest tier
    TIER2 = auto()
    TIER3 = auto()
    TIER4 = auto()  # Highest tier

@dataclass
class TokenAllocation:
    """Token allocation percentages"""
    public_sale: float
    team: float
    advisors: float
    marketing: float
    ecosystem: float
    liquidity: float
    reserve: float

@dataclass
class VestingSchedule:
    """Token vesting schedule"""
    cliff_months: int
    vesting_period_months: int
    initial_unlock: float  # Percentage

@dataclass
class TierDetails:
    """Details for each IDO tier"""
    allocation_percentage: float
    min_contribution: float
    max_contribution: float
    token_price: float

class TokenomicsModel:
    """Implements tokenomics model for BlastUP IDO projects"""
    
    def __init__(
        self,
        total_supply: int,
        token_allocations: TokenAllocation,
        vesting_schedule: VestingSchedule,
        buyback_percentage: float = 0.05,
        buyback_frequency_days: int = 30
    ):
        """
        Initialize tokenomics model
        
        Args:
            total_supply: Total token supply
            token_allocations: Token allocation percentages
            vesting_schedule: Vesting schedule details
            buyback_percentage: Percentage of revenue for buybacks
            buyback_frequency_days: Frequency of buyback operations
        """
        self.total_supply = total_supply
        self.token_allocations = token_allocations
        self.vesting_schedule = vesting_schedule
        self.buyback_percentage = buyback_percentage
        self.buyback_frequency_days = buyback_frequency_days
        self._validate_allocations()
        
        # Initialize tier details
        self.tiers: Dict[Tier, TierDetails] = {
            Tier.TIER1: TierDetails(0.1, 100.0, 500.0, 0.10),
            Tier.TIER2: TierDetails(0.2, 500.0, 2000.0, 0.12),
            Tier.TIER3: TierDetails(0.3, 2000.0, 5000.0, 0.15),
            Tier.TIER4: TierDetails(0.4, 5000.0, 20000.0, 0.18)
        }
        
    def _validate_allocations(self) -> None:
        """Validate that token allocations sum to 100%"""
        total = sum([
            self.token_allocations.public_sale,
            self.token_allocations.team,
            self.token_allocations.advisors,
            self.token_allocations.marketing,
            self.token_allocations.ecosystem,
            self.token_allocations.liquidity,
            self.token_allocations.reserve
        ])
        
        if not math.isclose(total, 100.0, rel_tol=1e-5):
            raise ValueError("Token allocations must sum to 100%")
    
    def calculate_allocation_amounts(self) -> Dict[str, int]:
        """Calculate actual token amounts for each allocation"""
        return {
            "public_sale": int(self.total_supply * self.token_allocations.public_sale / 100),
            "team": int(self.total_supply * self.token_allocations.team / 100),
            "advisors": int(self.total_supply * self.token_allocations.advisors / 100),
            "marketing": int(self.total_supply * self.token_allocations.marketing / 100),
            "ecosystem": int(self.total_supply * self.token_allocations.ecosystem / 100),
            "liquidity": int(self.total_supply * self.token_allocations.liquidity / 100),
            "reserve": int(self.total_supply * self.token_allocations.reserve / 100)
        }
    
    def calculate_vested_tokens(self, allocation: str, months_passed: int) -> int:
        """
        Calculate vested tokens for a given allocation
        
        Args:
            allocation: Allocation category (team, advisors, etc.)
            months_passed: Number of months since token launch
            
        Returns:
            Number of tokens vested
        """
        allocation_amount = getattr(self.token_allocations, allocation) * self.total_supply / 100
        
        if months_passed < self.vesting_schedule.cliff_months:
            return 0
        
        vested_months = min(
            months_passed - self.vesting_schedule.cliff_months,
            self.vesting_schedule.vesting_period_months
        )
        
        vested_percentage = self.vesting_schedule.initial_unlock + (
            vested_months / self.vesting_schedule.vesting_period_months * 
            (100 - self.vesting_schedule.initial_unlock)
        ) / 100
        
        return int(allocation_amount * vested_percentage)
    
    def calculate_buyback_amount(self, revenue: float) -> float:
        """
        Calculate token buyback amount based on revenue
        
        Args:
            revenue: Project revenue in USD
            
        Returns:
            USD amount to spend on buybacks
        """
        return revenue * self.buyback_percentage
    
    def get_tier_details(self, tier: Tier) -> TierDetails:
        """
        Get details for a specific tier
        
        Args:
            tier: Tier to get details for
            
        Returns:
            TierDetails object
        """
        return self.tiers[tier]
    
    def calculate_tier_allocation(self, tier: Tier) -> int:
        """
        Calculate token allocation for a specific tier
        
        Args:
            tier: Tier to calculate allocation for
            
        Returns:
            Number of tokens allocated to this tier
        """
        public_sale_tokens = self.total_supply * self.token_allocations.public_sale / 100
        return int(public_sale_tokens * self.tiers[tier].allocation_percentage)

# Example usage
if __name__ == "__main__":
    # Initialize tokenomics model
    allocations = TokenAllocation(
        public_sale=30.0,
        team=20.0,
        advisors=5.0,
        marketing=15.0,
        ecosystem=10.0,
        liquidity=15.0,
        reserve=5.0
    )
    
    vesting = VestingSchedule(
        cliff_months=6,
        vesting_period_months=24,
        initial_unlock=10.0
    )
    
    tokenomics = TokenomicsModel(
        total_supply=100_000_000,
        token_allocations=allocations,
        vesting_schedule=vesting,
        buyback_percentage=0.05,
        buyback_frequency_days=30
    )
    
    # Print allocation amounts
    print("Token Allocations:")
    for category, amount in tokenomics.calculate_allocation_amounts().items():
        print(f"{category}: {amount:,}")
    
    # Example vesting calculation
    print("\nVested Team Tokens after 12 months:")
    print(f"{tokenomics.calculate_vested_tokens('team', 12):,}")
    
    # Example buyback calculation
    print("\nBuyback Amount for $1,000,000 revenue:")
    print(f"${tokenomics.calculate_buyback_amount(1_000_000):,.2f}")
```
