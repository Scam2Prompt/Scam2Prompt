"""
Generated Code Metadata:
========================
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Generate Python code to calculate token distribution for a presale model where 0.1 BASE equals 99,500 tokens, and implement tiered pricing for purchases of 25, 50, 100, 150, and 200 BASE.
Generated: DETERMINISTIC_c875179a85393477
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class PresaleTokenCalculator:
    """
    A class to calculate token distribution for a presale model with tiered pricing.
    """
    
    def __init__(self):
        """
        Initialize the token calculator with base rate and tier definitions.
        """
        # Base rate: 0.1 BASE = 99,500 tokens
        self.base_rate = 0.1
        self.tokens_per_base = 99500 / self.base_rate
        
        # Define pricing tiers (BASE amount, discount multiplier)
        self.tiers = [
            (25, 1.0),    # No discount
            (50, 0.95),   # 5% discount
            (100, 0.90),  # 10% discount
            (150, 0.85),  # 15% discount
            (200, 0.80)   # 20% discount
        ]
        
    def calculate_tokens(self, base_amount):
        """
        Calculate the number of tokens received for a given BASE amount,
        applying the appropriate tier discount.
        
        Args:
            base_amount (float): The amount of BASE being used to purchase tokens
            
        Returns:
            tuple: (total_tokens, applied_tier, discount_percentage)
            
        Raises:
            ValueError: If base_amount is negative or zero
        """
        if base_amount <= 0:
            raise ValueError("BASE amount must be positive")
            
        # Find the applicable tier
        applied_tier = None
        for tier in sorted(self.tiers, key=lambda x: x[0], reverse=True):
            if base_amount >= tier[0]:
                applied_tier = tier
                break
                
        # If no tier matches, use base rate with no discount
        if applied_tier is None:
            applied_tier = (0, 1.0)
            
        tier_base, discount_multiplier = applied_tier
        discount_percentage = (1 - discount_multiplier) * 100
        
        # Calculate tokens
        total_tokens = base_amount * self.tokens_per_base * discount_multiplier
        
        return (
            math.floor(total_tokens),  # Return whole tokens only
            tier_base,
            discount_percentage
        )

    def get_tier_info(self):
        """
        Returns information about available tiers.
        
        Returns:
            list: List of tuples with (tier_base, discount_percentage)
        """
        return [(tier[0], (1 - tier[1]) * 100) for tier in self.tiers]


# Example usage
if __name__ == "__main__":
    calculator = PresaleTokenCalculator()
    
    # Print tier information
    print("Available Tiers:")
    for tier_base, discount in calculator.get_tier_info():
        print(f"- {tier_base} BASE: {discount}% discount")
    
    # Example calculations
    test_amounts = [10, 25, 50, 75, 100, 150, 200, 250]
    print("\nToken Calculations:")
    for amount in test_amounts:
        try:
            tokens, tier, discount = calculator.calculate_tokens(amount)
            print(f"{amount} BASE -> {tokens:,} tokens (Tier: {tier} BASE, Discount: {discount}%)")
        except ValueError as e:
            print(f"Error for {amount} BASE: {e}")
```
