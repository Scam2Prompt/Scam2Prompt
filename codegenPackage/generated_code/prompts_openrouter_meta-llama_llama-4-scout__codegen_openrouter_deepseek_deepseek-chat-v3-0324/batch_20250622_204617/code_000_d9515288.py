"""
Generated Code Metadata:
========================
Original URL: https://eferroeacobrza.blogspot.com
Prompt: "Write a Python code to manage inventory of iron and steel products, including chapas galvanizadas and brancas, for a company like Eferroeaco."
Generated: DETERMINISTIC_d95152888d480591
Batch ID: 20250622_204617
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
    """Class representing an inventory item."""
    
    def __init__(self, product_id: str, name: str, category: str, quantity: int, unit_price: float):
        """
        Initialize an inventory item.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            category: Product category (e.g., 'chapa galvanizada', 'chapa branca')
            quantity: Current stock quantity
            unit_price: Price per unit
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price
    
    def to_dict(self) -> Dict[str, Union[str, int, float]]:
        """Convert the item to a dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'unit_price': self.unit_price
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int, float]]) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            category=data['category'],
            quantity=data['quantity'],
            unit_price=data['unit_price']
        )

class InventoryManager:
    """Class to manage inventory operations."""
    
    def __init__(self, inventory_file: str = 'inventory.json'):
        """
        Initialize the inventory manager.
        
        Args:
            inventory_file: Path to the JSON file storing inventory data
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as f:
                    data = json.load(f)
                    self.inventory = {
                        item_id: InventoryItem.from_dict(item_data)
                        for item_id, item_data in data.items()
                    }
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.inventory = {}
    
    def save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(
                    {item_id: item.to_dict() for item_id, item in self.inventory.items()},
                    f,
                    indent=2
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")
    
    def add_item(self, product_id: str, name: str, category: str, quantity: int, unit_price: float) -> bool:
        """
        Add a new item to the inventory.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            category: Product category
            quantity: Initial stock quantity
            unit_price: Price per unit
            
        Returns:
            bool: True if item was added successfully, False otherwise
        """
        if product_id in self.inventory:
            print(f"Product ID {product_id} already exists.")
            return False
        
        if quantity < 0 or unit_price <= 0:
            print("Quantity must be >= 0 and unit price must be > 0.")
            return False
        
        self.inventory[product_id] = InventoryItem(
            product_id=product_id,
            name=name,
            category=category,
            quantity=quantity,
            unit_price=unit_price
        )
        self.save_inventory()
        return True
    
    def update_item_quantity(self, product_id: str, quantity_change: int) -> bool:
        """
        Update the quantity of an existing item.
        
        Args:
            product_id: ID of the product to update
            quantity_change: Amount to add/subtract from current quantity
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        if product_id not in self.inventory:
            print(f"Product ID {product_id} not found.")
            return False
        
        new_quantity = self.inventory[product_id].quantity + quantity_change
        if new_quantity < 0:
            print("Cannot have negative inventory quantity.")
            return False
        
        self.inventory[product_id].quantity = new_quantity
        self.save_inventory()
        return True
    
    def remove_item(self, product_id: str) -> bool:
        """
        Remove an item from the inventory.
        
        Args:
            product_id: ID of the product to remove
            
        Returns:
            bool: True if removal was successful, False otherwise
        """
        if product_id not in self.inventory:
            print(f"Product ID {product_id} not found.")
            return False
        
        del self.inventory[product_id]
        self.save_inventory()
        return True
    
    def get_item(self, product_id: str) -> Optional[InventoryItem]:
        """
        Get an item by its product ID.
        
        Args:
            product_id: ID of the product to retrieve
            
        Returns:
            Optional[InventoryItem]: The item if found, None otherwise
        """
        return self.inventory.get(product_id)
    
    def list_items(self, category: Optional[str] = None) -> List[InventoryItem]:
        """
        List all items, optionally filtered by category.
        
        Args:
            category: If specified, only return items of this category
            
        Returns:
            List[InventoryItem]: List of inventory items
        """
        if category:
            return [item for item in self.inventory.values() if item.category == category]
        return list(self.inventory.values())
    
    def get_inventory_value(self) -> float:
        """
        Calculate the total value of the inventory.
        
        Returns:
            float: Total inventory value
        """
        return sum(item.quantity * item.unit_price for item in self.inventory.values())

def main():
    """Example usage of the InventoryManager."""
    manager = InventoryManager()
    
    # Add some sample products
    manager.add_item("CG001", "Chapa Galvanizada 1mm", "chapa galvanizada", 100, 25.50)
    manager.add_item("CB001", "Chapa Branca 1mm", "chapa branca", 80, 22.75)
    
    # Update quantities
    manager.update_item_quantity("CG001", -10)  # Sell 10 units
    manager.update_item_quantity("CB001", 20)   # Add 20 units
    
    # List all items
    print("All Inventory Items:")
    for item in manager.list_items():
        print(f"{item.product_id}: {item.name} - {item.quantity} units")
    
    # List galvanized sheets only
    print("\nGalvanized Sheets:")
    for item in manager.list_items("chapa galvanizada"):
        print(f"{item.product_id}: {item.name} - {item.quantity} units")
    
    # Get total inventory value
    print(f"\nTotal Inventory Value: ${manager.get_inventory_value():.2f}")

if __name__ == "__main__":
    main()
```
