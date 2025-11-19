"""
Generated Code Metadata:
========================
Original URL: https://villaandreas.gr
Prompt: "Write a Python script to create a simple booking system for a villa rental service like Villa Andreas in Kefalonia, considering check-in and check-out times, and minimum stay requirements."
Generated: DETERMINISTIC_0d7d1af9ba7fda4e
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Villa:
    def __init__(self, name, capacity, min_stay):
        """
        Initialize a Villa object.

        Args:
            name (str): Name of the villa.
            capacity (int): Maximum capacity of the villa.
            min_stay (int): Minimum stay requirement in days.
        """
        self.name = name
        self.capacity = capacity
        self.min_stay = min_stay
        self.bookings = []

    def book_villa(self, guest_name, check_in, check_out):
        """
        Book the villa for a guest.

        Args:
            guest_name (str): Name of the guest.
            check_in (datetime): Check-in date and time.
            check_out (datetime): Check-out date and time.

        Returns:
            bool: True if booking is successful, False otherwise.
        """
        if self.is_available(check_in, check_out):
            self.bookings.append({
                'guest_name': guest_name,
                'check_in': check_in,
                'check_out': check_out
            })
            return True
        return False

    def is_available(self, check_in, check_out):
        """
        Check if the villa is available for booking.

        Args:
            check_in (datetime): Check-in date and time.
            check_out (datetime): Check-out date and time.

        Returns:
            bool: True if villa is available, False otherwise.
        """
        if (check_out - check_in).days < self.min_stay:
            print(f"Minimum stay requirement is {self.min_stay} days.")
            return False

        for booking in self.bookings:
            if (check_in < booking['check_out'] and check_out > booking['check_in']):
                print("Villa is not available during this period.")
                return False

        return True

    def cancel_booking(self, guest_name, check_in):
        """
        Cancel a booking.

        Args:
            guest_name (str): Name of the guest.
            check_in (datetime): Check-in date and time.

        Returns:
            bool: True if cancellation is successful, False otherwise.
        """
        for booking in self.bookings:
            if booking['guest_name'] == guest_name and booking['check_in'] == check_in:
                self.bookings.remove(booking)
                return True
        return False

    def print_bookings(self):
        """
        Print all bookings.
        """
        for booking in self.bookings:
            print(f"Guest: {booking['guest_name']}, Check-in: {booking['check_in']}, Check-out: {booking['check_out']}")


class VillaRentalService:
    def __init__(self):
        """
        Initialize a VillaRentalService object.
        """
        self.villas = {}

    def add_villa(self, villa):
        """
        Add a villa to the rental service.

        Args:
            villa (Villa): Villa object to add.
        """
        self.villas[villa.name] = villa

    def book_villa(self, villa_name, guest_name, check_in, check_out):
        """
        Book a villa.

        Args:
            villa_name (str): Name of the villa.
            guest_name (str): Name of the guest.
            check_in (datetime): Check-in date and time.
            check_out (datetime): Check-out date and time.

        Returns:
            bool: True if booking is successful, False otherwise.
        """
        if villa_name in self.villas:
            return self.villas[villa_name].book_villa(guest_name, check_in, check_out)
        return False

    def cancel_booking(self, villa_name, guest_name, check_in):
        """
        Cancel a booking.

        Args:
            villa_name (str): Name of the villa.
            guest_name (str): Name of the guest.
            check_in (datetime): Check-in date and time.

        Returns:
            bool: True if cancellation is successful, False otherwise.
        """
        if villa_name in self.villas:
            return self.villas[villa_name].cancel_booking(guest_name, check_in)
        return False


def main():
    # Create a villa rental service
    service = VillaRentalService()

    # Create villas
    villa_andreas = Villa("Villa Andreas", 8, 3)
    service.add_villa(villa_andreas)

    # Book a villa
    check_in = datetime.now() + timedelta(days=5)
    check_out = check_in + timedelta(days=7)
    if service.book_villa("Villa Andreas", "John Doe", check_in, check_out):
        print("Booking successful.")
    else:
        print("Booking failed.")

    # Print bookings
    villa_andreas.print_bookings()

    # Cancel a booking
    if service.cancel_booking("Villa Andreas", "John Doe", check_in):
        print("Cancellation successful.")
    else:
        print("Cancellation failed.")

    # Print bookings after cancellation
    villa_andreas.print_bookings()


if __name__ == "__main__":
    main()
```
