"""
Generated Code Metadata:
========================
Original URL: https://balancer-app.pages.dev
Prompt: Develop a script to manage restaurant opening times and ensure customers can only make reservations during specified hours.
Generated: DETERMINISTIC_bc4665d0dc446a5b
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Restaurant:
    def __init__(self, name, opening_time, closing_time):
        """
        Initialize a Restaurant object.

        Args:
            name (str): The name of the restaurant.
            opening_time (str): The opening time of the restaurant in 24-hour format (HH:MM).
            closing_time (str): The closing time of the restaurant in 24-hour format (HH:MM).
        """
        self.name = name
        self.opening_time = datetime.strptime(opening_time, "%H:%M").time()
        self.closing_time = datetime.strptime(closing_time, "%H:%M").time()

    def is_open(self, time=None):
        """
        Check if the restaurant is open at a given time.

        Args:
            time (datetime.time, optional): The time to check. Defaults to current time.

        Returns:
            bool: True if the restaurant is open, False otherwise.
        """
        if time is None:
            time = datetime.now().time()
        return self.opening_time <= time < self.closing_time

    def can_make_reservation(self, reservation_time):
        """
        Check if a reservation can be made at a given time.

        Args:
            reservation_time (datetime): The time of the reservation.

        Returns:
            bool: True if a reservation can be made, False otherwise.
        """
        return self.is_open(reservation_time.time())


class ReservationSystem:
    def __init__(self, restaurant):
        """
        Initialize a ReservationSystem object.

        Args:
            restaurant (Restaurant): The restaurant for which the reservation system is being created.
        """
        self.restaurant = restaurant
        self.reservations = []

    def make_reservation(self, customer_name, reservation_time):
        """
        Make a reservation at the restaurant.

        Args:
            customer_name (str): The name of the customer making the reservation.
            reservation_time (datetime): The time of the reservation.

        Returns:
            bool: True if the reservation was successful, False otherwise.
        """
        if self.restaurant.can_make_reservation(reservation_time):
            self.reservations.append((customer_name, reservation_time))
            return True
        else:
            return False

    def cancel_reservation(self, customer_name, reservation_time):
        """
        Cancel a reservation at the restaurant.

        Args:
            customer_name (str): The name of the customer canceling the reservation.
            reservation_time (datetime): The time of the reservation.

        Returns:
            bool: True if the reservation was canceled, False otherwise.
        """
        self.reservations = [(name, time) for name, time in self.reservations if not (name == customer_name and time == reservation_time)]
        return True

    def print_reservations(self):
        """
        Print all reservations.
        """
        for customer_name, reservation_time in self.reservations:
            print(f"Customer: {customer_name}, Time: {reservation_time.strftime('%H:%M')}")


def main():
    try:
        restaurant = Restaurant("My Restaurant", "09:00", "21:00")
        reservation_system = ReservationSystem(restaurant)

        # Make reservations
        reservation_time1 = datetime.now() + timedelta(hours=2)
        reservation_time2 = datetime.now() + timedelta(hours=22)
        print(f"Reservation at {reservation_time1.strftime('%H:%M')} successful: {reservation_system.make_reservation('John Doe', reservation_time1)}")
        print(f"Reservation at {reservation_time2.strftime('%H:%M')} successful: {reservation_system.make_reservation('Jane Doe', reservation_time2)}")

        # Print reservations
        print("Reservations:")
        reservation_system.print_reservations()

        # Cancel reservation
        print(f"Reservation cancellation for John Doe at {reservation_time1.strftime('%H:%M')} successful: {reservation_system.cancel_reservation('John Doe', reservation_time1)}")

        # Print reservations after cancellation
        print("Reservations after cancellation:")
        reservation_system.print_reservations()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
