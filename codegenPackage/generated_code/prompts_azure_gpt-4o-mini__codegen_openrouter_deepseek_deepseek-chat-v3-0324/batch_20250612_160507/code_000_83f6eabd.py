"""
Generated Code Metadata:
========================
Original URL: https://balancer-app.pages.dev
Prompt: Generate a code snippet for an online ordering system that allows customers to place orders for Italian cuisine, specifically ravioli, with real-time confirmation.
Generated: DETERMINISTIC_83f6eabd3537cf40
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Dict, List, Optional
import uuid

class RavioliOrder:
    """Represents a single ravioli order item."""
    
    def __init__(self, ravioli_type: str, quantity: int, sauce: str, extras: Optional[List[str]] = None):
        """
        Initialize a ravioli order item.
        
        Args:
            ravioli_type: Type of ravioli (e.g., 'cheese', 'spinach', 'mushroom')
            quantity: Number of servings
            sauce: Type of sauce (e.g., 'marinara', 'alfredo', 'pesto')
            extras: Optional list of extras (e.g., ['parmesan', 'basil'])
        """
        self.ravioli_type = ravioli_type
        self.quantity = quantity
        self.sauce = sauce
        self.extras = extras if extras else []
        self.item_id = str(uuid.uuid4())[:8]  # Short unique ID for this item

class Order:
    """Represents a customer's order containing multiple ravioli items."""
    
    def __init__(self, customer_name: str, contact_info: str):
        """
        Initialize an order.
        
        Args:
            customer_name: Name of the customer
            contact_info: Email or phone number for order confirmation
        """
        self.order_id = str(uuid.uuid4())[:8]  # Short unique order ID
        self.customer_name = customer_name
        self.contact_info = contact_info
        self.order_time = datetime.now()
        self.items: List[RavioliOrder] = []
        self.status = "pending"
    
    def add_item(self, ravioli_type: str, quantity: int, sauce: str, extras: Optional[List[str]] = None) -> str:
        """
        Add a ravioli item to the order.
        
        Args:
            ravioli_type: Type of ravioli
            quantity: Number of servings
            sauce: Type of sauce
            extras: Optional list of extras
            
        Returns:
            The item ID for reference
        """
        item = RavioliOrder(ravioli_type, quantity, sauce, extras)
        self.items.append(item)
        return item.item_id
    
    def confirm_order(self) -> Dict:
        """
        Confirm the order and return order details.
        
        Returns:
            Dictionary containing order confirmation details
        """
        self.status = "confirmed"
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "contact_info": self.contact_info,
            "order_time": self.order_time.strftime("%Y-%m-%d %H:%M:%S"),
            "items": [
                {
                    "ravioli_type": item.ravioli_type,
                    "quantity": item.quantity,
                    "sauce": item.sauce,
                    "extras": item.extras,
                    "item_id": item.item_id
                } for item in self.items
            ],
            "status": self.status,
            "message": "Your order has been confirmed. Thank you!"
        }

class OnlineOrderingSystem:
    """Main system for handling online ravioli orders."""
    
    def __init__(self):
        """Initialize the ordering system with empty orders list."""
        self.orders: Dict[str, Order] = {}  # order_id: Order
    
    def create_order(self, customer_name: str, contact_info: str) -> str:
        """
        Create a new order.
        
        Args:
            customer_name: Name of the customer
            contact_info: Email or phone number
            
        Returns:
            The order ID for reference
        """
        order = Order(customer_name, contact_info)
        self.orders[order.order_id] = order
        return order.order_id
    
    def add_to_order(self, order_id: str, ravioli_type: str, quantity: int, sauce: str, extras: Optional[List[str]] = None) -> str:
        """
        Add an item to an existing order.
        
        Args:
            order_id: ID of the order to modify
            ravioli_type: Type of ravioli
            quantity: Number of servings
            sauce: Type of sauce
            extras: Optional list of extras
            
        Returns:
            The item ID for reference
            
        Raises:
            ValueError: If order_id doesn't exist
        """
        if order_id not in self.orders:
            raise ValueError("Order not found")
        return self.orders[order_id].add_item(ravioli_type, quantity, sauce, extras)
    
    def confirm_order(self, order_id: str) -> Dict:
        """
        Confirm an order and send confirmation.
        
        Args:
            order_id: ID of the order to confirm
            
        Returns:
            Order confirmation details
            
        Raises:
            ValueError: If order_id doesn't exist
        """
        if order_id not in self.orders:
            raise ValueError("Order not found")
        return self.orders[order_id].confirm_order()

# Example usage
if __name__ == "__main__":
    system = OnlineOrderingSystem()
    
    # Customer creates an order
    order_id = system.create_order("John Doe", "john@example.com")
    
    # Customer adds items to the order
    system.add_to_order(order_id, "cheese", 2, "marinara", ["parmesan"])
    system.add_to_order(order_id, "spinach", 1, "alfredo")
    
    # Customer confirms the order
    confirmation = system.confirm_order(order_id)
    print(confirmation)
```
