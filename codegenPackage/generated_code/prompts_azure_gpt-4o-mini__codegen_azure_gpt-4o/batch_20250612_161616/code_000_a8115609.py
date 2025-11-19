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
from datetime import datetime
from typing import List, Dict, Optional


class Reservation:
    """
    Class to handle table reservations.
    """
    def __init__(self, customer_name: str, date: str, time: str, num_guests: int):
        self.customer_name = customer_name
        self.date = date  # Format: YYYY-MM-DD
        self.time = time  # Format: HH:MM
        self.num_guests = num_guests

    def __repr__(self):
        return f"Reservation({self.customer_name}, {self.date}, {self.time}, {self.num_guests} guests)"


class TakeoutOrder:
    """
    Class to handle takeout orders.
    """
    def __init__(self, customer_name: str, items: List[Dict[str, int]], pickup_time: str):
        """
        :param customer_name: Name of the customer
        :param items: List of items with their quantities, e.g., [{"item": "Pizza", "quantity": 2}]
        :param pickup_time: Time for pickup in HH:MM format
        """
        self.customer_name = customer_name
        self.items = items
        self.pickup_time = pickup_time

    def __repr__(self):
        return f"TakeoutOrder({self.customer_name}, {self.items}, Pickup: {self.pickup_time})"


class RestaurantManagementSystem:
    """
    Main class to manage restaurant operations including reservations and takeout orders.
    """
    def __init__(self):
        self.reservations: List[Reservation] = []
        self.takeout_orders: List[TakeoutOrder] = []

    def add_reservation(self, customer_name: str, date: str, time: str, num_guests: int) -> str:
        """
        Add a new table reservation.
        """
        try:
            # Validate date and time format
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(time, "%H:%M")
            if num_guests <= 0:
                raise ValueError("Number of guests must be greater than 0.")

            reservation = Reservation(customer_name, date, time, num_guests)
            self.reservations.append(reservation)
            return f"Reservation confirmed for {customer_name} on {date} at {time} for {num_guests} guests."
        except ValueError as e:
            return f"Error: {str(e)}"

    def add_takeout_order(self, customer_name: str, items: List[Dict[str, int]], pickup_time: str) -> str:
        """
        Add a new takeout order.
        """
        try:
            # Validate pickup time format
            datetime.strptime(pickup_time, "%H:%M")
            if not items or any(item.get("quantity", 0) <= 0 for item in items):
                raise ValueError("Each item must have a quantity greater than 0.")

            order = TakeoutOrder(customer_name, items, pickup_time)
            self.takeout_orders.append(order)
            return f"Takeout order confirmed for {customer_name}. Pickup at {pickup_time}."
        except ValueError as e:
            return f"Error: {str(e)}"

    def view_reservations(self) -> List[Reservation]:
        """
        View all reservations.
        """
        return self.reservations

    def view_takeout_orders(self) -> List[TakeoutOrder]:
        """
        View all takeout orders.
        """
        return self.takeout_orders


# Example usage
if __name__ == "__main__":
    system = RestaurantManagementSystem()

    # Add reservations
    print(system.add_reservation("Alice", "2023-10-15", "19:00", 4))
    print(system.add_reservation("Bob", "2023-10-16", "20:00", 2))

    # Add takeout orders
    print(system.add_takeout_order("Charlie", [{"item": "Burger", "quantity": 2}, {"item": "Fries", "quantity": 1}], "18:30"))
    print(system.add_takeout_order("Diana", [{"item": "Pizza", "quantity": 1}], "19:15"))

    # View reservations and takeout orders
    print("\nReservations:")
    for reservation in system.view_reservations():
        print(reservation)

    print("\nTakeout Orders:")
    for order in system.view_takeout_orders():
        print(order)
```
