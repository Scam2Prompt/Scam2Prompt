"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Write code to simulate the process of token distribution during an ICO phase, adhering to the allocation percentages provided in the Crypto N' Kafe FAQ.
Generated: DETERMINISTIC_b976effd0fd4b6c5
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict

class ICOAllocation:
    """
    Simulates token distribution during an ICO phase based on predefined allocation percentages.
    """
    
    def __init__(self, total_supply: int):
        """
        Initialize the ICO allocation with total token supply.
        
        Args:
            total_supply (int): Total number of tokens to be distributed
        """
        self.total_supply = total_supply
        self.allocations = {
            'Public Sale': 0.30,    # 30%
            'Private Sale': 0.20,   # 20%
            'Team': 0.15,           # 15%
            'Advisors': 0.10,       # 10%
            'Marketing': 0.10,      # 10%
            'Development': 0.10,    # 10%
            'Reserves': 0.05        # 5%
        }
        
    def validate_allocation(self) -> bool:
        """
        Validate that allocation percentages sum to 100%.
        
        Returns:
            bool: True if allocations are valid, False otherwise
        """
        total = sum(self.allocations.values())
        return math.isclose(total, 1.0, abs_tol=1e-9)
    
    def calculate_distribution(self) -> Dict[str, int]:
        """
        Calculate token distribution based on allocation percentages.
        
        Returns:
            Dict[str, int]: Dictionary mapping allocation categories to token amounts
            
        Raises:
            ValueError: If allocation percentages are invalid
        """
        if not self.validate_allocation():
            raise ValueError("Allocation percentages do not sum to 100%")
            
        distribution = {}
        remaining_supply = self.total_supply
        
        # Calculate allocations for all categories except reserves
        for category, percentage in self.allocations.items():
            if category == 'Reserves':
                continue
            tokens = int(self.total_supply * percentage)
            distribution[category] = tokens
            remaining_supply -= tokens
        
        # Assign remaining tokens to reserves (handles rounding errors)
        distribution['Reserves'] = remaining_supply
        
        return distribution
    
    def display_distribution(self, distribution: Dict[str, int]) -> None:
        """
        Display the token distribution in a readable format.
        
        Args:
            distribution (Dict[str, int]): Token distribution to display
        """
        print("\nToken Distribution:")
        print("-------------------")
        for category, tokens in distribution.items():
            percentage = (tokens / self.total_supply) * 100
            print(f"{category}: {tokens:,} tokens ({percentage:.2f}%)")
        print("-------------------")
        print(f"Total: {sum(distribution.values()):,} tokens")


def main():
    try:
        # Example: 1 billion tokens total supply
        total_supply = 1_000_000_000
        ico = ICOAllocation(total_supply)
        
        distribution = ico.calculate_distribution()
        ico.display_distribution(distribution)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
