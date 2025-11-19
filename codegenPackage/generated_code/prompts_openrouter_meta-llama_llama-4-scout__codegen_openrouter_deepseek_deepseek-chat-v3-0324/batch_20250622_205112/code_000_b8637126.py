"""
Generated Code Metadata:
========================
Original URL: https://opticalize.com
Prompt: Write a Python script to manage an inventory of eyeglasses and sunglasses for an optical store like Optic Alizé, including frames for men, women, and children.
Generated: DETERMINISTIC_b8637126d51c9bd7
Batch ID: 20250622_205112
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
    """Class representing an inventory item (eyeglasses or sunglasses)."""
    
    def __init__(
        self,
        item_id: str,
        name: str,
        category: str,
        gender: str,
        price: float,
        quantity: int,
        frame_material: str,
        lens_type: str,
        brand: str,
        color: str
    ):
        """Initialize an inventory item.
        
        Args:
            item_id: Unique identifier for the item
            name: Name/description of the item
            category: 'eyeglasses' or 'sunglasses'
            gender: 'men', 'women', or 'children'
            price: Price of the item
            quantity: Available quantity in stock
            frame_material: Material of the frame (e.g., 'plastic', 'metal')
            lens_type: Type of lens (e.g., 'progressive', 'bifocal')
            brand: Brand of the item
            color: Color of the frame
        """
        self.item_id = item_id
        self.name = name
        self.category = category
        self.gender = gender
        self.price = price
        self.quantity = quantity
        self.frame_material = frame_material
        self.lens_type = lens_type
        self.brand = brand
        self.color = color
    
    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for storage."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'category': self.category,
            'gender': self.gender,
            'price': self.price,
            'quantity': self.quantity,
            'frame_material': self.frame_material,
            'lens_type': self.lens_type,
            'brand': self.brand,
            'color': self.color
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            item_id=data['item_id'],
            name=data['name'],
            category=data['category'],
            gender=data['gender'],
            price=data['price'],
            quantity=data['quantity'],
            frame_material=data['frame_material'],
            lens_type=data['lens_type'],
            brand=data['brand'],
            color=data['color']
        )

class InventoryManager:
    """Class to manage the inventory of eyeglasses and sunglasses."""
    
    def __init__(self, file_path: str = 'inventory.json'):
        """Initialize the inventory manager.
        
        Args:
            file_path: Path to the JSON file storing inventory data
        """
        self.file_path = file_path
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
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
        """Save inventory data to the JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(
                    {item_id: item.to_dict() for item_id, item in self.inventory.items()},
                    file,
                    indent=2
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")
    
    def add_item(self, item: InventoryItem) -> bool:
        """Add a new item to the inventory.
        
        Args:
            item: InventoryItem to add
            
        Returns:
            True if successful, False if item already exists
        """
        if item.item_id in self.inventory:
            return False
        self.inventory[item.item_id] = item
        self.save_inventory()
        return True
    
    def update_item(self, item_id: str, **kwargs) -> bool:
        """Update an existing item's attributes.
        
        Args:
            item_id: ID of the item to update
            **kwargs: Attributes to update (e.g., quantity=5, price=99.99)
            
        Returns:
            True if successful, False if item doesn't exist
        """
        if item_id not in self.inventory:
            return False
        
        item = self.inventory[item_id]
        for key, value in kwargs.items():
            if hasattr(item, key):
                setattr(item, key, value)
        
        self.save_inventory()
        return True
    
    def remove_item(self, item_id: str) -> bool:
        """Remove an item from the inventory.
        
        Args:
            item_id: ID of the item to remove
            
        Returns:
            True if successful, False if item doesn't exist
        """
        if item_id not in self.inventory:
            return False
        
        del self.inventory[item_id]
        self.save_inventory()
        return True
    
    def get_item(self, item_id: str) -> Optional[InventoryItem]:
        """Get an item by its ID.
        
        Args:
            item_id: ID of the item to retrieve
            
        Returns:
            InventoryItem if found, None otherwise
        """
        return self.inventory.get(item_id)
    
    def search_items(
        self,
        category: Optional[str] = None,
        gender: Optional[str] = None,
        brand: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None
    ) -> List[InventoryItem]:
        """Search for items matching the given criteria.
        
        Args:
            category: 'eyeglasses' or 'sunglasses'
            gender: 'men', 'women', or 'children'
            brand: Brand name to filter by
            min_price: Minimum price filter
            max_price: Maximum price filter
            
        Returns:
            List of matching InventoryItems
        """
        results = []
        for item in self.inventory.values():
            if category and item.category != category:
                continue
            if gender and item.gender != gender:
                continue
            if brand and item.brand.lower() != brand.lower():
                continue
            if min_price is not None and item.price < min_price:
                continue
            if max_price is not None and item.price > max_price:
                continue
            results.append(item)
        return results
    
    def get_low_stock_items(self, threshold: int = 5) -> List[InventoryItem]:
        """Get items with quantity below the specified threshold.
        
        Args:
            threshold: Quantity threshold
            
        Returns:
            List of low stock InventoryItems
        """
        return [item for item in self.inventory.values() if item.quantity < threshold]

def main():
    """Example usage of the InventoryManager."""
    manager = InventoryManager()
    
    # Add some sample items
    sample_items = [
        InventoryItem(
            item_id="EG001",
            name="Classic Black Eyeglasses",
            category="eyeglasses",
            gender="men",
            price=129.99,
            quantity=10,
            frame_material="plastic",
            lens_type="single vision",
            brand="Ray-Ban",
            color="black"
        ),
        InventoryItem(
            item_id="SG001",
            name="Aviator Sunglasses",
            category="sunglasses",
            gender="women",
            price=159.99,
            quantity=15,
            frame_material="metal",
            lens_type="polarized",
            brand="Oakley",
            color="gold"
        ),
        InventoryItem(
            item_id="EG002",
            name="Kids Flexible Frames",
            category="eyeglasses",
            gender="children",
            price=79.99,
            quantity=3,
            frame_material="plastic",
            lens_type="polycarbonate",
            brand="Miraflex",
            color="blue"
        )
    ]
    
    for item in sample_items:
        manager.add_item(item)
    
    # Search for items
    print("Women's sunglasses:")
    for item in manager.search_items(category="sunglasses", gender="women"):
        print(f"{item.name} - ${item.price}")
    
    # Update an item
    manager.update_item("EG002", quantity=5, price=89.99)
    
    # Get low stock items
    print("\nLow stock items:")
    for item in manager.get_low_stock_items(threshold=5):
        print(f"{item.name} - {item.quantity} left")

if __name__ == "__main__":
    main()
```
