"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Write a function to manage inventory for schools, including stock tracking and purchase records, inspired by Him Saral's Inventory module.
Generated: DETERMINISTIC_db5e6d5d66b30156
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import json
import os
from enum import Enum, auto


class ItemCategory(Enum):
    """Enum representing different categories of inventory items."""
    STATIONERY = auto()
    FURNITURE = auto()
    ELECTRONICS = auto()
    LAB_EQUIPMENT = auto()
    SPORTS = auto()
    OTHER = auto()


@dataclass
class InventoryItem:
    """Class representing an inventory item."""
    item_id: str
    name: str
    category: ItemCategory
    quantity: int
    unit_price: float
    min_stock_level: int = 0
    last_restocked: Optional[datetime.date] = None
    supplier: Optional[str] = None


@dataclass
class PurchaseRecord:
    """Class representing a purchase record."""
    record_id: str
    item_id: str
    quantity: int
    purchase_date: datetime.date
    unit_price: float
    supplier: str
    notes: str = ""


class InventoryManager:
    """Class to manage school inventory including stock tracking and purchase records."""
    
    def __init__(self, data_dir: str = "inventory_data"):
        """Initialize the inventory manager with data directory."""
        self.data_dir = data_dir
        self.items: Dict[str, InventoryItem] = {}
        self.purchase_records: List[PurchaseRecord] = []
        
        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load existing data
        self._load_data()

    def _load_data(self) -> None:
        """Load inventory data from files."""
        try:
            # Load items
            items_path = os.path.join(self.data_dir, "items.json")
            if os.path.exists(items_path):
                with open(items_path, "r") as f:
                    items_data = json.load(f)
                    for item_id, item_data in items_data.items():
                        self.items[item_id] = InventoryItem(
                            item_id=item_id,
                            name=item_data["name"],
                            category=ItemCategory[item_data["category"]],
                            quantity=item_data["quantity"],
                            unit_price=item_data["unit_price"],
                            min_stock_level=item_data.get("min_stock_level", 0),
                            last_restocked=datetime.date.fromisoformat(item_data["last_restocked"]) 
                                if item_data.get("last_restocked") else None,
                            supplier=item_data.get("supplier")
                        )
            
            # Load purchase records
            records_path = os.path.join(self.data_dir, "purchase_records.json")
            if os.path.exists(records_path):
                with open(records_path, "r") as f:
                    records_data = json.load(f)
                    for record_data in records_data:
                        self.purchase_records.append(PurchaseRecord(
                            record_id=record_data["record_id"],
                            item_id=record_data["item_id"],
                            quantity=record_data["quantity"],
                            purchase_date=datetime.date.fromisoformat(record_data["purchase_date"]),
                            unit_price=record_data["unit_price"],
                            supplier=record_data["supplier"],
                            notes=record_data.get("notes", "")
                        ))
        except Exception as e:
            raise RuntimeError(f"Failed to load inventory data: {str(e)}")

    def _save_data(self) -> None:
        """Save inventory data to files."""
        try:
            # Save items
            items_path = os.path.join(self.data_dir, "items.json")
            items_data = {
                item_id: {
                    "name": item.name,
                    "category": item.category.name,
                    "quantity": item.quantity,
                    "unit_price": item.unit_price,
                    "min_stock_level": item.min_stock_level,
                    "last_restocked": item.last_restocked.isoformat() if item.last_restocked else None,
                    "supplier": item.supplier
                }
                for item_id, item in self.items.items()
            }
            with open(items_path, "w") as f:
                json.dump(items_data, f, indent=2)
            
            # Save purchase records
            records_path = os.path.join(self.data_dir, "purchase_records.json")
            records_data = [
                {
                    "record_id": record.record_id,
                    "item_id": record.item_id,
                    "quantity": record.quantity,
                    "purchase_date": record.purchase_date.isoformat(),
                    "unit_price": record.unit_price,
                    "supplier": record.supplier,
                    "notes": record.notes
                }
                for record in self.purchase_records
            ]
            with open(records_path, "w") as f:
                json.dump(records_data, f, indent=2)
        except Exception as e:
            raise RuntimeError(f"Failed to save inventory data: {str(e)}")

    def add_item(self, item_id: str, name: str, category: ItemCategory, quantity: int, 
                 unit_price: float, min_stock_level: int = 0, supplier: Optional[str] = None) -> None:
        """Add a new item to the inventory."""
        if item_id in self.items:
            raise ValueError(f"Item with ID {item_id} already exists")
        
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        if unit_price <= 0:
            raise ValueError("Unit price must be positive")
        
        self.items[item_id] = InventoryItem(
            item_id=item_id,
            name=name,
            category=category,
            quantity=quantity,
            unit_price=unit_price,
            min_stock_level=min_stock_level,
            supplier=supplier
        )
        self._save_data()

    def update_item_quantity(self, item_id: str, quantity_change: int) -> None:
        """Update the quantity of an existing item."""
        if item_id not in self.items:
            raise ValueError(f"Item with ID {item_id} not found")
        
        new_quantity = self.items[item_id].quantity + quantity_change
        if new_quantity < 0:
            raise ValueError("Resulting quantity cannot be negative")
        
        self.items[item_id].quantity = new_quantity
        self._save_data()

    def record_purchase(self, item_id: str, quantity: int, unit_price: float, 
                        supplier: str, purchase_date: Optional[datetime.date] = None, 
                        notes: str = "") -> str:
        """Record a purchase of an inventory item."""
        if item_id not in self.items:
            raise ValueError(f"Item with ID {item_id} not found")
        
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive")
        
        if unit_price <= 0:
            raise ValueError("Unit price must be positive")
        
        record_id = f"PR-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        purchase_date = purchase_date or datetime.date.today()
        
        record = PurchaseRecord(
            record_id=record_id,
            item_id=item_id,
            quantity=quantity,
            purchase_date=purchase_date,
            unit_price=unit_price,
            supplier=supplier,
            notes=notes
        )
        
        self.purchase_records.append(record)
        self.update_item_quantity(item_id, quantity)
        self.items[item_id].last_restocked = purchase_date
        self._save_data()
        
        return record_id

    def get_item(self, item_id: str) -> InventoryItem:
        """Get an inventory item by ID."""
        if item_id not in self.items:
            raise ValueError(f"Item with ID {item_id} not found")
        return self.items[item_id]

    def get_low_stock_items(self, threshold: Optional[int] = None) -> List[Tuple[InventoryItem, int]]:
        """Get items that are below their minimum stock level or a custom threshold."""
        low_stock = []
        for item in self.items.values():
            threshold_to_use = threshold if threshold is not None else item.min_stock_level
            if item.quantity < threshold_to_use:
                low_stock.append((item, item.quantity))
        return low_stock

    def get_purchase_history(self, item_id: Optional[str] = None, 
                            start_date: Optional[datetime.date] = None, 
                            end_date: Optional[datetime.date] = None) -> List[PurchaseRecord]:
        """Get purchase records filtered by item ID and/or date range."""
        filtered_records = []
        
        for record in self.purchase_records:
            # Filter by item ID if provided
            if item_id is not None and record.item_id != item_id:
                continue
                
            # Filter by date range if provided
            if start_date is not None and record.purchase_date < start_date:
                continue
            if end_date is not None and record.purchase_date > end_date:
                continue
                
            filtered_records.append(record)
            
        return filtered_records

    def generate_inventory_report(self) -> Dict:
        """Generate a summary report of the inventory."""
        total_items = len(self.items)
        total_quantity = sum(item.
