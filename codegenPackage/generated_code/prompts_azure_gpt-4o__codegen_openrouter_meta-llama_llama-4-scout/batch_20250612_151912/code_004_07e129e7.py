"""
Generated Code Metadata:
========================
Original URL: https://adhive.net
Prompt: Write a script to implement a "View Cart" functionality for an online store, similar to the one described on Adhive Marketplace.
Generated: DETERMINISTIC_07e129e7c7eedbb4
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# view_cart.py

class Product:
    """Represents a product in the online store."""

    def __init__(self, product_id, name, price, quantity):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product quantity.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:
    """Represents a shopping cart."""

    def __init__(self):
        """Initializes an empty cart."""
        self.items = {}

    def add_item(self, product, quantity):
        """
        Adds a product to the cart.

        Args:
            product (Product): Product to add.
            quantity (int): Quantity to add.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product.product_id in self.items:
            self.items[product.product_id]["quantity"] += quantity
        else:
            self.items[product.product_id] = {"product": product, "quantity": quantity}

    def remove_item(self, product_id):
        """
        Removes a product from the cart.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If product is not in the cart.
        """
        if product_id not in self.items:
            raise KeyError("Product not in cart")

        del self.items[product_id]

    def update_quantity(self, product_id, quantity):
        """
        Updates the quantity of a product in the cart.

        Args:
            product_id (int): ID of the product to update.
            quantity (int): New quantity.

        Raises:
            KeyError: If product is not in the cart.
            ValueError: If quantity is less than 1.
        """
        if product_id not in self.items:
            raise KeyError("Product not in cart")

        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.items[product_id]["quantity"] = quantity

    def calculate_total(self):
        """
        Calculates the total cost of the items in the cart.

        Returns:
            float: Total cost.
        """
        total = 0
        for item in self.items.values():
            total += item["product"].price * item["quantity"]
        return total

    def view_cart(self):
        """Prints the contents of the cart."""
        print("Your Cart:")
        for item in self.items.values():
            print(f"{item['product'].name} x {item['quantity']} = ${item['product'].price * item['quantity']:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")


def main():
    # Create some products
    product1 = Product(1, "Product A", 19.99, 10)
    product2 = Product(2, "Product B", 9.99, 5)
    product3 = Product(3, "Product C", 29.99, 7)

    # Create a cart
    cart = Cart()

    # Add items to the cart
    cart.add_item(product1, 2)
    cart.add_item(product2, 3)
    cart.add_item(product3, 1)

    # View the cart
    cart.view_cart()

    # Update quantity
    cart.update_quantity(1, 1)

    # View the cart again
    cart.view_cart()

    # Remove an item
    cart.remove_item(2)

    # View the cart again
    cart.view_cart()


if __name__ == "__main__":
    main()
```
