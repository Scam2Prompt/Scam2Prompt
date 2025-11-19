"""
Generated Code Metadata:
========================
Original URL: https://villapanorea.com
Prompt: Write a Python script to manage room bookings for a vacation rental property like Villa Panorea, including handling check-in/check-out dates and guest information.
Generated: DETERMINISTIC_4be71948597e14e5
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class BookingManager:
    """
    A class to manage room bookings for a vacation rental property.
    """

    def __init__(self):
        # Initialize an empty list to store bookings
        self.bookings = []

    def add_booking(self, guest_name, check_in_date, check_out_date):
        """
        Add a new booking to the system.

        :param guest_name: Name of the guest
        :param check_in_date: Check-in date (YYYY-MM-DD)
        :param check_out_date: Check-out date (YYYY-MM-DD)
        :return: None
        """
        try:
            # Convert string dates to datetime objects
            check_in = datetime.datetime.strptime(check_in_date, "%Y-%m-%d")
            check_out = datetime.datetime.strptime(check_out_date, "%Y-%m-%d")

            # Validate that check-out is after check-in
            if check_out <= check_in:
                raise ValueError("Check-out date must be after check-in date.")

            # Check for overlapping bookings
            for booking in self.bookings:
                if (check_in < booking['check_out'] and check_out > booking['check_in']):
                    raise ValueError("Booking dates overlap with an existing booking.")

            # Add the booking to the list
            self.bookings.append({
                'guest_name': guest_name,
                'check_in': check_in,
                'check_out': check_out
            })
            print(f"Booking successfully added for {guest_name} from {check_in_date} to {check_out_date}.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_bookings(self):
        """
        View all bookings in the system.

        :return: None
        """
        if not self.bookings:
            print("No bookings found.")
            return

        print("Current Bookings:")
        for booking in self.bookings:
            print(f"Guest: {booking['guest_name']}, Check-in: {booking['check_in'].strftime('%Y-%m-%d')}, "
                  f"Check-out: {booking['check_out'].strftime('%Y-%m-%d')}")

    def remove_booking(self, guest_name):
        """
        Remove a booking by guest name.

        :param guest_name: Name of the guest whose booking should be removed
        :return: None
        """
        try:
            # Find the booking to remove
            for booking in self.bookings:
                if booking['guest_name'] == guest_name:
                    self.bookings.remove(booking)
                    print(f"Booking for {guest_name} has been successfully removed.")
                    return

            # If no booking is found
            print(f"No booking found for guest: {guest_name}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    manager = BookingManager()

    # Add bookings
    manager.add_booking("Alice", "2023-11-01", "2023-11-05")
    manager.add_booking("Bob", "2023-11-06", "2023-11-10")

    # View bookings
    manager.view_bookings()

    # Attempt to add overlapping booking
    manager.add_booking("Charlie", "2023-11-04", "2023-11-07")

    # Remove a booking
    manager.remove_booking("Alice")

    # View bookings after removal
    manager.view_bookings()
```
