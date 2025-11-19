"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khalom.in
Prompt: Create a function in Python that calculates the total price of items in a shopping cart, incorporating discounts like the "FLAT 15% OFF" mentioned on Khalomclothing.
Generated: DETERMINISTIC_99fd541ea8795051
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: List[Dict[str, float]] = []

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """
        Add an item to the shopping cart.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item. Defaults to 1.
        """
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def calculate_total(self, discount_percentage: float = 0) -> float:
        """
        Calculate the total price of items in the cart, applying any discounts.

        Args:
            discount_percentage (float): The discount percentage to apply. Defaults to 0.

        Returns:
            float: The total price after discount.
        """
        if discount_percentage < 0:
            raise ValueError("Discount percentage must be non-negative.")

        total_price = sum(item['price'] * item['quantity'] for item in self.items)
        discount_amount = (total_price * discount_percentage) / 100
        total_price_after_discount = total_price - discount_amount
        
        return round(total_price_after_discount, 2)

    def clear_cart(self) -> None:
        """Clear all items from the shopping cart."""
        self.items.clear()

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("T-Shirt", 25.00, 2)
    cart.add_item("Jeans", 40.00, 1)
    
    try:
        total = cart.calculate_total(discount_percentage=15)
        print(f"Total price after discount: ${total}")
    except ValueError as e:
        print(f"Error: {e}")
```
