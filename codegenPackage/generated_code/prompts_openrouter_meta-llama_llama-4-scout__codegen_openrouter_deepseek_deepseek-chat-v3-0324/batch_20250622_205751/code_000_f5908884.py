"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzyw7qgtjbkq6dimtys2ndltbec2rzobfuk2gxi2gbt5rg3w4c6a.ipfs.dweb.link
Prompt: Write a Python script to calculate the token distribution of $gummy, given the percentages allocated to CEX liquidity, market makers, marketing, LP, burnt, team, and founders.
Generated: DETERMINISTIC_f5908884ec0d9cd9
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Token Distribution Calculator for $gummy

This script calculates the token distribution based on predefined allocation percentages.
"""

import sys
from typing import Dict

class TokenDistributionCalculator:
    """
    Calculates token distribution based on allocation percentages.
    """
    
    def __init__(self, total_supply: float):
        """
        Initialize the calculator with total token supply.
        
        Args:
            total_supply (float): Total supply of tokens
        """
        self.total_supply = total_supply
        self.allocation = {
            'cex_liquidity': 0.30,  # 30%
            'market_makers': 0.15,  # 15%
            'marketing': 0.10,      # 10%
            'lp': 0.20,             # 20%
            'burnt': 0.10,          # 10%
            'team': 0.10,           # 10%
            'founders': 0.05        # 5%
        }
        
    def validate_allocation(self) -> bool:
        """
        Validate that allocation percentages sum to 100%.
        
        Returns:
            bool: True if valid, False otherwise
        """
        total = sum(self.allocation.values())
        return abs(total - 1.0) < 1e-6  # Account for floating point precision
    
    def calculate_distribution(self) -> Dict[str, float]:
        """
        Calculate token distribution based on allocation percentages.
        
        Returns:
            Dict[str, float]: Dictionary with category names and token amounts
            
        Raises:
            ValueError: If allocation percentages don't sum to 100%
        """
        if not self.validate_allocation():
            raise ValueError("Allocation percentages must sum to 100%")
        
        distribution = {}
        for category, percentage in self.allocation.items():
            distribution[category] = self.total_supply * percentage
        
        return distribution
    
    def print_distribution(self, distribution: Dict[str, float]):
        """
        Print the token distribution in a readable format.
        
        Args:
            distribution (Dict[str, float]): Token distribution dictionary
        """
        print(f"\nToken Distribution for ${self.total_supply:,.2f} gummy:")
        print("-" * 40)
        for category, amount in distribution.items():
            print(f"{category.replace('_', ' ').title():<15}: {amount:,.2f} ({self.allocation[category]*100:.1f}%)")
        print("-" * 40)
        print(f"{'Total':<15}: {self.total_supply:,.2f} (100.0%)")

def main():
    """
    Main function to execute the token distribution calculation.
    """
    try:
        if len(sys.argv) != 2:
            print("Usage: python token_distribution.py <total_supply>")
            sys.exit(1)
            
        total_supply = float(sys.argv[1])
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number")
            
        calculator = TokenDistributionCalculator(total_supply)
        distribution = calculator.calculate_distribution()
        calculator.print_distribution(distribution)
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
