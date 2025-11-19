"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://final3223.vercel.app
Prompt: Explain how to implement a tiered pricing model for NFT sales similar to the one described, including the calculation of token distribution based on SOL payments.
Generated: DETERMINISTIC_548184d41bad6f1f
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
NFT Tiered Pricing Model Implementation
This Python script implements a tiered pricing model for NFT sales.
NFTs are distributed based on SOL payments, with different tiers offering varying amounts of tokens.
"""

# Required imports
import math

class NFTTieredPricing:
    """
    Class to handle tiered pricing and token distribution for NFT sales.
    """

    def __init__(self, tiers):
        """
        Initialize the pricing model with tiers.
        Args:
            tiers (list of dict): List of tiers, each having 'min_payment', 'max_payment', and 'tokens'.
        Example:
            tiers = [
                {"min_payment": 0, "max_payment": 1, "tokens": 1},
                {"min_payment": 1, "max_payment": 5, "tokens": 5},
                {"min_payment": 5, "max_payment": 10, "tokens": 10}
            ]
        """
        self.tiers = sorted(tiers, key=lambda x: x['min_payment'])  # Sort tiers by min_payment for consistency

    def get_token_distribution(self, sol_payment):
        """
        Calculate the number of tokens based on SOL payment.
        Args:
            sol_payment (float): The amount of SOL paid by the user.
        Returns:
            int: The number of tokens the user will receive.
        Raises:
            ValueError: If the SOL payment does not fit in any tier.
        """
        for tier in self.tiers:
            if tier['min_payment'] <= sol_payment <= tier['max_payment']:
                return tier['tokens']
        raise ValueError(f"Payment of {sol_payment} SOL does not fit in any pricing tier.")

    def simulate_sale(self, sol_payment):
        """
        Simulates an NFT sale and returns the result.
        Args:
            sol_payment (float): The amount of SOL paid by the user.
        Returns:
            dict: A summary of the sale (SOL payment and tokens distributed).
        """
        try:
            tokens = self.get_token_distribution(sol_payment)
            return {
                "sol_payment": sol_payment,
                "tokens_distributed": tokens
            }
        except ValueError as e:
            return {
                "error": str(e)
            }

# Example usage
if __name__ == "__main__":
    # Define the NFT pricing tiers
    tiers = [
        {"min_payment": 0, "max_payment": 1, "tokens": 1},
        {"min_payment": 1, "max_payment": 5, "tokens": 5},
        {"min_payment": 5, "max_payment": 10, "tokens": 10}
    ]

    # Initialize the pricing model
    pricing_model = NFTTieredPricing(tiers)

    # Simulate sales
    payments = [0.5, 1.5, 5, 7.5, 11]  # Example SOL payments
    for payment in payments:
        result = pricing_model.simulate_sale(payment)
        print(result)
```
