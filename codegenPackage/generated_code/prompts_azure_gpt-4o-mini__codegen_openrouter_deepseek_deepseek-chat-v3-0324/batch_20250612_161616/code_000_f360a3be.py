"""
Generated Code Metadata:
========================
Original URL: https://snackpointemmen.nl
Prompt: Generate a code snippet for a restaurant ordering system that includes features for takeaway and contactless payment, similar to Snackpoint Emmen's services.
Generated: DETERMINISTIC_f360a3beb2af621a
Batch ID: 20250612_161616
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
from enum import Enum, auto

class OrderStatus(Enum):
    """Enum representing the status of an order."""
    PENDING = auto()
    PREPARING = auto()
    READY = auto()
    COMPLETED = auto()
    CANCELLED = auto()

class PaymentMethod(Enum):
    """Enum representing payment methods."""
    CASH = auto()
    CARD = auto()
    CONTACTLESS = auto()
    ONLINE = auto()

class MenuItem:
    """Class representing a menu item."""
    def __init__(self, item_id: int, name: str, price: float, description: str = ""):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.description = description

    def to_dict(self):
        """Convert MenuItem to dictionary for serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }

class OrderItem:
    """Class representing an item in an order."""
    def __init__(self, menu_item: MenuItem, quantity: int = 1, special_requests: str = ""):
        self.menu_item = menu_item
        self.quantity = quantity
        self.special_requests = special_requests

    def get_total_price(self) -> float:
        """Calculate total price for this order item."""
        return self.menu_item.price * self.quantity

    def to_dict(self):
        """Convert OrderItem to dictionary for serialization."""
        return {
            'menu_item': self.menu_item.to_dict(),
            'quantity': self.quantity,
            'special_requests': self.special_requests
        }

class Order:
    """Class representing a customer order."""
    def __init__(self, order_id: int, customer_name: str, is_takeaway: bool = False):
        self.order_id = order_id
        self.customer_name = customer_name
        self.is_takeaway = is_takeaway
        self.order_items = []
        self.status = OrderStatus.PENDING
        self.payment_method = None
        self.order_time = datetime.now()
        self.total_price = 0.0

    def add_item(self, order_item: OrderItem):
        """Add an item to the order."""
        self.order_items.append(order_item)
        self._update_total_price()

    def remove_item(self, item_index: int):
        """Remove an item from the order by index."""
        if 0 <= item_index < len(self.order_items):
            self.order_items.pop(item_index)
            self._update_total_price()

    def set_payment_method(self, method: PaymentMethod):
        """Set the payment method for the order."""
        self.payment_method = method

    def update_status(self, new_status: OrderStatus):
        """Update the status of the order."""
        self.status = new_status

    def _update_total_price(self):
        """Recalculate the total price of the order."""
        self.total_price = sum(item.get_total_price() for item in self.order_items)

    def to_dict(self):
        """Convert Order to dictionary for serialization."""
        return {
            'order_id': self.order_id,
            'customer_name': self.customer_name,
            'is_takeaway': self.is_takeaway,
            'order_items': [item.to_dict() for item in self.order_items],
            'status': self.status.name,
            'payment_method': self.payment_method.name if self.payment_method else None,
            'order_time': self.order_time.isoformat(),
            'total_price': self.total_price
        }

class RestaurantOrderSystem:
    """Main class for the restaurant ordering system."""
    def __init__(self):
        self.orders = {}
        self.menu = {}
        self.next_order_id = 1

    def add_menu_item(self, menu_item: MenuItem):
        """Add a new item to the menu."""
        self.menu[menu_item.item_id] = menu_item

    def create_order(self, customer_name: str, is_takeaway: bool = False) -> Order:
        """Create a new order."""
        order = Order(self.next_order_id, customer_name, is_takeaway)
        self.orders[order.order_id] = order
        self.next_order_id += 1
        return order

    def get_order(self, order_id: int) -> Order:
        """Retrieve an order by ID."""
        return self.orders.get(order_id)

    def process_payment(self, order_id: int, payment_method: PaymentMethod, amount: float) -> bool:
        """Process payment for an order."""
        order = self.get_order(order_id)
        if not order:
            return False
        
        if amount < order.total_price:
            return False
        
        order.set_payment_method(payment_method)
        order.update_status(OrderStatus.PREPARING)
        return True

    def complete_order(self, order_id: int) -> bool:
        """Mark an order as completed."""
        order = self.get_order(order_id)
        if not order or order.status != OrderStatus.READY:
            return False
        
        order.update_status(OrderStatus.COMPLETED)
        return True

    def cancel_order(self, order_id: int) -> bool:
        """Cancel an order."""
        order = self.get_order(order_id)
        if not order or order.status in (OrderStatus.COMPLETED, OrderStatus.CANCELLED):
            return False
        
        order.update_status(OrderStatus.CANCELLED)
        return True

    def save_orders_to_file(self, filename: str):
        """Save all orders to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'orders': [order.to_dict() for order in self.orders.values()],
                    'next_order_id': self.next_order_id
                }, f, indent=2)
        except IOError as e:
            print(f"Error saving orders: {e}")

    def load_orders_from_file(self, filename: str):
        """Load orders from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.next_order_id = data['next_order_id']
                
                for order_data in data['orders']:
                    order = Order(
                        order_data['order_id'],
                        order_data['customer_name'],
                        order_data['is_takeaway']
                    )
                    order.status = OrderStatus[order_data['status']]
                    if order_data['payment_method']:
                        order.payment_method = PaymentMethod[order_data['payment_method']]
                    order.order_time = datetime.fromisoformat(order_data['order_time'])
                    order.total_price = order_data['total_price']
                    
                    for item_data in order_data['order_items']:
                        menu_item = MenuItem(
                            item_data['menu_item']['item_id'],
                            item_data['menu_item']['name'],
                            item_data['menu_item']['price'],
                            item_data['menu_item']['description']
                        )
                        order_item = OrderItem(
                            menu_item,
                            item_data['quantity'],
                            item_data['special_requests']
                        )
                        order.order_items.append(order_item)
                    
                    self.orders[order.order_id] = order
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading orders: {e}")

# Example usage
if __name__ == "__main__":
    system = RestaurantOrderSystem()
    
    # Add menu items
    system.add_menu_item(MenuItem(1, "Burger", 8.99, "Classic beef burger"))
    system.add_menu_item(MenuItem(2, "Pizza", 12.99, "Margherita pizza"))
    system.add_menu_item(MenuItem(3, "Salad", 6.99, "Caesar salad"))
    
    # Create an order
    order = system.create_order("John Doe", is_takeaway=True)
    burger = system.menu[1]
    pizza = system.menu[2]
    
    order.add_item(OrderItem(burger, 2))
    order.add_item(OrderItem(pizza, 1, "Extra cheese"))
    
    # Process payment
    if system.process_payment(order.order_id, PaymentMethod.CONTACTLESS, order.total_price):
        print("Payment processed successfully")
    
    # Save orders to file
    system.save_orders_to_file("orders.json")
```
