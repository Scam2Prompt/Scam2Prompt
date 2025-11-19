"""
Generated Code Metadata:
========================
Original URL: https://blackhillsports.com
Prompt: "Write a Python script to manage custom apparel orders for a clothing manufacturer like Black Hill Sports, including services such as cut & sew, embroidery, and printing."
Generated: DETERMINISTIC_d1e7075881df47ee
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Tuple


class ServiceType(Enum):
    """Enum representing available apparel services."""
    CUT_SEW = "Cut & Sew"
    EMBROIDERY = "Embroidery"
    PRINTING = "Printing"


class OrderStatus(Enum):
    """Enum representing order statuses."""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class ApparelItem:
    """Class representing an apparel item in an order."""
    
    def __init__(
        self,
        item_id: str,
        name: str,
        quantity: int,
        materials: List[str],
        services: List[ServiceType],
        measurements: Optional[Dict[str, float]] = None,
        design_files: Optional[List[str]] = None
    ):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.materials = materials
        self.services = services
        self.measurements = measurements or {}
        self.design_files = design_files or []

    def to_dict(self) -> Dict:
        """Convert the apparel item to a dictionary."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "quantity": self.quantity,
            "materials": self.materials,
            "services": [service.value for service in self.services],
            "measurements": self.measurements,
            "design_files": self.design_files
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'ApparelItem':
        """Create an apparel item from a dictionary."""
        services = [ServiceType(service) for service in data["services"]]
        return cls(
            item_id=data["item_id"],
            name=data["name"],
            quantity=data["quantity"],
            materials=data["materials"],
            services=services,
            measurements=data.get("measurements", {}),
            design_files=data.get("design_files", [])
        )


class Order:
    """Class representing a customer order."""
    
    def __init__(
        self,
        order_id: str,
        customer_id: str,
        items: List[ApparelItem],
        status: OrderStatus = OrderStatus.PENDING,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        notes: Optional[str] = None
    ):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.status = status
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.notes = notes or ""

    def update_status(self, new_status: OrderStatus) -> None:
        """Update the order status and set the updated timestamp."""
        self.status = new_status
        self.updated_at = datetime.now()

    def add_item(self, item: ApparelItem) -> None:
        """Add an item to the order."""
        self.items.append(item)
        self.updated_at = datetime.now()

    def remove_item(self, item_id: str) -> bool:
        """Remove an item from the order by ID."""
        for i, item in enumerate(self.items):
            if item.item_id == item_id:
                self.items.pop(i)
                self.updated_at = datetime.now()
                return True
        return False

    def to_dict(self) -> Dict:
        """Convert the order to a dictionary."""
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "items": [item.to_dict() for item in self.items],
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Order':
        """Create an order from a dictionary."""
        items = [ApparelItem.from_dict(item) for item in data["items"]]
        return cls(
            order_id=data["order_id"],
            customer_id=data["customer_id"],
            items=items,
            status=OrderStatus(data["status"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            notes=data.get("notes", "")
        )


class OrderManager:
    """Class to manage apparel orders."""
    
    def __init__(self, storage_file: str = "orders.json"):
        self.storage_file = storage_file
        self.orders: Dict[str, Order] = {}
        self._load_orders()

    def _load_orders(self) -> None:
        """Load orders from the storage file."""
        try:
            with open(self.storage_file, "r") as f:
                orders_data = json.load(f)
                self.orders = {
                    order_id: Order.from_dict(order_data)
                    for order_id, order_data in orders_data.items()
                }
        except FileNotFoundError:
            self.orders = {}
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in storage file")

    def _save_orders(self) -> None:
        """Save orders to the storage file."""
        orders_data = {
            order_id: order.to_dict()
            for order_id, order in self.orders.items()
        }
        with open(self.storage_file, "w") as f:
            json.dump(orders_data, f, indent=2)

    def create_order(self, customer_id: str, items: List[ApparelItem]) -> Order:
        """Create a new order."""
        order_id = f"ORD-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        order = Order(order_id, customer_id, items)
        self.orders[order_id] = order
        self._save_orders()
        return order

    def get_order(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by ID."""
        return self.orders.get(order_id)

    def update_order_status(self, order_id: str, new_status: OrderStatus) -> bool:
        """Update the status of an order."""
        if order_id not in self.orders:
            return False
        
        self.orders[order_id].update_status(new_status)
        self._save_orders()
        return True

    def add_item_to_order(self, order_id: str, item: ApparelItem) -> bool:
        """Add an item to an existing order."""
        if order_id not in self.orders:
            return False
        
        self.orders[order_id].add_item(item)
        self._save_orders()
        return True

    def remove_item_from_order(self, order_id: str, item_id: str) -> bool:
        """Remove an item from an existing order."""
        if order_id not in self.orders:
            return False
        
        success = self.orders[order_id].remove_item(item_id)
        if success:
            self._save_orders()
        return success

    def get_orders_by_status(self, status: OrderStatus) -> List[Order]:
        """Get all orders with a specific status."""
        return [
            order for order in self.orders.values()
            if order.status == status
        ]

    def get_customer_orders(self, customer_id: str) -> List[Order]:
        """Get all orders for a specific customer."""
        return [
            order for order in self.orders.values()
            if order.customer_id == customer_id
        ]


def main():
    """Example usage of the OrderManager."""
    manager = OrderManager()
    
    # Create sample items
    t_shirt = ApparelItem(
        item_id="ITEM-001",
        name="Custom T-Shirt",
        quantity=50,
        materials=["Cotton"],
        services=[ServiceType.PRINTING],
        design_files=["design1.png", "design2.png"]
    )
    
    hoodie = ApparelItem(
        item_id="ITEM-002",
        name="Embroidered Hoodie",
        quantity=25,
        materials=["Polyester"],
        services=[ServiceType.EMBROIDERY],
        measurements={"chest": 42, "length": 28}
    )
    
    # Create an order
    order = manager.create_order(
        customer_id="CUST-123",
        items=[t_shirt, hoodie]
    )
    
    print(f"Created order: {order.order_id}")
    
    # Update order status
    manager.update_order_status(order.order_id, OrderStatus.IN_PROGRESS)
    
    # Retrieve order
    retrieved_order = manager.get_order(order.order_id)
    if retrieved_order:
        print(f"Order status: {retrieved_order.status.value}")


if __name__ == "__main__":
    main()
```
