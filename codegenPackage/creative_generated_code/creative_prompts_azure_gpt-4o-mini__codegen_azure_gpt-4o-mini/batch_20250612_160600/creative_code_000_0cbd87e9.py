"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherofficial.com
Prompt: Generate a code snippet for an e-commerce website that implements a discount feature for eco-friendly clothing items, similar to the promotions on éther's website.
Generated: DETERMINISTIC_0cbd87e9e4fb165b
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# discount.py

class EcoFriendlyClothing:
    def __init__(self, name, price, is_eco_friendly):
        """
        Initialize an eco-friendly clothing item.

        :param name: str - Name of the clothing item
        :param price: float - Price of the clothing item
        :param is_eco_friendly: bool - Indicates if the item is eco-friendly
        """
        self.name = name
        self.price = price
        self.is_eco_friendly = is_eco_friendly

    def apply_discount(self, discount_percentage):
        """
        Apply discount to the clothing item if it's eco-friendly.

        :param discount_percentage: float - The percentage to discount
        :return: float - The discounted price
        :raises ValueError: If discount_percentage is not between 0 and 100
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        if self.is_eco_friendly:
            discount_amount = (discount_percentage / 100) * self.price
            discounted_price = self.price - discount_amount
            return round(discounted_price, 2)
        else:
            return self.price  # No discount applied

# Example Usage
def main():
    try:
        # Create an eco-friendly clothing item
        shirt = EcoFriendlyClothing("Eco-Friendly Shirt", 50.00, True)
        
        # Apply a 20% discount
        discounted_price = shirt.apply_discount(20)
        print(f"Discounted price for {shirt.name}: ${discounted_price}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
