"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Develop a program to manage customer orders for personalized promotional items, incorporating customization options like DTF printing and vinyl textile designs.
Generated: DETERMINISTIC_f5bcbc010a77c73c
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
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime

class CustomizationType(Enum):
    """Enumeration for different types of customization options."""
    DTF_PRINTING = "DTF Printing"
    VINYL_TEXTILE = "Vinyl Textile"

class OrderStatus(Enum):
    """Enumeration for order statuses."""
    PENDING = "Pending"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class CustomizationOption:
    """Class representing a customization option for an order."""
    def __init__(self, option_type: CustomizationType, description: str, additional_cost: float):
        self.option_type = option_type
        self.description = description
        self.additional_cost = additional_cost

    def to_dict(self) -> Dict:
        """Convert the customization option to a dictionary."""
        return {
            "option_type": self.option_type.value,
            "description": self.description,
            "additional_cost": self.additional_cost
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'CustomizationOption':
        """Create a CustomizationOption from a dictionary."""
        return cls(
            option_type=CustomizationType(data["option_type"]),
            description=data["description"],
            additional_cost=data["additional_cost"]
        )

class Order:
    """Class representing a customer order."""
    def __init__(self, order_id: str, customer_name: str, items: List[str], base_cost: float):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.base_cost = base_cost
        self.customizations: List[CustomizationOption] = []
        self.status = OrderStatus.PENDING
        self.created_at = datetime.now()

    def add_customization(self, customization: CustomizationOption) -> None:
        """Add a customization option to the order."""
        self.customizations.append(customization)

    def calculate_total_cost(self) -> float:
        """Calculate the total cost of the order including customizations."""
        total = self.base_cost
        for customization in self.customizations:
            total += customization.additional_cost
        return total

    def update_status(self, new_status: OrderStatus) -> None:
        """Update the status of the order."""
        self.status = new_status

    def to_dict(self) -> Dict:
        """Convert the order to a dictionary."""
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "items": self.items,
            "base_cost": self.base_cost,
            "customizations": [c.to_dict() for c in self.customizations],
            "status": self.status.value,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Order':
        """Create an Order from a dictionary."""
        order = cls(
            order_id=data["order_id"],
            customer_name=data["customer_name"],
            items=data["items"],
            base_cost=data["base_cost"]
        )
        order.customizations = [CustomizationOption.from_dict(c) for c in data["customizations"]]
        order.status = OrderStatus(data["status"])
        order.created_at = datetime.fromisoformat(data["created_at"])
        return order

class OrderManager:
    """Class to manage customer orders."""
    def __init__(self, storage_file: str = "orders.json"):
        self.storage_file = storage_file
        self.orders: Dict[str, Order] = {}
        self.load_orders()

    def add_order(self, order: Order) -> None:
        """Add an order to the manager."""
        if order.order_id in self.orders:
            raise ValueError(f"Order with ID {order.order_id} already exists.")
        self.orders[order.order_id] = order
        self.save_orders()

    def get_order(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by its ID."""
        return self.orders.get(order_id)

    def update_order_status(self, order_id: str, new_status: OrderStatus) -> None:
        """Update the status of an order."""
        order = self.get_order(order_id)
        if not order:
            raise ValueError(f"Order with ID {order_id} not found.")
        order.update_status(new_status)
        self.save_orders()

    def delete_order(self, order_id: str) -> None:
        """Delete an order by its ID."""
        if order_id not in self.orders:
            raise ValueError(f"Order with ID {order_id} not found.")
        del self.orders[order_id]
        self.save_orders()

    def save_orders(self) -> None:
        """Save orders to the storage file."""
        with open(self.storage_file, "w") as f:
            json.dump(
                {order_id: order.to_dict() for order_id, order in self.orders.items()},
                f,
                indent=4
            )

    def load_orders(self) -> None:
        """Load orders from the storage file."""
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.orders = {
                    order_id: Order.from_dict(order_data)
                    for order_id, order_data in data.items()
                }
        except FileNotFoundError:
            self.orders = {}

# Example usage
if __name__ == "__main__":
    manager = OrderManager()

    # Create a new order
    order = Order(
        order_id="ORD123",
        customer_name="John Doe",
        items=["T-Shirt", "Mug"],
        base_cost=25.99
    )

    # Add customizations
    order.add_customization(
        CustomizationOption(
            option_type=CustomizationType.DTF_PRINTING,
            description="Company Logo",
            additional_cost=5.99
        )
    )
    order.add_customization(
        CustomizationOption(
            option_type=CustomizationType.VINYL_TEXTILE,
            description="Custom Text",
            additional_cost=3.99
        )
    )

    # Add order to manager
    manager.add_order(order)

    # Retrieve and print order
    retrieved_order = manager.get_order("ORD123")
    if retrieved_order:
        print(f"Order Total: ${retrieved_order.calculate_total_cost():.2f}")
        print(f"Status: {retrieved_order.status.value}")
```
