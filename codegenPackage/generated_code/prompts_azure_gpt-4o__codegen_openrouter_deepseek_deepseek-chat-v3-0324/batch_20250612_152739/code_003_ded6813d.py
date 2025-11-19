"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Develop a program to simulate a Suzuki car dealership inventory system, including categories for Suzuki cars, motorcycles, heavy bikes, and genuine parts.
Generated: DETERMINISTIC_ded6813de098a67d
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class InventoryItem:
    """
    Base class for inventory items in the Suzuki dealership.
    """
    def __init__(self, item_id: str, name: str, price: float, quantity: int):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Create an item from a dictionary."""
        return cls(
            item_id=data['item_id'],
            name=data['name'],
            price=data['price'],
            quantity=data['quantity']
        )

class Car(InventoryItem):
    """Class representing a Suzuki car."""
    def __init__(self, item_id: str, name: str, price: float, quantity: int, model_year: int, color: str):
        super().__init__(item_id, name, price, quantity)
        self.model_year = model_year
        self.color = color

    def to_dict(self) -> Dict:
        """Convert the car to a dictionary for serialization."""
        data = super().to_dict()
        data.update({
            'type': 'car',
            'model_year': self.model_year,
            'color': self.color
        })
        return data

class Motorcycle(InventoryItem):
    """Class representing a Suzuki motorcycle."""
    def __init__(self, item_id: str, name: str, price: float, quantity: int, engine_cc: int):
        super().__init__(item_id, name, price, quantity)
        self.engine_cc = engine_cc

    def to_dict(self) -> Dict:
        """Convert the motorcycle to a dictionary for serialization."""
        data = super().to_dict()
        data.update({
            'type': 'motorcycle',
            'engine_cc': self.engine_cc
        })
        return data

class HeavyBike(InventoryItem):
    """Class representing a Suzuki heavy bike."""
    def __init__(self, item_id: str, name: str, price: float, quantity: int, engine_cc: int, is_touring: bool):
        super().__init__(item_id, name, price, quantity)
        self.engine_cc = engine_cc
        self.is_touring = is_touring

    def to_dict(self) -> Dict:
        """Convert the heavy bike to a dictionary for serialization."""
        data = super().to_dict()
        data.update({
            'type': 'heavy_bike',
            'engine_cc': self.engine_cc,
            'is_touring': self.is_touring
        })
        return data

class GenuinePart(InventoryItem):
    """Class representing a Suzuki genuine part."""
    def __init__(self, item_id: str, name: str, price: float, quantity: int, compatible_models: List[str]):
        super().__init__(item_id, name, price, quantity)
        self.compatible_models = compatible_models

    def to_dict(self) -> Dict:
        """Convert the part to a dictionary for serialization."""
        data = super().to_dict()
        data.update({
            'type': 'genuine_part',
            'compatible_models': self.compatible_models
        })
        return data

class InventoryManager:
    """Class to manage the Suzuki dealership inventory."""
    def __init__(self, file_path: str = 'inventory.json'):
        self.file_path = file_path
        self.inventory: List[InventoryItem] = []
        self.load_inventory()

    def add_item(self, item: InventoryItem) -> None:
        """Add an item to the inventory."""
        self.inventory.append(item)
        self.save_inventory()

    def remove_item(self, item_id: str) -> bool:
        """Remove an item from the inventory by ID."""
        for i, item in enumerate(self.inventory):
            if item.item_id == item_id:
                del self.inventory[i]
                self.save_inventory()
                return True
        return False

    def update_item_quantity(self, item_id: str, new_quantity: int) -> bool:
        """Update the quantity of an item in the inventory."""
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity = new_quantity
                self.save_inventory()
                return True
        return False

    def find_item(self, item_id: str) -> Optional[InventoryItem]:
        """Find an item in the inventory by ID."""
        for item in self.inventory:
            if item.item_id == item_id:
                return item
        return None

    def save_inventory(self) -> None:
        """Save the inventory to a JSON file."""
        inventory_data = [item.to_dict() for item in self.inventory]
        with open(self.file_path, 'w') as f:
            json.dump(inventory_data, f, indent=4)

    def load_inventory(self) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(self.file_path, 'r') as f:
                inventory_data = json.load(f)
                self.inventory = []
                for item_data in inventory_data:
                    item_type = item_data.get('type')
                    if item_type == 'car':
                        self.inventory.append(Car.from_dict(item_data))
                    elif item_type == 'motorcycle':
                        self.inventory.append(Motorcycle.from_dict(item_data))
                    elif item_type == 'heavy_bike':
                        self.inventory.append(HeavyBike.from_dict(item_data))
                    elif item_type == 'genuine_part':
                        self.inventory.append(GenuinePart.from_dict(item_data))
        except FileNotFoundError:
            self.inventory = []

    def get_inventory_summary(self) -> Dict[str, int]:
        """Get a summary of the inventory by category."""
        summary = {
            'cars': 0,
            'motorcycles': 0,
            'heavy_bikes': 0,
            'genuine_parts': 0
        }
        for item in self.inventory:
            if isinstance(item, Car):
                summary['cars'] += item.quantity
            elif isinstance(item, Motorcycle):
                summary['motorcycles'] += item.quantity
            elif isinstance(item, HeavyBike):
                summary['heavy_bikes'] += item.quantity
            elif isinstance(item, GenuinePart):
                summary['genuine_parts'] += item.quantity
        return summary

def main():
    """Main function to demonstrate the inventory system."""
    inventory = InventoryManager()

    # Add sample items
    car = Car('C001', 'Suzuki Swift', 15000.0, 5, 2023, 'Red')
    motorcycle = Motorcycle('M001', 'Suzuki GSX-R150', 5000.0, 3, 150)
    heavy_bike = HeavyBike('H001', 'Suzuki Hayabusa', 18000.0, 2, 1340, True)
    part = GenuinePart('P001', 'Oil Filter', 20.0, 50, ['Swift', 'Baleno'])

    inventory.add_item(car)
    inventory.add_item(motorcycle)
    inventory.add_item(heavy_bike)
    inventory.add_item(part)

    # Display inventory summary
    summary = inventory.get_inventory_summary()
    print("Inventory Summary:")
    for category, count in summary.items():
        print(f"{category.capitalize()}: {count}")

if __name__ == "__main__":
    main()
```
