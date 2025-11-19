"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Write code to calculate the storage requirements for a warehouse based on incoming and outgoing goods, tailored to Fealty Worldwide's warehousing services.
Generated: DETERMINISTIC_617e755446d2d249
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Warehouse Storage Calculator for Fealty Worldwide

This module calculates the storage requirements for a warehouse based on incoming
and outgoing goods. It provides functionality to track inventory levels, calculate
storage needs, and generate reports.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime
import csv
import json
import os


@dataclass
class GoodsRecord:
    """Data class representing a goods movement record."""
    item_id: str
    item_name: str
    quantity: int
    movement_type: str  # 'incoming' or 'outgoing'
    date: datetime
    storage_volume: float  # in cubic meters


class WarehouseStorageCalculator:
    """Main class for warehouse storage calculations."""
    
    def __init__(self, initial_inventory: Optional[Dict[str, int]] = None):
        """
        Initialize the calculator with optional initial inventory.
        
        Args:
            initial_inventory: Dictionary of {item_id: quantity} for initial stock
        """
        self.inventory = initial_inventory if initial_inventory else {}
        self.storage_records: List[GoodsRecord] = []
        self.total_storage_volume = 0.0
        
    def add_goods_record(self, record: GoodsRecord) -> None:
        """Add a goods movement record and update inventory."""
        if record.movement_type not in ('incoming', 'outgoing'):
            raise ValueError("Movement type must be 'incoming' or 'outgoing'")
            
        if record.quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        self.storage_records.append(record)
        
        # Update inventory
        current_quantity = self.inventory.get(record.item_id, 0)
        if record.movement_type == 'incoming':
            self.inventory[record.item_id] = current_quantity + record.quantity
            self.total_storage_volume += record.storage_volume * record.quantity
        else:
            if current_quantity < record.quantity:
                raise ValueError("Not enough stock to fulfill outgoing goods")
            self.inventory[record.item_id] = current_quantity - record.quantity
            self.total_storage_volume -= record.storage_volume * record.quantity
    
    def calculate_current_storage(self) -> float:
        """Calculate current total storage volume in use."""
        return self.total_storage_volume
    
    def get_inventory_levels(self) -> Dict[str, int]:
        """Return current inventory levels."""
        return self.inventory.copy()
    
    def generate_storage_report(self) -> Dict:
        """Generate a comprehensive storage report."""
        return {
            "timestamp": datetime.now().isoformat(),
            "total_storage_volume": self.total_storage_volume,
            "inventory_levels": self.inventory,
            "total_items": len(self.inventory),
            "movement_records_count": len(self.storage_records)
        }
    
    def export_to_csv(self, filename: str) -> None:
        """Export movement records to CSV file."""
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['item_id', 'item_name', 'quantity', 
                            'movement_type', 'date', 'storage_volume']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for record in self.storage_records:
                    writer.writerow({
                        'item_id': record.item_id,
                        'item_name': record.item_name,
                        'quantity': record.quantity,
                        'movement_type': record.movement_type,
                        'date': record.date.isoformat(),
                        'storage_volume': record.storage_volume
                    })
        except IOError as e:
            raise IOError(f"Failed to write CSV file: {e}")
    
    def import_from_csv(self, filename: str) -> None:
        """Import movement records from CSV file."""
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        record = GoodsRecord(
                            item_id=row['item_id'],
                            item_name=row['item_name'],
                            quantity=int(row['quantity']),
                            movement_type=row['movement_type'],
                            date=datetime.fromisoformat(row['date']),
                            storage_volume=float(row['storage_volume'])
                        )
                        self.add_goods_record(record)
                    except (ValueError, KeyError) as e:
                        print(f"Skipping invalid record: {e}")
        except IOError as e:
            raise IOError(f"Failed to read CSV file: {e}")
    
    def save_state(self, filename: str) -> None:
        """Save current state to JSON file."""
        state = {
            'inventory': self.inventory,
            'total_storage_volume': self.total_storage_volume,
            'storage_records': [
                {
                    'item_id': r.item_id,
                    'item_name': r.item_name,
                    'quantity': r.quantity,
                    'movement_type': r.movement_type,
                    'date': r.date.isoformat(),
                    'storage_volume': r.storage_volume
                }
                for r in self.storage_records
            ]
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(state, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save state: {e}")
    
    def load_state(self, filename: str) -> None:
        """Load state from JSON file."""
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
                
            self.inventory = state['inventory']
            self.total_storage_volume = state['total_storage_volume']
            
            self.storage_records = []
            for record in state['storage_records']:
                self.storage_records.append(GoodsRecord(
                    item_id=record['item_id'],
                    item_name=record['item_name'],
                    quantity=record['quantity'],
                    movement_type=record['movement_type'],
                    date=datetime.fromisoformat(record['date']),
                    storage_volume=record['storage_volume']
                ))
        except (IOError, KeyError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load state: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize calculator
    calculator = WarehouseStorageCalculator()
    
    # Add some sample records
    try:
        calculator.add_goods_record(GoodsRecord(
            item_id="P001",
            item_name="Product A",
            quantity=100,
            movement_type="incoming",
            date=datetime.now(),
            storage_volume=0.5
        ))
        
        calculator.add_goods_record(GoodsRecord(
            item_id="P002",
            item_name="Product B",
            quantity=50,
            movement_type="incoming",
            date=datetime.now(),
            storage_volume=1.2
        ))
        
        calculator.add_goods_record(GoodsRecord(
            item_id="P001",
            item_name="Product A",
            quantity=30,
            movement_type="outgoing",
            date=datetime.now(),
            storage_volume=0.5
        ))
        
        # Generate report
        report = calculator.generate_storage_report()
        print("Storage Report:")
        print(json.dumps(report, indent=2))
        
        # Export to CSV
        calculator.export_to_csv("warehouse_movements.csv")
        print("Data exported to warehouse_movements.csv")
        
    except ValueError as e:
        print(f"Error: {e}")
```
