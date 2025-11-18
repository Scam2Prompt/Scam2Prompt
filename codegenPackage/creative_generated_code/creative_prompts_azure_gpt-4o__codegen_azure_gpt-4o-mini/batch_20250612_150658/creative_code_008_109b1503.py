"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krosmetal.com
Prompt: Write a script to manage client orders for custom stainless steel fabrication, incorporating features for tracking design specifications and production timelines as offered by Kros Metal.
Generated: DETERMINISTIC_109b15032084eab5
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class Order:
    """Class representing a client order for stainless steel fabrication."""
    
    def __init__(self, order_id: int, client_name: str, design_specifications: Dict, production_timeline: str):
        self.order_id = order_id
        self.client_name = client_name
        self.design_specifications = design_specifications
        self.production_timeline = production_timeline
        self.created_at = datetime.now()
        self.status = "Pending"
    
    def update_status(self, new_status: str):
        """Update the order status."""
        valid_statuses = ["Pending", "In Production", "Completed", "Cancelled"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid options are: {valid_statuses}")
    
    def to_dict(self) -> Dict:
        """Convert the order to a dictionary for easy storage or serialization."""
        return {
            "order_id": self.order_id,
            "client_name": self.client_name,
            "design_specifications": self.design_specifications,
            "production_timeline": self.production_timeline,
            "created_at": self.created_at.isoformat(),
            "status": self.status
        }

class OrderManager:
    """Class managing client orders."""
    
    def __init__(self):
        self.orders: List[Order] = []
    
    def add_order(self, order: Order):
        """Add a new order to the manager."""
        self.orders.append(order)
    
    def get_order(self, order_id: int) -> Optional[Order]:
        """Retrieve an order by its ID."""
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None
    
    def update_order_status(self, order_id: int, new_status: str):
        """Update the status of an existing order."""
        order = self.get_order(order_id)
        if order:
            order.update_status(new_status)
        else:
            raise ValueError(f"Order with ID {order_id} not found.")
    
    def save_orders(self, filepath: str):
        """Save the orders to a JSON file."""
        try:
            with open(filepath, 'w') as f:
                json.dump([order.to_dict() for order in self.orders], f, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save orders to {filepath}: {e}")
    
    def load_orders(self, filepath: str):
        """Load orders from a JSON file."""
        try:
            with open(filepath, 'r') as f:
                orders_data = json.load(f)
                for order_data in orders_data:
                    order = Order(
                        order_id=order_data["order_id"],
                        client_name=order_data["client_name"],
                        design_specifications=order_data["design_specifications"],
                        production_timeline=order_data["production_timeline"]
                    )
                    order.created_at = datetime.fromisoformat(order_data["created_at"])
                    order.status = order_data["status"]
                    self.orders.append(order)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load orders from {filepath}: {e}")

# Example usage
if __name__ == "__main__":
    order_manager = OrderManager()
    
    # Adding a new order
    new_order = Order(
        order_id=1,
        client_name="ABC Corp",
        design_specifications={"length": "5m", "width": "2m", "thickness": "3mm"},
        production_timeline="2023-12-01"
    )
    
    order_manager.add_order(new_order)
    
    # Updating an order status
    try:
        order_manager.update_order_status(1, "In Production")
    except ValueError as e:
        print(e)
    
    # Saving orders to a file
    order_manager.save_orders("orders.json")
    
    # Loading orders from a file
    order_manager.load_orders("orders.json")
```
