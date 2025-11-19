"""
Generated Code Metadata:
========================
Original URL: https://bafybeidxxnu2mmv3h3e3o4pjboi7c2ou6bluyjywr5cbxb53ltxd2gp244.ipfs.dweb.link
Prompt: Write code to calculate pledge percentages for a cryptocurrency investment firm, referencing DWF Labs' "$DWF Pledge Now" feature.
Generated: DETERMINISTIC_a1dba0c478d1126d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple, Optional

class PledgeCalculator:
    """
    A class to calculate pledge percentages for cryptocurrency investments.
    Inspired by DWF Labs' "$DWF Pledge Now" feature.
    """
    
    def __init__(self, base_pledge_rate: float = 0.05, max_pledge_rate: float = 0.20):
        """
        Initialize the pledge calculator with base and maximum pledge rates.
        
        Args:
            base_pledge_rate: The minimum pledge percentage (default: 5%)
            max_pledge_rate: The maximum pledge percentage (default: 20%)
        """
        if base_pledge_rate <= 0 or max_pledge_rate <= 0:
            raise ValueError("Pledge rates must be positive")
        if base_pledge_rate > max_pledge_rate:
            raise ValueError("Base pledge rate cannot exceed max pledge rate")
            
        self.base_pledge_rate = base_pledge_rate
        self.max_pledge_rate = max_pledge_rate
    
    def calculate_pledge(
        self,
        investment_amount: float,
        loyalty_factor: float = 1.0,
        market_conditions: float = 1.0
    ) -> Dict[str, float]:
        """
        Calculate the pledge percentage and amount based on investment parameters.
        
        Args:
            investment_amount: The amount being invested
            loyalty_factor: Multiplier based on investor loyalty (default: 1.0)
            market_conditions: Market condition multiplier (default: 1.0)
            
        Returns:
            Dictionary containing:
                - base_rate: The base pledge rate
                - adjusted_rate: The final pledge rate after adjustments
                - pledge_amount: The calculated pledge amount
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be positive")
        if loyalty_factor <= 0:
            raise ValueError("Loyalty factor must be positive")
        if market_conditions <= 0:
            raise ValueError("Market conditions factor must be positive")
        
        # Calculate adjusted pledge rate with caps
        adjusted_rate = min(
            self.max_pledge_rate,
            self.base_pledge_rate * loyalty_factor * market_conditions
        )
        
        pledge_amount = investment_amount * adjusted_rate
        
        return {
            "base_rate": self.base_pledge_rate,
            "adjusted_rate": adjusted_rate,
            "pledge_amount": pledge_amount
        }
    
    def batch_calculate(
        self,
        investments: List[Tuple[float, Optional[float], Optional[float]]]
    ) -> List[Dict[str, float]]:
        """
        Calculate pledges for multiple investments at once.
        
        Args:
            investments: List of tuples containing:
                - investment_amount
                - loyalty_factor (optional)
                - market_conditions (optional)
                
        Returns:
            List of pledge calculation results
        """
        results = []
        for investment in investments:
            try:
                # Unpack with defaults
                amount = investment[0]
                loyalty = investment[1] if len(investment) > 1 and investment[1] is not None else 1.0
                market = investment[2] if len(investment) > 2 and investment[2] is not None else 1.0
                
                result = self.calculate_pledge(amount, loyalty, market)
                results.append(result)
            except ValueError as e:
                # Skip invalid investments and continue processing others
                print(f"Skipping invalid investment: {e}")
                continue
                
        return results


# Example usage
if __name__ == "__main__":
    try:
        calculator = PledgeCalculator()
        
        # Single investment
        result = calculator.calculate_pledge(10000, loyalty_factor=1.2, market_conditions=1.1)
        print("Single investment result:", result)
        
        # Batch processing
        investments = [
            (5000, 1.1, None),
            (15000, None, 1.2),
            (20000, 1.3, 1.1),
            (-1000, 1.0, 1.0),  # Invalid (will be skipped)
            (30000, 0.5, 1.0)   # Will use base rate
        ]
        batch_results = calculator.batch_calculate(investments)
        print("\nBatch results:")
        for res in batch_results:
            print(res)
            
    except ValueError as e:
        print(f"Initialization error: {e}")
```
