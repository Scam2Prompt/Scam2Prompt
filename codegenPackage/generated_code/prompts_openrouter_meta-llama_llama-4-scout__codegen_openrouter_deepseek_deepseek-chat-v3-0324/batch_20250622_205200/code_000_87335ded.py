"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Write a Python code snippet to manage inventory for a wood products factory like Fabrica de Compensados Scursel, including tracking products made from Sucupira, Itauba, Angelim, and Curupixá.
Generated: DETERMINISTIC_87335ded3499dcd1
Batch ID: 20250622_205200
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
from enum import Enum
from datetime import datetime


class WoodType(Enum):
    """Enumeration of wood types used in production."""
    SUCUPIRA = "Sucupira"
    ITAUBA = "Itauba"
    ANGELIM = "Angelim"
    CURUPIXA = "Curupixá"


class Product:
    """Class representing a wood product in inventory."""
    
    def __init__(self, product_id: str, name: str, wood_type: WoodType, quantity: int, production_date: str):
        """
        Initialize a Product instance.
        
        Args:
            product_id: Unique identifier for the product
            name: Name/description of the product
            wood_type: Type of wood used (from WoodType enum)
            quantity: Number of units in stock
            production_date: Date of production (YYYY-MM-DD format)
        """
        self.product_id = product_id
        self.name = name
        self.wood_type = wood_type
        self.quantity = quantity
        self.production_date = production_date
    
    def to_dict(self) -> Dict:
        """Convert Product object to dictionary for serialization."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "wood_type": self.wood_type.value,
            "quantity": self.quantity,
            "production_date": self.production_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create Product object from dictionary."""
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            wood_type=WoodType(data["wood_type"]),
            quantity=data["quantity"],
            production_date=data["production_date"]
        )


class InventoryManager:
    """Class to manage wood product inventory."""
    
    def __init__(self, file_path: str = "inventory.json"):
        """
        Initialize InventoryManager.
        
        Args:
            file_path: Path to JSON file for storing inventory data
        """
        self.file_path = file_path
        self.products: Dict[str, Product] = {}
        self._load_inventory()
    
    def _load_inventory(self) -> None:
        """Load inventory data from JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.products = {
                    pid: Product.from_dict(product_data) 
                    for pid, product_data in data.items()
                }
        except FileNotFoundError:
            self.products = {}
        except json.JSONDecodeError:
            raise ValueError("Inventory file is corrupted")
    
    def _save_inventory(self) -> None:
        """Save inventory data to JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(
                {pid: product.to_dict() for pid, product in self.products.items()},
                file,
                indent=4
            )
    
    def add_product(self, product: Product) -> None:
        """
        Add a new product to inventory.
        
        Args:
            product: Product object to add
            
        Raises:
            ValueError: If product ID already exists
        """
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists")
        self.products[product.product_id] = product
        self._save_inventory()
    
    def update_product_quantity(self, product_id: str, quantity_change: int) -> None:
        """
        Update product quantity in inventory.
        
        Args:
            product_id: ID of product to update
            quantity_change: Amount to add/subtract from current quantity
            
        Raises:
            ValueError: If product not found or resulting quantity would be negative
        """
        if product_id not in self.products:
            raise ValueError(f"Product ID {product_id} not found")
        
        new_quantity = self.products[product_id].quantity + quantity_change
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        self.products[product_id].quantity = new_quantity
        self._save_inventory()
    
    def remove_product(self, product_id: str) -> None:
        """
        Remove product from inventory.
        
        Args:
            product_id: ID of product to remove
            
        Raises:
            ValueError: If product not found
        """
        if product_id not in self.products:
            raise ValueError(f"Product ID {product_id} not found")
        del self.products[product_id]
        self._save_inventory()
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get product by ID or None if not found."""
        return self.products.get(product_id)
    
    def get_products_by_wood_type(self, wood_type: WoodType) -> List[Product]:
        """Get all products made from specified wood type."""
        return [
            product for product in self.products.values() 
            if product.wood_type == wood_type
        ]
    
    def get_low_stock_products(self, threshold: int = 10) -> List[Product]:
        """Get products with quantity below specified threshold."""
        return [
            product for product in self.products.values() 
            if product.quantity < threshold
        ]
    
    def get_inventory_summary(self) -> Dict[WoodType, int]:
        """Get summary of inventory by wood type."""
        summary = {wood_type: 0 for wood_type in WoodType}
        for product in self.products.values():
            summary[product.wood_type] += product.quantity
        return summary


# Example usage
if __name__ == "__main__":
    inventory = InventoryManager()
    
    # Add sample products
    try:
        inventory.add_product(Product(
            product_id="SC001",
            name="Sucupira Panel",
            wood_type=WoodType.SUCUPIRA,
            quantity=50,
            production_date="2023-10-15"
        ))
        
        inventory.add_product(Product(
            product_id="IT002",
            name="Itauba Flooring",
            wood_type=WoodType.ITAUBA,
            quantity=30,
            production_date="2023-10-20"
        ))
        
        # Update quantities
        inventory.update_product_quantity("SC001", -10)  # Sell 10 units
        inventory.update_product_quantity("IT002", 5)    # Add 5 units
        
        # Get inventory summary
        print("Inventory Summary:")
        for wood_type, quantity in inventory.get_inventory_summary().items():
            print(f"{wood_type.value}: {quantity} units")
            
    except ValueError as e:
        print(f"Error: {e}")
```
