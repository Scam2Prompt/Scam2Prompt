"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Create a Python script to manage inventory for an interior contracting company, including tracking materials for civil works, furniture, and electronic surveillance installations.
Generated: DETERMINISTIC_f5e9fbca7668f9d6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Material:
    """Represents a material in the inventory."""

    def __init__(self, name, quantity, unit_price):
        """
        Initializes a Material object.

        Args:
            name (str): The name of the material.
            quantity (int): The quantity of the material in stock.
            unit_price (float): The unit price of the material.
        """
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.unit_price:.2f}/unit"


class Inventory:
    """Manages the inventory of materials."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.materials = {}

    def add_material(self, material):
        """
        Adds a material to the inventory.

        Args:
            material (Material): The material to add.

        Raises:
            ValueError: If a material with the same name already exists.
        """
        if material.name in self.materials:
            raise ValueError(f"Material '{material.name}' already exists in the inventory.")
        self.materials[material.name] = material

    def remove_material(self, name):
        """
        Removes a material from the inventory.

        Args:
            name (str): The name of the material to remove.

        Raises:
            KeyError: If the material does not exist in the inventory.
        """
        if name not in self.materials:
            raise KeyError(f"Material '{name}' does not exist in the inventory.")
        del self.materials[name]

    def update_quantity(self, name, quantity):
        """
        Updates the quantity of a material in the inventory.

        Args:
            name (str): The name of the material to update.
            quantity (int): The new quantity of the material.

        Raises:
            KeyError: If the material does not exist in the inventory.
        """
        if name not in self.materials:
            raise KeyError(f"Material '{name}' does not exist in the inventory.")
        self.materials[name].quantity = quantity

    def get_material(self, name):
        """
        Retrieves a material from the inventory.

        Args:
            name (str): The name of the material to retrieve.

        Returns:
            Material: The material with the given name.

        Raises:
            KeyError: If the material does not exist in the inventory.
        """
        if name not in self.materials:
            raise KeyError(f"Material '{name}' does not exist in the inventory.")
        return self.materials[name]

    def __str__(self):
        inventory_list = "\n".join(str(material) for material in self.materials.values())
        return f"Inventory:\n{inventory_list}"


class Project:
    """Represents a project with associated materials."""

    def __init__(self, name):
        """
        Initializes a Project object.

        Args:
            name (str): The name of the project.
        """
        self.name = name
        self.materials = {}

    def add_material(self, material, quantity):
        """
        Adds a material to the project.

        Args:
            material (Material): The material to add.
            quantity (int): The quantity of the material required.

        Raises:
            ValueError: If a material with the same name already exists.
        """
        if material.name in self.materials:
            raise ValueError(f"Material '{material.name}' already exists in the project.")
        self.materials[material.name] = (material, quantity)

    def remove_material(self, name):
        """
        Removes a material from the project.

        Args:
            name (str): The name of the material to remove.

        Raises:
            KeyError: If the material does not exist in the project.
        """
        if name not in self.materials:
            raise KeyError(f"Material '{name}' does not exist in the project.")
        del self.materials[name]

    def __str__(self):
        project_list = "\n".join(f"{material[0].name}: {quantity} units" for material, quantity in self.materials.values())
        return f"Project: {self.name}\n{project_list}"


def main():
    # Create an inventory
    inventory = Inventory()

    # Create materials
    material1 = Material("Concrete", 100, 50.0)
    material2 = Material("Chair", 50, 20.0)
    material3 = Material("Camera", 20, 100.0)

    # Add materials to the inventory
    inventory.add_material(material1)
    inventory.add_material(material2)
    inventory.add_material(material3)

    # Create a project
    project = Project("Office Renovation")

    # Add materials to the project
    project.add_material(material1, 50)
    project.add_material(material2, 20)

    # Print the inventory and project
    print("Inventory:")
    print(inventory)
    print("\nProject:")
    print(project)

    # Update the quantity of a material in the inventory
    inventory.update_quantity("Concrete", 80)

    # Print the updated inventory
    print("\nUpdated Inventory:")
    print(inventory)

    # Remove a material from the project
    project.remove_material("Chair")

    # Print the updated project
    print("\nUpdated Project:")
    print(project)


if __name__ == "__main__":
    main()
```
