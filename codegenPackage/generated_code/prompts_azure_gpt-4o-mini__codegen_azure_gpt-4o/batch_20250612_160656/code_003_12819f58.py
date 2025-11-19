"""
Generated Code Metadata:
========================
Original URL: https://forestx.se
Prompt: Develop a function that automates order and freight management using the features discussed in the Setra case study from ForestX.
Generated: DETERMINISTIC_12819f58a7cd6028
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Order:
    """
    Represents an order with details about the product, quantity, and destination.
    """
    def __init__(self, order_id, product, quantity, destination):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.destination = destination
        self.created_at = datetime.datetime.now()

class Freight:
    """
    Represents freight details for transporting orders.
    """
    def __init__(self, freight_id, capacity, current_load=0):
        self.freight_id = freight_id
        self.capacity = capacity
        self.current_load = current_load

    def can_accommodate(self, load):
        """
        Checks if the freight can accommodate the given load.
        """
        return self.current_load + load <= self.capacity

    def add_load(self, load):
        """
        Adds load to the freight if capacity allows.
        """
        if self.can_accommodate(load):
            self.current_load += load
            return True
        return False

class OrderManager:
    """
    Manages orders and freight assignments.
    """
    def __init__(self):
        self.orders = []
        self.freights = []

    def add_order(self, order):
        """
        Adds a new order to the system.
        """
        if not isinstance(order, Order):
            raise ValueError("Invalid order object.")
        self.orders.append(order)

    def add_freight(self, freight):
        """
        Adds a new freight to the system.
        """
        if not isinstance(freight, Freight):
            raise ValueError("Invalid freight object.")
        self.freights.append(freight)

    def assign_orders_to_freight(self):
        """
        Assigns orders to available freights based on capacity.
        """
        for order in self.orders:
            assigned = False
            for freight in self.freights:
                if freight.add_load(order.quantity):
                    print(f"Order {order.order_id} assigned to Freight {freight.freight_id}.")
                    assigned = True
                    break
            if not assigned:
                print(f"Order {order.order_id} could not be assigned due to insufficient capacity.")

    def list_orders(self):
        """
        Lists all orders in the system.
        """
        for order in self.orders:
            print(f"Order ID: {order.order_id}, Product: {order.product}, Quantity: {order.quantity}, Destination: {order.destination}")

    def list_freights(self):
        """
        Lists all freights in the system.
        """
        for freight in self.freights:
            print(f"Freight ID: {freight.freight_id}, Capacity: {freight.capacity}, Current Load: {freight.current_load}")

# Example usage
if __name__ == "__main__":
    # Initialize the order manager
    manager = OrderManager()

    # Create some orders
    order1 = Order(order_id=1, product="Wood Planks", quantity=50, destination="Stockholm")
    order2 = Order(order_id=2, product="Plywood Sheets", quantity=30, destination="Gothenburg")
    order3 = Order(order_id=3, product="Timber Logs", quantity=70, destination="Malmo")

    # Add orders to the manager
    manager.add_order(order1)
    manager.add_order(order2)
    manager.add_order(order3)

    # Create some freights
    freight1 = Freight(freight_id=101, capacity=100)
    freight2 = Freight(freight_id=102, capacity=50)

    # Add freights to the manager
    manager.add_freight(freight1)
    manager.add_freight(freight2)

    # List all orders and freights
    print("Orders:")
    manager.list_orders()
    print("\nFreights:")
    manager.list_freights()

    # Assign orders to freights
    print("\nAssigning orders to freights...")
    manager.assign_orders_to_freight()

    # List freights after assignment
    print("\nFreights after assignment:")
    manager.list_freights()
```
