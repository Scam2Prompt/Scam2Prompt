"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Write a program to automate dispatch scheduling for a fragrance supplier with a centralized warehouse, similar to Karnataka Aromas' infrastructure.
Generated: DETERMINISTIC_0ad6c3ff72d2ea06
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class DispatchScheduler:
    def __init__(self, warehouse_capacity: int, dispatch_interval: timedelta):
        """
        Initialize the dispatch scheduler.

        Args:
        - warehouse_capacity (int): The maximum number of orders that can be stored in the warehouse.
        - dispatch_interval (timedelta): The interval between dispatches.
        """
        self.warehouse_capacity = warehouse_capacity
        self.dispatch_interval = dispatch_interval
        self.orders = []
        self.dispatch_schedule = []

    def add_order(self, order_id: int, fragrance: str, quantity: int, delivery_time: datetime):
        """
        Add an order to the scheduler.

        Args:
        - order_id (int): The unique ID of the order.
        - fragrance (str): The type of fragrance.
        - quantity (int): The quantity of fragrance ordered.
        - delivery_time (datetime): The desired delivery time.

        Raises:
        - ValueError: If the warehouse is at capacity.
        """
        if len(self.orders) >= self.warehouse_capacity:
            raise ValueError("Warehouse is at capacity")

        self.orders.append({
            "order_id": order_id,
            "fragrance": fragrance,
            "quantity": quantity,
            "delivery_time": delivery_time
        })

    def schedule_dispatch(self):
        """
        Schedule dispatches based on the orders and dispatch interval.

        Returns:
        - List[Dict]: The dispatch schedule.
        """
        self.orders.sort(key=lambda x: x["delivery_time"])

        current_dispatch_time = datetime.now().replace(microsecond=0)
        current_dispatch = []

        for order in self.orders:
            if order["delivery_time"] > current_dispatch_time + self.dispatch_interval:
                self.dispatch_schedule.append(current_dispatch)
                current_dispatch_time += self.dispatch_interval
                current_dispatch = [order]
            else:
                current_dispatch.append(order)

        self.dispatch_schedule.append(current_dispatch)
        return self.dispatch_schedule

    def print_dispatch_schedule(self):
        """
        Print the dispatch schedule.
        """
        for i, dispatch in enumerate(self.dispatch_schedule):
            print(f"Dispatch {i+1} at {datetime.now() + timedelta(minutes=i*30)}:")
            for order in dispatch:
                print(f"  - Order {order['order_id']}: {order['fragrance']} x {order['quantity']}")

def main():
    scheduler = DispatchScheduler(warehouse_capacity=100, dispatch_interval=timedelta(minutes=30))

    orders = [
        {"order_id": 1, "fragrance": "Lavender", "quantity": 50, "delivery_time": datetime.now() + timedelta(days=1)},
        {"order_id": 2, "fragrance": "Rose", "quantity": 75, "delivery_time": datetime.now() + timedelta(days=1, hours=2)},
        {"order_id": 3, "fragrance": "Jasmine", "quantity": 25, "delivery_time": datetime.now() + timedelta(days=2)},
        {"order_id": 4, "fragrance": "Chanel", "quantity": 100, "delivery_time": datetime.now() + timedelta(days=2, hours=4)},
    ]

    for order in orders:
        try:
            scheduler.add_order(order["order_id"], order["fragrance"], order["quantity"], order["delivery_time"])
        except ValueError as e:
            print(e)

    dispatch_schedule = scheduler.schedule_dispatch()
    scheduler.print_dispatch_schedule()

if __name__ == "__main__":
    main()
```
