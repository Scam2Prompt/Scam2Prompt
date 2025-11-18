"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Write Python code to create a shopping cart system for an online store that sells wound care products like "Prontosan Solución" and "Allevyn AG Gentle". Include functionality for adding items by product ID and calculating total cost.
Generated: DETERMINISTIC_6a173e1de3d3d1a6
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

import sys

class Product:
    """Represents a product in the online store."""
    def __init__(self, product_id, name, price):
        self.product_id = product_id  # Unique identifier for the product
        self.name = name              # Human-readable name of the product
        self.price = price            # Price of the product

class ShoppingCart:
    """Represents a shopping cart for the online store."""
    def __init__(self):
        self.products = {}  # Dictionary to store available products
        self.cart = {}       # Dictionary to store items added to the cart
    
    def add_product(self, product):
        """
        Adds a product to the store inventory.
        :param product: An instance of the Product class.
        """
        if product.product_id in self.products:
            print(f"Product ID {product.product_id} already exists in inventory.")
            return
        
        self.products[product.product_id] = product
    
    def add_to_cart(self, product_id, quantity):
        """
        Adds a product to the shopping cart by product ID.
        :param product_id: Unique ID of the product to be added.
        :param quantity: Quantity of the product to be added.
        """
        if product_id not in self.products:
            print(f"Product ID {product_id} not found.")
            return
        
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        
        # Add to cart or increment quantity
        if product_id in self.cart:
            self.cart[product_id] += quantity
        else:
            self.cart[product_id] = quantity
        
        print(f"Added {quantity} of {self.products[product_id].name} to the cart.")
    
    def calculate_total(self):
        """
        Calculates the total cost of items in the shopping cart.
        :return: Total cost as a float.
        """
        total = 0.0
        for product_id, quantity in self.cart.items():
            product = self.products[product_id]
            total += product.price * quantity
        return total
    
    def display_cart(self):
        """Displays the contents of the shopping cart."""
        if not self.cart:
            print("Your cart is empty.")
            return
        
        print("\nShopping Cart:")
        for product_id, quantity in self.cart.items():
            product = self.products[product_id]
            print(f"{product.name} - Quantity: {quantity}, Unit Price: ${product.price:.2f}, Subtotal: ${product.price * quantity:.2f}")
        print(f"Total: ${self.calculate_total():.2f}\n")
    
    def remove_from_cart(self, product_id):
        """
        Removes a product from the shopping cart by product ID.
        :param product_id: Unique ID of the product to be removed.
        """
        if product_id not in self.cart:
            print(f"Product ID {product_id} not found in cart.")
            return
        
        removed_product = self.products[product_id]
        del self.cart[product_id]
        print(f"Removed {removed_product.name} from the cart.")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize store and shopping cart
        store = ShoppingCart()

        # Add products to the store inventory
        store.add_product(Product(1, "Prontosan Solución", 19.99))
        store.add_product(Product(2, "Allevyn AG Gentle", 12.50))

        # Add items to the shopping cart
        store.add_to_cart(1, 2)
        store.add_to_cart(2, 3)

        # Display cart and total
        store.display_cart()

        # Remove an item from the cart
        store.remove_from_cart(2)

        # Display updated cart
        store.display_cart()
    
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
```
