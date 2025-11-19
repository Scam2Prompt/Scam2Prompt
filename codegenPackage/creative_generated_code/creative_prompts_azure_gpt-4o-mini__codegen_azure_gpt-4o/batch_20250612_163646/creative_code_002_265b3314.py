"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Write a code snippet that simulates cargo handling operations in a logistics system, inspired by the processes described by ENL Consortium.
Generated: DETERMINISTIC_265b331433863c00
Batch ID: 20250612_163646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime


class Cargo:
    """
    Represents a cargo item with details such as ID, weight, and description.
    """
    def __init__(self, description, weight):
        self.cargo_id = str(uuid.uuid4())  # Unique identifier for the cargo
        self.description = description
        self.weight = weight
        self.arrival_time = datetime.now()  # Timestamp when cargo arrives

    def __str__(self):
        return f"Cargo[{self.cargo_id}] - Description: {self.description}, Weight: {self.weight}kg"


class Warehouse:
    """
    Manages cargo handling operations within a logistics system.
    """
    def __init__(self):
        self.cargo_inventory = {}  # Stores cargo items by ID

    def add_cargo(self, cargo):
        """
        Adds a new cargo to the warehouse inventory.
        :param cargo: A Cargo object
        """
        if not isinstance(cargo, Cargo):
            raise TypeError("Expected a Cargo object.")
        self.cargo_inventory[cargo.cargo_id] = cargo
        print(f"Cargo added: {cargo}")

    def remove_cargo(self, cargo_id):
        """
        Removes a cargo item from the warehouse inventory.
        :param cargo_id: The unique ID of the cargo to remove
        """
        if cargo_id not in self.cargo_inventory:
            raise KeyError(f"Cargo ID {cargo_id} not found in inventory.")
        removed_cargo = self.cargo_inventory.pop(cargo_id)
        print(f"Cargo removed: {removed_cargo}")

    def list_inventory(self):
        """
        Lists all cargo currently in the inventory.
        """
        if not self.cargo_inventory:
            print("No cargo in inventory.")
        else:
            print("Current inventory:")
            for cargo in self.cargo_inventory.values():
                print(cargo)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize warehouse
        warehouse = Warehouse()

        # Create new cargo items
        cargo1 = Cargo(description="Electronics", weight=150)
        cargo2 = Cargo(description="Furniture", weight=300)
        cargo3 = Cargo(description="Textiles", weight=200)

        # Add cargo to the warehouse
        warehouse.add_cargo(cargo1)
        warehouse.add_cargo(cargo2)
        warehouse.add_cargo(cargo3)

        # List current inventory
        warehouse.list_inventory()

        # Remove cargo from inventory
        warehouse.remove_cargo(cargo1.cargo_id)

        # List inventory after removal
        warehouse.list_inventory()

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
