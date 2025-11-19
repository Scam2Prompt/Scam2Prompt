"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cakco.com
Prompt: Generate a code snippet for a shopping cart system that includes features for selecting multiple variants of trendy bags, as described on the Cakco website.
Generated: DETERMINISTIC_7750aaeebc794778
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py
class BagVariant:
    """Class to represent a variant of a bag."""
    
    def __init__(self, name, price, color, size):
        self.name = name
        self.price = price
        self.color = color
        self.size = size

    def __str__(self):
        return f"{self.name} - {self.color} - {self.size}: ${self.price:.2f}"


class ShoppingCart:
    """Class to manage the shopping cart functionality."""
    
    def __init__(self):
        self.items = []

    def add_variant(self, variant: BagVariant):
        """Add a bag variant to the shopping cart."""
        if not isinstance(variant, BagVariant):
            raise TypeError("Expected a BagVariant instance.")
        self.items.append(variant)
        print(f"Added to cart: {variant}")

    def remove_variant(self, variant: BagVariant):
        """Remove a bag variant from the shopping cart."""
        try:
            self.items.remove(variant)
            print(f"Removed from cart: {variant}")
        except ValueError:
            print("Item not found in cart.")

    def total_price(self) -> float:
        """Calculate the total price of the items in the cart."""
        return sum(item.price for item in self.items)

    def display_cart(self):
        """Display items in the cart."""
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items:
                print(f"- {item}")
            print(f"Total Price: ${self.total_price():.2f}")


# Example usage:
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Create some bag variants
    bag1 = BagVariant("Trendy Tote", 49.99, "Red", "Large")
    bag2 = BagVariant("Chic Backpack", 69.99, "Blue", "Medium")
    bag3 = BagVariant("Stylish Crossbody", 39.99, "Black", "Small")

    # Add variants to the cart
    cart.add_variant(bag1)
    cart.add_variant(bag2)
    cart.add_variant(bag3)

    # Display the cart contents
    cart.display_cart()

    # Remove an item from the cart
    cart.remove_variant(bag2)

    # Display the cart contents again
    cart.display_cart()
```
