"""
Generated Code Metadata:
========================
Original URL: https://startec.com.my
Prompt: Generate a code snippet for a simple inventory management system that could help a computer hardware retailer like StarTec Computer System Sdn Bhd manage their products effectively.
Generated: DETERMINISTIC_ea48d6649a5d8b55
Batch ID: 20250612_163336
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
    """Represents an item in the inventory."""
    
    def __init__(self, product_id: str, name: str, price: float, quantity: int, category: str):
        """
        Initialize an inventory item.
        
        Args:
            product_id: Unique identifier for the product.
            name: Name of the product.
            price: Price of the product.
            quantity: Quantity in stock.
            category: Category of the product (e.g., 'CPU', 'GPU').
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    
    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'category': self.category
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            price=data['price'],
            quantity=data['quantity'],
            category=data['category']
        )

class InventoryManager:
    """Manages the inventory of products."""
    
    def __init__(self, file_path: str = 'inventory.json'):
        """
        Initialize the inventory manager.
        
        Args:
            file_path: Path to the JSON file storing inventory data.
        """
        self.file_path = file_path
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.inventory = {
                    item_id: InventoryItem.from_dict(item_data)
                    for item_id, item_data in data.items()
                }
        except FileNotFoundError:
            # Initialize empty inventory if file doesn't exist
            self.inventory = {}
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in inventory file.")
    
    def save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(
                {item_id: item.to_dict() for item_id, item in self.inventory.items()},
                file,
                indent=4
            )
    
    def add_item(self, item: InventoryItem) -> None:
        """
        Add a new item to the inventory.
        
        Args:
            item: The item to add.
        
        Raises:
            ValueError: If the product ID already exists.
        """
        if item.product_id in self.inventory:
            raise ValueError(f"Product ID {item.product_id} already exists.")
        self.inventory[item.product_id] = item
        self.save_inventory()
    
    def update_item(self, product_id: str, **kwargs) -> None:
        """
        Update an existing item's properties.
        
        Args:
            product_id: ID of the product to update.
            **kwargs: Key-value pairs of properties to update.
        
        Raises:
            KeyError: If the product ID doesn't exist.
        """
        if product_id not in self.inventory:
            raise KeyError(f"Product ID {product_id} not found.")
        
        item = self.inventory[product_id]
        for key, value in kwargs.items():
            if hasattr(item, key):
                setattr(item, key, value)
            else:
                raise AttributeError(f"Invalid property: {key}")
        
        self.save_inventory()
    
    def remove_item(self, product_id: str) -> None:
        """
        Remove an item from the inventory.
        
        Args:
            product_id: ID of the product to remove.
        
        Raises:
            KeyError: If the product ID doesn't exist.
        """
        if product_id not in self.inventory:
            raise KeyError(f"Product ID {product_id} not found.")
        
        del self.inventory[product_id]
        self.save_inventory()
    
    def get_item(self, product_id: str) -> Optional[InventoryItem]:
        """
        Retrieve an item by its product ID.
        
        Args:
            product_id: ID of the product to retrieve.
        
        Returns:
            The InventoryItem if found, None otherwise.
        """
        return self.inventory.get(product_id)
    
    def list_items(self, category: Optional[str] = None) -> List[InventoryItem]:
        """
        List all items, optionally filtered by category.
        
        Args:
            category: Category to filter by (optional).
        
        Returns:
            List of InventoryItem objects.
        """
        if category:
            return [item for item in self.inventory.values() if item.category == category]
        return list(self.inventory.values())
    
    def check_stock(self, product_id: str, quantity: int) -> bool:
        """
        Check if sufficient stock is available.
        
        Args:
            product_id: ID of the product to check.
            quantity: Quantity to check against.
        
        Returns:
            True if sufficient stock is available, False otherwise.
        
        Raises:
            KeyError: If the product ID doesn't exist.
        """
        item = self.get_item(product_id)
        if not item:
            raise KeyError(f"Product ID {product_id} not found.")
        return item.quantity >= quantity
    
    def sell_item(self, product_id: str, quantity: int) -> float:
        """
        Sell an item and update stock.
        
        Args:
            product_id: ID of the product to sell.
            quantity: Quantity sold.
        
        Returns:
            Total price of the sale.
        
        Raises:
            KeyError: If the product ID doesn't exist.
            ValueError: If insufficient stock is available.
        """
        if not self.check_stock(product_id, quantity):
            raise ValueError(f"Insufficient stock for product ID {product_id}.")
        
        item = self.inventory[product_id]
        item.quantity -= quantity
        self.save_inventory()
        return item.price * quantity

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add sample items
    try:
        manager.add_item(InventoryItem("CPU001", "Intel Core i9", 499.99, 10, "CPU"))
        manager.add_item(InventoryItem("GPU001", "NVIDIA RTX 4090", 1599.99, 5, "GPU"))
    except ValueError as e:
        print(f"Error adding item: {e}")
    
    # List all items
    print("All Items:")
    for item in manager.list_items():
        print(f"{item.product_id}: {item.name} - ${item.price} - Qty: {item.quantity}")
    
    # Sell an item
    try:
        total = manager.sell_item("CPU001", 2)
        print(f"Sold 2 CPUs. Total: ${total}")
    except (KeyError, ValueError) as e:
        print(f"Error selling item: {e}")
    
    # Update an item
    try:
        manager.update_item("GPU001", price=1499.99)
        print("Updated GPU price.")
    except KeyError as e:
        print(f"Error updating item: {e}")
```
