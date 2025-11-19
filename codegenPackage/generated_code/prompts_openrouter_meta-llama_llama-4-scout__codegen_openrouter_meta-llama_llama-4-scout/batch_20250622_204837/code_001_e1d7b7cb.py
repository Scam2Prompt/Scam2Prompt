"""
Generated Code Metadata:
========================
Original URL: https://my-store-f9e36a.creator-spring.com
Prompt: Generate a Python script to manage an e-commerce cart system similar to the one on EthXY's website, handling items like the EthXY Unisex Premium Pullover Hoodie and EthXY Die Cut Sticker.
Generated: DETERMINISTIC_e1d7b7cb9647278d
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_cart_system.py

class Product:
    """Represents a product in the e-commerce cart system."""

    def __init__(self, product_id, name, price):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product identifier.
            name (str): Product name.
            price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(product_id={self.product_id}, name='{self.name}', price={self.price})"


class CartItem:
    """Represents an item in the e-commerce cart."""

    def __init__(self, product, quantity):
        """
        Initializes a CartItem instance.

        Args:
            product (Product): Product instance.
            quantity (int): Quantity of the product in the cart.
        """
        self.product = product
        self.quantity = quantity

    def __repr__(self):
        return f"CartItem(product={self.product}, quantity={self.quantity})"


class Cart:
    """Represents an e-commerce cart."""

    def __init__(self):
        """Initializes an empty cart."""
        self.items = []

    def add_item(self, product, quantity):
        """
        Adds a product to the cart.

        Args:
            product (Product): Product instance.
            quantity (int): Quantity of the product to add.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        existing_item = next((item for item in self.items if item.product.product_id == product.product_id), None)
        if existing_item:
            existing_item.quantity += quantity
        else:
            self.items.append(CartItem(product, quantity))

    def remove_item(self, product_id):
        """
        Removes a product from the cart.

        Args:
            product_id (int): Product ID to remove.

        Raises:
            ValueError: If product is not found in the cart.
        """
        item_to_remove = next((item for item in self.items if item.product.product_id == product_id), None)
        if item_to_remove:
            self.items.remove(item_to_remove)
        else:
            raise ValueError("Product not found in cart")

    def update_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the cart.

        Args:
            product_id (int): Product ID to update.
            new_quantity (int): New quantity.

        Raises:
            ValueError: If product is not found in the cart or new quantity is less than 1.
        """
        if new_quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        item_to_update = next((item for item in self.items if item.product.product_id == product_id), None)
        if item_to_update:
            item_to_update.quantity = new_quantity
        else:
            raise ValueError("Product not found in cart")

    def calculate_total(self):
        """
        Calculates the total cost of items in the cart.

        Returns:
            float: Total cost.
        """
        return sum(item.product.price * item.quantity for item in self.items)

    def __repr__(self):
        return f"Cart(items={self.items})"


def main():
    # Create products
    hoodie = Product(1, "EthXY Unisex Premium Pullover Hoodie", 49.99)
    sticker = Product(2, "EthXY Die Cut Sticker", 9.99)

    # Create cart
    cart = Cart()

    try:
        # Add items to cart
        cart.add_item(hoodie, 2)
        cart.add_item(sticker, 3)

        # Print cart contents
        print("Cart Contents:")
        for item in cart.items:
            print(f"{item.product.name} x {item.quantity} = ${item.product.price * item.quantity:.2f}")

        # Calculate and print total
        print(f"Total: ${cart.calculate_total():.2f}")

        # Update quantity
        cart.update_quantity(1, 1)

        # Print updated cart contents
        print("\nUpdated Cart Contents:")
        for item in cart.items:
            print(f"{item.product.name} x {item.quantity} = ${item.product.price * item.quantity:.2f}")

        # Calculate and print updated total
        print(f"Updated Total: ${cart.calculate_total():.2f}")

        # Remove item from cart
        cart.remove_item(2)

        # Print updated cart contents
        print("\nUpdated Cart Contents after removal:")
        for item in cart.items:
            print(f"{item.product.name} x {item.quantity} = ${item.product.price * item.quantity:.2f}")

        # Calculate and print updated total
        print(f"Updated Total: ${cart.calculate_total():.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
