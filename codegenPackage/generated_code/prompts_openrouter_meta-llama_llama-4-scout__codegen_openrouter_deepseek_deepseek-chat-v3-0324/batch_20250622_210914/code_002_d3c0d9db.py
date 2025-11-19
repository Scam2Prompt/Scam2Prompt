"""
Generated Code Metadata:
========================
Original URL: https://ng-mc.de
Prompt: Develop a code snippet to calculate a company's competitiveness score based on Norbert Gabriel's management consulting approach.
Generated: DETERMINISTIC_d3c0d9db04dbf945
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Optional

class CompetitivenessCalculator:
    """
    Calculates a company's competitiveness score based on Norbert Gabriel's approach.
    The score is derived from multiple weighted factors including market position,
    financial health, operational efficiency, and innovation capability.
    """
    
    def __init__(self, weights: Optional[Dict[str, float]] = None):
        """
        Initialize the calculator with optional custom weights.
        Default weights follow Gabriel's standard model.
        """
        self.default_weights = {
            'market_position': 0.3,
            'financial_health': 0.25,
            'operational_efficiency': 0.25,
            'innovation_capability': 0.2
        }
        self.weights = weights if weights else self.default_weights
        
        # Validate weights sum to 1 (±0.01 tolerance)
        if not math.isclose(sum(self.weights.values()), 1.0, abs_tol=0.01):
            raise ValueError("Weights must sum to 1.0")

    def calculate_score(self, factors: Dict[str, float]) -> float:
        """
        Calculate the overall competitiveness score.
        
        Args:
            factors: Dictionary containing factor scores (0-1 scale)
            
        Returns:
            float: Overall competitiveness score (0-1 scale)
            
        Raises:
            ValueError: If required factors are missing or scores are invalid
        """
        # Validate input factors
        required_factors = set(self.weights.keys())
        if not required_factors.issubset(factors.keys()):
            missing = required_factors - set(factors.keys())
            raise ValueError(f"Missing required factors: {missing}")
        
        for factor, score in factors.items():
            if not 0 <= score <= 1:
                raise ValueError(f"Factor '{factor}' score must be between 0 and 1")
        
        # Calculate weighted score
        weighted_scores = [
            factors[factor] * weight 
            for factor, weight in self.weights.items()
        ]
        
        return sum(weighted_scores)

    def get_competitive_level(self, score: float) -> str:
        """
        Classify the competitiveness level based on the score.
        
        Args:
            score: Competitiveness score (0-1 scale)
            
        Returns:
            str: Competitive level classification
            
        Raises:
            ValueError: If score is outside valid range
        """
        if not 0 <= score <= 1:
            raise ValueError("Score must be between 0 and 1")
            
        if score >= 0.8:
            return "Market Leader"
        elif score >= 0.6:
            return "Strong Competitor"
        elif score >= 0.4:
            return "Average Performer"
        elif score >= 0.2:
            return "Weak Competitor"
        else:
            return "Non-Competitive"
```
