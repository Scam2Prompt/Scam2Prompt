"""
Generated Code Metadata:
========================
Original URL: https://agoda.host
Prompt: "Write a product description for a spa gift basket focused on citrus-inspired elegance for blissful pampering."
Generated: DETERMINISTIC_86304d0459cb3e1a
Batch ID: 20250622_212043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SpaGiftBasket:
    """
    A class to represent a spa gift basket focused on citrus-inspired elegance for blissful pampering.
    """

    def __init__(self, items, price):
        """
        Initializes the SpaGiftBasket with a list of items and a price.

        :param items: List of items included in the gift basket.
        :param price: Price of the gift basket.
        """
        self.items = items
        self.price = price

    def display_description(self):
        """
        Displays a product description for the spa gift basket.
        """
        description = (
            "Indulge in the refreshing essence of citrus with our Spa Gift Basket, "
            "designed for those who seek blissful pampering. This elegant collection "
            "features a variety of luxurious items that will transport you to a serene "
            "oasis of relaxation.\n\n"
            "Included in this basket:\n"
        )
        
        for item in self.items:
            description += f"- {item}\n"
        
        description += (
            f"\nPerfect for gifting or treating yourself, this basket is priced at ${self.price:.2f}. "
            "Experience the uplifting aroma of citrus and let your worries melt away."
        )
        
        return description

    def apply_discount(self, discount_percentage):
        """
        Applies a discount to the price of the gift basket.

        :param discount_percentage: The percentage discount to apply (0-100).
        :raises ValueError: If discount_percentage is not between 0 and 100.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        discount_amount = (discount_percentage / 100) * self.price
        self.price -= discount_amount

    def __str__(self):
        """
        Returns a string representation of the SpaGiftBasket.
        """
        return f"SpaGiftBasket(items={self.items}, price={self.price:.2f})"


# Example usage
if __name__ == "__main__":
    try:
        items = [
            "Citrus-scented candle",
            "Lemon verbena body scrub",
            "Orange blossom bath salts",
            "Grapefruit essential oil",
            "Lime-infused hand cream"
        ]
        basket = SpaGiftBasket(items, 59.99)
        print(basket.display_description())
        
        # Apply a discount
        basket.apply_discount(10)  # Apply a 10% discount
        print(f"\nAfter discount: ${basket.price:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
