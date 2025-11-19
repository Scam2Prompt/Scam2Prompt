"""
Generated Code Metadata:
========================
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Generate a code snippet for an inventory management system that tracks computer hardware and accessories like SSDs and projectors, similar to the offerings on mixpelinfobrazz.
Generated: DETERMINISTIC_f60f03bf7ef5e141
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py
"""
Inventory Management System for Computer Hardware and Accessories

This module provides functionality to track inventory items such as SSDs, projectors,
and other computer hardware similar to mixpelinfobrazz offerings.

Features:
- Add new inventory items
- Update existing items
- Remove items
- Search/filter items
- Generate inventory reports
"""

from dataclasses import dataclass
from typing import List, Optional
import csv
from datetime import datetime
import os


@dataclass
class InventoryItem:
    """Class representing an inventory item"""
    id: str
    name: str
    category: str  # e.g., "SSD", "Projector", "Monitor"
    quantity: int
    price: float
    last_updated: str
    description: Optional[str] = None
    manufacturer: Optional[str] = None
    model_number: Optional[str] = None


class InventoryManager:
    """Main inventory management class"""
    
    def __init__(self, storage_file: str = "inventory.csv"):
        self.storage_file = storage_file
        self.items: List[InventoryItem] = []
        self._load_inventory()
    
    def _load_inventory(self) -> None:
        """Load inventory data from storage file"""
        if not os.path.exists(self.storage_file):
            return
            
        with open(self.storage_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.items.append(InventoryItem(
                    id=row['id'],
                    name=row['name'],
                    category=row['category'],
                    quantity=int(row['quantity']),
                    price=float(row['price']),
                    last_updated=row['last_updated'],
                    description=row.get('description'),
                    manufacturer=row.get('manufacturer'),
                    model_number=row.get('model_number')
                ))
    
    def _save_inventory(self) -> None:
        """Save inventory data to storage file"""
        with open(self.storage_file, mode='w', newline='') as file:
            fieldnames = [
                'id', 'name', 'category', 'quantity', 'price', 
                'last_updated', 'description', 'manufacturer', 'model_number'
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for item in self.items:
                writer.writerow({
                    'id': item.id,
                    'name': item.name,
                    'category': item.category,
                    'quantity': item.quantity,
                    'price': item.price,
                    'last_updated': item.last_updated,
                    'description': item.description,
                    'manufacturer': item.manufacturer,
                    'model_number': item.model_number
                })
    
    def _generate_id(self) -> str:
        """Generate a unique ID for new items"""
        return str(datetime.now().timestamp()).replace('.', '')[-10:]
    
    def add_item(self, name: str, category: str, quantity: int, price: float,
                 description: str = None, manufacturer: str = None, 
                 model_number: str = None) -> InventoryItem:
        """
        Add a new item to inventory
        
        Args:
            name: Item name
            category: Item category (e.g., "SSD", "Projector")
            quantity: Available quantity
            price: Unit price
            description: Optional description
            manufacturer: Optional manufacturer name
            model_number: Optional model number
            
        Returns:
            The newly created inventory item
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        if not name or not category:
            raise ValueError("Name and category are required")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if price <= 0:
            raise ValueError("Price must be positive")
            
        new_item = InventoryItem(
            id=self._generate_id(),
            name=name,
            category=category,
            quantity=quantity,
            price=price,
            last_updated=datetime.now().isoformat(),
            description=description,
            manufacturer=manufacturer,
            model_number=model_number
        )
        
        self.items.append(new_item)
        self._save_inventory()
        return new_item
    
    def update_item(self, item_id: str, **kwargs) -> InventoryItem:
        """
        Update an existing inventory item
        
        Args:
            item_id: ID of item to update
            **kwargs: Fields to update (name, category, quantity, price, etc.)
            
        Returns:
            The updated inventory item
            
        Raises:
            ValueError: If item not found or invalid updates provided
        """
        item = next((i for i in self.items if i.id == item_id), None)
        if not item:
            raise ValueError(f"Item with ID {item_id} not found")
            
        valid_fields = ['name', 'category', 'quantity', 'price', 
                       'description', 'manufacturer', 'model_number']
        
        for field, value in kwargs.items():
            if field not in valid_fields:
                raise ValueError(f"Invalid field: {field}")
            if field == 'quantity' and value < 0:
                raise ValueError("Quantity cannot be negative")
            if field == 'price' and value <= 0:
                raise ValueError("Price must be positive")
            setattr(item, field, value)
        
        item.last_updated = datetime.now().isoformat()
        self._save_inventory()
        return item
    
    def remove_item(self, item_id: str) -> None:
        """
        Remove an item from inventory
        
        Args:
            item_id: ID of item to remove
            
        Raises:
            ValueError: If item not found
        """
        item = next((i for i in self.items if i.id == item_id), None)
        if not item:
            raise ValueError(f"Item with ID {item_id} not found")
            
        self.items.remove(item)
        self._save_inventory()
    
    def search_items(self, name: str = None, category: str = None, 
                    min_price: float = None, max_price: float = None) -> List[InventoryItem]:
        """
        Search inventory items based on criteria
        
        Args:
            name: Partial name match
            category: Exact category match
            min_price: Minimum price
            max_price: Maximum price
            
        Returns:
            List of matching inventory items
        """
        results = self.items
        
        if name:
            results = [i for i in results if name.lower() in i.name.lower()]
        if category:
            results = [i for i in results if i.category.lower() == category.lower()]
        if min_price is not None:
            results = [i for i in results if i.price >= min_price]
        if max_price is not None:
            results = [i for i in results if i.price <= max_price]
            
        return results
    
    def generate_inventory_report(self) -> str:
        """
        Generate a summary report of inventory status
        
        Returns:
            Formatted inventory report string
        """
        total_items = len(self.items)
        total_value = sum(item.price * item.quantity for item in self.items)
        categories = {item.category for item in self.items}
        
        report = [
            "Inventory Report",
            "----------------",
            f"Total Items: {total_items}",
            f"Total Inventory Value: ${total_value:,.2f}",
            f"Categories: {', '.join(categories)}",
            "",
            "Item Breakdown:"
        ]
        
        for category in categories:
            cat_items = [i for i in self.items if i.category == category]
            cat_count = len(cat_items)
            cat_value = sum(i.price * i.quantity for i in cat_items)
            report.append(
                f"- {category}: {cat_count} items (${cat_value:,.2f})"
            )
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add sample items
    manager.add_item(
        name="Samsung 1TB SSD",
        category="SSD",
        quantity=10,
        price=99.99,
        manufacturer="Samsung",
        model_number="870 EVO"
    )
    
    manager.add_item(
        name="Epson Home Cinema 1080p",
        category="Projector",
        quantity=5,
        price=599.99,
        manufacturer="Epson",
        description="Full HD 1080p home theater projector"
    )
    
    # Generate report
    print(manager.generate_inventory_report())
```
