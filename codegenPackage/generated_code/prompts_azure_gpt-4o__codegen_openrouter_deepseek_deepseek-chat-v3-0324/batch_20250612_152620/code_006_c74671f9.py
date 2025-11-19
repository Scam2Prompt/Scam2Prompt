"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-def.web.app
Prompt: Write code to calculate tokenomics distribution for $SCOTTY based on the percentages provided (e.g., public sale, staking, development, marketing).
Generated: DETERMINISTIC_c74671f9b265dc51
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenomicsCalculator:
    """
    A class to calculate token distribution based on predefined allocation percentages.
    """
    
    def __init__(self, total_supply: int):
        """
        Initialize the TokenomicsCalculator with the total token supply.
        
        Args:
            total_supply (int): The total supply of tokens to be distributed.
        """
        self.total_supply = total_supply
        self.allocations = {
            'public_sale': 0.30,    # 30%
            'staking': 0.25,        # 25%
            'development': 0.20,    # 20%
            'marketing': 0.15,      # 15%
            'team': 0.10            # 10%
        }
        
    def validate_percentages(self) -> bool:
        """
        Validate that the allocation percentages sum to 100%.
        
        Returns:
            bool: True if percentages sum to 100%, False otherwise.
        """
        total = sum(self.allocations.values())
        return abs(total - 1.0) < 1e-9  # Account for floating point precision
    
    def calculate_distribution(self) -> dict:
        """
        Calculate the token distribution based on the allocation percentages.
        
        Returns:
            dict: A dictionary containing the token amounts for each allocation.
            
        Raises:
            ValueError: If the allocation percentages do not sum to 100%.
        """
        if not self.validate_percentages():
            raise ValueError("Allocation percentages do not sum to 100%")
        
        distribution = {}
        for category, percentage in self.allocations.items():
            distribution[category] = int(self.total_supply * percentage)
        
        return distribution
    
    def print_distribution(self):
        """
        Print the token distribution in a human-readable format.
        """
        try:
            distribution = self.calculate_distribution()
            print(f"Token Distribution for Total Supply: {self.total_supply:,}")
            print("-" * 40)
            for category, amount in distribution.items():
                print(f"{category.replace('_', ' ').title():<15}: {amount:,} ({self.allocations[category] * 100:.0f}%)")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    TOTAL_SUPPLY = 1_000_000_000  # 1 billion tokens
    
    calculator = TokenomicsCalculator(TOTAL_SUPPLY)
    calculator.print_distribution()
```
