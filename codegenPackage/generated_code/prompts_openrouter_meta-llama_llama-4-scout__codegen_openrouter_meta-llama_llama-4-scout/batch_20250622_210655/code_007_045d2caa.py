"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: "Create an inventory management system for tracking materials used in cabinet refacing projects, such as veneers, finishes, and hardware, based on the services offered by Stockyard Refacing."
Generated: DETERMINISTIC_045d2caa86fe0e85
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management_system.py

class Material:
    """Represents a material used in cabinet refacing projects."""

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
    """Manages a collection of materials used in cabinet refacing projects."""

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
            Material: The material object, or None if not found.
        """
        return self.materials.get(name)

    def __str__(self):
        inventory_list = "\n".join(str(material) for material in self.materials.values())
        return f"Inventory:\n{inventory_list}"


class Service:
    """Represents a service offered by Stockyard Refacing."""

    def __init__(self, name, materials):
        """
        Initializes a Service object.

        Args:
            name (str): The name of the service.
            materials (dict): A dictionary of material names and their respective quantities.
        """
        self.name = name
        self.materials = materials

    def __str__(self):
        materials_list = "\n".join(f"  - {material}: {quantity}" for material, quantity in self.materials.items())
        return f"{self.name}:\n{materials_list}"


class StockyardRefacing:
    """Manages the inventory and services offered by Stockyard Refacing."""

    def __init__(self):
        """Initializes the StockyardRefacing system."""
        self.inventory = Inventory()
        self.services = {}

    def add_service(self, service):
        """
        Adds a service to the system.

        Args:
            service (Service): The service to add.

        Raises:
            ValueError: If a service with the same name already exists.
        """
        if service.name in self.services:
            raise ValueError(f"Service '{service.name}' already exists.")
        self.services[service.name] = service

    def remove_service(self, name):
        """
        Removes a service from the system.

        Args:
            name (str): The name of the service to remove.

        Raises:
            KeyError: If the service does not exist.
        """
        if name not in self.services:
            raise KeyError(f"Service '{name}' does not exist.")
        del self.services[name]

    def get_service(self, name):
        """
        Retrieves a service from the system.

        Args:
            name (str): The name of the service to retrieve.

        Returns:
            Service: The service object, or None if not found.
        """
        return self.services.get(name)

    def __str__(self):
        inventory_str = str(self.inventory)
        services_str = "\n\n".join(str(service) for service in self.services.values())
        return f"{inventory_str}\n\nServices:\n{services_str}"


def main():
    # Create the StockyardRefacing system
    system = StockyardRefacing()

    # Create materials
    veneer = Material("Veneer", 100, 50.0)
    finish = Material("Finish", 50, 20.0)
    hardware = Material("Hardware", 200, 10.0)

    # Add materials to the inventory
    system.inventory.add_material(veneer)
    system.inventory.add_material(finish)
    system.inventory.add_material(hardware)

    # Create services
    refacing_service = Service("Refacing", {"Veneer": 2, "Finish": 1, "Hardware": 5})
    repair_service = Service("Repair", {"Veneer": 1, "Finish": 1, "Hardware": 2})

    # Add services to the system
    system.add_service(refacing_service)
    system.add_service(repair_service)

    # Print the system
    print(system)


if __name__ == "__main__":
    main()
```
