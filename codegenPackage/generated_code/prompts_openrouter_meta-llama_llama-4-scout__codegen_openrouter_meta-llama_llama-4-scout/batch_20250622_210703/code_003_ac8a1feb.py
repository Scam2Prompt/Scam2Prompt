"""
Generated Code Metadata:
========================
Original URL: https://breakthroughstudio.in
Prompt: Create a code snippet to manage online bookings and demo sessions for a fitness studio, specifically designed for suspension training services like Breakthrough Studio.
Generated: DETERMINISTIC_ac8a1febd914efb4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

# Define an Enum for booking status
class BookingStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    CANCELED = 3

# Define a class for Booking
class Booking:
    def __init__(self, id, customer_name, session_date, session_time, status=BookingStatus.PENDING):
        """
        Initialize a Booking object.

        Args:
            id (int): Unique booking ID.
            customer_name (str): Name of the customer.
            session_date (str): Date of the session in YYYY-MM-DD format.
            session_time (str): Time of the session in HH:MM format.
            status (BookingStatus, optional): Status of the booking. Defaults to BookingStatus.PENDING.
        """
        self.id = id
        self.customer_name = customer_name
        self.session_date = session_date
        self.session_time = session_time
        self.status = status

    def __str__(self):
        return f"Booking {self.id}: {self.customer_name} on {self.session_date} at {self.session_time} - {self.status.name}"

# Define a class for DemoSession
class DemoSession(Booking):
    def __init__(self, id, customer_name, session_date, session_time, status=BookingStatus.PENDING):
        """
        Initialize a DemoSession object.

        Args:
            id (int): Unique demo session ID.
            customer_name (str): Name of the customer.
            session_date (str): Date of the demo session in YYYY-MM-DD format.
            session_time (str): Time of the demo session in HH:MM format.
            status (BookingStatus, optional): Status of the demo session. Defaults to BookingStatus.PENDING.
        """
        super().__init__(id, customer_name, session_date, session_time, status)

# Define a class for OnlineBooking
class OnlineBooking(Booking):
    def __init__(self, id, customer_name, session_date, session_time, service_type, status=BookingStatus.PENDING):
        """
        Initialize an OnlineBooking object.

        Args:
            id (int): Unique online booking ID.
            customer_name (str): Name of the customer.
            session_date (str): Date of the online booking in YYYY-MM-DD format.
            session_time (str): Time of the online booking in HH:MM format.
            service_type (str): Type of suspension training service.
            status (BookingStatus, optional): Status of the online booking. Defaults to BookingStatus.PENDING.
        """
        super().__init__(id, customer_name, session_date, session_time, status)
        self.service_type = service_type

    def __str__(self):
        return f"Online Booking {self.id}: {self.customer_name} on {self.session_date} at {self.session_time} for {self.service_type} - {self.status.name}"

# Define a class for BookingManager
class BookingManager:
    def __init__(self):
        """
        Initialize a BookingManager object.
        """
        self.bookings = []
        self.demo_sessions = []
        self.online_bookings = []

    def add_booking(self, booking):
        """
        Add a booking to the booking list.

        Args:
            booking (Booking): Booking object to add.
        """
        self.bookings.append(booking)

    def add_demo_session(self, demo_session):
        """
        Add a demo session to the demo session list.

        Args:
            demo_session (DemoSession): DemoSession object to add.
        """
        self.demo_sessions.append(demo_session)

    def add_online_booking(self, online_booking):
        """
        Add an online booking to the online booking list.

        Args:
            online_booking (OnlineBooking): OnlineBooking object to add.
        """
        self.online_bookings.append(online_booking)

    def cancel_booking(self, booking_id):
        """
        Cancel a booking by ID.

        Args:
            booking_id (int): ID of the booking to cancel.

        Returns:
            bool: True if the booking was canceled, False otherwise.
        """
        for booking in self.bookings:
            if booking.id == booking_id:
                booking.status = BookingStatus.CANCELED
                return True
        return False

    def confirm_booking(self, booking_id):
        """
        Confirm a booking by ID.

        Args:
            booking_id (int): ID of the booking to confirm.

        Returns:
            bool: True if the booking was confirmed, False otherwise.
        """
        for booking in self.bookings:
            if booking.id == booking_id:
                booking.status = BookingStatus.CONFIRMED
                return True
        return False

    def get_upcoming_bookings(self):
        """
        Get a list of upcoming bookings.

        Returns:
            list: List of upcoming Booking objects.
        """
        upcoming_bookings = []
        for booking in self.bookings:
            session_date = datetime.strptime(booking.session_date, "%Y-%m-%d")
            if session_date >= datetime.today():
                upcoming_bookings.append(booking)
        return upcoming_bookings

def main():
    # Create a BookingManager
    manager = BookingManager()

    # Create bookings
    booking1 = OnlineBooking(1, "John Doe", "2024-09-20", "10:00", "Suspension Training")
    booking2 = DemoSession(2, "Jane Doe", "2024-09-21", "11:00")
    booking3 = OnlineBooking(3, "Bob Smith", "2024-09-22", "12:00", "Suspension Training")

    # Add bookings to manager
    manager.add_online_booking(booking1)
    manager.add_demo_session(booking2)
    manager.add_online_booking(booking3)

    # Print bookings
    print("Bookings:")
    for booking in manager.bookings:
        print(booking)

    # Print demo sessions
    print("\nDemo Sessions:")
    for demo_session in manager.demo_sessions:
        print(demo_session)

    # Print online bookings
    print("\nOnline Bookings:")
    for online_booking in manager.online_bookings:
        print(online_booking)

    # Confirm a booking
    manager.confirm_booking(1)
    print(f"\nBooking 1 status after confirmation: {manager.online_bookings[0].status.name}")

    # Cancel a booking
    manager.cancel_booking(2)
    print(f"\nDemo Session 2 status after cancellation: {manager.demo_sessions[0].status.name}")

    # Get upcoming bookings
    upcoming_bookings = manager.get_upcoming_bookings()
    print("\nUpcoming Bookings:")
    for booking in upcoming_bookings:
        print(booking)

if __name__ == "__main__":
    main()
```
