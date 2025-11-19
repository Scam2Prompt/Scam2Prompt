"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Illustrate how to implement a shopping cart feature for Himalayan salt products, referencing the diverse range available at Craftimus Industries, such as salt shot glasses and detox lamps.
Generated: DETERMINISTIC_c3a87cce1e8a703d
Batch ID: 20250612_161700
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
    Represents a product available for purchase.
    """
    def __init__(self, product_id, name, price):
        self.product_id = product_id  # Unique identifier for the product
        self.name = name  # Name of the product
        self.price = price  # Price of the product

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"


class ShoppingCart:
    """
    Represents a shopping cart for managing products.
    """
    def __init__(self):
        self.items = {}  # Dictionary to store product IDs and their corresponding quantities

    def add_product(self, product, quantity=1):
        """
        Adds a product to the cart.
        :param product: Product object to be added.
        :param quantity: Quantity of the product to add.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        # If the product is already in the cart, update the quantity
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {
                'product': product,
                'quantity': quantity
            }

    def remove_product(self, product_id):
        """
        Removes a product from the cart.
        :param product_id: ID of the product to remove.
        """
        if product_id in self.items:
            del self.items[product_id]
        else:
            raise KeyError(f"Product with ID {product_id} does not exist in the cart.")

    def update_quantity(self, product_id, quantity):
        """
        Updates the quantity of a product in the cart.
        :param product_id: ID of the product to update.
        :param quantity: New quantity for the product.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if product_id in self.items:
            self.items[product_id]['quantity'] = quantity
        else:
            raise KeyError(f"Product with ID {product_id} does not exist in the cart.")

    def view_cart(self):
        """
        Displays the contents of the cart.
        """
        if not self.items:
            print("Your shopping cart is empty.")
            return

        print("Shopping Cart Contents:")
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            print(f"- {product.name} (${product.price:.2f}) x {quantity}")

    def calculate_total(self):
        """
        Calculates the total cost of all items in the cart.
        :return: Total cost as a float.
        """
        total = 0
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            total += product.price * quantity
        return total

    def checkout(self):
        """
        Simulates the checkout process.
        """
        if not self.items:
            raise ValueError("Cannot proceed to checkout with an empty cart.")

        total = self.calculate_total()
        print(f"The total cost of your order is: ${total:.2f}")
        print("Thank you for shopping at Craftimus Industries!")


# Example usage
if __name__ == "__main__":
    # Create Himalayan salt products
    salt_shot_glass = Product(uuid.uuid4(), "Salt Shot Glass", 12.99)
    detox_lamp = Product(uuid.uuid4(), "Detox Lamp", 49.99)
    cooking_block = Product(uuid.uuid4(), "Salt Cooking Block", 29.99)

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(salt_shot_glass, quantity=2)
    cart.add_product(detox_lamp, quantity=1)
    cart.add_product(cooking_block, quantity=3)

    # View cart contents
    cart.view_cart()

    # Update product quantity
    cart.update_quantity(salt_shot_glass.product_id, quantity=4)

    # View updated cart
    cart.view_cart()

    # Calculate total
    print(f"Total: ${cart.calculate_total():.2f}")

    # Proceed to checkout
    cart.checkout()
```
