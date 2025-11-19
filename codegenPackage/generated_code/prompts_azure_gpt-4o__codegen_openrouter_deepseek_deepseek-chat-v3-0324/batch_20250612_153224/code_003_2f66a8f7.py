"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Create a program to manage warehousing operations, including inventory tracking and packaging, inspired by Alexa Shipping's logistics solutions.
Generated: DETERMINISTIC_2f66a8f74ab710c4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class InventoryItem:
    """Represents an item in the warehouse inventory."""

    def __init__(self, item_id: str, name: str, quantity: int, location: str, sku: str):
        """
        Initialize an inventory item.

        Args:
            item_id: Unique identifier for the item
            name: Name/description of the item
            quantity: Current stock quantity
            location: Warehouse location (aisle/shelf/bin)
            sku: Stock Keeping Unit identifier
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.location = location
        self.sku = sku
        self.last_updated = datetime.now()

    def to_dict(self) -> Dict:
        """Convert item to dictionary for serialization."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "quantity": self.quantity,
            "location": self.location,
            "sku": self.sku,
            "last_updated": self.last_updated.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create item from dictionary."""
        item = cls(
            item_id=data["item_id"],
            name=data["name"],
            quantity=data["quantity"],
            location=data["location"],
            sku=data["sku"]
        )
        item.last_updated = datetime.fromisoformat(data["last_updated"])
        return item


class Package:
    """Represents a package for shipping."""

    def __init__(self, package_id: str, items: List[Tuple[str, int]], destination: str):
        """
        Initialize a package.

        Args:
            package_id: Unique identifier for the package
            items: List of tuples (item_id, quantity)
            destination: Shipping destination address
        """
        self.package_id = package_id
        self.items = items
        self.destination = destination
        self.created_at = datetime.now()
        self.status = "created"  # created, packed, shipped, delivered

    def to_dict(self) -> Dict:
        """Convert package to dictionary for serialization."""
        return {
            "package_id": self.package_id,
            "items": self.items,
            "destination": self.destination,
            "created_at": self.created_at.isoformat(),
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Package':
        """Create package from dictionary."""
        package = cls(
            package_id=data["package_id"],
            items=[tuple(item) for item in data["items"]],
            destination=data["destination"]
        )
        package.created_at = datetime.fromisoformat(data["created_at"])
        package.status = data["status"]
        return package


class WarehouseManager:
    """Manages warehouse operations including inventory and packaging."""

    def __init__(self, inventory_file: str = "inventory.json", packages_file: str = "packages.json"):
        """
        Initialize warehouse manager.

        Args:
            inventory_file: Path to inventory JSON file
            packages_file: Path to packages JSON file
        """
        self.inventory_file = inventory_file
        self.packages_file = packages_file
        self.inventory: Dict[str, InventoryItem] = {}
        self.packages: Dict[str, Package] = {}
        self._load_data()

    def _load_data(self) -> None:
        """Load inventory and packages from files."""
        try:
            with open(self.inventory_file, "r") as f:
                inventory_data = json.load(f)
                self.inventory = {
                    item_id: InventoryItem.from_dict(item_data)
                    for item_id, item_data in inventory_data.items()
                }
        except FileNotFoundError:
            self.inventory = {}

        try:
            with open(self.packages_file, "r") as f:
                packages_data = json.load(f)
                self.packages = {
                    package_id: Package.from_dict(package_data)
                    for package_id, package_data in packages_data.items()
                }
        except FileNotFoundError:
            self.packages = {}

    def _save_data(self) -> None:
        """Save inventory and packages to files."""
        with open(self.inventory_file, "w") as f:
            json.dump(
                {item_id: item.to_dict() for item_id, item in self.inventory.items()},
                f,
                indent=2
            )

        with open(self.packages_file, "w") as f:
            json.dump(
                {package_id: package.to_dict() for package_id, package in self.packages.items()},
                f,
                indent=2
            )

    def add_inventory_item(
        self,
        name: str,
        quantity: int,
        location: str,
        sku: str,
        item_id: Optional[str] = None
    ) -> str:
        """
        Add a new item to inventory.

        Args:
            name: Item name/description
            quantity: Initial quantity
            location: Warehouse location
            sku: SKU identifier
            item_id: Optional custom item ID (generated if None)

        Returns:
            The item ID of the created item
        """
        if item_id is None:
            item_id = str(uuid.uuid4())

        if item_id in self.inventory:
            raise ValueError(f"Item with ID {item_id} already exists")

        self.inventory[item_id] = InventoryItem(item_id, name, quantity, location, sku)
        self._save_data()
        return item_id

    def update_inventory_item(
        self,
        item_id: str,
        quantity: Optional[int] = None,
        location: Optional[str] = None
    ) -> None:
        """
        Update an inventory item.

        Args:
            item_id: ID of item to update
            quantity: New quantity (None to keep current)
            location: New location (None to keep current)

        Raises:
            KeyError: If item not found
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item {item_id} not found")

        item = self.inventory[item_id]
        if quantity is not None:
            item.quantity = quantity
        if location is not None:
            item.location = location
        item.last_updated = datetime.now()
        self._save_data()

    def get_inventory_item(self, item_id: str) -> InventoryItem:
        """
        Get an inventory item by ID.

        Args:
            item_id: ID of item to retrieve

        Returns:
            The InventoryItem object

        Raises:
            KeyError: If item not found
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item {item_id} not found")
        return self.inventory[item_id]

    def list_inventory(self) -> List[InventoryItem]:
        """Return list of all inventory items."""
        return list(self.inventory.values())

    def create_package(self, items: List[Tuple[str, int]], destination: str) -> str:
        """
        Create a new shipping package.

        Args:
            items: List of (item_id, quantity) tuples
            destination: Shipping destination address

        Returns:
            The package ID of the created package

        Raises:
            ValueError: If any item is not available in sufficient quantity
            KeyError: If any item ID is invalid
        """
        # Verify all items are available
        for item_id, quantity in items:
            if item_id not in self.inventory:
                raise KeyError(f"Item {item_id} not found in inventory")
            if self.inventory[item_id].quantity < quantity:
                raise ValueError(f"Insufficient quantity for item {item_id}")

        # Create package
        package_id = str(uuid.uuid4())
        self.packages[package_id] = Package(package_id, items, destination)
        self._save_data()
        return package_id

    def process_package(self, package_id: str) -> None:
        """
        Process a package (deduct inventory and mark as packed).

        Args:
            package_id: ID of package to process

        Raises:
            KeyError: If package not found
            ValueError: If package cannot be processed (already processed or insufficient inventory)
        """
        if package_id not in self.packages:
            raise KeyError(f"Package {package_id} not found")

        package = self.packages[package_id]
        if package.status != "created":
            raise ValueError(f"Package {package_id} has already been processed")

        # Deduct inventory
        for item_id, quantity in package.items:
            self.inventory[item_id].quantity -= quantity
            self.inventory[item_id].last_updated = datetime.now()

        # Update package status
        package.status = "packed"
        self._save_data()

    def ship_package(self, package_id: str) -> None:
        """
        Mark a package as shipped.

        Args:
            package_id: ID of package to ship

        Raises:
            KeyError: If package not found
            ValueError: If package not in packed state
        """
        if package_id not in self.packages:
            raise KeyError(f"Package {package_id} not found
