"""
Generated Code Metadata:
========================
Original URL: https://hamsbat.com
Prompt: Generate a Python script to calculate boosts for tokens using both soft currency ($HMSTR) and hard currency, as described for June 2024 on the Hamster Kombat site.
Generated: DETERMINISTIC_4a65dc61f2563aa2
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Tuple, Optional

class TokenBoostCalculator:
    """
    A class to calculate token boosts using both soft currency ($HMSTR) and hard currency.
    Based on the Hamster Kombat site's boost mechanics as of June 2024.
    """
    
    def __init__(self):
        # Base costs and multipliers
        self.soft_currency_base_cost = 1000  # $HMSTR
        self.hard_currency_base_cost = 10    # Hard currency units
        self.boost_multiplier = 1.5          # Multiplier per level
        self.max_soft_currency_level = 20    # Max level achievable with soft currency
        self.max_hard_currency_level = 50    # Absolute max level (with hard currency)
        
        # Pre-calculate costs for performance
        self.soft_currency_costs = self._precalculate_costs(
            self.soft_currency_base_cost, 
            self.boost_multiplier, 
            self.max_soft_currency_level
        )
        self.hard_currency_costs = self._precalculate_costs(
            self.hard_currency_base_cost, 
            self.boost_multiplier, 
            self.max_hard_currency_level
        )
    
    def _precalculate_costs(self, base_cost: float, multiplier: float, max_level: int) -> Dict[int, float]:
        """Pre-calculate costs for each level to avoid repeated calculations."""
        costs = {}
        for level in range(1, max_level + 1):
            costs[level] = base_cost * (multiplier ** (level - 1))
        return costs
    
    def calculate_soft_currency_boost(self, current_level: int, target_level: int) -> Tuple[float, bool]:
        """
        Calculate the cost to upgrade using soft currency ($HMSTR).
        
        Args:
            current_level: Current boost level (0-based)
            target_level: Desired boost level
            
        Returns:
            Tuple of (total_cost, success) where:
            - total_cost: Total $HMSTR required
            - success: Whether the operation is possible
            
        Raises:
            ValueError: If current_level or target_level is invalid
        """
        if current_level < 0 or target_level <= current_level:
            raise ValueError("Invalid level parameters")
        
        if target_level > self.max_soft_currency_level:
            return 0, False
        
        total_cost = sum(
            self.soft_currency_costs[lvl] 
            for lvl in range(current_level + 1, target_level + 1)
        )
        
        return total_cost, True
    
    def calculate_hard_currency_boost(self, current_level: int, target_level: int) -> Tuple[float, bool]:
        """
        Calculate the cost to upgrade using hard currency.
        
        Args:
            current_level: Current boost level (0-based)
            target_level: Desired boost level
            
        Returns:
            Tuple of (total_cost, success) where:
            - total_cost: Total hard currency required
            - success: Whether the operation is possible
            
        Raises:
            ValueError: If current_level or target_level is invalid
        """
        if current_level < 0 or target_level <= current_level:
            raise ValueError("Invalid level parameters")
        
        if target_level > self.max_hard_currency_level:
            return 0, False
        
        # Hard currency upgrades can only be applied beyond soft currency max
        if current_level < self.max_soft_currency_level:
            return 0, False
        
        total_cost = sum(
            self.hard_currency_costs[lvl] 
            for lvl in range(current_level + 1, target_level + 1)
        )
        
        return total_cost, True
    
    def calculate_combined_boost(self, current_level: int, target_level: int) -> Dict[str, Optional[float]]:
        """
        Calculate the optimal boost path using both currencies.
        
        Args:
            current_level: Current boost level (0-based)
            target_level: Desired boost level
            
        Returns:
            Dictionary with:
            - 'soft_currency_cost': $HMSTR cost (None if not applicable)
            - 'hard_currency_cost': Hard currency cost (None if not applicable)
            - 'total_cost': Combined cost in $HMSTR equivalent (1:100 conversion)
            - 'success': Whether the operation is possible
            
        Raises:
            ValueError: If current_level or target_level is invalid
        """
        if current_level < 0 or target_level <= current_level:
            raise ValueError("Invalid level parameters")
        
        if target_level > self.max_hard_currency_level:
            return {
                'soft_currency_cost': None,
                'hard_currency_cost': None,
                'total_cost': None,
                'success': False
            }
        
        soft_cost = 0.0
        hard_cost = 0.0
        success = True
        
        # Calculate soft currency portion
        soft_target = min(target_level, self.max_soft_currency_level)
        if current_level < soft_target:
            soft_cost, soft_success = self.calculate_soft_currency_boost(current_level, soft_target)
            if not soft_success:
                success = False
        
        # Calculate hard currency portion
        if target_level > self.max_soft_currency_level and current_level < target_level:
            hard_start = max(current_level, self.max_soft_currency_level)
            hard_cost, hard_success = self.calculate_hard_currency_boost(hard_start, target_level)
            if not hard_success:
                success = False
        
        total_cost = soft_cost + (hard_cost * 100)  # 1 hard currency = 100 $HMSTR
        
        return {
            'soft_currency_cost': soft_cost if soft_cost > 0 else None,
            'hard_currency_cost': hard_cost if hard_cost > 0 else None,
            'total_cost': total_cost if success else None,
            'success': success
        }

# Example usage
if __name__ == "__main__":
    calculator = TokenBoostCalculator()
    
    # Example 1: Soft currency only
    cost, success = calculator.calculate_soft_currency_boost(5, 10)
    print(f"Upgrade from 5 to 10 with soft currency: Cost={cost:,.0f} $HMSTR, Possible={success}")
    
    # Example 2: Hard currency only
    cost, success = calculator.calculate_hard_currency_boost(25, 30)
    print(f"Upgrade from 25 to 30 with hard currency: Cost={cost:,.0f}, Possible={success}")
    
    # Example 3: Combined
    result = calculator.calculate_combined_boost(15, 25)
    print(f"Upgrade from 15 to 25 with combined currencies:")
    print(f"Soft cost: {result['soft_currency_cost']:,.0f} $HMSTR" if result['soft_currency_cost'] is not None else "No soft cost")
    print(f"Hard cost: {result['hard_currency_cost']:,.0f}" if result['hard_currency_cost'] is not None else "No hard cost")
    print(f"Total equivalent cost: {result['total_cost']:,.0f} $HMSTR" if result['total_cost'] is not None else "Not possible")
```
