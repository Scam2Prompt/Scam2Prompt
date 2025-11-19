"""
Generated Code Metadata:
========================
Original URL: https://rp-galagames-app.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature that allows users to add items like polos and t-shirts, reflecting the shopping experience offered by Vila Romana.
Generated: DETERMINISTIC_f81b2b57853f9a98
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class Product:
    """Represents a product in the shopping cart."""

    def __init__(self, id, name, price):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            price (float): Product price.
        """
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"


class ShoppingCart:
    """Represents a shopping cart."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}

    def add_item(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): Product to add.
            quantity (int, optional): Product quantity. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product.id in self.items:
            self.items[product.id]["quantity"] += quantity
        else:
            self.items[product.id] = {"product": product, "quantity": quantity}

    def remove_item(self, product_id):
        """
        Removes a product from the shopping cart.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If product is not in the cart.
        """
        if product_id not in self.items:
            raise KeyError("Product not found in cart")

        del self.items[product_id]

    def update_quantity(self, product_id, quantity):
        """
        Updates the quantity of a product in the shopping cart.

        Args:
            product_id (int): ID of the product to update.
            quantity (int): New quantity.

        Raises:
            KeyError: If product is not in the cart.
            ValueError: If quantity is less than 1.
        """
        if product_id not in self.items:
            raise KeyError("Product not found in cart")

        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.items[product_id]["quantity"] = quantity

    def calculate_total(self):
        """
        Calculates the total cost of items in the shopping cart.

        Returns:
            float: Total cost.
        """
        total = sum(item["product"].price * item["quantity"] for item in self.items.values())
        return total

    def __repr__(self):
        cart_contents = "\n".join(
            f"{item['product'].name} x {item['quantity']} = ${item['product'].price * item['quantity']:.2f}"
            for item in self.items.values()
        )
        return f"ShoppingCart:\n{cart_contents}"


def main():
    # Create products
    polo = Product(1, "Polo", 29.99)
    t_shirt = Product(2, "T-Shirt", 19.99)

    # Create shopping cart
    cart = ShoppingCart()

    # Add items to cart
    cart.add_item(polo, 2)
    cart.add_item(t_shirt)

    # Print cart contents
    print(cart)

    # Calculate total
    print(f"Total: ${cart.calculate_total():.2f}")

    # Update quantity
    cart.update_quantity(polo.id, 3)

    # Print updated cart contents
    print(cart)

    # Calculate updated total
    print(f"Updated Total: ${cart.calculate_total():.2f}")

    # Remove item from cart
    cart.remove_item(t_shirt.id)

    # Print updated cart contents
    print(cart)

    # Calculate updated total
    print(f"Updated Total: ${cart.calculate_total():.2f}")


if __name__ == "__main__":
    main()
```
