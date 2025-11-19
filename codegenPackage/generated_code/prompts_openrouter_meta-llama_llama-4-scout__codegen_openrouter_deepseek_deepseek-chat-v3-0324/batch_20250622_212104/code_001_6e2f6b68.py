"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: Write a Python code snippet to manage inventory of ferramentas and equipment, including tracking device serial numbers and maintenance schedules.
Generated: DETERMINISTIC_6e2f6b68669d157b
Batch ID: 20250622_212104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List, Optional
import json
import os


class InventoryItem:
    """Represents an inventory item with serial number and maintenance details."""

    def __init__(
        self,
        name: str,
        serial_number: str,
        purchase_date: datetime.date,
        last_maintenance_date: Optional[datetime.date] = None,
        maintenance_interval_days: int = 365,
    ):
        """
        Initialize an inventory item.

        Args:
            name: Name of the item.
            serial_number: Unique serial number.
            purchase_date: Date when the item was purchased.
            last_maintenance_date: Date of last maintenance (optional).
            maintenance_interval_days: Days between maintenance (default: 365).
        """
        self.name = name
        self.serial_number = serial_number
        self.purchase_date = purchase_date
        self.last_maintenance_date = last_maintenance_date
        self.maintenance_interval_days = maintenance_interval_days

    def needs_maintenance(self) -> bool:
        """Check if the item is due for maintenance."""
        if not self.last_maintenance_date:
            return True
        next_maintenance_date = self.last_maintenance_date + datetime.timedelta(
            days=self.maintenance_interval_days
        )
        return datetime.date.today() >= next_maintenance_date

    def perform_maintenance(self) -> None:
        """Update the last maintenance date to today."""
        self.last_maintenance_date = datetime.date.today()

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            "name": self.name,
            "serial_number": self.serial_number,
            "purchase_date": self.purchase_date.isoformat(),
            "last_maintenance_date": (
                self.last_maintenance_date.isoformat()
                if self.last_maintenance_date
                else None
            ),
            "maintenance_interval_days": self.maintenance_interval_days,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "InventoryItem":
        """Create an InventoryItem from a dictionary."""
        return cls(
            name=data["name"],
            serial_number=data["serial_number"],
            purchase_date=datetime.date.fromisoformat(data["purchase_date"]),
            last_maintenance_date=(
                datetime.date.fromisoformat(data["last_maintenance_date"])
                if data["last_maintenance_date"]
                else None
            ),
            maintenance_interval_days=data["maintenance_interval_days"],
        )


class InventoryManager:
    """Manages a collection of inventory items."""

    def __init__(self, file_path: str = "inventory.json"):
        """
        Initialize the inventory manager.

        Args:
            file_path: Path to the JSON file for storing inventory data.
        """
        self.file_path = file_path
        self.items: Dict[str, InventoryItem] = {}
        self._load_inventory()

    def _load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
        if not os.path.exists(self.file_path):
            return

        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                for item_data in data.values():
                    item = InventoryItem.from_dict(item_data)
                    self.items[item.serial_number] = item
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to load inventory: {e}")

    def _save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        try:
            with open(self.file_path, "w") as file:
                json.dump(
                    {sn: item.to_dict() for sn, item in self.items.items()},
                    file,
                    indent=2,
                )
        except IOError as e:
            raise RuntimeError(f"Failed to save inventory: {e}")

    def add_item(self, item: InventoryItem) -> None:
        """
        Add an item to the inventory.

        Args:
            item: InventoryItem to add.

        Raises:
            ValueError: If an item with the same serial number already exists.
        """
        if item.serial_number in self.items:
            raise ValueError(
                f"Item with serial number {item.serial_number} already exists."
            )
        self.items[item.serial_number] = item
        self._save_inventory()

    def remove_item(self, serial_number: str) -> None:
        """
        Remove an item from the inventory.

        Args:
            serial_number: Serial number of the item to remove.

        Raises:
            KeyError: If the item does not exist.
        """
        if serial_number not in self.items:
            raise KeyError(f"No item with serial number {serial_number} found.")
        del self.items[serial_number]
        self._save_inventory()

    def get_item(self, serial_number: str) -> InventoryItem:
        """
        Retrieve an item by serial number.

        Args:
            serial_number: Serial number of the item to retrieve.

        Returns:
            The requested InventoryItem.

        Raises:
            KeyError: If the item does not exist.
        """
        if serial_number not in self.items:
            raise KeyError(f"No item with serial number {serial_number} found.")
        return self.items[serial_number]

    def list_items(self) -> List[InventoryItem]:
        """Return a list of all inventory items."""
        return list(self.items.values())

    def list_items_needing_maintenance(self) -> List[InventoryItem]:
        """Return a list of items that need maintenance."""
        return [item for item in self.items.values() if item.needs_maintenance()]

    def perform_maintenance(self, serial_number: str) -> None:
        """
        Perform maintenance on an item and update the last maintenance date.

        Args:
            serial_number: Serial number of the item to maintain.

        Raises:
            KeyError: If the item does not exist.
        """
        item = self.get_item(serial_number)
        item.perform_maintenance()
        self._save_inventory()


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add some items
    try:
        manager.add_item(
            InventoryItem(
                name="Drill",
                serial_number="DR123",
                purchase_date=datetime.date(2022, 1, 15),
                maintenance_interval_days=180,
            )
        )
        manager.add_item(
            InventoryItem(
                name="Saw",
                serial_number="SA456",
                purchase_date=datetime.date(2021, 5, 20),
                last_maintenance_date=datetime.date(2023, 1, 10),
            )
        )
    except ValueError as e:
        print(f"Error adding item: {e}")

    # List items needing maintenance
    print("Items needing maintenance:")
    for item in manager.list_items_needing_maintenance():
        print(f"{item.name} (SN: {item.serial_number})")

    # Perform maintenance on an item
    try:
        manager.perform_maintenance("DR123")
        print("Maintenance performed on DR123")
    except KeyError as e:
        print(f"Error performing maintenance: {e}")

    # Remove an item
    try:
        manager.remove_item("SA456")
        print("Removed item SA456")
    except KeyError as e:
        print(f"Error removing item: {e}")
```
