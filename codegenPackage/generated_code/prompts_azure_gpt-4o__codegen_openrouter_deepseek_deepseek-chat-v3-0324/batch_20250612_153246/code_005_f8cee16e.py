"""
Generated Code Metadata:
========================
Original URL: https://sanurisupplies.com
Prompt: Develop a program to categorize office supplies into different sections (computers, printers, files, folders, etc.) for large-scale and small-scale businesses, as mentioned on Sanuri Supplies' website.
Generated: DETERMINISTIC_f8cee16ec6549a65
Batch ID: 20250612_153246
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

class OfficeSupply:
    """Base class representing an office supply item."""
    
    def __init__(self, name: str, category: str, quantity: int, price: float):
        """
        Initialize an office supply item.
        
        Args:
            name: Name of the item.
            category: Category of the item (e.g., computers, printers).
            quantity: Quantity available.
            price: Price per unit.
        """
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', category='{self.category}', quantity={self.quantity}, price={self.price})"

class InventoryManager:
    """Manages inventory of office supplies for businesses."""
    
    def __init__(self):
        """Initialize the inventory manager with empty inventory."""
        self.inventory: Dict[str, List[OfficeSupply]] = {}
    
    def add_supply(self, supply: OfficeSupply) -> None:
        """
        Add a supply item to the inventory.
        
        Args:
            supply: OfficeSupply object to add.
            
        Raises:
            ValueError: If supply is not an instance of OfficeSupply.
        """
        if not isinstance(supply, OfficeSupply):
            raise ValueError("Supply must be an instance of OfficeSupply.")
        
        if supply.category not in self.inventory:
            self.inventory[supply.category] = []
        self.inventory[supply.category].append(supply)
    
    def remove_supply(self, category: str, name: str) -> bool:
        """
        Remove a supply item from the inventory.
        
        Args:
            category: Category of the item to remove.
            name: Name of the item to remove.
            
        Returns:
            bool: True if item was removed, False otherwise.
        """
        if category not in self.inventory:
            return False
        
        for idx, item in enumerate(self.inventory[category]):
            if item.name == name:
                self.inventory[category].pop(idx)
                if not self.inventory[category]:
                    del self.inventory[category]
                return True
        return False
    
    def get_supplies_by_category(self, category: str) -> Optional[List[OfficeSupply]]:
        """
        Get all supplies in a specific category.
        
        Args:
            category: Category to filter by.
            
        Returns:
            Optional[List[OfficeSupply]]: List of supplies in the category, or None if category doesn't exist.
        """
        return self.inventory.get(category, None)
    
    def get_total_value(self) -> float:
        """
        Calculate the total value of all supplies in inventory.
        
        Returns:
            float: Total value of inventory.
        """
        total = 0.0
        for category in self.inventory:
            for item in self.inventory[category]:
                total += item.quantity * item.price
        return total
    
    def save_to_file(self, filename: str) -> None:
        """
        Save inventory to a JSON file.
        
        Args:
            filename: Name of the file to save to.
            
        Raises:
            IOError: If file cannot be written.
        """
        try:
            with open(filename, 'w') as f:
                inventory_data = {
                    category: [
                        {
                            'name': item.name,
                            'category': item.category,
                            'quantity': item.quantity,
                            'price': item.price
                        }
                        for item in items
                    ]
                    for category, items in self.inventory.items()
                }
                json.dump(inventory_data, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory to file: {e}")
    
    def load_from_file(self, filename: str) -> None:
        """
        Load inventory from a JSON file.
        
        Args:
            filename: Name of the file to load from.
            
        Raises:
            IOError: If file cannot be read.
            ValueError: If file contains invalid data.
        """
        try:
            with open(filename, 'r') as f:
                inventory_data = json.load(f)
                self.inventory = {}
                for category, items in inventory_data.items():
                    self.inventory[category] = [
                        OfficeSupply(
                            name=item['name'],
                            category=item['category'],
                            quantity=item['quantity'],
                            price=item['price']
                        )
                        for item in items
                    ]
        except IOError as e:
            raise IOError(f"Failed to load inventory from file: {e}")
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Invalid inventory data in file: {e}")

# Example usage
if __name__ == "__main__":
    # Create inventory manager
    manager = InventoryManager()
    
    # Add some supplies
    manager.add_supply(OfficeSupply("Laptop", "computers", 10, 999.99))
    manager.add_supply(OfficeSupply("Inkjet Printer", "printers", 5, 199.99))
    manager.add_supply(OfficeSupply("Manila Folder", "folders", 100, 0.99))
    manager.add_supply(OfficeSupply("Hanging File", "files", 50, 1.49))
    
    # Print inventory by category
    print("Inventory by category:")
    for category in manager.inventory:
        print(f"\n{category}:")
        for item in manager.inventory[category]:
            print(f"  - {item.name}: {item.quantity} units at ${item.price:.2f} each")
    
    # Print total inventory value
    print(f"\nTotal inventory value: ${manager.get_total_value():.2f}")
    
    # Save and load inventory
    try:
        manager.save_to_file("inventory.json")
        manager.load_from_file("inventory.json")
    except (IOError, ValueError) as e:
        print(f"Error: {e}")
```
