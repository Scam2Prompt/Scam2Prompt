"""
Generated Code Metadata:
========================
Original URL: https://cbupdates.com
Prompt: Write a function to calculate the potential profitability of a franchise opportunity based on individual strengths and business goals, as offered by Franchise Teacher.
Generated: DETERMINISTIC_183d1b8a63db7ad2
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Optional, Union

class FranchiseProfitabilityCalculator:
    """
    A class to calculate the potential profitability of a franchise opportunity.
    """
    
    def __init__(self):
        self._weights = {
            'initial_investment': 0.2,
            'royalty_fees': 0.15,
            'advertising_fees': 0.1,
            'location_score': 0.25,
            'market_demand': 0.2,
            'personal_strengths': 0.1
        }
    
    def _validate_input(self, inputs: Dict[str, Union[int, float]]) -> None:
        """
        Validates the input parameters.
        
        Args:
            inputs: Dictionary containing input parameters.
            
        Raises:
            ValueError: If any input is invalid.
        """
        required_keys = [
            'initial_investment',
            'royalty_fees',
            'advertising_fees',
            'location_score',
            'market_demand',
            'personal_strengths'
        ]
        
        for key in required_keys:
            if key not in inputs:
                raise ValueError(f"Missing required parameter: {key}")
            
            value = inputs[key]
            if not isinstance(value, (int, float)):
                raise ValueError(f"Parameter {key} must be a number")
            
            if key in ['location_score', 'market_demand', 'personal_strengths']:
                if not 0 <= value <= 1:
                    raise ValueError(f"Parameter {key} must be between 0 and 1")
    
    def calculate_profitability_score(
        self,
        initial_investment: float,
        royalty_fees: float,
        advertising_fees: float,
        location_score: float,
        market_demand: float,
        personal_strengths: float,
        custom_weights: Optional[Dict[str, float]] = None
    ) -> float:
        """
        Calculates the profitability score for a franchise opportunity.
        
        Args:
            initial_investment: Initial investment amount (lower is better).
            royalty_fees: Ongoing royalty fees percentage (lower is better).
            advertising_fees: Advertising fees percentage (lower is better).
            location_score: Location quality score (0-1, higher is better).
            market_demand: Market demand score (0-1, higher is better).
            personal_strengths: Personal strengths alignment (0-1, higher is better).
            custom_weights: Optional custom weights for calculation factors.
            
        Returns:
            float: Profitability score between 0 and 1 (higher is better).
        """
        inputs = {
            'initial_investment': initial_investment,
            'royalty_fees': royalty_fees,
            'advertising_fees': advertising_fees,
            'location_score': location_score,
            'market_demand': market_demand,
            'personal_strengths': personal_strengths
        }
        
        self._validate_input(inputs)
        
        weights = custom_weights if custom_weights else self._weights
        
        # Normalize investment and fees (lower values should increase score)
        max_investment = 1000000  # Example max value for normalization
        max_fees = 0.2  # Example max value for normalization (20%)
        
        norm_investment = 1 - min(initial_investment / max_investment, 1)
        norm_royalty = 1 - min(royalty_fees / max_fees, 1)
        norm_advertising = 1 - min(advertising_fees / max_fees, 1)
        
        score = (
            weights['initial_investment'] * norm_investment +
            weights['royalty_fees'] * norm_royalty +
            weights['advertising_fees'] * norm_advertising +
            weights['location_score'] * location_score +
            weights['market_demand'] * market_demand +
            weights['personal_strengths'] * personal_strengths
        )
        
        return max(0, min(score, 1))  # Ensure score is between 0 and 1
    
    def calculate_estimated_profit(
        self,
        profitability_score: float,
        market_size: float,
        average_margin: float,
        growth_factor: float = 1.0
    ) -> float:
        """
        Estimates potential profit based on profitability score and market factors.
        
        Args:
            profitability_score: Score from calculate_profitability_score (0-1).
            market_size: Total addressable market in dollars.
            average_margin: Average profit margin (0-1).
            growth_factor: Multiplier for growth potential (default 1.0).
            
        Returns:
            float: Estimated annual profit in dollars.
        """
        if not 0 <= profitability_score <= 1:
            raise ValueError("Profitability score must be between 0 and 1")
        if market_size <= 0:
            raise ValueError("Market size must be positive")
        if not 0 <= average_margin <= 1:
            raise ValueError("Average margin must be between 0 and 1")
        if growth_factor <= 0:
            raise ValueError("Growth factor must be positive")
        
        market_share = profitability_score * 0.2  # Max 20% market share
        return market_size * market_share * average_margin * growth_factor
```
