"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Write a Python script to manage inventory for a company like PDC Brush that produces private label household cleaning tools, considering factors like FSC-certified wood and sustainability.
Generated: DETERMINISTIC_5aa03fc155e09616
Batch ID: 20250622_212556
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
from datetime import datetime
from typing import Dict, List, Optional, Union


class InventoryItem:
    """
    Represents an inventory item with sustainability attributes.
    """
    
    def __init__(
        self,
        sku: str,
        name: str,
        description: str,
        quantity: int,
        unit_price: float,
        fsc_certified: bool,
        materials: List[str],
        supplier: str,
        last_restock_date: Optional[str] = None
    ):
        """
        Initialize an inventory item.
        
        Args:
            sku: Stock Keeping Unit identifier
            name: Product name
            description: Product description
            quantity: Current stock quantity
            unit_price: Price per unit
            fsc_certified: Whether the wood is FSC-certified
            materials: List of materials used in product
            supplier: Supplier name
            last_restock_date: Date of last restock (YYYY-MM-DD)
        """
        self.sku = sku
        self.name = name
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price
        self.fsc_certified = fsc_certified
        self.materials = materials
        self.supplier = supplier
        self.last_restock_date = last_restock_date or datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            "sku": self.sku,
            "name": self.name,
            "description": self.description,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "fsc_certified": self.fsc_certified,
            "materials": self.materials,
            "supplier": self.supplier,
            "last_restock_date": self.last_restock_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            sku=data["sku"],
            name=data["name"],
            description=data["description"],
            quantity=data["quantity"],
            unit_price=data["unit_price"],
            fsc_certified=data["fsc_certified"],
            materials=data["materials"],
            supplier=data["supplier"],
            last_restock_date=data.get("last_restock_date")
        )


class InventoryManager:
    """
    Manages inventory with sustainability tracking.
    """
    
    def __init__(self, data_file: str = "inventory.json"):
        """
        Initialize the inventory manager.
        
        Args:
            data_file: Path to JSON file for persistent storage
        """
        self.data_file = data_file
        self.inventory: Dict[str, InventoryItem] = {}
        self._load_inventory()
    
    def _load_inventory(self) -> None:
        """Load inventory from the data file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.inventory = {
                        sku: InventoryItem.from_dict(item_data)
                        for sku, item_data in data.items()
                    }
        except Exception as e:
            raise Exception(f"Failed to load inventory: {str(e)}")
    
    def _save_inventory(self) -> None:
        """Save inventory to the data file."""
        try:
            with open(self.data_file, "w") as f:
                json.dump(
                    {sku: item.to_dict() for sku, item in self.inventory.items()},
                    f,
                    indent=2
                )
        except Exception as e:
            raise Exception(f"Failed to save inventory: {str(e)}")
    
    def add_item(self, item: InventoryItem) -> None:
        """
        Add a new item to inventory.
        
        Args:
            item: InventoryItem to add
            
        Raises:
            ValueError: If SKU already exists
        """
        if item.sku in self.inventory:
            raise ValueError(f"SKU {item.sku} already exists in inventory")
        self.inventory[item.sku] = item
        self._save_inventory()
    
    def update_item(self, sku: str, **kwargs) -> None:
        """
        Update an existing inventory item.
        
        Args:
            sku: SKU of item to update
            **kwargs: Fields to update with new values
            
        Raises:
            KeyError: If SKU doesn't exist
            ValueError: If invalid fields are provided
        """
        if sku not in self.inventory:
            raise KeyError(f"SKU {sku} not found in inventory")
        
        item = self.inventory[sku]
        valid_fields = {
            "name", "description", "quantity", "unit_price",
            "fsc_certified", "materials", "supplier", "last_restock_date"
        }
        
        for field, value in kwargs.items():
            if field not in valid_fields:
                raise ValueError(f"Invalid field: {field}")
            setattr(item, field, value)
        
        self._save_inventory()
    
    def remove_item(self, sku: str) -> None:
        """
        Remove an item from inventory.
        
        Args:
            sku: SKU of item to remove
            
        Raises:
            KeyError: If SKU doesn't exist
        """
        if sku not in self.inventory:
            raise KeyError(f"SKU {sku} not found in inventory")
        del self.inventory[sku]
        self._save_inventory()
    
    def get_item(self, sku: str) -> InventoryItem:
        """
        Get an inventory item by SKU.
        
        Args:
            sku: SKU of item to retrieve
            
        Returns:
            The requested InventoryItem
            
        Raises:
            KeyError: If SKU doesn't exist
        """
        if sku not in self.inventory:
            raise KeyError(f"SKU {sku} not found in inventory")
        return self.inventory[sku]
    
    def list_items(self, fsc_only: bool = False) -> List[InventoryItem]:
        """
        List all inventory items, optionally filtered by FSC certification.
        
        Args:
            fsc_only: Whether to return only FSC-certified items
            
        Returns:
            List of InventoryItems matching criteria
        """
        items = list(self.inventory.values())
        if fsc_only:
            items = [item for item in items if item.fsc_certified]
        return items
    
    def restock_item(self, sku: str, quantity: int) -> None:
        """
        Restock an item by adding to its quantity.
        
        Args:
            sku: SKU of item to restock
            quantity: Amount to add to current stock
            
        Raises:
            KeyError: If SKU doesn't exist
            ValueError: If quantity is not positive
        """
        if sku not in self.inventory:
            raise KeyError(f"SKU {sku} not found in inventory")
        if quantity <= 0:
            raise ValueError("Restock quantity must be positive")
        
        item = self.inventory[sku]
        item.quantity += quantity
        item.last_restock_date = datetime.now().strftime("%Y-%m-%d")
        self._save_inventory()
    
    def sell_item(self, sku: str, quantity: int) -> float:
        """
        Sell items from inventory and return total price.
        
        Args:
            sku: SKU of item to sell
            quantity: Number of units to sell
            
        Returns:
            Total price of sold items
            
        Raises:
            KeyError: If SKU doesn't exist
            ValueError: If quantity exceeds available stock or is not positive
        """
        if sku not in self.inventory:
            raise KeyError(f"SKU {sku} not found in inventory")
        if quantity <= 0:
            raise ValueError("Sale quantity must be positive")
        
        item = self.inventory[sku]
        if item.quantity < quantity:
            raise ValueError(f"Insufficient stock. Available: {item.quantity}")
        
        item.quantity -= quantity
        self._save_inventory()
        return item.unit_price * quantity
    
    def get_low_stock_items(self, threshold: int = 10) -> List[InventoryItem]:
        """
        Get items with stock below specified threshold.
        
        Args:
            threshold: Minimum stock level threshold
            
        Returns:
            List of InventoryItems with low stock
        """
        return [
            item for item in self.inventory.values()
            if item.quantity < threshold
        ]
    
    def get_sustainability_report(self) -> Dict[str, Union[int, float]]:
        """
        Generate a sustainability report.
        
        Returns:
            Dictionary containing sustainability metrics
        """
        total_items = len(self.inventory)
        fsc_items = sum(1 for item in self.inventory.values() if item.fsc_certified)
        sustainable_materials = set()
        
        for item in self.inventory.values():
            sustainable_materials.update(
                material for material in item.materials
                if material.lower() in {"fsc wood", "bamboo", "re
