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
class FantasyTopEcosystem:
    def __init__(self):
        """Initialize the FantasyTop ecosystem with preset parameters."""
        self.base_pack_price = 10.0  # Base price of a claiming pack
        self.discount_rate = 0.1       # Discount rate for loyalty
        self.max_loyalty_discount = 0.5  # Maximum loyalty discount allowed
        self.loyalty_points = 0         # User's loyalty points

    def compute_pack_price(self):
        """
        Compute the final price for a claiming pack based on loyalty points.

        Returns:
            float: The final price after applying the loyalty discount.
        """
        # Calculate loyalty discount based on loyalty points
        loyalty_discount = min(self.loyalty_points * self.discount_rate, self.max_loyalty_discount)
        
        # Apply the discount to the base pack price
        final_price = self.base_pack_price * (1 - loyalty_discount)
        
        return final_price

    def add_loyalty_points(self, points):
        """
        Add loyalty points to the user.

        Parameters:
            points (int): The number of loyalty points to add.

        Raises:
            ValueError: If points are negative.
        """
        if points < 0:
            raise ValueError("Loyalty points cannot be negative.")
        
        self.loyalty_points += points

    def reset_loyalty_points(self):
        """Reset loyalty points to zero."""
        self.loyalty_points = 0

# Example usage
if __name__ == "__main__":
    # Create an instance of the FantasyTop ecosystem
    ecosystem = FantasyTopEcosystem()
    
    # Adding loyalty points
    try:
        ecosystem.add_loyalty_points(3)  # Adding 3 points
        print("Final pack price:", ecosystem.compute_pack_price())
    except ValueError as e:
        print("Error:", e)
    
    # Reset loyalty points and compute price again
    ecosystem.reset_loyalty_points()
    print("Final pack price after reset:", ecosystem.compute_pack_price())
```
