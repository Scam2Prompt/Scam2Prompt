"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibqsvjqfvqtsrjjykxkbbgwkxnz32gxfxyrhaa4y5d3xr67l6gnzq.ipfs.dweb.link
Prompt: Explain how the price computation works for packs in the FantasyTop Pack distribution system.
Generated: DETERMINISTIC_68cc1e5e4913d027
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# fantasy_top_pack.py

# Import necessary libraries
import logging

# Configure logging to capture and log errors
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class FantasyTopPack:
    """
    A class to represent the FantasyTop Pack distribution system.

    Attributes:
        base_price (float): The base price of a single pack.
        discount_rules (dict): Discount rules based on pack quantity.
    """

    def __init__(self):
        """
        Initialize the FantasyTopPack distribution system with
        default pricing and discount rules.
        """
        self.base_price = 10.0  # Base price for a single pack
        self.discount_rules = {
            5: 0.05,   # 5% discount for 5 packs
            10: 0.10,  # 10% discount for 10 packs
            20: 0.20,  # 20% discount for 20 packs
        }

    def compute_price(self, quantity):
        """
        Compute the total price for a given quantity of packs.

        Args:
            quantity (int): The number of packs to purchase.

        Returns:
            float: The computed total price after applying discounts.

        Raises:
            ValueError: If the quantity is invalid (e.g., <= 0).
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        # Calculate base price without discount
        total_price = self.base_price * quantity
        
        # Determine applicable discount (if any)
        applicable_discount = 0.0
        for qty, discount in self.discount_rules.items():
            if quantity >= qty:
                applicable_discount = discount
        
        # Apply the discount to the total price
        total_price *= (1 - applicable_discount)
        
        # Log the computation details
        logging.info(
            "Computed price for %d packs: %.2f (Discount applied: %.1f%%)",
            quantity, total_price, applicable_discount * 100
        )
        
        return total_price


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of FantasyTopPack
        pack_system = FantasyTopPack()
        
        # Example: Compute price for 15 packs
        quantity = 15
        total_price = pack_system.compute_price(quantity)
        
        # Output the price
        print(f"Total price for {quantity} packs: ${total_price:.2f}")
    
    except ValueError as e:
        # Handle invalid quantity error
        logging.error("Error computing price: %s", e)
```
