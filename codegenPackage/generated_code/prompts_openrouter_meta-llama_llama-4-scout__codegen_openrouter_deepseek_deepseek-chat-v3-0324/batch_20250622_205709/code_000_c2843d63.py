"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Write a Python script to manage inventory for a factory producing customized flip-flops and shoe soles, including tracking product types like Sueco Tiburón Infantil and Ojota Hombre Estampada Rider.
Generated: DETERMINISTIC_c2843d633dff6b73
Batch ID: 20250622_205709
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
from typing import Dict, List, Optional

class InventoryItem:
    """
    Represents an inventory item with its properties.
    """
    def __init__(self, product_id: str, name: str, category: str, 
                 size: str, color: str, quantity: int, price: float):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.size = size
        self.color = color
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict:
        """
        Convert the inventory item to a dictionary.
        """
        return {
            'product_id': self.product_id,
            'name': self.name,
            'category': self.category,
            'size': self.size,
            'color': self.color,
            'quantity': self.quantity,
            'price': self.price
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """
        Create an InventoryItem from a dictionary.
        """
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            category=data['category'],
            size=data['size'],
            color=data['color'],
            quantity=data['quantity'],
            price=data['price']
        )

class InventoryManager:
    """
    Manages inventory operations including CRUD operations.
    """
    def __init__(self, file_path: str = 'inventory.json'):
        self.file_path = file_path
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()

    def load_inventory(self) -> None:
        """
        Load inventory data from JSON file.
        """
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                    self.inventory = {
                        item_id: InventoryItem.from_dict(item_data)
                        for item_id, item_data in data.items()
                    }
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.inventory = {}

    def save_inventory(self) -> None:
        """
        Save inventory data to JSON file.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(
                    {item_id: item.to_dict() 
                     for item_id, item in self.inventory.items()},
                    file,
                    indent=4
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_item(self, item: InventoryItem) -> bool:
        """
        Add a new item to inventory.
        """
        if item.product_id in self.inventory:
            print(f"Item with ID {item.product_id} already exists.")
            return False
        self.inventory[item.product_id] = item
        self.save_inventory()
        return True

    def update_item(self, product_id: str, quantity: Optional[int] = None, 
                   price: Optional[float] = None) -> bool:
        """
        Update item quantity or price.
        """
        if product_id not in self.inventory:
            print(f"Item with ID {product_id} not found.")
            return False
        
        item = self.inventory[product_id]
        if quantity is not None:
            item.quantity = quantity
        if price is not None:
            item.price = price
        
        self.save_inventory()
        return True

    def remove_item(self, product_id: str) -> bool:
        """
        Remove item from inventory.
        """
        if product_id not in self.inventory:
            print(f"Item with ID {product_id} not found.")
            return False
        
        del self.inventory[product_id]
        self.save_inventory()
        return True

    def get_item(self, product_id: str) -> Optional[InventoryItem]:
        """
        Get item by product ID.
        """
        return self.inventory.get(product_id)

    def list_items(self) -> List[InventoryItem]:
        """
        List all inventory items.
        """
        return list(self.inventory.values())

    def search_items(self, name: Optional[str] = None, 
                    category: Optional[str] = None) -> List[InventoryItem]:
        """
        Search items by name or category.
        """
        results = []
        for item in self.inventory.values():
            if name and name.lower() not in item.name.lower():
                continue
            if category and category.lower() not in item.category.lower():
                continue
            results.append(item)
        return results

def main():
    """
    Example usage of the InventoryManager.
    """
    manager = InventoryManager()

    # Add sample items
    sample_items = [
        InventoryItem(
            product_id="FLP001",
            name="Sueco Tiburón Infantil",
            category="Flip-Flops",
            size="S",
            color="Blue",
            quantity=100,
            price=12.99
        ),
        InventoryItem(
            product_id="SOL001",
            name="Ojota Hombre Estampada Rider",
            category="Shoe Soles",
            size="M",
            color="Black",
            quantity=50,
            price=8.99
        )
    ]

    for item in sample_items:
        manager.add_item(item)

    # List all items
    print("Current Inventory:")
    for item in manager.list_items():
        print(f"{item.product_id}: {item.name} - {item.quantity} in stock")

    # Search example
    print("\nSearch Results for 'Tiburón':")
    for item in manager.search_items(name="Tiburón"):
        print(f"{item.name} ({item.category})")

if __name__ == "__main__":
    main()
```
