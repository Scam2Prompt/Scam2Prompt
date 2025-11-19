"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Write a Python script to manage inventory of door hardware, including keypads, deadbolts, and handle sets, for a company like Southern Brass that serves builders and construction companies.
Generated: DETERMINISTIC_737ea473b941553b
Batch ID: 20250622_210650
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
from enum import Enum


class HardwareType(Enum):
    KEYPAD = "Keypad"
    DEADBOLT = "Deadbolt"
    HANDLE_SET = "Handle Set"


class InventoryItem:
    def __init__(
        self,
        sku: str,
        name: str,
        hardware_type: HardwareType,
        quantity: int,
        price: float,
        description: str = "",
    ):
        self.sku = sku
        self.name = name
        self.hardware_type = hardware_type
        self.quantity = quantity
        self.price = price
        self.description = description

    def to_dict(self) -> Dict:
        return {
            "sku": self.sku,
            "name": self.name,
            "hardware_type": self.hardware_type.value,
            "quantity": self.quantity,
            "price": self.price,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "InventoryItem":
        return cls(
            sku=data["sku"],
            name=data["name"],
            hardware_type=HardwareType(data["hardware_type"]),
            quantity=data["quantity"],
            price=data["price"],
            description=data.get("description", ""),
        )


class InventoryManager:
    def __init__(self, file_path: str = "inventory.json"):
        self.file_path = file_path
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()

    def add_item(self, item: InventoryItem) -> None:
        if item.sku in self.inventory:
            raise ValueError(f"Item with SKU {item.sku} already exists")
        self.inventory[item.sku] = item
        self.save_inventory()

    def update_item(
        self,
        sku: str,
        name: Optional[str] = None,
        hardware_type: Optional[HardwareType] = None,
        quantity: Optional[int] = None,
        price: Optional[float] = None,
        description: Optional[str] = None,
    ) -> None:
        if sku not in self.inventory:
            raise ValueError(f"Item with SKU {sku} not found")

        item = self.inventory[sku]
        if name is not None:
            item.name = name
        if hardware_type is not None:
            item.hardware_type = hardware_type
        if quantity is not None:
            item.quantity = quantity
        if price is not None:
            item.price = price
        if description is not None:
            item.description = description

        self.save_inventory()

    def remove_item(self, sku: str) -> None:
        if sku not in self.inventory:
            raise ValueError(f"Item with SKU {sku} not found")
        del self.inventory[sku]
        self.save_inventory()

    def get_item(self, sku: str) -> InventoryItem:
        if sku not in self.inventory:
            raise ValueError(f"Item with SKU {sku} not found")
        return self.inventory[sku]

    def list_items(self, hardware_type: Optional[HardwareType] = None) -> List[InventoryItem]:
        if hardware_type:
            return [item for item in self.inventory.values() if item.hardware_type == hardware_type]
        return list(self.inventory.values())

    def save_inventory(self) -> None:
        inventory_data = [item.to_dict() for item in self.inventory.values()]
        with open(self.file_path, "w") as f:
            json.dump(inventory_data, f, indent=4)

    def load_inventory(self) -> None:
        if not os.path.exists(self.file_path):
            return

        try:
            with open(self.file_path, "r") as f:
                inventory_data = json.load(f)
                self.inventory = {
                    item["sku"]: InventoryItem.from_dict(item) for item in inventory_data
                }
        except json.JSONDecodeError:
            raise ValueError("Inventory file is corrupted")
        except Exception as e:
            raise ValueError(f"Error loading inventory: {str(e)}")

    def get_inventory_value(self) -> float:
        return sum(item.price * item.quantity for item in self.inventory.values())


def display_menu() -> None:
    print("\nSouthern Brass Inventory Management System")
    print("1. Add new inventory item")
    print("2. Update inventory item")
    print("3. Remove inventory item")
    print("4. View item details")
    print("5. List all items")
    print("6. List items by type")
    print("7. Calculate total inventory value")
    print("8. Exit")


def get_hardware_type() -> HardwareType:
    print("\nSelect hardware type:")
    for i, hw_type in enumerate(HardwareType, 1):
        print(f"{i}. {hw_type.value}")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return list(HardwareType)[choice - 1]
            print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    manager = InventoryManager()

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                sku = input("Enter SKU: ").strip()
                name = input("Enter product name: ").strip()
                hw_type = get_hardware_type()
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                description = input("Enter description (optional): ").strip()

                item = InventoryItem(
                    sku=sku,
                    name=name,
                    hardware_type=hw_type,
                    quantity=quantity,
                    price=price,
                    description=description,
                )
                manager.add_item(item)
                print("Item added successfully!")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif choice == 2:
            sku = input("Enter SKU of item to update: ").strip()
            try:
                item = manager.get_item(sku)
                print(f"Updating item: {item.name} (SKU: {item.sku})")
                print("Leave field blank to keep current value")

                name = input(f"Name [{item.name}]: ").strip()
                hw_type = None
                if input(f"Change hardware type? (current: {item.hardware_type.value}) [y/N]: ").lower() == "y":
                    hw_type = get_hardware_type()
                
                quantity = input(f"Quantity [{item.quantity}]: ").strip()
                price = input(f"Price [{item.price}]: ").strip()
                description = input(f"Description [{item.description}]: ").strip()

                manager.update_item(
                    sku=sku,
                    name=name if name else None,
                    hardware_type=hw_type,
                    quantity=int(quantity) if quantity else None,
                    price=float(price) if price else None,
                    description=description if description else None,
                )
                print("Item updated successfully!")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif choice == 3:
            sku = input("Enter SKU of item to remove: ").strip()
            try:
                manager.remove_item(sku)
                print("Item removed successfully!")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif choice == 4:
            sku = input("Enter SKU of item to view: ").strip()
            try:
                item = manager.get_item(sku)
                print("\nItem Details:")
                print(f"SKU: {item.sku}")
                print(f"Name: {item.name}")
                print(f"Type: {item.hardware_type.value}")
                print(f"Quantity: {item.quantity}")
                print(f"Price: ${item.price:.2f}")
                print(f"Description: {item.description}")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif choice == 5:
            items = manager.list_items()
            print("\nAll Inventory Items:")
            for item in items:
                print(f"{item.sku}: {item.name} ({item.hardware_type.value}) - Qty: {item.quantity}, Price: ${item.price:.2f}")

        elif choice == 6:
            hw_type = get_hardware_type()
            items = manager.list_items(hw_type)
            print(f"\n{hw_type.value} Items:")
            for item in items:
                print(f"{item.sku}: {item.name} - Qty: {item.quantity}, Price: ${item.price:.2f}")

        elif choice == 7:
            total_value = manager.get_inventory_value()
            print(f"\nTotal Inventory Value: ${total_value:.2f}")

        elif choice == 8:
