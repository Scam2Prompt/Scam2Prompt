"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Write code to calculate bonus interest shares for Silo Liquidity Providers based on their positions, referencing the Silo Rewards Proposal.
Generated: DETERMINISTIC_0c46ac29a5eff390
Batch ID: 20250612_150228
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
from typing import List, Dict

@dataclass
class LiquidityProvider:
    """Represents a liquidity provider in the Silo protocol."""
    address: str
    liquidity_amount: float  # Amount of liquidity provided
    duration: int           # Duration in days the liquidity was provided
    base_apr: float         # Base APR for the liquidity pool

@dataclass
class BonusTier:
    """Represents a bonus tier for liquidity providers."""
    min_duration: int       # Minimum duration in days to qualify
    multiplier: float       # Bonus multiplier for this tier

class SiloRewardsCalculator:
    """
    Calculates bonus interest shares for Silo Liquidity Providers
    based on the Silo Rewards Proposal.
    """
    
    def __init__(self, bonus_tiers: List[BonusTier]):
        """
        Initialize the calculator with bonus tiers.
        
        Args:
            bonus_tiers: List of BonusTier objects defining the reward structure
        """
        # Sort tiers by min_duration to ensure proper tier selection
        self.bonus_tiers = sorted(bonus_tiers, key=lambda x: x.min_duration)
        
    def calculate_bonus_multiplier(self, duration: int) -> float:
        """
        Calculate the bonus multiplier based on the duration of liquidity provision.
        
        Args:
            duration: Number of days liquidity was provided
            
        Returns:
            Bonus multiplier (1.0 if no bonus applies)
        """
        # Default to no bonus
        multiplier = 1.0
        
        # Find the highest applicable bonus tier
        for tier in reversed(self.bonus_tiers):
            if duration >= tier.min_duration:
                multiplier = tier.multiplier
                break
                
        return multiplier
    
    def calculate_interest_shares(self, provider: LiquidityProvider) -> float:
        """
        Calculate the interest shares for a liquidity provider including any bonuses.
        
        Args:
            provider: LiquidityProvider object
            
        Returns:
            Total interest shares (base + bonus)
            
        Raises:
            ValueError: If input values are invalid
        """
        # Input validation
        if provider.liquidity_amount <= 0:
            raise ValueError("Liquidity amount must be positive")
        if provider.duration <= 0:
            raise ValueError("Duration must be positive")
        if provider.base_apr < 0:
            raise ValueError("Base APR cannot be negative")
            
        # Calculate base interest
        base_interest = provider.liquidity_amount * (provider.base_apr / 365) * provider.duration
        
        # Calculate bonus multiplier
        bonus_multiplier = self.calculate_bonus_multiplier(provider.duration)
        
        # Calculate total interest with bonus
        total_interest = base_interest * bonus_multiplier
        
        return total_interest
    
    def calculate_all_shares(self, providers: List[LiquidityProvider]) -> Dict[str, float]:
        """
        Calculate interest shares for all providers.
        
        Args:
            providers: List of LiquidityProvider objects
            
        Returns:
            Dictionary mapping provider addresses to their interest shares
        """
        results = {}
        
        for provider in providers:
            try:
                shares = self.calculate_interest_shares(provider)
                results[provider.address] = shares
            except ValueError as e:
                print(f"Error calculating shares for {provider.address}: {str(e)}")
                continue
                
        return results

# Example usage
if __name__ == "__main__":
    # Define bonus tiers based on Silo Rewards Proposal
    bonus_tiers = [
        BonusTier(min_duration=30, multiplier=1.1),   # 10% bonus for 30+ days
        BonusTier(min_duration=90, multiplier=1.25),  # 25% bonus for 90+ days
        BonusTier(min_duration=180, multiplier=1.5)   # 50% bonus for 180+ days
    ]
    
    # Create calculator with bonus tiers
    calculator = SiloRewardsCalculator(bonus_tiers)
    
    # Example providers
    providers = [
        LiquidityProvider(
            address="0x123...",
            liquidity_amount=10000.0,
            duration=45,
            base_apr=0.05  # 5% APR
        ),
        LiquidityProvider(
            address="0x456...",
            liquidity_amount=5000.0,
            duration=120,
            base_apr=0.07  # 7% APR
        ),
        LiquidityProvider(
            address="0x789...",
            liquidity_amount=20000.0,
            duration=200,
            base_apr=0.06  # 6% APR
        )
    ]
    
    # Calculate all shares
    shares = calculator.calculate_all_shares(providers)
    
    # Print results
    for address, share in shares.items():
        print(f"Provider {address}: {share:.2f} interest shares")
```
