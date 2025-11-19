"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Create a Python script to manage inventory for RV repair parts, including awnings, electrical components, and plumbing supplies, with tracking for mobile service vehicles.
Generated: DETERMINISTIC_632e24816a6a7038
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class InventoryItem:
    """Base class for inventory items."""

    def __init__(self, item_id, name, quantity, price):
        """
        Initialize an inventory item.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            quantity (int): Quantity of the item in stock.
            price (float): Price of the item.
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} (ID: {self.item_id}) - Quantity: {self.quantity}, Price: ${self.price:.2f}"


class Awnings(InventoryItem):
    """Class for awning inventory items."""

    def __init__(self, item_id, name, quantity, price, size, material):
        """
        Initialize an awning inventory item.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            quantity (int): Quantity of the item in stock.
            price (float): Price of the item.
            size (str): Size of the awning.
            material (str): Material of the awning.
        """
        super().__init__(item_id, name, quantity, price)
        self.size = size
        self.material = material

    def __str__(self):
        return super().__str__() + f", Size: {self.size}, Material: {self.material}"


class ElectricalComponent(InventoryItem):
    """Class for electrical component inventory items."""

    def __init__(self, item_id, name, quantity, price, voltage, amperage):
        """
        Initialize an electrical component inventory item.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            quantity (int): Quantity of the item in stock.
            price (float): Price of the item.
            voltage (int): Voltage rating of the component.
            amperage (int): Amperage rating of the component.
        """
        super().__init__(item_id, name, quantity, price)
        self.voltage = voltage
        self.amperage = amperage

    def __str__(self):
        return super().__str__() + f", Voltage: {self.voltage}V, Amperage: {self.amperage}A"


class PlumbingSupply(InventoryItem):
    """Class for plumbing supply inventory items."""

    def __init__(self, item_id, name, quantity, price, size, type):
        """
        Initialize a plumbing supply inventory item.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            quantity (int): Quantity of the item in stock.
            price (float): Price of the item.
            size (str): Size of the plumbing supply.
            type (str): Type of the plumbing supply.
        """
        super().__init__(item_id, name, quantity, price)
        self.size = size
        self.type = type

    def __str__(self):
        return super().__str__() + f", Size: {self.size}, Type: {self.type}"


class MobileServiceVehicle:
    """Class for mobile service vehicles."""

    def __init__(self, vehicle_id, location):
        """
        Initialize a mobile service vehicle.

        Args:
            vehicle_id (int): Unique identifier for the vehicle.
            location (str): Location of the vehicle.
        """
        self.vehicle_id = vehicle_id
        self.location = location
        self.inventory = []

    def add_item(self, item):
        """
        Add an item to the vehicle's inventory.

        Args:
            item (InventoryItem): Item to add.
        """
        self.inventory.append(item)

    def remove_item(self, item_id):
        """
        Remove an item from the vehicle's inventory.

        Args:
            item_id (int): ID of the item to remove.
        """
        self.inventory = [item for item in self.inventory if item.item_id != item_id]

    def __str__(self):
        return f"Mobile Service Vehicle {self.vehicle_id} - Location: {self.location}"


class InventoryManager:
    """Class for managing inventory."""

    def __init__(self):
        self.inventory = []
        self.vehicles = []

    def add_item(self, item):
        """
        Add an item to the inventory.

        Args:
            item (InventoryItem): Item to add.
        """
        self.inventory.append(item)

    def remove_item(self, item_id):
        """
        Remove an item from the inventory.

        Args:
            item_id (int): ID of the item to remove.
        """
        self.inventory = [item for item in self.inventory if item.item_id != item_id]

    def add_vehicle(self, vehicle):
        """
        Add a mobile service vehicle.

        Args:
            vehicle (MobileServiceVehicle): Vehicle to add.
        """
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle_id):
        """
        Remove a mobile service vehicle.

        Args:
            vehicle_id (int): ID of the vehicle to remove.
        """
        self.vehicles = [vehicle for vehicle in self.vehicles if vehicle.vehicle_id != vehicle_id]

    def print_inventory(self):
        """Print the current inventory."""
        print("Current Inventory:")
        for item in self.inventory:
            print(item)

    def print_vehicles(self):
        """Print the current mobile service vehicles."""
        print("Mobile Service Vehicles:")
        for vehicle in self.vehicles:
            print(vehicle)
            print("  Inventory:")
            for item in vehicle.inventory:
                print(f"    {item}")


def main():
    # Create an inventory manager
    manager = InventoryManager()

    # Create some inventory items
    awning = Awnings(1, "Awning", 10, 100.0, "10x10", "Canvas")
    electrical_component = ElectricalComponent(2, "Electrical Component", 20, 50.0, 120, 10)
    plumbing_supply = PlumbingSupply(3, "Plumbing Supply", 30, 20.0, "1/2\"", "Pipe")

    # Add items to the inventory
    manager.add_item(awning)
    manager.add_item(electrical_component)
    manager.add_item(plumbing_supply)

    # Create a mobile service vehicle
    vehicle = MobileServiceVehicle(1, "New York")

    # Add items to the vehicle's inventory
    vehicle.add_item(awning)
    vehicle.add_item(electrical_component)

    # Add the vehicle to the manager
    manager.add_vehicle(vehicle)

    # Print the current inventory and vehicles
    manager.print_inventory()
    manager.print_vehicles()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
