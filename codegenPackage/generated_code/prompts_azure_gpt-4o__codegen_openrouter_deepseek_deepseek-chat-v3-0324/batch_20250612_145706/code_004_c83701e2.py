"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.pages.dev
Prompt: Write code to calculate token allocations for presale, staking, marketing, rewards, and liquidity, based on the $FROP tokenomics percentages.
Generated: DETERMINISTIC_c83701e2c6ead63e
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class TokenAllocator:
    """
    A class to calculate token allocations based on predefined tokenomics percentages.
    """
    
    def __init__(self, total_supply: int):
        """
        Initialize the TokenAllocator with the total token supply.
        
        Args:
            total_supply (int): The total supply of tokens to be allocated
        """
        self.total_supply = total_supply
        self.tokenomics = {
            'presale': 0.30,    # 30%
            'staking': 0.25,    # 25%
            'marketing': 0.15,  # 15%
            'rewards': 0.20,    # 20%
            'liquidity': 0.10   # 10%
        }
        
    def validate_percentages(self) -> bool:
        """
        Validate that the tokenomics percentages sum to 100%.
        
        Returns:
            bool: True if percentages sum to 100%, False otherwise
        """
        total = sum(self.tokenomics.values())
        return math.isclose(total, 1.0, rel_tol=1e-9)
    
    def calculate_allocations(self) -> dict:
        """
        Calculate token allocations based on tokenomics percentages.
        
        Returns:
            dict: A dictionary containing allocation names and their token amounts
            
        Raises:
            ValueError: If tokenomics percentages don't sum to 100%
        """
        if not self.validate_percentages():
            raise ValueError("Tokenomics percentages must sum to 100%")
            
        allocations = {}
        for category, percentage in self.tokenomics.items():
            allocations[category] = int(self.total_supply * percentage)
            
        return allocations
    
    def print_allocations(self, allocations: dict):
        """
        Print the token allocations in a readable format.
        
        Args:
            allocations (dict): The allocations dictionary to print
        """
        print(f"Token Allocations (Total Supply: {self.total_supply:,}):")
        print("-" * 40)
        for category, amount in allocations.items():
            percentage = self.tokenomics[category] * 100
            print(f"{category.capitalize():<10}: {amount:,} ({percentage:.0f}%)")
        print("-" * 40)
        print(f"Total Allocated: {sum(allocations.values()):,}")


def main():
    try:
        # Example usage
        total_supply = 1_000_000_000  # 1 billion tokens
        allocator = TokenAllocator(total_supply)
        
        allocations = allocator.calculate_allocations()
        allocator.print_allocations(allocations)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
