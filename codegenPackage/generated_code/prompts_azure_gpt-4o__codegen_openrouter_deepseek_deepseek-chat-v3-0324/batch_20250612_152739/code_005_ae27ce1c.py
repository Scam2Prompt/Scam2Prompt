"""
Generated Code Metadata:
========================
Original URL: https://jessecom.pages.dev
Prompt: Create a Python program that simulates the distribution of JESSE tokens based on the presale cap of 1000 BASE and the pricing structure provided.
Generated: DETERMINISTIC_ae27ce1cac580d99
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple

class JesseTokenDistribution:
    """
    Simulates the distribution of JESSE tokens based on the presale cap and pricing structure.
    """
    
    def __init__(self, presale_cap_base: float = 1000.0):
        """
        Initialize the token distribution simulator.
        
        Args:
            presale_cap_base: Total presale cap in BASE tokens (default: 1000)
        """
        self.presale_cap_base = presale_cap_base
        self.total_jesse_tokens = 0
        self.base_raised = 0.0
        self.investments: List[Tuple[str, float]] = []
        
        # Pricing tiers: (BASE amount threshold, JESSE tokens per BASE)
        self.pricing_tiers = [
            (100, 1000),   # Tier 1: 0-100 BASE = 1000 JESSE/BASE
            (300, 800),    # Tier 2: 100-300 BASE = 800 JESSE/BASE
            (600, 600),    # Tier 3: 300-600 BASE = 600 JESSE/BASE
            (1000, 400)    # Tier 4: 600-1000 BASE = 400 JESSE/BASE
        ]
    
    def calculate_tokens_for_base(self, base_amount: float) -> float:
        """
        Calculate JESSE tokens for a given BASE investment amount based on pricing tiers.
        
        Args:
            base_amount: Amount of BASE tokens to invest
            
        Returns:
            Amount of JESSE tokens allocated
            
        Raises:
            ValueError: If base_amount is negative or exceeds remaining presale capacity
        """
        if base_amount <= 0:
            raise ValueError("Investment amount must be positive")
            
        remaining_capacity = self.presale_cap_base - self.base_raised
        if base_amount > remaining_capacity:
            raise ValueError(f"Investment exceeds remaining presale capacity of {remaining_capacity} BASE")
            
        remaining_amount = base_amount
        tokens_allocated = 0.0
        
        for i, (threshold, rate) in enumerate(self.pricing_tiers):
            # Determine the applicable amount for this tier
            if self.base_raised >= threshold:
                continue
                
            tier_max = threshold - self.base_raised
            tier_amount = min(remaining_amount, tier_max)
            
            tokens_allocated += tier_amount * rate
            remaining_amount -= tier_amount
            
            if remaining_amount <= 0:
                break
                
        return tokens_allocated
    
    def add_investment(self, investor: str, base_amount: float) -> Dict[str, float]:
        """
        Process an investment and allocate JESSE tokens.
        
        Args:
            investor: Investor identifier
            base_amount: Amount of BASE tokens to invest
            
        Returns:
            Dictionary containing:
                - base_invested: Actual BASE invested (may be less than requested if cap reached)
                - jesse_allocated: JESSE tokens allocated
                
        Raises:
            ValueError: If base_amount is invalid
        """
        if base_amount <= 0:
            raise ValueError("Investment amount must be positive")
            
        remaining_capacity = self.presale_cap_base - self.base_raised
        if remaining_capacity <= 0:
            return {
                'base_invested': 0.0,
                'jesse_allocated': 0.0
            }
            
        actual_investment = min(base_amount, remaining_capacity)
        tokens = self.calculate_tokens_for_base(actual_investment)
        
        self.base_raised += actual_investment
        self.total_jesse_tokens += tokens
        self.investments.append((investor, actual_investment))
        
        return {
            'base_invested': actual_investment,
            'jesse_allocated': tokens
        }
    
    def get_summary(self) -> Dict[str, float]:
        """
        Get summary of the token distribution.
        
        Returns:
            Dictionary containing:
                - total_base_raised: Total BASE raised
                - total_jesse_allocated: Total JESSE allocated
                - remaining_capacity: Remaining BASE capacity
                - average_rate: Average JESSE per BASE rate
        """
        avg_rate = 0.0
        if self.base_raised > 0:
            avg_rate = self.total_jesse_tokens / self.base_raised
            
        return {
            'total_base_raised': self.base_raised,
            'total_jesse_allocated': self.total_jesse_tokens,
            'remaining_capacity': self.presale_cap_base - self.base_raised,
            'average_rate': avg_rate
        }


# Example usage
if __name__ == "__main__":
    distribution = JesseTokenDistribution()
    
    # Simulate investments
    investments = [
        ("Alice", 50),
        ("Bob", 150),
        ("Charlie", 200),
        ("Dana", 300),
        ("Eve", 400)
    ]
    
    for investor, amount in investments:
        try:
            result = distribution.add_investment(investor, amount)
            print(f"{investor} invested {result['base_invested']} BASE, received {result['jesse_allocated']} JESSE")
        except ValueError as e:
            print(f"Error processing {investor}'s investment: {e}")
    
    # Print summary
    summary = distribution.get_summary()
    print("\nPresale Summary:")
    print(f"Total BASE raised: {summary['total_base_raised']}")
    print(f"Total JESSE allocated: {summary['total_jesse_allocated']}")
    print(f"Remaining capacity: {summary['remaining_capacity']} BASE")
    print(f"Average rate: {summary['average_rate']:.2f} JESSE/BASE")
```
