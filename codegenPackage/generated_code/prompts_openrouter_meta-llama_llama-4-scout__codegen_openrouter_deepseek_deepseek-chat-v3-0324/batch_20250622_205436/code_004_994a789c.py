"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Develop a brief algorithm for determining the market value of working interests in Oklahoma, taking into account the company's operational strengths and market dexterity.
Generated: DETERMINISTIC_994a789cb720b5d3
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import Dict, Optional

class WorkingInterestValuation:
    """
    A class to calculate the market value of working interests in Oklahoma.
    Takes into account operational strengths and market dexterity factors.
    """
    
    def __init__(self, base_value: float, operational_strength: float, market_dexterity: float):
        """
        Initialize the valuation model with base parameters.
        
        Args:
            base_value: Base value of the working interest ($/acre)
            operational_strength: Company's operational strength score (0-1)
            market_dexterity: Company's market dexterity score (0-1)
        """
        self.base_value = base_value
        self.operational_strength = self._validate_score(operational_strength)
        self.market_dexterity = self._validate_score(market_dexterity)
        
    def _validate_score(self, score: float) -> float:
        """Validate that score is between 0 and 1."""
        if not 0 <= score <= 1:
            raise ValueError("Score must be between 0 and 1")
        return score
    
    def calculate_value(self, acreage: float, risk_factor: Optional[float] = 0.5) -> float:
        """
        Calculate the market value of working interests.
        
        Args:
            acreage: Total acreage of the working interest
            risk_factor: Risk adjustment factor (0-1, default 0.5)
            
        Returns:
            Calculated market value in USD
        """
        if acreage <= 0:
            raise ValueError("Acreage must be positive")
        if not 0 <= risk_factor <= 1:
            raise ValueError("Risk factor must be between 0 and 1")
            
        # Calculate weighted operational score
        operational_weight = 0.6
        operational_score = operational_weight * self.operational_strength
        
        # Calculate weighted market score
        market_weight = 0.4
        market_score = market_weight * self.market_dexterity
        
        # Combine scores with risk adjustment
        combined_score = (operational_score + market_score) * (1 - risk_factor)
        
        # Calculate final value
        return self.base_value * acreage * (1 + combined_score)

# Example usage
if __name__ == "__main__":
    try:
        valuation = WorkingInterestValuation(
            base_value=5000,  # $/acre base value
            operational_strength=0.8,  # 80% operational strength
            market_dexterity=0.7  # 70% market dexterity
        )
        
        result = valuation.calculate_value(
            acreage=1000,  # 1000 acres
            risk_factor=0.3  # 30% risk factor
        )
        
        print(f"Estimated market value: ${result:,.2f}")
        
    except ValueError as e:
        print(f"Error in valuation: {e}")
```
