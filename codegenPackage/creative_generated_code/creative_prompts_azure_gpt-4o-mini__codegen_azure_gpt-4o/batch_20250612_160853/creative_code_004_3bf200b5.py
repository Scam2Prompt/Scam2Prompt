"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeia7nsxhythcoyvksls2kh5wotf2bgadzvtbvxj6lojfkxu2cnzrhm.ipfs.dweb.link
Prompt: Explain how the price computation works for claiming packs in the FantasyTop ecosystem.
Generated: DETERMINISTIC_3bf200b533cd6c6a
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class FantasyTopPricing:
    """
    A class to compute the price of claiming packs in the FantasyTop ecosystem.
    """

    def __init__(self, base_price: float, rarity_multiplier: dict, discount_rates: dict):
        """
        Initializes the pricing computation system.

        Args:
            base_price (float): The base price for a single pack.
            rarity_multiplier (dict): A dictionary mapping pack rarity to its price multiplier.
            discount_rates (dict): A dictionary mapping quantity thresholds to discount rates.
        """
        self.base_price = base_price
        self.rarity_multiplier = rarity_multiplier
        self.discount_rates = discount_rates

    def compute_price(self, rarity: str, quantity: int) -> float:
        """
        Computes the total price for a given rarity and quantity of packs.

        Args:
            rarity (str): The rarity of the pack (e.g., 'common', 'rare', 'legendary').
            quantity (int): The number of packs being claimed.

        Returns:
            float: The total price after applying multipliers and discounts.

        Raises:
            ValueError: If the rarity is not valid or quantity is less than 1.
        """
        # Validate rarity
        if rarity not in self.rarity_multiplier:
            raise ValueError(f"Invalid rarity '{rarity}'. Valid options are: {', '.join(self.rarity_multiplier.keys())}")
        
        # Validate quantity
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        # Apply rarity multiplier to base price
        pack_price = self.base_price * self.rarity_multiplier[rarity]

        # Determine applicable discount rate
        applicable_discount = max(
            (rate for threshold, rate in self.discount_rates.items() if quantity >= threshold),
            default=0  # Default to no discount if no thresholds are met
        )

        # Compute final price
        total_price = pack_price * quantity
        discounted_price = total_price * (1 - applicable_discount)

        return round(discounted_price, 2)  # Round to two decimal places for currency

# Example usage
if __name__ == "__main__":
    try:
        # Configuration for FantasyTopPricing
        base_price = 10.0  # Base price for a single pack
        rarity_multiplier = {
            "common": 1.0,
            "rare": 2.0,
            "legendary": 5.0
        }
        discount_rates = {
            10: 0.10,  # 10% discount for 10 or more packs
            20: 0.20,  # 20% discount for 20 or more packs
            50: 0.30   # 30% discount for 50 or more packs
        }

        # Initialize the pricing system
        pricing_system = FantasyTopPricing(base_price, rarity_multiplier, discount_rates)

        # Compute price for a specific rarity and quantity
        rarity = "legendary"
        quantity = 25
        total_price = pricing_system.compute_price(rarity, quantity)

        print(f"The total price for {quantity} {rarity} packs is: ${total_price}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
