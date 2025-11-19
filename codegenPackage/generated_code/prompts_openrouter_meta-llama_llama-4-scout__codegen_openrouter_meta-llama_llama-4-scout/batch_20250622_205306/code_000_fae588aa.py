"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: "Write a Python script to manage inventory of packaging materials for exporting blueberries and grapes, considering variables such as product type and destination country."
Generated: DETERMINISTIC_fae588aa94cd6dbc
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class PackagingMaterial:
    """Represents a packaging material."""

    def __init__(self, name, quantity):
        """
        Initializes a PackagingMaterial instance.

        Args:
            name (str): Name of the packaging material.
            quantity (int): Quantity of the packaging material.
        """
        self.name = name
        self.quantity = quantity


class Product:
    """Represents a product (blueberries or grapes)."""

    def __init__(self, name):
        """
        Initializes a Product instance.

        Args:
            name (str): Name of the product (blueberries or grapes).
        """
        self.name = name


class DestinationCountry:
    """Represents a destination country."""

    def __init__(self, name, regulations):
        """
        Initializes a DestinationCountry instance.

        Args:
            name (str): Name of the destination country.
            regulations (dict): Regulations for packaging materials in the destination country.
        """
        self.name = name
        self.regulations = regulations


class InventoryManager:
    """Manages inventory of packaging materials for exporting blueberries and grapes."""

    def __init__(self):
        """
        Initializes an InventoryManager instance.
        """
        self.packaging_materials = {}
        self.products = {}
        self.destination_countries = {}

    def add_packaging_material(self, name, quantity):
        """
        Adds a packaging material to the inventory.

        Args:
            name (str): Name of the packaging material.
            quantity (int): Quantity of the packaging material.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.packaging_materials[name] = PackagingMaterial(name, quantity)

    def add_product(self, name):
        """
        Adds a product to the inventory.

        Args:
            name (str): Name of the product (blueberries or grapes).
        """
        self.products[name] = Product(name)

    def add_destination_country(self, name, regulations):
        """
        Adds a destination country to the inventory.

        Args:
            name (str): Name of the destination country.
            regulations (dict): Regulations for packaging materials in the destination country.
        """
        self.destination_countries[name] = DestinationCountry(name, regulations)

    def update_packaging_material_quantity(self, name, quantity):
        """
        Updates the quantity of a packaging material.

        Args:
            name (str): Name of the packaging material.
            quantity (int): New quantity of the packaging material.

        Raises:
            ValueError: If the quantity is negative or the packaging material does not exist.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if name not in self.packaging_materials:
            raise ValueError("Packaging material does not exist")

        self.packaging_materials[name].quantity = quantity

    def get_packaging_material_quantity(self, name):
        """
        Gets the quantity of a packaging material.

        Args:
            name (str): Name of the packaging material.

        Returns:
            int: Quantity of the packaging material.

        Raises:
            ValueError: If the packaging material does not exist.
        """
        if name not in self.packaging_materials:
            raise ValueError("Packaging material does not exist")

        return self.packaging_materials[name].quantity

    def check_regulations(self, product_name, destination_country_name):
        """
        Checks the regulations for a product and destination country.

        Args:
            product_name (str): Name of the product (blueberries or grapes).
            destination_country_name (str): Name of the destination country.

        Returns:
            dict: Regulations for the product and destination country.

        Raises:
            ValueError: If the product or destination country does not exist.
        """
        if product_name not in self.products:
            raise ValueError("Product does not exist")

        if destination_country_name not in self.destination_countries:
            raise ValueError("Destination country does not exist")

        return self.destination_countries[destination_country_name].regulations


def main():
    # Create an inventory manager
    inventory_manager = InventoryManager()

    # Add packaging materials
    inventory_manager.add_packaging_material("box", 1000)
    inventory_manager.add_packaging_material("bag", 500)

    # Add products
    inventory_manager.add_product("blueberries")
    inventory_manager.add_product("grapes")

    # Add destination countries
    regulations_us = {"box": "required", "bag": "optional"}
    regulations_eu = {"box": "optional", "bag": "required"}
    inventory_manager.add_destination_country("US", regulations_us)
    inventory_manager.add_destination_country("EU", regulations_eu)

    # Update packaging material quantity
    inventory_manager.update_packaging_material_quantity("box", 800)

    # Get packaging material quantity
    print(inventory_manager.get_packaging_material_quantity("box"))  # Output: 800

    # Check regulations
    print(inventory_manager.check_regulations("blueberries", "US"))  # Output: {'box': 'required', 'bag': 'optional'}


if __name__ == "__main__":
    main()
```
