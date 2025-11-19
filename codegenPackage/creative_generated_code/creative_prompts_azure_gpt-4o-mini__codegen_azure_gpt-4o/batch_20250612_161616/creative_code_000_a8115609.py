"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purebite.fi
Prompt: Generate a code snippet for a restaurant management system that includes features for online table reservations and takeout orders, inspired by the services offered by Purebite.
Generated: DETERMINISTIC_a81156092e0796ed
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# restaurant_management_system.py

import datetime


class RestaurantManagementSystem:
    def __init__(self):
        # Initialize the system with an empty list of reservations and takeout orders
        self.reservations = []
        self.takeout_orders = []

    def reserve_table(self, name, phone, date_time, num_guests):
        """
        Allows a customer to reserve a table.

        :param name: Name of the customer
        :param phone: Phone number of the customer
        :param date_time: Date and time of the reservation (datetime object)
        :param num_guests: Number of guests for the reservation
        """
        # Validate the reservation details
        if num_guests <= 0:
            raise ValueError("Number of guests must be greater than zero.")
        if date_time <= datetime.datetime.now():
            raise ValueError("Reservation time must be in the future.")

        reservation = {
            "name": name,
            "phone": phone,
            "date_time": date_time,
            "num_guests": num_guests,
        }
        self.reservations.append(reservation)
        return f"Reservation confirmed for {name} on {date_time} for {num_guests} guests."

    def place_takeout_order(self, name, phone, order_items):
        """
        Allows a customer to place a takeout order.

        :param name: Name of the customer
        :param phone: Phone number of the customer
        :param order_items: List of items ordered (non-empty list)
        """
        # Validate the order items
        if not order_items:
            raise ValueError("Order must contain at least one item.")

        order = {
            "name": name,
            "phone": phone,
            "order_items": order_items,
            "order_time": datetime.datetime.now(),
        }
        self.takeout_orders.append(order)
        return f"Takeout order placed successfully for {name}. Order: {', '.join(order_items)}."

    def view_reservations(self):
        """
        Returns a list of all table reservations.

        :return: List of reservations
        """
        return self.reservations

    def view_takeout_orders(self):
        """
        Returns a list of all takeout orders.

        :return: List of takeout orders
        """
        return self.takeout_orders


# Example Usage
if __name__ == "__main__":
    # Create an instance of the system
    restaurant_system = RestaurantManagementSystem()

    try:
        # Reserve a table
        print(
            restaurant_system.reserve_table(
                name="John Doe",
                phone="555-1234",
                date_time=datetime.datetime(2023, 10, 15, 19, 0),
                num_guests=4,
            )
        )

        # Place a takeout order
        print(
            restaurant_system.place_takeout_order(
                name="Jane Smith", phone="555-5678", order_items=["Pizza", "Salad"]
            )
        )

        # View reservations
        print("Reservations:")
        for reservation in restaurant_system.view_reservations():
            print(reservation)

        # View takeout orders
        print("Takeout Orders:")
        for order in restaurant_system.view_takeout_orders():
            print(order)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
