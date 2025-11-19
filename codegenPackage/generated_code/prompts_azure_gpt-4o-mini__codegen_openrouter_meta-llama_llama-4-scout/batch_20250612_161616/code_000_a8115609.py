"""
Generated Code Metadata:
========================
Original URL: https://purebite.fi
Prompt: Generate a code snippet for a restaurant management system that includes features for online table reservations and takeout orders, inspired by the services offered by Purebite.
Generated: DETERMINISTIC_a81156092e0796ed
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# restaurant_management_system.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class OrderStatus(Enum):
    """Order status enumeration"""
    PENDING = 1
    PREPARING = 2
    READY_FOR_PICKUP = 3
    DELIVERED = 4
    CANCELED = 5

class TableStatus(Enum):
    """Table status enumeration"""
    AVAILABLE = 1
    OCCUPIED = 2
    RESERVED = 3

class MenuItem:
    """Menu item class"""
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

class Order:
    """Order class"""
    def __init__(self, id: int, customer_name: str, order_status: OrderStatus = OrderStatus.PENDING):
        self.id = id
        self.customer_name = customer_name
        self.order_status = order_status
        self.items: List[MenuItem] = []
        self.total_cost: float = 0.0

    def add_item(self, item: MenuItem):
        """Add item to order"""
        self.items.append(item)
        self.total_cost += item.price

    def update_status(self, status: OrderStatus):
        """Update order status"""
        self.order_status = status

class Table:
    """Table class"""
    def __init__(self, id: int, capacity: int, table_status: TableStatus = TableStatus.AVAILABLE):
        self.id = id
        self.capacity = capacity
        self.table_status = table_status
        self.reservation_time: datetime = None

    def reserve_table(self, reservation_time: datetime):
        """Reserve table"""
        self.table_status = TableStatus.RESERVED
        self.reservation_time = reservation_time

    def occupy_table(self):
        """Occupy table"""
        self.table_status = TableStatus.OCCUPIED

    def release_table(self):
        """Release table"""
        self.table_status = TableStatus.AVAILABLE
        self.reservation_time = None

class RestaurantManagementSystem:
    """Restaurant management system class"""
    def __init__(self):
        self.tables: Dict[int, Table] = {}
        self.orders: Dict[int, Order] = {}
        self.menu_items: Dict[int, MenuItem] = {}

    def add_table(self, table: Table):
        """Add table to system"""
        self.tables[table.id] = table

    def add_order(self, order: Order):
        """Add order to system"""
        self.orders[order.id] = order

    def add_menu_item(self, item: MenuItem):
        """Add menu item to system"""
        self.menu_items[item.id] = item

    def reserve_table(self, table_id: int, reservation_time: datetime):
        """Reserve table"""
        if table_id in self.tables:
            self.tables[table_id].reserve_table(reservation_time)
        else:
            raise ValueError("Table not found")

    def place_order(self, order_id: int, customer_name: str):
        """Place order"""
        order = Order(order_id, customer_name)
        self.add_order(order)
        return order

    def add_item_to_order(self, order_id: int, item_id: int):
        """Add item to order"""
        if order_id in self.orders and item_id in self.menu_items:
            self.orders[order_id].add_item(self.menu_items[item_id])
        else:
            raise ValueError("Order or menu item not found")

    def update_order_status(self, order_id: int, status: OrderStatus):
        """Update order status"""
        if order_id in self.orders:
            self.orders[order_id].update_status(status)
        else:
            raise ValueError("Order not found")

def main():
    # Create restaurant management system
    system = RestaurantManagementSystem()

    # Create menu items
    item1 = MenuItem(1, "Burger", 10.99)
    item2 = MenuItem(2, "Fries", 4.99)
    system.add_menu_item(item1)
    system.add_menu_item(item2)

    # Create tables
    table1 = Table(1, 4)
    table2 = Table(2, 6)
    system.add_table(table1)
    system.add_table(table2)

    # Reserve table
    reservation_time = datetime.now() + timedelta(hours=1)
    system.reserve_table(1, reservation_time)

    # Place order
    order = system.place_order(1, "John Doe")
    system.add_item_to_order(1, 1)
    system.add_item_to_order(1, 2)

    # Update order status
    system.update_order_status(1, OrderStatus.PREPARING)

    # Print order details
    print(f"Order ID: {order.id}")
    print(f"Customer Name: {order.customer_name}")
    print(f"Order Status: {order.order_status.name}")
    print("Items:")
    for item in order.items:
        print(f"- {item.name}: ${item.price:.2f}")
    print(f"Total Cost: ${order.total_cost:.2f}")

if __name__ == "__main__":
    main()
```
