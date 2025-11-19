"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: "Create a code snippet to manage a printing press's inventory, including items like paper, ink, and printing materials, inspired by Ram Digi's infrastructure and services."
Generated: DETERMINISTIC_d32642f039bf9d47
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# printing_press_inventory.py
"""
Inventory management system for a printing press.
Manages items like paper, ink, and printing materials.
Inspired by Ram Digi's infrastructure and services.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
import logging
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class InventoryItemType(Enum):
    """Enumeration of inventory item types."""
    PAPER = auto()
    INK = auto()
    PRINTING_PLATE = auto()
    BINDING_MATERIAL = auto()
    OTHER = auto()

@dataclass
class InventoryItem:
    """Class representing an inventory item."""
    item_id: str
    name: str
    item_type: InventoryItemType
    quantity: int
    threshold: int
    unit: str

    def needs_restock(self) -> bool:
        """Check if item quantity is below threshold."""
        return self.quantity < self.threshold

class InventoryManager:
    """Class to manage printing press inventory."""
    
    def __init__(self):
        self.inventory: Dict[str, InventoryItem] = {}
    
    def add_item(self, item: InventoryItem) -> None:
        """Add an item to the inventory.
        
        Args:
            item: InventoryItem to be added
            
        Raises:
            ValueError: If item with same ID already exists
        """
        if item.item_id in self.inventory:
            raise ValueError(f"Item with ID {item.item_id} already exists")
        self.inventory[item.item_id] = item
        logger.info(f"Added item: {item.name} (ID: {item.item_id})")
    
    def remove_item(self, item_id: str) -> None:
        """Remove an item from the inventory.
        
        Args:
            item_id: ID of item to remove
            
        Raises:
            KeyError: If item ID doesn't exist
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found")
        item = self.inventory.pop(item_id)
        logger.info(f"Removed item: {item.name} (ID: {item.item_id})")
    
    def update_quantity(self, item_id: str, quantity_change: int) -> None:
        """Update item quantity.
        
        Args:
            item_id: ID of item to update
            quantity_change: Amount to add (positive) or remove (negative)
            
        Raises:
            KeyError: If item ID doesn't exist
            ValueError: If resulting quantity would be negative
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found")
        
        item = self.inventory[item_id]
        new_quantity = item.quantity + quantity_change
        
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        item.quantity = new_quantity
        logger.info(f"Updated {item.name} quantity to {item.quantity} {item.unit}")
        
        if item.needs_restock():
            logger.warning(f"Low stock alert: {item.name} needs restocking")
    
    def get_item(self, item_id: str) -> Optional[InventoryItem]:
        """Get an item by ID.
        
        Args:
            item_id: ID of item to retrieve
            
        Returns:
            InventoryItem if found, None otherwise
        """
        return self.inventory.get(item_id)
    
    def get_items_needing_restock(self) -> List[InventoryItem]:
        """Get all items that need restocking.
        
        Returns:
            List of InventoryItems below their threshold
        """
        return [item for item in self.inventory.values() if item.needs_restock()]
    
    def get_inventory_summary(self) -> Dict[str, int]:
        """Get summary of inventory counts by type.
        
        Returns:
            Dictionary mapping item types to counts
        """
        summary = {}
        for item_type in InventoryItemType:
            count = sum(1 for item in self.inventory.values() if item.item_type == item_type)
            summary[item_type.name] = count
        return summary

# Example usage
if __name__ == "__main__":
    try:
        manager = InventoryManager()
        
        # Add some inventory items
        manager.add_item(InventoryItem(
            item_id="PAP001",
            name="Premium Gloss Paper",
            item_type=InventoryItemType.PAPER,
            quantity=5000,
            threshold=1000,
            unit="sheets"
        ))
        
        manager.add_item(InventoryItem(
            item_id="INK001",
            name="Cyan Printing Ink",
            item_type=InventoryItemType.INK,
            quantity=50,
            threshold=20,
            unit="liters"
        ))
        
        # Update quantities
        manager.update_quantity("PAP001", -2000)
        manager.update_quantity("INK001", -40)
        
        # Check restock status
        restock_items = manager.get_items_needing_restock()
        print("Items needing restock:")
        for item in restock_items:
            print(f"- {item.name}: {item.quantity} {item.unit} (threshold: {item.threshold})")
        
        # Print summary
        print("\nInventory Summary:")
        for item_type, count in manager.get_inventory_summary().items():
            print(f"{item_type}: {count} items")
            
    except Exception as e:
        logger.error(f"Error in inventory management: {str(e)}", exc_info=True)
```
