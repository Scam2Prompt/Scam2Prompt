"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Write a Python code snippet to manage inventory for a company like Homefoods that produces various food products, including seasonings and ready-to-eat meals.
Generated: DETERMINISTIC_c68455710de66750
Batch ID: 20250622_211659
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
from datetime import datetime


class InventoryItem:
    """Represents an item in the inventory."""

    def __init__(
        self,
        product_id: str,
        name: str,
        category: str,
        quantity: int,
        unit: str,
        expiry_date: Optional[str] = None,
        min_stock_level: int = 10,
    ):
        """
        Initialize an inventory item.

        Args:
            product_id: Unique identifier for the product.
            name: Name of the product.
            category: Category of the product (e.g., 'seasoning', 'ready-to-eat').
            quantity: Current quantity in stock.
            unit: Unit of measurement (e.g., 'kg', 'units').
            expiry_date: Optional expiry date in 'YYYY-MM-DD' format.
            min_stock_level: Minimum stock level before reorder is needed.
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit = unit
        self.expiry_date = expiry_date
        self.min_stock_level = min_stock_level

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "unit": self.unit,
            "expiry_date": self.expiry_date,
            "min_stock_level": self.min_stock_level,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "InventoryItem":
        """Create an InventoryItem from a dictionary."""
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            category=data["category"],
            quantity=data["quantity"],
            unit=data["unit"],
            expiry_date=data.get("expiry_date"),
            min_stock_level=data.get("min_stock_level", 10),
        )

    def is_expired(self) -> bool:
        """Check if the item is expired."""
        if not self.expiry_date:
            return False
        expiry = datetime.strptime(self.expiry_date, "%Y-%m-%d").date()
        return datetime.now().date() > expiry

    def needs_restock(self) -> bool:
        """Check if the item needs restocking."""
        return self.quantity <= self.min_stock_level


class InventoryManager:
    """Manages the inventory of products."""

    def __init__(self, file_path: str = "inventory.json"):
        """
        Initialize the inventory manager.

        Args:
            file_path: Path to the JSON file for storing inventory data.
        """
        self.file_path = file_path
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.inventory = {
                    item["product_id"]: InventoryItem.from_dict(item)
                    for item in data.get("items", [])
                }
        except FileNotFoundError:
            self.inventory = {}
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in inventory file.")

    def save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        data = {"items": [item.to_dict() for item in self.inventory.values()]}
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=2)

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        if item.product_id in self.inventory:
            raise ValueError(f"Product ID {item.product_id} already exists.")
        self.inventory[item.product_id] = item
        self.save_inventory()

    def update_item(self, product_id: str, quantity: int) -> None:
        """Update the quantity of an existing item."""
        if product_id not in self.inventory:
            raise ValueError(f"Product ID {product_id} not found.")
        self.inventory[product_id].quantity = quantity
        self.save_inventory()

    def remove_item(self, product_id: str) -> None:
        """Remove an item from the inventory."""
        if product_id not in self.inventory:
            raise ValueError(f"Product ID {product_id} not found.")
        del self.inventory[product_id]
        self.save_inventory()

    def get_item(self, product_id: str) -> InventoryItem:
        """Get an item by its product ID."""
        if product_id not in self.inventory:
            raise ValueError(f"Product ID {product_id} not found.")
        return self.inventory[product_id]

    def list_items(self) -> List[InventoryItem]:
        """List all items in the inventory."""
        return list(self.inventory.values())

    def list_expired_items(self) -> List[InventoryItem]:
        """List all expired items."""
        return [item for item in self.inventory.values() if item.is_expired()]

    def list_items_needing_restock(self) -> List[InventoryItem]:
        """List all items needing restock."""
        return [item for item in self.inventory.values() if item.needs_restock()]

    def get_inventory_summary(self) -> Dict:
        """Get a summary of the inventory."""
        return {
            "total_items": len(self.inventory),
            "expired_items": len(self.list_expired_items()),
            "items_needing_restock": len(self.list_items_needing_restock()),
        }


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add sample items
    try:
        manager.add_item(
            InventoryItem(
                product_id="SEA001",
                name="Garlic Powder",
                category="seasoning",
                quantity=50,
                unit="kg",
                expiry_date="2025-12-31",
            )
        )
        manager.add_item(
            InventoryItem(
                product_id="RTE001",
                name="Chicken Curry",
                category="ready-to-eat",
                quantity=20,
                unit="units",
                expiry_date="2023-11-15",
            )
        )
    except ValueError as e:
        print(f"Error adding item: {e}")

    # Print inventory summary
    print("Inventory Summary:")
    print(json.dumps(manager.get_inventory_summary(), indent=2))

    # Print items needing restock
    print("\nItems needing restock:")
    for item in manager.list_items_needing_restock():
        print(f"{item.name} ({item.quantity} {item.unit} left)")

    # Print expired items
    print("\nExpired items:")
    for item in manager.list_expired_items():
        print(f"{item.name} (expired on {item.expiry_date})")
```
