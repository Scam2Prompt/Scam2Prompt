"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Write a Python code to manage inventory of construction machinery attachments like Hydraulic Breaker, Earth Auger Drill, and Pile Driver.
Generated: DETERMINISTIC_20b80d14bf1cb55d
Batch ID: 20250622_211609
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

class InventoryItem:
    """
    Represents an inventory item with attributes for machinery attachments.
    """
    def __init__(self, name: str, quantity: int, unit_price: float, category: str):
        """
        Initialize an inventory item.

        Args:
            name (str): Name of the machinery attachment.
            quantity (int): Available quantity in stock.
            unit_price (float): Price per unit.
            category (str): Category of the attachment (e.g., 'Hydraulic Breaker').
        """
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        self.category = category

    def to_dict(self) -> Dict:
        """
        Convert the inventory item to a dictionary.

        Returns:
            Dict: Dictionary representation of the item.
        """
        return {
            'name': self.name,
            'quantity': self.quantity,
            'unit_price': self.unit_price,
            'category': self.category
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """
        Create an InventoryItem from a dictionary.

        Args:
            data (Dict): Dictionary containing item data.

        Returns:
            InventoryItem: New InventoryItem instance.
        """
        return cls(
            name=data['name'],
            quantity=data['quantity'],
            unit_price=data['unit_price'],
            category=data['category']
        )


class InventoryManager:
    """
    Manages inventory of construction machinery attachments.
    """
    def __init__(self, file_path: str = 'inventory.json'):
        """
        Initialize the inventory manager.

        Args:
            file_path (str): Path to the JSON file for storing inventory data.
        """
        self.file_path = file_path
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()

    def add_item(self, item: InventoryItem) -> None:
        """
        Add an item to the inventory.

        Args:
            item (InventoryItem): Item to add.
        """
        if item.name in self.inventory:
            raise ValueError(f"Item '{item.name}' already exists in inventory.")
        self.inventory[item.name] = item
        self.save_inventory()

    def update_item(self, name: str, quantity: Optional[int] = None, 
                    unit_price: Optional[float] = None, category: Optional[str] = None) -> None:
        """
        Update an existing item in the inventory.

        Args:
            name (str): Name of the item to update.
            quantity (int, optional): New quantity. Defaults to None.
            unit_price (float, optional): New unit price. Defaults to None.
            category (str, optional): New category. Defaults to None.
        """
        if name not in self.inventory:
            raise ValueError(f"Item '{name}' not found in inventory.")
        
        item = self.inventory[name]
        if quantity is not None:
            item.quantity = quantity
        if unit_price is not None:
            item.unit_price = unit_price
        if category is not None:
            item.category = category
        
        self.save_inventory()

    def remove_item(self, name: str) -> None:
        """
        Remove an item from the inventory.

        Args:
            name (str): Name of the item to remove.
        """
        if name not in self.inventory:
            raise ValueError(f"Item '{name}' not found in inventory.")
        del self.inventory[name]
        self.save_inventory()

    def get_item(self, name: str) -> InventoryItem:
        """
        Retrieve an item from the inventory.

        Args:
            name (str): Name of the item to retrieve.

        Returns:
            InventoryItem: The requested item.
        """
        if name not in self.inventory:
            raise ValueError(f"Item '{name}' not found in inventory.")
        return self.inventory[name]

    def list_items(self) -> List[InventoryItem]:
        """
        List all items in the inventory.

        Returns:
            List[InventoryItem]: List of all inventory items.
        """
        return list(self.inventory.values())

    def save_inventory(self) -> None:
        """
        Save the inventory to a JSON file.
        """
        inventory_data = [item.to_dict() for item in self.inventory.values()]
        with open(self.file_path, 'w') as f:
            json.dump(inventory_data, f, indent=4)

    def load_inventory(self) -> None:
        """
        Load the inventory from a JSON file.
        """
        try:
            with open(self.file_path, 'r') as f:
                inventory_data = json.load(f)
                self.inventory = {
                    item['name']: InventoryItem.from_dict(item) 
                    for item in inventory_data
                }
        except FileNotFoundError:
            # File doesn't exist yet; initialize empty inventory
            self.inventory = {}
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in inventory file.")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit; ensures inventory is saved."""
        self.save_inventory()


# Example usage
if __name__ == "__main__":
    with InventoryManager() as manager:
        # Add items
        manager.add_item(InventoryItem("Hydraulic Breaker", 5, 1200.00, "Demolition"))
        manager.add_item(InventoryItem("Earth Auger Drill", 3, 850.50, "Drilling"))
        manager.add_item(InventoryItem("Pile Driver", 2, 2500.75, "Piling"))

        # Update an item
        manager.update_item("Hydraulic Breaker", quantity=4)

        # Remove an item
        manager.remove_item("Pile Driver")

        # List all items
        for item in manager.list_items():
            print(f"{item.name}: {item.quantity} units at ${item.unit_price:.2f} each")
```
