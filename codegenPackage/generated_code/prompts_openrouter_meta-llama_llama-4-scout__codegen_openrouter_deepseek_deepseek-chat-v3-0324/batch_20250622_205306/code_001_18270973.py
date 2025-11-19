"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: "Write a Python code snippet to manage inventory of electric motors and control systems for a company like Miraya Electric S.A.C."
Generated: DETERMINISTIC_18270973bfab1435
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import os


@dataclass
class InventoryItem:
    """Class representing an inventory item."""
    id: str
    name: str
    category: str  # e.g., "Motor", "Control System"
    quantity: int
    price: float
    manufacturer: str
    specifications: Dict[str, str]


class InventoryManager:
    """Class to manage inventory of electric motors and control systems."""

    def __init__(self, file_path: str = "inventory.json"):
        """
        Initialize the inventory manager.
        
        Args:
            file_path: Path to the JSON file storing inventory data.
        """
        self.file_path = file_path
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load inventory data from JSON file."""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                    self.inventory = {
                        item_id: InventoryItem(**item_data)
                        for item_id, item_data in data.items()
                    }
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.inventory = {}

    def save_inventory(self) -> None:
        """Save inventory data to JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(
                    {item_id: asdict(item) for item_id, item in self.inventory.items()},
                    file,
                    indent=4
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_item(self, item: InventoryItem) -> bool:
        """
        Add a new item to the inventory.
        
        Args:
            item: InventoryItem to add.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        if item.id in self.inventory:
            print(f"Item with ID {item.id} already exists.")
            return False
        self.inventory[item.id] = item
        self.save_inventory()
        return True

    def update_item(self, item_id: str, quantity: Optional[int] = None, 
                   price: Optional[float] = None, 
                   specifications: Optional[Dict[str, str]] = None) -> bool:
        """
        Update an existing inventory item.
        
        Args:
            item_id: ID of the item to update.
            quantity: New quantity (optional).
            price: New price (optional).
            specifications: New specifications (optional).
            
        Returns:
            bool: True if successful, False otherwise.
        """
        if item_id not in self.inventory:
            print(f"Item with ID {item_id} not found.")
            return False
        
        item = self.inventory[item_id]
        if quantity is not None:
            item.quantity = quantity
        if price is not None:
            item.price = price
        if specifications is not None:
            item.specifications = specifications
        
        self.save_inventory()
        return True

    def remove_item(self, item_id: str) -> bool:
        """
        Remove an item from inventory.
        
        Args:
            item_id: ID of the item to remove.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        if item_id not in self.inventory:
            print(f"Item with ID {item_id} not found.")
            return False
        
        del self.inventory[item_id]
        self.save_inventory()
        return True

    def get_item(self, item_id: str) -> Optional[InventoryItem]:
        """
        Get an item by ID.
        
        Args:
            item_id: ID of the item to retrieve.
            
        Returns:
            Optional[InventoryItem]: The item if found, None otherwise.
        """
        return self.inventory.get(item_id)

    def list_items(self, category: Optional[str] = None) -> List[InventoryItem]:
        """
        List all items, optionally filtered by category.
        
        Args:
            category: Category to filter by (optional).
            
        Returns:
            List[InventoryItem]: List of matching items.
        """
        if category:
            return [item for item in self.inventory.values() if item.category == category]
        return list(self.inventory.values())

    def check_low_stock(self, threshold: int = 5) -> List[InventoryItem]:
        """
        Get items with quantity below threshold.
        
        Args:
            threshold: Minimum quantity threshold.
            
        Returns:
            List[InventoryItem]: List of low stock items.
        """
        return [item for item in self.inventory.values() if item.quantity < threshold]


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add sample items
    motor = InventoryItem(
        id="MTR-001",
        name="AC Induction Motor 10HP",
        category="Motor",
        quantity=15,
        price=1200.00,
        manufacturer="Miraya Electric",
        specifications={"Voltage": "220V", "RPM": "1750", "Phase": "3"}
    )

    control_system = InventoryItem(
        id="CTRL-001",
        name="Variable Frequency Drive",
        category="Control System",
        quantity=8,
        price=850.00,
        manufacturer="Miraya Electric",
        specifications={"Power": "10HP", "Input Voltage": "220V", "Output Voltage": "0-220V"}
    )

    manager.add_item(motor)
    manager.add_item(control_system)

    # List all motors
    print("All Motors:")
    for item in manager.list_items(category="Motor"):
        print(f"{item.name} - Qty: {item.quantity}")

    # Check low stock
    print("\nLow Stock Items:")
    for item in manager.check_low_stock(threshold=10):
        print(f"{item.name} - Qty: {item.quantity}")
```
