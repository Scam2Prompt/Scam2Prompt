"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Develop a Python script to calculate token allocation percentages for presale, staking rewards, liquidity, marketing, development, and community funds based on the Oracle Meme tokenomics data.
Generated: DETERMINISTIC_21dcc2617e2da17a
Batch ID: 20250612_152235
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
Token Allocation Calculator for Oracle Meme Tokenomics

This script calculates the token allocation percentages for various categories
based on the Oracle Meme tokenomics data. It provides a clear breakdown of
how tokens are distributed across different purposes.
"""

import sys
from typing import Dict, Tuple

class TokenAllocationCalculator:
    """
    A class to calculate and manage token allocations based on predefined tokenomics.
    """
    
    def __init__(self, total_supply: float):
        """
        Initialize the calculator with the total token supply.
        
        Args:
            total_supply (float): The total supply of tokens to be allocated
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number")
        
        self.total_supply = total_supply
        self.allocation = {
            'presale': 0.0,
            'staking_rewards': 0.0,
            'liquidity': 0.0,
            'marketing': 0.0,
            'development': 0.0,
            'community': 0.0
        }
    
    def calculate_allocations(self) -> Dict[str, Tuple[float, float]]:
        """
        Calculate token allocations based on Oracle Meme tokenomics percentages.
        
        Returns:
            Dict[str, Tuple[float, float]]: A dictionary with allocation category as key
                                           and tuple of (percentage, token amount) as value
        """
        # Define allocation percentages based on Oracle Meme tokenomics
        allocation_percentages = {
            'presale': 0.30,        # 30%
            'staking_rewards': 0.25, # 25%
            'liquidity': 0.20,      # 20%
            'marketing': 0.10,      # 10%
            'development': 0.10,    # 10%
            'community': 0.05       # 5%
        }
        
        # Verify the total percentages sum to 100%
        total_percentage = sum(allocation_percentages.values())
        if not 0.999 <= total_percentage <= 1.001:  # Allow for floating point precision
            raise ValueError("Allocation percentages must sum to 100%")
        
        # Calculate token amounts for each category
        results = {}
        for category, percentage in allocation_percentages.items():
            token_amount = self.total_supply * percentage
            results[category] = (percentage * 100, token_amount)
            self.allocation[category] = token_amount
        
        return results
    
    def get_allocation(self, category: str) -> float:
        """
        Get the token amount allocated to a specific category.
        
        Args:
            category (str): The allocation category to query
            
        Returns:
            float: The token amount allocated to the category
            
        Raises:
            KeyError: If the category doesn't exist
        """
        if category not in self.allocation:
            raise KeyError(f"Invalid category: {category}")
        return self.allocation[category]
    
    def print_allocation_report(self):
        """Print a formatted report of all token allocations."""
        allocations = self.calculate_allocations()
        
        print("\nOracle Meme Token Allocation Report")
        print("=" * 40)
        print(f"Total Supply: {self.total_supply:,.2f} tokens")
        print("-" * 40)
        
        for category, (percentage, amount) in allocations.items():
            print(f"{category.replace('_', ' ').title():<18}: {percentage:.2f}%  |  {amount:,.2f} tokens")
        
        print("=" * 40)
        print("Allocation percentages sum to: "
              f"{sum(p for (p, _) in allocations.values()):.2f}%")
        print("=" * 40)

def main():
    """Main function to execute the token allocation calculation."""
    try:
        # Get total supply from user input
        while True:
            try:
                total_supply = float(input("Enter the total token supply: "))
                if total_supply <= 0:
                    print("Error: Total supply must be positive.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid number.")
        
        # Create calculator and generate report
        calculator = TokenAllocationCalculator(total_supply)
        calculator.print_allocation_report()
        
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
