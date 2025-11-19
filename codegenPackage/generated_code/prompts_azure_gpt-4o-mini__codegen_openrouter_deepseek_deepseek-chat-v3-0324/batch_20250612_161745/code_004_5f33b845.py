"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Illustrate how to implement a discount feature in a shopping cart application, taking cues from the 5% discount offer mentioned on ebrasilbrazz.
Generated: DETERMINISTIC_5f33b8453faf8005
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class ShoppingCart:
    """
    A simple shopping cart implementation with discount functionality.
    """

    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = []
        self.discount = 0  # Default discount percentage

    def add_item(self, name, price, quantity=1):
        """
        Add an item to the shopping cart.

        Args:
            name (str): Name of the item
            price (float): Price per unit
            quantity (int): Quantity to add (default: 1)
        """
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def apply_discount(self, percentage):
        """
        Apply a discount percentage to the cart.

        Args:
            percentage (float): Discount percentage (0-100)
        
        Raises:
            ValueError: If percentage is invalid
        """
        if not 0 <= percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        self.discount = percentage

    def remove_discount(self):
        """Remove any applied discount."""
        self.discount = 0

    def calculate_subtotal(self):
        """Calculate the subtotal before discounts."""
        return sum(item['price'] * item['quantity'] for item in self.items)

    def calculate_total(self):
        """
        Calculate the total after applying discount.

        Returns:
            float: Total amount after discount
        """
        subtotal = self.calculate_subtotal()
        discount_amount = subtotal * (self.discount / 100)
        return subtotal - discount_amount

    def clear_cart(self):
        """Remove all items and reset discount."""
        self.items = []
        self.discount = 0


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Add some items
    cart.add_item("Laptop", 1000.00)
    cart.add_item("Mouse", 25.50, 2)
    
    # Apply 5% discount like ebrasilbrazz
    cart.apply_discount(5)
    
    # Calculate and display totals
    print(f"Subtotal: ${cart.calculate_subtotal():.2f}")
    print(f"Discount ({cart.discount}%): ${cart.calculate_subtotal() * (cart.discount/100):.2f}")
    print(f"Total: ${cart.calculate_total():.2f}")
```
