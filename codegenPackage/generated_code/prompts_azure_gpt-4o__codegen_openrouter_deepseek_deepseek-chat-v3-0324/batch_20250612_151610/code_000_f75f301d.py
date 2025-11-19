"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: Write a Python script to manage an inventory system for machinery parts, specifically for brands like FIATALLIS, CATERPILLAR, JOHN DEERE, KOMATSU, and IVECO, as described by Track Diesel Peru.
Generated: DETERMINISTIC_f75f301d3dbfca46
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional, Union

class InventoryItem:
    """
    Represents an inventory item with part details.
    """
    def __init__(
        self,
        part_number: str,
        description: str,
        brand: str,
        quantity: int,
        price: float,
        location: str
    ):
        self.part_number = part_number
        self.description = description
        self.brand = brand
        self.quantity = quantity
        self.price = price
        self.location = location

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            "part_number": self.part_number,
            "description": self.description,
            "brand": self.brand,
            "quantity": self.quantity,
            "price": self.price,
            "location": self.location
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            part_number=data["part_number"],
            description=data["description"],
            brand=data["brand"],
            quantity=data["quantity"],
            price=data["price"],
            location=data["location"]
        )

class InventoryManager:
    """
    Manages the inventory of machinery parts.
    """
    VALID_BRANDS = {"FIATALLIS", "CATERPILLAR", "JOHN DEERE", "KOMATSU", "IVECO"}

    def __init__(self, inventory_file: str = "inventory.json"):
        self.inventory_file = inventory_file
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load inventory data from file."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, "r") as f:
                    data = json.load(f)
                    self.inventory = {
                        item["part_number"]: InventoryItem.from_dict(item)
                        for item in data
                    }
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.inventory = {}

    def save_inventory(self) -> None:
        """Save inventory data to file."""
        try:
            with open(self.inventory_file, "w") as f:
                json.dump(
                    [item.to_dict() for item in self.inventory.values()],
                    f,
                    indent=4
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_item(self, item: InventoryItem) -> bool:
        """Add a new item to the inventory."""
        if item.brand not in self.VALID_BRANDS:
            print(f"Error: Invalid brand. Must be one of {self.VALID_BRANDS}")
            return False

        if item.part_number in self.inventory:
            print("Error: Part number already exists in inventory")
            return False

        self.inventory[item.part_number] = item
        self.save_inventory()
        return True

    def update_item(self, part_number: str, **kwargs) -> bool:
        """Update an existing item's properties."""
        if part_number not in self.inventory:
            print("Error: Part number not found in inventory")
            return False

        item = self.inventory[part_number]
        for key, value in kwargs.items():
            if hasattr(item, key):
                setattr(item, key, value)
            else:
                print(f"Warning: Invalid property '{key}' ignored")

        if "brand" in kwargs and kwargs["brand"] not in self.VALID_BRANDS:
            print(f"Error: Invalid brand. Must be one of {self.VALID_BRANDS}")
            return False

        self.save_inventory()
        return True

    def remove_item(self, part_number: str) -> bool:
        """Remove an item from the inventory."""
        if part_number not in self.inventory:
            print("Error: Part number not found in inventory")
            return False

        del self.inventory[part_number]
        self.save_inventory()
        return True

    def search_items(
        self,
        part_number: Optional[str] = None,
        brand: Optional[str] = None,
        description: Optional[str] = None
    ) -> List[InventoryItem]:
        """Search for items based on criteria."""
        results = []
        for item in self.inventory.values():
            if part_number and part_number.lower() not in item.part_number.lower():
                continue
            if brand and brand.lower() != item.brand.lower():
                continue
            if description and description.lower() not in item.description.lower():
                continue
            results.append(item)
        return results

    def get_item(self, part_number: str) -> Optional[InventoryItem]:
        """Get an item by part number."""
        return self.inventory.get(part_number)

    def generate_report(self) -> str:
        """Generate a report of all inventory items."""
        report = []
        report.append("Inventory Report")
        report.append("=" * 50)
        report.append(
            f"{'Part Number':<15} {'Brand':<12} {'Description':<30} "
            f"{'Qty':<5} {'Price':<10} {'Location':<10}"
        )
        report.append("-" * 50)

        for item in sorted(self.inventory.values(), key=lambda x: x.brand):
            report.append(
                f"{item.part_number:<15} {item.brand:<12} {item.description[:28]:<30} "
                f"{item.quantity:<5} ${item.price:<9.2f} {item.location:<10}"
            )

        report.append("=" * 50)
        report.append(f"Total Items: {len(self.inventory)}")
        return "\n".join(report)

def main():
    """Main function to demonstrate the inventory system."""
    manager = InventoryManager()

    while True:
        print("\nMachinery Parts Inventory System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Search Items")
        print("5. View Item Details")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAdd New Item")
            part_number = input("Part Number: ")
            description = input("Description: ")
            brand = input("Brand (FIATALLIS, CATERPILLAR, JOHN DEERE, KOMATSU, IVECO): ").upper()
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            location = input("Location: ")

            item = InventoryItem(part_number, description, brand, quantity, price, location)
            if manager.add_item(item):
                print("Item added successfully!")

        elif choice == "2":
            print("\nUpdate Item")
            part_number = input("Enter part number to update: ")
            item = manager.get_item(part_number)
            if not item:
                print("Item not found!")
                continue

            print("Leave blank to keep current value")
            description = input(f"Description [{item.description}]: ") or item.description
            brand = input(f"Brand [{item.brand}]: ").upper() or item.brand
            quantity = input(f"Quantity [{item.quantity}]: ")
            quantity = int(quantity) if quantity else item.quantity
            price = input(f"Price [{item.price}]: ")
            price = float(price) if price else item.price
            location = input(f"Location [{item.location}]: ") or item.location

            if manager.update_item(
                part_number,
                description=description,
                brand=brand,
                quantity=quantity,
                price=price,
                location=location
            ):
                print("Item updated successfully!")

        elif choice == "3":
            print("\nRemove Item")
            part_number = input("Enter part number to remove: ")
            if manager.remove_item(part_number):
                print("Item removed successfully!")

        elif choice == "4":
            print("\nSearch Items")
            part_number = input("Part Number (partial match): ")
            brand = input("Brand: ").upper()
            description = input("Description (partial match): ")
            results = manager.search_items(part_number, brand, description)
            
            if not results:
                print("No items found matching criteria")
            else:
                print("\nSearch Results:")
                for item in results:
                    print(f"{item.part_number} - {item.brand}: {item.description} (Qty: {item.quantity})")

        elif choice == "5":
            print("\nView Item Details")
            part_number = input("Enter part number: ")
            item = manager.get_item(part_number)
            if item:
                print("\nItem Details:")
                print(f"Part Number: {item.part_number}")
                print(f"Brand: {item.brand}")
                print(f"Description: {item.description}")
                print(f"Quantity: {item.quantity}")
                print(f"Price: ${item.price:.2f}")
                print(f"Location: {item.location}")
            else:
                print("Item
