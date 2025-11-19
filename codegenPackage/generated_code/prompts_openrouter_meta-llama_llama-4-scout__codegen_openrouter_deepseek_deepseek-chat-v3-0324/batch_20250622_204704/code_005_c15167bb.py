"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ai-presale.pages.dev
Prompt: Design a tokenomics model for a new cryptocurrency project, inspired by WienerAI's allocation strategy (30% presale, 20% staking, etc.).
Generated: DETERMINISTIC_c15167bb4381ccd5
Batch ID: 20250622_204704
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics Model for Cryptocurrency Project
import math
from dataclasses import dataclass
from typing import Dict

@dataclass
class TokenAllocation:
    """Data class representing token allocation percentages"""
    presale: float
    staking: float
    team: float
    marketing: float
    liquidity: float
    ecosystem: float
    reserve: float

class TokenomicsModel:
    """Implements tokenomics calculations based on allocation strategy"""
    
    def __init__(self, total_supply: int, allocation: TokenAllocation):
        """
        Initialize tokenomics model
        
        Args:
            total_supply: Total token supply (integer)
            allocation: TokenAllocation object with percentage distributions
        """
        self.total_supply = total_supply
        self.allocation = allocation
        self._validate_allocation()
        
    def _validate_allocation(self):
        """Validate that allocation percentages sum to 100%"""
        total = sum(vars(self.allocation).values())
        if not math.isclose(total, 100.0, rel_tol=1e-5):
            raise ValueError(f"Allocation percentages must sum to 100% (current sum: {total}%)")
    
    def calculate_distribution(self) -> Dict[str, int]:
        """
        Calculate token distribution based on allocation percentages
        
        Returns:
            Dictionary mapping allocation category to token amount
        """
        distribution = {}
        for category, percentage in vars(self.allocation).items():
            tokens = int(self.total_supply * (percentage / 100))
            distribution[category] = tokens
        
        # Adjust for rounding errors by adding remaining tokens to reserve
        distributed = sum(distribution.values())
        if distributed != self.total_supply:
            distribution['reserve'] += self.total_supply - distributed
        
        return distribution
    
    def get_vesting_schedule(self, category: str, duration_months: int, cliff_months: int = 0) -> Dict[int, int]:
        """
        Generate linear vesting schedule for a token category
        
        Args:
            category: Allocation category (e.g., 'team')
            duration_months: Total vesting duration in months
            cliff_months: Cliff period in months (no tokens released before)
            
        Returns:
            Dictionary mapping month number to tokens released
        """
        if category not in vars(self.allocation):
            raise ValueError(f"Invalid category: {category}")
            
        distribution = self.calculate_distribution()
        total_tokens = distribution[category]
        
        if cliff_months >= duration_months:
            raise ValueError("Cliff period must be shorter than vesting duration")
            
        schedule = {}
        if duration_months == 0:
            return {0: total_tokens}
            
        monthly_amount = total_tokens // (duration_months - cliff_months)
        
        for month in range(1, duration_months + 1):
            if month <= cliff_months:
                schedule[month] = 0
            else:
                remaining = total_tokens - sum(schedule.values())
                schedule[month] = min(monthly_amount, remaining)
                
        return schedule

# Example usage (WienerAI-inspired allocation)
if __name__ == "__main__":
    TOTAL_SUPPLY = 1_000_000_000  # 1 billion tokens
    
    allocation = TokenAllocation(
        presale=30.0,
        staking=20.0,
        team=15.0,
        marketing=10.0,
        liquidity=10.0,
        ecosystem=10.0,
        reserve=5.0
    )
    
    model = TokenomicsModel(TOTAL_SUPPLY, allocation)
    
    try:
        distribution = model.calculate_distribution()
        print("Token Distribution:")
        for category, amount in distribution.items():
            print(f"{category.title()}: {amount:,} tokens ({allocation.__getattribute__(category)}%)")
            
        print("\nTeam Vesting Schedule (24 months with 6 month cliff):")
        vesting = model.get_vesting_schedule('team', 24, 6)
        for month, tokens in vesting.items():
            print(f"Month {month}: {tokens:,} tokens")
            
    except ValueError as e:
        print(f"Error in tokenomics model: {e}")
```
