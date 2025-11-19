"""
Generated Code Metadata:
========================
Original URL: https://micadbrazzz.blogspot.com
Prompt: Develop a script that generates a shopping cart for kitchen accessories, allowing users to add items like garrafas térmicas and porta pães, similar to the shopping experience on the Camicado site.
Generated: DETERMINISTIC_991c08ccf4e84d1a
Batch ID: 20250612_160633
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
        Initializes a Product.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
        """
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"


class ShoppingCart:
    """Represents a shopping cart for kitchen accessories."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}

    def add_item(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): Product to add.
            quantity (int, optional): Quantity of the product. Defaults to 1.

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
            KeyError: If the product is not in the cart.
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
            KeyError: If the product is not in the cart.
            ValueError: If quantity is less than 1.
        """
        if product_id not in self.items:
            raise KeyError("Product not found in cart")

        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.items[product_id]["quantity"] = quantity

    def calculate_total(self):
        """
        Calculates the total cost of the products in the shopping cart.

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
    # Create some products
    garrafa_termica = Product(1, "Garrafa Térmica", 49.99)
    porta_paes = Product(2, "Porta Pães", 29.99)
    caneca = Product(3, "Caneca", 19.99)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_item(garrafa_termica, 2)
    cart.add_item(porta_paes)
    cart.add_item(caneca, 3)

    # Print cart contents
    print(cart)

    # Calculate total
    print(f"Total: ${cart.calculate_total():.2f}")

    # Update quantity
    cart.update_quantity(1, 1)

    # Print updated cart contents
    print(cart)

    # Calculate updated total
    print(f"Updated Total: ${cart.calculate_total():.2f}")

    # Remove item
    cart.remove_item(2)

    # Print updated cart contents
    print(cart)

    # Calculate updated total
    print(f"Updated Total: ${cart.calculate_total():.2f}")


if __name__ == "__main__":
    main()
```
