"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature for auto parts, using the product details and pricing structure from the autopecasbrazz webpage.
Generated: DETERMINISTIC_2226aff220694b18
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from typing import List, Dict, Optional

class Product:
    """A class to represent a product in the shopping cart."""
    
    def __init__(self, product_id: int, name: str, price: float, quantity: int = 1):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        """Calculate the total price for the given quantity of the product."""
        return self.price * self.quantity


class ShoppingCart:
    """A class to represent a shopping cart."""
    
    def __init__(self):
        self.items: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a product to the shopping cart."""
        self.items.append(product)

    def remove_product(self, product_id: int) -> bool:
        """Remove a product from the shopping cart by product_id."""
        for index, item in enumerate(self.items):
            if item.product_id == product_id:
                del self.items[index]
                return True
        return False

    def update_quantity(self, product_id: int, quantity: int) -> bool:
        """Update the quantity of a product in the shopping cart."""
        for item in self.items:
            if item.product_id == product_id:
                if quantity < 1:
                    return False  # Quantity must be at least 1
                item.quantity = quantity
                return True
        return False

    def calculate_total(self) -> float:
        """Calculate the total price of the shopping cart."""
        return sum(item.total_price() for item in self.items)

    def display_cart(self) -> None:
        """Display the contents of the shopping cart."""
        if not self.items:
            print("Your cart is empty.")
            return
        
        print("Shopping Cart Contents:")
        for item in self.items:
            print(f"{item.name} (ID: {item.product_id}) - Quantity: {item.quantity}, Price: ${item.price:.2f}, Total: ${item.total_price():.2f}")
        
        print(f"Total Price: ${self.calculate_total():.2f}")

def main():
    """Main function to demonstrate shopping cart functionality."""
    
    # Create a shopping cart instance
    cart = ShoppingCart()

    # Sample products (would typically be retrieved from a database or an API)
    product1 = Product(product_id=101, name="Oil Filter", price=15.99)
    product2 = Product(product_id=102, name="Brake Pad Set", price=49.99)
    
    # Add products to the cart
    cart.add_product(product1)
    cart.add_product(product2)

    # Display the cart contents
    cart.display_cart()

    # Update quantity and display cart again
    cart.update_quantity(product_id=101, quantity=2)
    cart.display_cart()

    # Remove a product and display cart again
    cart.remove_product(product_id=102)
    cart.display_cart()

if __name__ == "__main__":
    main()
```
