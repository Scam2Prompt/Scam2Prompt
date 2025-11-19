"""
Generated Code Metadata:
========================
Original URL: https://shop.isabelreinachic.com
Prompt: Write a Python code snippet to manage an e-commerce shopping cart for a sewing machine store, including adding and removing items, and calculating the total cost.
Generated: DETERMINISTIC_95ac00d77bcc616d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class SewingMachine:
    """Represents a sewing machine product."""

    def __init__(self, product_id, name, price):
        """
        Initializes a SewingMachine object.

        Args:
            product_id (int): Unique product identifier.
            name (str): Product name.
            price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"SewingMachine(product_id={self.product_id}, name='{self.name}', price={self.price})"


class ShoppingCart:
    """Manages an e-commerce shopping cart."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}

    def add_item(self, sewing_machine, quantity=1):
        """
        Adds a sewing machine to the shopping cart.

        Args:
            sewing_machine (SewingMachine): Sewing machine to add.
            quantity (int, optional): Quantity to add. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if sewing_machine.product_id in self.items:
            self.items[sewing_machine.product_id]["quantity"] += quantity
        else:
            self.items[sewing_machine.product_id] = {"sewing_machine": sewing_machine, "quantity": quantity}

    def remove_item(self, product_id, quantity=1):
        """
        Removes a sewing machine from the shopping cart.

        Args:
            product_id (int): Product ID of the sewing machine to remove.
            quantity (int, optional): Quantity to remove. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1.
            KeyError: If product ID is not in the shopping cart.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product_id not in self.items:
            raise KeyError("Product ID not found in shopping cart")

        if self.items[product_id]["quantity"] <= quantity:
            del self.items[product_id]
        else:
            self.items[product_id]["quantity"] -= quantity

    def calculate_total(self):
        """
        Calculates the total cost of items in the shopping cart.

        Returns:
            float: Total cost.
        """
        total = sum(item["sewing_machine"].price * item["quantity"] for item in self.items.values())
        return total

    def __repr__(self):
        return f"ShoppingCart(items={self.items})"


def main():
    # Create sewing machines
    machine1 = SewingMachine(1, "Basic Sewing Machine", 99.99)
    machine2 = SewingMachine(2, "Advanced Sewing Machine", 199.99)

    # Create shopping cart
    cart = ShoppingCart()

    # Add items to cart
    cart.add_item(machine1, 2)
    cart.add_item(machine2)

    # Print cart contents
    print("Shopping Cart:")
    for product_id, item in cart.items.items():
        print(f"Product ID: {product_id}, Name: {item['sewing_machine'].name}, Quantity: {item['quantity']}")

    # Calculate and print total cost
    total_cost = cart.calculate_total()
    print(f"Total Cost: ${total_cost:.2f}")

    # Remove item from cart
    cart.remove_item(1)

    # Print updated cart contents
    print("\nUpdated Shopping Cart:")
    for product_id, item in cart.items.items():
        print(f"Product ID: {product_id}, Name: {item['sewing_machine'].name}, Quantity: {item['quantity']}")

    # Calculate and print updated total cost
    updated_total_cost = cart.calculate_total()
    print(f"Updated Total Cost: ${updated_total_cost:.2f}")


if __name__ == "__main__":
    main()
```
