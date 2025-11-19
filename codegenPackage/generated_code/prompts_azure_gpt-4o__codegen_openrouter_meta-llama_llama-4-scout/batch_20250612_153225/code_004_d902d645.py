"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Write code to model the logistics and warehouse management system for delivering orders to customers' doorsteps, inspired by the infrastructure described on the Aayra International website.
Generated: DETERMINISTIC_d902d645c15416fb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

class OrderStatus(Enum):
    """Enum for order status"""
    PENDING = 1
    IN_TRANSIT = 2
    DELIVERED = 3
    CANCELED = 4

class Customer:
    """Class to represent a customer"""
    def __init__(self, customer_id: int, name: str, address: str, phone_number: str):
        """
        Initialize a customer object

        Args:
        - customer_id (int): Unique customer ID
        - name (str): Customer name
        - address (str): Customer address
        - phone_number (str): Customer phone number
        """
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone_number = phone_number

class Order:
    """Class to represent an order"""
    def __init__(self, order_id: int, customer: Customer, order_date: str):
        """
        Initialize an order object

        Args:
        - order_id (int): Unique order ID
        - customer (Customer): Customer object
        - order_date (str): Order date
        """
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.status = OrderStatus.PENDING
        self.packages: List[Package] = []

    def add_package(self, package: 'Package'):
        """Add a package to the order"""
        self.packages.append(package)

    def update_status(self, status: OrderStatus):
        """Update the order status"""
        self.status = status

class Package:
    """Class to represent a package"""
    def __init__(self, package_id: int, weight: float, dimensions: str):
        """
        Initialize a package object

        Args:
        - package_id (int): Unique package ID
        - weight (float): Package weight
        - dimensions (str): Package dimensions
        """
        self.package_id = package_id
        self.weight = weight
        self.dimensions = dimensions

class Warehouse:
    """Class to represent a warehouse"""
    def __init__(self, warehouse_id: int, address: str):
        """
        Initialize a warehouse object

        Args:
        - warehouse_id (int): Unique warehouse ID
        - address (str): Warehouse address
        """
        self.warehouse_id = warehouse_id
        self.address = address
        self.orders: Dict[int, Order] = {}

    def receive_order(self, order: Order):
        """Receive an order in the warehouse"""
        self.orders[order.order_id] = order

    def ship_order(self, order_id: int):
        """Ship an order from the warehouse"""
        if order_id in self.orders:
            order = self.orders[order_id]
            order.update_status(OrderStatus.IN_TRANSIT)
            print(f"Order {order_id} shipped successfully")
        else:
            print(f"Order {order_id} not found in warehouse")

    def deliver_order(self, order_id: int):
        """Deliver an order to the customer"""
        if order_id in self.orders:
            order = self.orders[order_id]
            order.update_status(OrderStatus.DELIVERED)
            print(f"Order {order_id} delivered successfully")
        else:
            print(f"Order {order_id} not found in warehouse")

class LogisticsSystem:
    """Class to represent the logistics system"""
    def __init__(self):
        self.warehouses: Dict[int, Warehouse] = {}
        self.customers: Dict[int, Customer] = {}

    def add_warehouse(self, warehouse: Warehouse):
        """Add a warehouse to the logistics system"""
        self.warehouses[warehouse.warehouse_id] = warehouse

    def add_customer(self, customer: Customer):
        """Add a customer to the logistics system"""
        self.customers[customer.customer_id] = customer

    def create_order(self, order_id: int, customer_id: int, warehouse_id: int):
        """Create a new order"""
        if customer_id in self.customers and warehouse_id in self.warehouses:
            customer = self.customers[customer_id]
            warehouse = self.warehouses[warehouse_id]
            order = Order(order_id, customer, "2024-09-16")
            warehouse.receive_order(order)
            return order
        else:
            print("Customer or warehouse not found")
            return None

def main():
    logistics_system = LogisticsSystem()

    # Create customers
    customer1 = Customer(1, "John Doe", "123 Main St", "1234567890")
    logistics_system.add_customer(customer1)

    # Create warehouses
    warehouse1 = Warehouse(1, "456 Warehouse St")
    logistics_system.add_warehouse(warehouse1)

    # Create order
    order1 = logistics_system.create_order(1, 1, 1)

    # Add packages to order
    package1 = Package(1, 10.0, "10x10x10")
    order1.add_package(package1)

    # Ship and deliver order
    warehouse1.ship_order(1)
    warehouse1.deliver_order(1)

if __name__ == "__main__":
    main()
```
