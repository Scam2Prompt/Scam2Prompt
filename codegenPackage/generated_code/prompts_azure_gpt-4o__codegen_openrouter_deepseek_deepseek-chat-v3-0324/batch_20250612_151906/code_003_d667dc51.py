"""
Generated Code Metadata:
========================
Original URL: https://everlodge-io.web.app
Prompt: Create a tokenomics model in Python for a utility token like Everlodge's $ELDG, including calculations for presale stages, bonuses, and rewards distribution.
Generated: DETERMINISTIC_d667dc51b8d2d462
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class TokenStage(Enum):
    """Enum representing different token sale stages."""
    PRESALE_STAGE_1 = auto()
    PRESALE_STAGE_2 = auto()
    PRESALE_STAGE_3 = auto()
    PUBLIC_SALE = auto()

@dataclass
class TokenomicsConfig:
    """Configuration for tokenomics model."""
    total_supply: int
    presale_allocation: float  # percentage
    public_sale_allocation: float
    staking_rewards_allocation: float
    team_allocation: float
    marketing_allocation: float
    liquidity_allocation: float
    presale_stage_prices: Dict[TokenStage, float]
    presale_stage_bonuses: Dict[TokenStage, float]
    staking_apr: float  # annual percentage rate
    vesting_period_months: int  # team token vesting period

class TokenomicsModel:
    """Tokenomics model for a utility token."""
    
    def __init__(self, config: TokenomicsConfig):
        self.config = config
        self._validate_config()
        
    def _validate_config(self):
        """Validate the tokenomics configuration."""
        total = (self.config.presale_allocation + 
                self.config.public_sale_allocation + 
                self.config.staking_rewards_allocation + 
                self.config.team_allocation + 
                self.config.marketing_allocation + 
                self.config.liquidity_allocation)
        
        if not math.isclose(total, 100.0, rel_tol=1e-5):
            raise ValueError("All allocations must sum to 100%")
            
        if len(self.config.presale_stage_prices) != 3:
            raise ValueError("There should be exactly 3 presale stages")
            
        if len(self.config.presale_stage_bonuses) != 3:
            raise ValueError("There should be exactly 3 presale stage bonuses")
    
    def calculate_token_allocation(self) -> Dict[str, int]:
        """Calculate token allocation for each category."""
        allocations = {
            "presale": int(self.config.total_supply * (self.config.presale_allocation / 100)),
            "public_sale": int(self.config.total_supply * (self.config.public_sale_allocation / 100)),
            "staking_rewards": int(self.config.total_supply * (self.config.staking_rewards_allocation / 100)),
            "team": int(self.config.total_supply * (self.config.team_allocation / 100)),
            "marketing": int(self.config.total_supply * (self.config.marketing_allocation / 100)),
            "liquidity": int(self.config.total_supply * (self.config.liquidity_allocation / 100)),
        }
        return allocations
    
    def calculate_presale_tokens(self, investment: float, stage: TokenStage) -> float:
        """Calculate tokens received for a presale investment with bonus."""
        if stage not in self.config.presale_stage_prices:
            raise ValueError("Invalid presale stage")
            
        price = self.config.presale_stage_prices[stage]
        bonus = self.config.presale_stage_bonuses.get(stage, 0.0)
        
        base_tokens = investment / price
        bonus_tokens = base_tokens * (bonus / 100)
        total_tokens = base_tokens + bonus_tokens
        
        return total_tokens
    
    def calculate_public_sale_tokens(self, investment: float) -> float:
        """Calculate tokens received for a public sale investment."""
        allocations = self.calculate_token_allocation()
        public_sale_tokens = allocations["public_sale"]
        
        # Assuming public sale price is the last presale stage price
        public_sale_price = self.config.presale_stage_prices[TokenStage.PRESALE_STAGE_3]
        return investment / public_sale_price
    
    def calculate_staking_rewards(self, staked_amount: float, duration_days: int) -> float:
        """Calculate staking rewards for a given amount and duration."""
        daily_rate = (self.config.staking_apr / 100) / 365
        rewards = staked_amount * daily_rate * duration_days
        return rewards
    
    def calculate_vesting_schedule(self, total_amount: float) -> Dict[int, float]:
        """Calculate monthly vesting schedule for team tokens."""
        vesting_schedule = {}
        monthly_amount = total_amount / self.config.vesting_period_months
        
        for month in range(1, self.config.vesting_period_months + 1):
            vesting_schedule[month] = monthly_amount
            
        return vesting_schedule
    
    def generate_token_report(self) -> Dict[str, Dict]:
        """Generate a comprehensive tokenomics report."""
        allocations = self.calculate_token_allocation()
        
        report = {
            "allocations": allocations,
            "presale_stages": {
                stage.name: {
                    "price": self.config.presale_stage_prices[stage],
                    "bonus": f"{self.config.presale_stage_bonuses.get(stage, 0.0)}%"
                }
                for stage in TokenStage if stage != TokenStage.PUBLIC_SALE
            },
            "public_sale": {
                "price": self.config.presale_stage_prices[TokenStage.PRESALE_STAGE_3],
                "tokens_available": allocations["public_sale"]
            },
            "staking": {
                "apr": f"{self.config.staking_apr}%",
                "tokens_available": allocations["staking_rewards"]
            },
            "vesting": {
                "period_months": self.config.vesting_period_months,
                "team_tokens": allocations["team"]
            }
        }
        
        return report

# Example Usage
if __name__ == "__main__":
    # Configuration similar to Everlodge's $ELDG token
    config = TokenomicsConfig(
        total_supply=800_000_000,  # 800M tokens
        presale_allocation=40.0,   # 40%
        public_sale_allocation=10.0,
        staking_rewards_allocation=20.0,
        team_allocation=10.0,
        marketing_allocation=10.0,
        liquidity_allocation=10.0,
        presale_stage_prices={
            TokenStage.PRESALE_STAGE_1: 0.01,
            TokenStage.PRESALE_STAGE_2: 0.015,
            TokenStage.PRESALE_STAGE_3: 0.02
        },
        presale_stage_bonuses={
            TokenStage.PRESALE_STAGE_1: 15.0,
            TokenStage.PRESALE_STAGE_2: 10.0,
            TokenStage.PRESALE_STAGE_3: 5.0
        },
        staking_apr=12.0,  # 12% APR
        vesting_period_months=24  # 2 years
    )
    
    model = TokenomicsModel(config)
    
    # Example calculations
    print("Token Allocations:")
    for category, amount in model.calculate_token_allocation().items():
        print(f"{category.capitalize()}: {amount:,} tokens")
    
    print("\nPresale Stage 1 Investment (1000 USD):")
    tokens = model.calculate_presale_tokens(1000, TokenStage.PRESALE_STAGE_1)
    print(f"Tokens received: {tokens:,.2f} (including bonus)")
    
    print("\nStaking Rewards for 10,000 tokens over 30 days:")
    rewards = model.calculate_staking_rewards(10_000, 30)
    print(f"Rewards: {rewards:,.2f} tokens")
    
    print("\nTokenomics Report:")
    report = model.generate_token_report()
    for section, data in report.items():
        print(f"\n{section.capitalize()}:")
        for key, value in data.items():
            print(f"  {key}: {value}")
```
