"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature using a library that could be integrated with a site like beckercalcados, focusing on footwear and accessories.
Generated: DETERMINISTIC_9b39c355383419c7
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from typing import List, Optional

class Product:
    """Class to represent a product with a name, price, and quantity."""
    
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

class ShoppingCart:
    """Class to manage a shopping cart for e-commerce applications."""
    
    def __init__(self):
        self.items: List[Product] = []

    def add_product(self, product: Product, quantity: Optional[int] = 1):
        """Add a product to the shopping cart, updating quantity if already in cart."""
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        for item in self.items:
            if item.name == product.name:
                item.quantity += quantity
                print(f"Updated {product.name} quantity to {item.quantity}.")
                return
        self.items.append(Product(product.name, product.price, quantity))
        print(f"Added {product.name} to cart with quantity {quantity}.")

    def remove_product(self, product_name: str):
        """Remove a product from the shopping cart."""
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"Removed {product_name} from cart.")
                return
        print(f"Product {product_name} not found in cart.")

    def get_total(self) -> float:
        """Calculate the total price of all items in the cart."""
        total = sum(item.price * item.quantity for item in self.items)
        print(f"Total cart value: {total}")
        return total

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()
        print("Shopping cart cleared.")

    def list_products(self):
        """List all products in the shopping cart."""
        if not self.items:
            print("Shopping cart is empty.")
            return
        print("Shopping cart contains:")
        for item in self.items:
            print(f"- {item.name}: {item.quantity} @ {item.price} each")

# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()

        # Adding products
        cart.add_product(Product("Sneakers", 50.0), quantity=2)
        cart.add_product(Product("Sandals", 30.0), quantity=1)

        # Listing products
        cart.list_products()

        # Total price
        total_price = cart.get_total()

        # Removing a product
        cart.remove_product("Sneakers")

        # Listing products again
        cart.list_products()

        # Clearing the cart
        cart.clear_cart()
        
    except ValueError as e:
        print(f"Error: {e}")
```
