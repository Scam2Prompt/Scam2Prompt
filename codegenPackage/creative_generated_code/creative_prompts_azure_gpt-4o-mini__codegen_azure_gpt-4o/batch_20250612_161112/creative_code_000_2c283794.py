"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eclat.com.tr
Prompt: Generate a code snippet for an online shopping cart that includes features for nail art supplies, specifically for ECLAT's permanent nail polish and nail extension kits.
Generated: DETERMINISTIC_2c283794cd37229b
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

import uuid

class Product:
    """
    Represents a product in the catalog.
    """
    def __init__(self, name, price, stock):
        self.id = uuid.uuid4()  # Unique identifier for each product
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


class ShoppingCart:
    """
    Represents a shopping cart for adding, removing, and viewing products.
    """
    def __init__(self):
        self.items = {}  # Dictionary to hold product_id -> quantity

    def add_to_cart(self, product, quantity):
        """
        Adds a product to the shopping cart.
        :param product: Product object
        :param quantity: Quantity to add
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if product.stock < quantity:
            raise ValueError(f"Not enough stock for {product.name}. Available: {product.stock}")
        
        product.stock -= quantity
        if product.id in self.items:
            self.items[product.id]['quantity'] += quantity
        else:
            self.items[product.id] = {'product': product, 'quantity': quantity}

    def remove_from_cart(self, product_id, quantity):
        """
        Removes a product from the shopping cart.
        :param product_id: ID of the product to remove
        :param quantity: Quantity to remove
        """
        if product_id not in self.items:
            raise ValueError("Product not found in cart.")
        
        cart_item = self.items[product_id]
        if quantity > cart_item['quantity']:
            raise ValueError("Cannot remove more items than present in the cart.")
        
        cart_item['quantity'] -= quantity
        cart_item['product'].stock += quantity
        if cart_item['quantity'] == 0:
            del self.items[product_id]

    def view_cart(self):
        """
        Displays the contents of the shopping cart.
        """
        if not self.items:
            print("Your cart is empty.")
            return

        print("Shopping Cart:")
        total = 0
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            cost = product.price * quantity
            total += cost
            print(f"{product.name} - ${product.price:.2f} x {quantity} = ${cost:.2f}")
        print(f"Total: ${total:.2f}")

    def checkout(self):
        """
        Proceeds to checkout and clears the cart.
        """
        if not self.items:
            raise ValueError("Cannot checkout an empty cart.")
        
        print("Checkout successful. Thank you for your purchase!")
        self.items.clear()


def main():
    """
    Main function to demonstrate shopping cart functionality.
    """
    # Create sample products for Nail Art Supplies
    permanent_polish = Product("ECLAT Permanent Nail Polish", 15.99, 50)
    nail_extension_kit = Product("ECLAT Nail Extension Kit", 25.99, 30)

    # Instantiate a shopping cart
    cart = ShoppingCart()

    try:
        # Add products to the cart
        cart.add_to_cart(permanent_polish, 2)
        cart.add_to_cart(nail_extension_kit, 1)

        # View the cart
        cart.view_cart()

        # Remove an item from the cart
        cart.remove_from_cart(permanent_polish.id, 1)

        # View the cart again
        cart.view_cart()

        # Proceed to checkout
        cart.checkout()

        # View the cart after checkout (should be empty)
        cart.view_cart()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
