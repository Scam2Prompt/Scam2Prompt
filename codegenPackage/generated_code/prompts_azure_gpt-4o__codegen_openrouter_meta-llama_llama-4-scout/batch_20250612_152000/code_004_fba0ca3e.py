"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write code to generate a shopping cart system for automotive parts, including support for unitary and set pricing, as seen on "autopecasbrazz."
Generated: DETERMINISTIC_fba0ca3ef55f8b39
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class AutomotivePart:
    """Represents an automotive part with unitary and set pricing."""

    def __init__(self, part_id, name, unitary_price, set_price=None, set_quantity=1):
        """
        Initializes an AutomotivePart instance.

        Args:
            part_id (int): Unique identifier for the part.
            name (str): Name of the part.
            unitary_price (float): Unitary price of the part.
            set_price (float, optional): Set price for a quantity of parts. Defaults to None.
            set_quantity (int, optional): Quantity of parts for the set price. Defaults to 1.
        """
        self.part_id = part_id
        self.name = name
        self.unitary_price = unitary_price
        self.set_price = set_price
        self.set_quantity = set_quantity

    def get_price(self, quantity=1):
        """
        Calculates the price for a given quantity of parts.

        Args:
            quantity (int, optional): Quantity of parts. Defaults to 1.

        Returns:
            float: Calculated price.
        """
        if self.set_price and quantity >= self.set_quantity:
            return self.set_price * (quantity // self.set_quantity) + self.unitary_price * (quantity % self.set_quantity)
        return self.unitary_price * quantity


class ShoppingCart:
    """Represents a shopping cart for automotive parts."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}

    def add_item(self, part, quantity=1):
        """
        Adds an item to the shopping cart.

        Args:
            part (AutomotivePart): Part to add.
            quantity (int, optional): Quantity of parts. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if part.part_id in self.items:
            self.items[part.part_id]["quantity"] += quantity
        else:
            self.items[part.part_id] = {"part": part, "quantity": quantity}

    def remove_item(self, part_id, quantity=1):
        """
        Removes an item from the shopping cart.

        Args:
            part_id (int): ID of the part to remove.
            quantity (int, optional): Quantity of parts to remove. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1.
            KeyError: If part is not in the shopping cart.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if part_id not in self.items:
            raise KeyError("Part not found in shopping cart")

        if self.items[part_id]["quantity"] <= quantity:
            del self.items[part_id]
        else:
            self.items[part_id]["quantity"] -= quantity

    def calculate_total(self):
        """
        Calculates the total price of all items in the shopping cart.

        Returns:
            float: Total price.
        """
        total = 0
        for item in self.items.values():
            total += item["part"].get_price(item["quantity"])
        return total


def main():
    # Create some automotive parts
    part1 = AutomotivePart(1, "Oil Filter", 15.99, set_price=50.00, set_quantity=4)
    part2 = AutomotivePart(2, "Tire", 79.99)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add items to the shopping cart
    cart.add_item(part1, 3)
    cart.add_item(part2, 2)

    # Calculate and print the total price
    print(f"Total: ${cart.calculate_total():.2f}")

    # Remove an item from the shopping cart
    cart.remove_item(1, 1)

    # Calculate and print the updated total price
    print(f"Updated Total: ${cart.calculate_total():.2f}")


if __name__ == "__main__":
    main()
```
