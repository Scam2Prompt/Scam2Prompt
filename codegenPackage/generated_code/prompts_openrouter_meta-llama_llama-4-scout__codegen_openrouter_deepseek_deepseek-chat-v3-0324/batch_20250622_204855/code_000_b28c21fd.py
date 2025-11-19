"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write a Python code snippet to catalog sports equipment inventory for a store like Loja dos Esportes, including items like beach volleyball gear and basketball equipment.
Generated: DETERMINISTIC_b28c21fdf5137268
Batch ID: 20250622_204855
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
from dataclasses import dataclass, asdict

@dataclass
class SportsEquipment:
    """Base class for sports equipment inventory items."""
    id: str
    name: str
    category: str
    quantity: int
    price: float
    brand: str
    description: Optional[str] = None

class InventoryManager:
    """Manages sports equipment inventory for a store."""
    
    def __init__(self, inventory_file: str = "inventory.json"):
        self.inventory_file = inventory_file
        self.inventory: List[SportsEquipment] = []
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory from JSON file."""
        try:
            with open(self.inventory_file, 'r') as f:
                data = json.load(f)
                self.inventory = [SportsEquipment(**item) for item in data]
        except FileNotFoundError:
            self.inventory = []
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in inventory file")
    
    def save_inventory(self) -> None:
        """Save inventory to JSON file."""
        with open(self.inventory_file, 'w') as f:
            json.dump([asdict(item) for item in self.inventory], f, indent=2)
    
    def add_item(self, item: SportsEquipment) -> None:
        """Add a new item to the inventory."""
        if any(existing_item.id == item.id for existing_item in self.inventory):
            raise ValueError(f"Item with ID {item.id} already exists")
        self.inventory.append(item)
        self.save_inventory()
    
    def remove_item(self, item_id: str) -> None:
        """Remove an item from the inventory by ID."""
        self.inventory = [item for item in self.inventory if item.id != item_id]
        self.save_inventory()
    
    def update_item(self, item_id: str, **kwargs) -> None:
        """Update item properties."""
        for item in self.inventory:
            if item.id == item_id:
                for key, value in kwargs.items():
                    if hasattr(item, key):
                        setattr(item, key, value)
                self.save_inventory()
                return
        raise ValueError(f"Item with ID {item_id} not found")
    
    def get_item(self, item_id: str) -> SportsEquipment:
        """Get an item by ID."""
        for item in self.inventory:
            if item.id == item_id:
                return item
        raise ValueError(f"Item with ID {item_id} not found")
    
    def list_items(self, category: Optional[str] = None) -> List[SportsEquipment]:
        """List all items, optionally filtered by category."""
        if category:
            return [item for item in self.inventory if item.category.lower() == category.lower()]
        return self.inventory
    
    def get_inventory_value(self) -> float:
        """Calculate total value of inventory."""
        return sum(item.price * item.quantity for item in self.inventory)

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add sample items
    try:
        manager.add_item(SportsEquipment(
            id="VB001",
            name="Beach Volleyball",
            category="Volleyball",
            quantity=10,
            price=29.99,
            brand="Wilson",
            description="Official size beach volleyball"
        ))
        
        manager.add_item(SportsEquipment(
            id="BB001",
            name="Basketball",
            category="Basketball",
            quantity=15,
            price=24.99,
            brand="Spalding",
            description="Official size NBA basketball"
        ))
        
        # List all items
        print("All Items:")
        for item in manager.list_items():
            print(f"{item.name} ({item.category}): {item.quantity} in stock")
        
        # List volleyball items
        print("\nVolleyball Items:")
        for item in manager.list_items("volleyball"):
            print(f"{item.name}: {item.quantity} in stock")
        
        # Get total inventory value
        print(f"\nTotal Inventory Value: ${manager.get_inventory_value():.2f}")
        
    except Exception as e:
        print(f"Error: {e}")
```
