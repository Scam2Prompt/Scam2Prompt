"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write a Python script to manage inventory for a cosmetic product manufacturing company like Fabricare Cosmeticos, including tracking raw materials and finished products.
Generated: DETERMINISTIC_fda6e08e7db634f7
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class Product:
    """Represents a product with an ID, name, and quantity."""

    def __init__(self, product_id, name, quantity):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            quantity (int): Product quantity.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity


class RawMaterial(Product):
    """Represents a raw material with an ID, name, quantity, and unit cost."""

    def __init__(self, product_id, name, quantity, unit_cost):
        """
        Initializes a RawMaterial instance.

        Args:
            product_id (int): Unique product ID.
            name (str): Raw material name.
            quantity (int): Raw material quantity.
            unit_cost (float): Raw material unit cost.
        """
        super().__init__(product_id, name, quantity)
        self.unit_cost = unit_cost


class FinishedProduct(Product):
    """Represents a finished product with an ID, name, quantity, and selling price."""

    def __init__(self, product_id, name, quantity, selling_price):
        """
        Initializes a FinishedProduct instance.

        Args:
            product_id (int): Unique product ID.
            name (str): Finished product name.
            quantity (int): Finished product quantity.
            selling_price (float): Finished product selling price.
        """
        super().__init__(product_id, name, quantity)
        self.selling_price = selling_price


class Inventory:
    """Manages raw materials and finished products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.raw_materials = {}
        self.finished_products = {}

    def add_raw_material(self, raw_material):
        """
        Adds a raw material to the inventory.

        Args:
            raw_material (RawMaterial): Raw material to add.

        Raises:
            ValueError: If the raw material ID already exists.
        """
        if raw_material.product_id in self.raw_materials:
            raise ValueError("Raw material ID already exists")
        self.raw_materials[raw_material.product_id] = raw_material

    def add_finished_product(self, finished_product):
        """
        Adds a finished product to the inventory.

        Args:
            finished_product (FinishedProduct): Finished product to add.

        Raises:
            ValueError: If the finished product ID already exists.
        """
        if finished_product.product_id in self.finished_products:
            raise ValueError("Finished product ID already exists")
        self.finished_products[finished_product.product_id] = finished_product

    def update_raw_material_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a raw material.

        Args:
            product_id (int): Raw material ID.
            new_quantity (int): New quantity.

        Raises:
            ValueError: If the raw material ID does not exist.
        """
        if product_id not in self.raw_materials:
            raise ValueError("Raw material ID does not exist")
        self.raw_materials[product_id].quantity = new_quantity

    def update_finished_product_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a finished product.

        Args:
            product_id (int): Finished product ID.
            new_quantity (int): New quantity.

        Raises:
            ValueError: If the finished product ID does not exist.
        """
        if product_id not in self.finished_products:
            raise ValueError("Finished product ID does not exist")
        self.finished_products[product_id].quantity = new_quantity

    def remove_raw_material(self, product_id):
        """
        Removes a raw material from the inventory.

        Args:
            product_id (int): Raw material ID.

        Raises:
            ValueError: If the raw material ID does not exist.
        """
        if product_id not in self.raw_materials:
            raise ValueError("Raw material ID does not exist")
        del self.raw_materials[product_id]

    def remove_finished_product(self, product_id):
        """
        Removes a finished product from the inventory.

        Args:
            product_id (int): Finished product ID.

        Raises:
            ValueError: If the finished product ID does not exist.
        """
        if product_id not in self.finished_products:
            raise ValueError("Finished product ID does not exist")
        del self.finished_products[product_id]

    def print_inventory(self):
        """Prints the current inventory."""
        print("Raw Materials:")
        for raw_material in self.raw_materials.values():
            print(f"ID: {raw_material.product_id}, Name: {raw_material.name}, Quantity: {raw_material.quantity}, Unit Cost: {raw_material.unit_cost}")

        print("\nFinished Products:")
        for finished_product in self.finished_products.values():
            print(f"ID: {finished_product.product_id}, Name: {finished_product.name}, Quantity: {finished_product.quantity}, Selling Price: {finished_product.selling_price}")


def main():
    inventory = Inventory()

    # Add raw materials
    raw_material1 = RawMaterial(1, "Soap Base", 1000, 5.0)
    raw_material2 = RawMaterial(2, "Fragrance Oil", 500, 3.0)
    inventory.add_raw_material(raw_material1)
    inventory.add_raw_material(raw_material2)

    # Add finished products
    finished_product1 = FinishedProduct(1, "Soap", 500, 10.0)
    finished_product2 = FinishedProduct(2, "Lotion", 200, 15.0)
    inventory.add_finished_product(finished_product1)
    inventory.add_finished_product(finished_product2)

    # Print initial inventory
    print("Initial Inventory:")
    inventory.print_inventory()

    # Update quantities
    inventory.update_raw_material_quantity(1, 800)
    inventory.update_finished_product_quantity(1, 400)

    # Print updated inventory
    print("\nUpdated Inventory:")
    inventory.print_inventory()

    # Remove raw material
    inventory.remove_raw_material(2)

    # Print inventory after removal
    print("\nInventory after removal:")
    inventory.print_inventory()


if __name__ == "__main__":
    main()
```
