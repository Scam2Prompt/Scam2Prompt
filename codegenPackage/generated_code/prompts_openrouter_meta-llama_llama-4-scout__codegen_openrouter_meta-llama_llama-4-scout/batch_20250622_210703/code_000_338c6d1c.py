"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: "Write a Python code snippet to manage the inventory of fiberglass products, including Glass fiber reinforced concrete (GFRC), IDGFiber® PPF, and Ceramic fiber."
Generated: DETERMINISTIC_338c6d1cd95048d0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class FiberglassProduct:
    """Base class for fiberglass products."""

    def __init__(self, name, quantity, unit_price):
        """
        Initialize a fiberglass product.

        Args:
            name (str): Product name.
            quantity (int): Product quantity.
            unit_price (float): Product unit price.
        """
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def get_total_value(self):
        """Calculate the total value of the product."""
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.unit_price:.2f}/unit"


class Inventory:
    """Manage the inventory of fiberglass products."""

    def __init__(self):
        """Initialize an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the inventory.

        Args:
            product (FiberglassProduct): Product to add.

        Raises:
            ValueError: If a product with the same name already exists.
        """
        if product.name in self.products:
            raise ValueError(f"Product '{product.name}' already exists in the inventory.")
        self.products[product.name] = product

    def remove_product(self, name):
        """
        Remove a product from the inventory.

        Args:
            name (str): Name of the product to remove.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if name not in self.products:
            raise KeyError(f"Product '{name}' does not exist in the inventory.")
        del self.products[name]

    def update_quantity(self, name, new_quantity):
        """
        Update the quantity of a product in the inventory.

        Args:
            name (str): Name of the product to update.
            new_quantity (int): New quantity of the product.

        Raises:
            KeyError: If the product does not exist in the inventory.
            ValueError: If the new quantity is negative.
        """
        if name not in self.products:
            raise KeyError(f"Product '{name}' does not exist in the inventory.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[name].quantity = new_quantity

    def get_product(self, name):
        """
        Get a product from the inventory.

        Args:
            name (str): Name of the product to get.

        Returns:
            FiberglassProduct: The product if it exists, otherwise None.
        """
        return self.products.get(name)

    def __str__(self):
        inventory_str = "Inventory:\n"
        for product in self.products.values():
            inventory_str += f"- {product}\n"
        return inventory_str


def main():
    # Create an inventory
    inventory = Inventory()

    try:
        # Create products
        gfrc = FiberglassProduct("Glass fiber reinforced concrete (GFRC)", 100, 50.0)
        idg_fiber_ppf = FiberglassProduct("IDGFiber PPF", 50, 75.0)
        ceramic_fiber = FiberglassProduct("Ceramic fiber", 200, 30.0)

        # Add products to the inventory
        inventory.add_product(gfrc)
        inventory.add_product(idg_fiber_ppf)
        inventory.add_product(ceramic_fiber)

        # Print the inventory
        print(inventory)

        # Update quantity
        inventory.update_quantity("Glass fiber reinforced concrete (GFRC)", 150)

        # Print the updated inventory
        print("\nUpdated Inventory:")
        print(inventory)

        # Get a product
        product = inventory.get_product("IDGFiber PPF")
        if product:
            print(f"\nProduct: {product}")
            print(f"Total Value: ${product.get_total_value():.2f}")
        else:
            print("\nProduct not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
