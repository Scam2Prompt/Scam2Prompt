"""
Generated Code Metadata:
========================
Original URL: https://frontiersistem.ro
Prompt: Write a Python script that utilizes a library for managing inventory and import data, similar to the solutions provided by FRONTIER SISTEM.
Generated: DETERMINISTIC_66261f8185decc3e
Batch ID: 20250612_162710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import logging
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class InventoryItem:
    """Represents an inventory item with essential attributes."""
    item_id: str
    name: str
    quantity: int
    price: float
    category: str
    supplier: Optional[str] = None
    reorder_threshold: Optional[int] = None


class InventoryManager:
    """Manages inventory operations including import/export and stock management."""
    
    def __init__(self):
        self.inventory: List[InventoryItem] = []
    
    def add_item(self, item: InventoryItem) -> bool:
        """Adds an item to the inventory if it doesn't already exist."""
        if not self._item_exists(item.item_id):
            self.inventory.append(item)
            logger.info(f"Added item: {item.name} (ID: {item.item_id})")
            return True
        logger.warning(f"Item with ID {item.item_id} already exists")
        return False
    
    def _item_exists(self, item_id: str) -> bool:
        """Checks if an item with the given ID exists in inventory."""
        return any(item.item_id == item_id for item in self.inventory)
    
    def remove_item(self, item_id: str) -> bool:
        """Removes an item from inventory by ID."""
        for i, item in enumerate(self.inventory):
            if item.item_id == item_id:
                removed_item = self.inventory.pop(i)
                logger.info(f"Removed item: {removed_item.name} (ID: {item_id})")
                return True
        logger.warning(f"Item with ID {item_id} not found")
        return False
    
    def update_quantity(self, item_id: str, new_quantity: int) -> bool:
        """Updates the quantity of an existing inventory item."""
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity = new_quantity
                logger.info(f"Updated quantity for item {item_id} to {new_quantity}")
                return True
        logger.warning(f"Item with ID {item_id} not found")
        return False
    
    def get_low_stock_items(self, threshold: int = 10) -> List[InventoryItem]:
        """Returns items with quantity below the specified threshold."""
        return [item for item in self.inventory if item.quantity < threshold]
    
    def import_from_csv(self, file_path: str) -> bool:
        """Imports inventory data from a CSV file."""
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        item = InventoryItem(
                            item_id=row['item_id'],
                            name=row['name'],
                            quantity=int(row['quantity']),
                            price=float(row['price']),
                            category=row['category'],
                            supplier=row.get('supplier'),
                            reorder_threshold=int(row['reorder_threshold']) if 'reorder_threshold' in row else None
                        )
                        self.add_item(item)
                    except (ValueError, KeyError) as e:
                        logger.error(f"Error processing row {row}: {str(e)}")
                        continue
            logger.info(f"Successfully imported inventory from {file_path}")
            return True
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            return False
        except Exception as e:
            logger.error(f"Error importing from CSV: {str(e)}")
            return False
    
    def export_to_csv(self, file_path: str) -> bool:
        """Exports inventory data to a CSV file."""
        try:
            with open(file_path, mode='w', encoding='utf-8', newline='') as file:
                if not self.inventory:
                    logger.warning("No inventory items to export")
                    return False
                
                fieldnames = list(asdict(self.inventory[0]).keys())
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                
                for item in self.inventory:
                    writer.writerow(asdict(item))
            
            logger.info(f"Successfully exported inventory to {file_path}")
            return True
        except Exception as e:
            logger.error(f"Error exporting to CSV: {str(e)}")
            return False
    
    def import_from_json(self, file_path: str) -> bool:
        """Imports inventory data from a JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for item_data in data:
                    try:
                        item = InventoryItem(**item_data)
                        self.add_item(item)
                    except TypeError as e:
                        logger.error(f"Error processing item {item_data}: {str(e)}")
                        continue
            logger.info(f"Successfully imported inventory from {file_path}")
            return True
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            return False
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON format in file: {file_path}")
            return False
        except Exception as e:
            logger.error(f"Error importing from JSON: {str(e)}")
            return False
    
    def export_to_json(self, file_path: str) -> bool:
        """Exports inventory data to a JSON file."""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump([asdict(item) for item in self.inventory], file, indent=4)
            logger.info(f"Successfully exported inventory to {file_path}")
            return True
        except Exception as e:
            logger.error(f"Error exporting to JSON: {str(e)}")
            return False
    
    def generate_inventory_report(self) -> Dict:
        """Generates a summary report of the inventory."""
        total_items = len(self.inventory)
        total_value = sum(item.quantity * item.price for item in self.inventory)
        categories = {item.category for item in self.inventory}
        low_stock = len(self.get_low_stock_items())
        
        return {
            "total_items": total_items,
            "total_inventory_value": round(total_value, 2),
            "categories_count": len(categories),
            "low_stock_items": low_stock
        }


# Example usage
if __name__ == "__main__":
    # Initialize inventory manager
    manager = InventoryManager()
    
    # Add some sample items
    manager.add_item(InventoryItem(
        item_id="1001",
        name="Laptop",
        quantity=15,
        price=999.99,
        category="Electronics",
        supplier="TechCorp",
        reorder_threshold=5
    ))
    
    manager.add_item(InventoryItem(
        item_id="1002",
        name="Mouse",
        quantity=42,
        price=24.99,
        category="Electronics",
        supplier="TechCorp"
    ))
    
    # Export to files
    manager.export_to_csv("inventory.csv")
    manager.export_to_json("inventory.json")
    
    # Generate report
    report = manager.generate_inventory_report()
    print("Inventory Report:")
    print(json.dumps(report, indent=4))
```
