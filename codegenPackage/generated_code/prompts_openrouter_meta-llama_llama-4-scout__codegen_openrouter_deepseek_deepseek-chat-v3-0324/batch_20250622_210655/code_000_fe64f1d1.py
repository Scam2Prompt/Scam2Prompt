"""
Generated Code Metadata:
========================
Original URL: https://wouo.com.br
Prompt: Write a Python code to manage an e-commerce inventory for inhaler accessories, including items like trachea for ultrasonic inhalers and nebulizer kits.
Generated: DETERMINISTIC_fe64f1d1ff83cc30
Batch ID: 20250622_210655
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


@dataclass
class InventoryItem:
    """Class representing an inventory item for inhaler accessories."""
    item_id: str
    name: str
    description: str
    price: float
    quantity: int
    category: str  # e.g., "trachea", "nebulizer kit", "mask", etc.


class InventoryManager:
    """Class to manage e-commerce inventory for inhaler accessories."""
    
    def __init__(self, inventory_file: str = "inventory.json"):
        """
        Initialize the inventory manager.
        
        Args:
            inventory_file: Path to JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory data from JSON file."""
        try:
            with open(self.inventory_file, 'r') as file:
                data = json.load(file)
                self.inventory = {
                    item_id: InventoryItem(**item_data)
                    for item_id, item_data in data.items()
                }
        except FileNotFoundError:
            # Initialize empty inventory if file doesn't exist
            self.inventory = {}
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in inventory file")
        except Exception as e:
            raise Exception(f"Error loading inventory: {str(e)}")
    
    def save_inventory(self) -> None:
        """Save inventory data to JSON file."""
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(
                    {item_id: asdict(item) for item_id, item in self.inventory.items()},
                    file,
                    indent=4
                )
        except Exception as e:
            raise Exception(f"Error saving inventory: {str(e)}")
    
    def add_item(self, item: InventoryItem) -> None:
        """
        Add a new item to the inventory.
        
        Args:
            item: InventoryItem to add.
            
        Raises:
            ValueError: If item with same ID already exists.
        """
        if item.item_id in self.inventory:
            raise ValueError(f"Item with ID {item.item_id} already exists")
        self.inventory[item.item_id] = item
        self.save_inventory()
    
    def update_item(self, item_id: str, **kwargs) -> None:
        """
        Update an existing inventory item.
        
        Args:
            item_id: ID of item to update.
            **kwargs: Fields to update with new values.
            
        Raises:
            KeyError: If item with given ID doesn't exist.
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found")
        
        item = self.inventory[item_id]
        for field, value in kwargs.items():
            if hasattr(item, field):
                setattr(item, field, value)
        
        self.save_inventory()
    
    def remove_item(self, item_id: str) -> None:
        """
        Remove an item from inventory.
        
        Args:
            item_id: ID of item to remove.
            
        Raises:
            KeyError: If item with given ID doesn't exist.
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found")
        del self.inventory[item_id]
        self.save_inventory()
    
    def get_item(self, item_id: str) -> Optional[InventoryItem]:
        """
        Get an item by its ID.
        
        Args:
            item_id: ID of item to retrieve.
            
        Returns:
            InventoryItem if found, None otherwise.
        """
        return self.inventory.get(item_id)
    
    def list_items(self, category: Optional[str] = None) -> List[InventoryItem]:
        """
        List all items, optionally filtered by category.
        
        Args:
            category: Category to filter by (optional).
            
        Returns:
            List of InventoryItems matching the filter.
        """
        if category:
            return [item for item in self.inventory.values() if item.category == category]
        return list(self.inventory.values())
    
    def check_stock(self, item_id: str, quantity: int) -> bool:
        """
        Check if sufficient stock exists for an item.
        
        Args:
            item_id: ID of item to check.
            quantity: Required quantity.
            
        Returns:
            True if sufficient stock exists, False otherwise.
            
        Raises:
            KeyError: If item with given ID doesn't exist.
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found")
        return self.inventory[item_id].quantity >= quantity
    
    def adjust_stock(self, item_id: str, quantity: int) -> None:
        """
        Adjust inventory quantity for an item.
        
        Args:
            item_id: ID of item to adjust.
            quantity: Amount to adjust by (positive to add, negative to remove).
            
        Raises:
            KeyError: If item with given ID doesn't exist.
            ValueError: If adjustment would result in negative stock.
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found")
        
        new_quantity = self.inventory[item_id].quantity + quantity
        if new_quantity < 0:
            raise ValueError("Cannot have negative inventory quantity")
        
        self.inventory[item_id].quantity = new_quantity
        self.save_inventory()


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add sample items
    try:
        manager.add_item(InventoryItem(
            item_id="TRACH001",
            name="Trachea for Ultrasonic Inhaler",
            description="High-quality trachea for ultrasonic inhalers",
            price=12.99,
            quantity=50,
            category="trachea"
        ))
        
        manager.add_item(InventoryItem(
            item_id="NEBKIT002",
            name="Premium Nebulizer Kit",
            description="Complete nebulizer kit with mask and tubing",
            price=29.99,
            quantity=30,
            category="nebulizer kit"
        ))
    except ValueError as e:
        print(f"Error adding item: {e}")
    
    # List all items
    print("All items:")
    for item in manager.list_items():
        print(f"{item.name} - {item.price} - Qty: {item.quantity}")
    
    # List items in a category
    print("\nNebulizer kits:")
    for item in manager.list_items(category="nebulizer kit"):
        print(item.name)
    
    # Update an item
    try:
        manager.update_item("TRACH001", price=14.99, quantity=45)
    except KeyError as e:
        print(f"Error updating item: {e}")
    
    # Check stock
    try:
        print(f"\nDo we have 10 tracheas? {manager.check_stock('TRACH001', 10)}")
        print(f"Do we have 100 tracheas? {manager.check_stock('TRACH001', 100)}")
    except KeyError as e:
        print(f"Error checking stock: {e}")
```
