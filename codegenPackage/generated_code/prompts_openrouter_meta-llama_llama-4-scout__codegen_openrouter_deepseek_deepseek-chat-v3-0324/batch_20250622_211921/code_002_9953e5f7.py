"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: "Write a Python code snippet to manage inventory for different types of natural stone bracelets, including their prices and sale prices, as seen on Hoorainz."
Generated: DETERMINISTIC_9953e5f70dee34f7
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, asdict
from enum import Enum


class StoneType(Enum):
    """Enumeration of natural stone types."""
    AMETHYST = "Amethyst"
    TURQUOISE = "Turquoise"
    JADE = "Jade"
    QUARTZ = "Quartz"
    LAPIS_LAZULI = "Lapis Lazuli"
    OBSIDIAN = "Obsidian"


@dataclass
class Bracelet:
    """Represents a natural stone bracelet with inventory details."""
    stone_type: StoneType
    price: float
    sale_price: Optional[float] = None
    quantity: int = 0
    sku: Optional[str] = None

    def __post_init__(self):
        """Validate the bracelet data after initialization."""
        if self.price <= 0:
            raise ValueError("Price must be positive")
        if self.sale_price is not None and self.sale_price <= 0:
            raise ValueError("Sale price must be positive")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.sku is not None and not isinstance(self.sku, str):
            raise ValueError("SKU must be a string")


class InventoryManager:
    """Manages inventory of natural stone bracelets."""
    
    def __init__(self):
        """Initialize with empty inventory."""
        self.inventory: Dict[str, Bracelet] = {}
    
    def add_bracelet(self, bracelet: Bracelet) -> None:
        """Add a bracelet to inventory.
        
        Args:
            bracelet: Bracelet object to add
            
        Raises:
            ValueError: If SKU already exists in inventory
        """
        if bracelet.sku in self.inventory:
            raise ValueError(f"SKU {bracelet.sku} already exists in inventory")
        self.inventory[bracelet.sku] = bracelet
    
    def remove_bracelet(self, sku: str) -> None:
        """Remove a bracelet from inventory by SKU.
        
        Args:
            sku: SKU of bracelet to remove
            
        Raises:
            KeyError: If SKU doesn't exist in inventory
        """
        if sku not in self.inventory:
            raise KeyError(f"SKU {sku} not found in inventory")
        del self.inventory[sku]
    
    def update_quantity(self, sku: str, quantity: int) -> None:
        """Update quantity of a bracelet in inventory.
        
        Args:
            sku: SKU of bracelet to update
            quantity: New quantity value
            
        Raises:
            KeyError: If SKU doesn't exist in inventory
            ValueError: If quantity is negative
        """
        if sku not in self.inventory:
            raise KeyError(f"SKU {sku} not found in inventory")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.inventory[sku].quantity = quantity
    
    def update_pricing(self, sku: str, price: float, sale_price: Optional[float] = None) -> None:
        """Update pricing for a bracelet.
        
        Args:
            sku: SKU of bracelet to update
            price: New regular price
            sale_price: New sale price (optional)
            
        Raises:
            KeyError: If SKU doesn't exist in inventory
            ValueError: If prices are invalid
        """
        if sku not in self.inventory:
            raise KeyError(f"SKU {sku} not found in inventory")
        if price <= 0:
            raise ValueError("Price must be positive")
        if sale_price is not None and sale_price <= 0:
            raise ValueError("Sale price must be positive")
        
        self.inventory[sku].price = price
        self.inventory[sku].sale_price = sale_price
    
    def get_bracelet(self, sku: str) -> Bracelet:
        """Retrieve a bracelet by SKU.
        
        Args:
            sku: SKU of bracelet to retrieve
            
        Returns:
            The matching Bracelet object
            
        Raises:
            KeyError: If SKU doesn't exist in inventory
        """
        if sku not in self.inventory:
            raise KeyError(f"SKU {sku} not found in inventory")
        return self.inventory[sku]
    
    def list_inventory(self) -> List[Bracelet]:
        """List all bracelets in inventory.
        
        Returns:
            List of all Bracelet objects in inventory
        """
        return list(self.inventory.values())
    
    def save_to_file(self, filename: str) -> None:
        """Save inventory to JSON file.
        
        Args:
            filename: Path to save file
            
        Raises:
            IOError: If file operations fail
        """
        try:
            with open(filename, 'w') as f:
                inventory_data = [asdict(bracelet) for bracelet in self.inventory.values()]
                json.dump(inventory_data, f, indent=2, default=str)
        except IOError as e:
            raise IOError(f"Failed to save inventory: {str(e)}")
    
    def load_from_file(self, filename: str) -> None:
        """Load inventory from JSON file.
        
        Args:
            filename: Path to load file
            
        Raises:
            IOError: If file operations fail
            ValueError: If file contains invalid data
        """
        try:
            with open(filename, 'r') as f:
                inventory_data = json.load(f)
                self.inventory.clear()
                for item in inventory_data:
                    try:
                        stone_type = StoneType(item['stone_type'])
                        bracelet = Bracelet(
                            stone_type=stone_type,
                            price=item['price'],
                            sale_price=item.get('sale_price'),
                            quantity=item['quantity'],
                            sku=item['sku']
                        )
                        self.inventory[bracelet.sku] = bracelet
                    except (KeyError, ValueError) as e:
                        raise ValueError(f"Invalid bracelet data: {str(e)}")
        except IOError as e:
            raise IOError(f"Failed to load inventory: {str(e)}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {str(e)}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    try:
        # Add some bracelets
        manager.add_bracelet(Bracelet(
            stone_type=StoneType.AMETHYST,
            price=29.99,
            sale_price=24.99,
            quantity=10,
            sku="AM-001"
        ))
        
        manager.add_bracelet(Bracelet(
            stone_type=StoneType.TURQUOISE,
            price=34.99,
            quantity=5,
            sku="TQ-001"
        ))
        
        # Update quantities and prices
        manager.update_quantity("AM-001", 8)
        manager.update_pricing("TQ-001", 32.99, 29.99)
        
        # Save to file
        manager.save_to_file("inventory.json")
        
        # Print inventory
        print("Current Inventory:")
        for bracelet in manager.list_inventory():
            print(f"{bracelet.stone_type.value} Bracelet (SKU: {bracelet.sku}):")
            print(f"  Price: ${bracelet.price:.2f}")
            if bracelet.sale_price:
                print(f"  Sale Price: ${bracelet.sale_price:.2f}")
            print(f"  Quantity: {bracelet.quantity}")
            print()
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
