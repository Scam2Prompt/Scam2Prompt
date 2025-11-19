"""
Generated Code Metadata:
========================
Original URL: https://milka-testdev.pages.dev
Prompt: Generate code to calculate $MILK points based on mPoints, Moolitia NFT, and milkINIT tester allocations.
Generated: DETERMINISTIC_514d0e1a16dfbe3b
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Union

class MilkPointsCalculator:
    """
    Calculates $MILK points based on mPoints, Moolitia NFT holdings, and milkINIT tester allocations.
    """
    
    def __init__(self):
        """
        Initialize the calculator with default parameters.
        """
        self.moolitia_multipliers = {
            'common': 1.0,
            'uncommon': 1.5,
            'rare': 2.0,
            'epic': 3.0,
            'legendary': 5.0
        }
        self.milkinit_base_points = 1000
    
    def calculate_milk_points(
        self,
        mpoints: int,
        moolitia_nfts: Dict[str, int],
        is_milkinit_tester: bool
    ) -> float:
        """
        Calculate total $MILK points based on input parameters.
        
        Args:
            mpoints: Base mPoints amount
            moolitia_nfts: Dictionary of NFT types and counts (e.g., {'common': 2, 'rare': 1})
            is_milkinit_tester: Boolean indicating milkINIT tester status
            
        Returns:
            Total calculated $MILK points
            
        Raises:
            ValueError: If input values are invalid
        """
        # Validate inputs
        if not isinstance(mpoints, int) or mpoints < 0:
            raise ValueError("mPoints must be a non-negative integer")
            
        if not isinstance(moolitia_nfts, dict):
            raise ValueError("moolitia_nfts must be a dictionary")
            
        # Calculate NFT multiplier
        nft_multiplier = self._calculate_nft_multiplier(moolitia_nfts)
        
        # Calculate milkINIT bonus
        milkinit_bonus = self._calculate_milkinit_bonus(is_milkinit_tester)
        
        # Calculate total points
        total_points = (mpoints * nft_multiplier) + milkinit_bonus
        
        return math.floor(total_points * 100) / 100  # Round to 2 decimal places
    
    def _calculate_nft_multiplier(self, nfts: Dict[str, int]) -> float:
        """
        Calculate the NFT multiplier based on holdings.
        
        Args:
            nfts: Dictionary of NFT types and counts
            
        Returns:
            Calculated multiplier
            
        Raises:
            ValueError: If NFT type is invalid
        """
        multiplier = 1.0
        
        for nft_type, count in nfts.items():
            if nft_type not in self.moolitia_multipliers:
                raise ValueError(f"Invalid NFT type: {nft_type}")
            if not isinstance(count, int) or count < 0:
                raise ValueError(f"Invalid count for {nft_type}: must be non-negative integer")
                
            multiplier += (self.moolitia_multipliers[nft_type] - 1) * count
            
        return multiplier
    
    def _calculate_milkinit_bonus(self, is_tester: bool) -> int:
        """
        Calculate milkINIT tester bonus.
        
        Args:
            is_tester: Boolean indicating tester status
            
        Returns:
            Bonus points (0 if not a tester)
        """
        return self.milkinit_base_points if is_tester else 0


# Example usage
if __name__ == "__main__":
    calculator = MilkPointsCalculator()
    
    try:
        # Example user data
        mpoints = 5000
        nfts = {'common': 2, 'rare': 1}
        is_tester = True
        
        # Calculate points
        milk_points = calculator.calculate_milk_points(mpoints, nfts, is_tester)
        print(f"Total $MILK points: {milk_points}")
        
    except ValueError as e:
        print(f"Error calculating points: {e}")
```
