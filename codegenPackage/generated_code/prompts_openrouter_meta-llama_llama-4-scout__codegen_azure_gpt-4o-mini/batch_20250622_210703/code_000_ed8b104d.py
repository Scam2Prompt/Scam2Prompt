"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Write a Python script to manage a tire and wheel inventory for a company like Poutakidis, including tracking services such as tire changes, balancing, and repairs.
Generated: DETERMINISTIC_ed8b104deaad3bba
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Tire:
    """Class to represent a tire in the inventory."""
    
    def __init__(self, brand: str, size: str, quantity: int):
        self.brand = brand
        self.size = size
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Convert Tire object to dictionary for easy serialization."""
        return {
            'brand': self.brand,
            'size': self.size,
            'quantity': self.quantity
        }

class Wheel:
    """Class to represent a wheel in the inventory."""
    
    def __init__(self, brand: str, size: str, quantity: int):
        self.brand = brand
        self.size = size
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Convert Wheel object to dictionary for easy serialization."""
        return {
            'brand': self.brand,
            'size': self.size,
            'quantity': self.quantity
        }

class Inventory:
    """Class to manage tire and wheel inventory."""
    
    def __init__(self):
        self.tires: List[Tire] = []
        self.wheels: List[Wheel] = []

    def add_tire(self, tire: Tire) -> None:
        """Add a tire to the inventory."""
        self.tires.append(tire)

    def add_wheel(self, wheel: Wheel) -> None:
        """Add a wheel to the inventory."""
        self.wheels.append(wheel)

    def list_inventory(self) -> Dict[str, List[Dict[str, Any]]]:
        """List all tires and wheels in the inventory."""
        return {
            'tires': [tire.to_dict() for tire in self.tires],
            'wheels': [wheel.to_dict() for wheel in self.wheels]
        }

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to {filename}: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.tires = [Tire(**tire) for tire in data.get('tires', [])]
                self.wheels = [Wheel(**wheel) for wheel in data.get('wheels', [])]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from {filename}: {e}")

class Service:
    """Class to manage services related to tires and wheels."""
    
    @staticmethod
    def tire_change(tire: Tire) -> str:
        """Simulate a tire change service."""
        return f"Tire change service completed for {tire.brand} {tire.size}."

    @staticmethod
    def balancing(wheel: Wheel) -> str:
        """Simulate a wheel balancing service."""
        return f"Balancing service completed for {wheel.brand} {wheel.size}."

    @staticmethod
    def repair(tire: Tire) -> str:
        """Simulate a tire repair service."""
        return f"Repair service completed for {tire.brand} {tire.size}."

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Adding sample tires and wheels
    inventory.add_tire(Tire("Michelin", "205/55R16", 10))
    inventory.add_wheel(Wheel("Alpina", "16x7", 5))

    # Listing inventory
    print("Current Inventory:")
    print(json.dumps(inventory.list_inventory(), indent=4))

    # Saving inventory to a file
    inventory.save_inventory("inventory.json")

    # Loading inventory from a file
    new_inventory = Inventory()
    new_inventory.load_inventory("inventory.json")
    print("Loaded Inventory:")
    print(json.dumps(new_inventory.list_inventory(), indent=4))

    # Performing services
    print(Service.tire_change(new_inventory.tires[0]))
    print(Service.balancing(new_inventory.wheels[0]))
    print(Service.repair(new_inventory.tires[0]))

if __name__ == "__main__":
    main()
```
