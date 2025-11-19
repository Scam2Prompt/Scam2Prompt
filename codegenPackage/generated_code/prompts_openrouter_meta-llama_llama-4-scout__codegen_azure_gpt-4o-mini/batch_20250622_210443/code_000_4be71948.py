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

class BookingError(Exception):
    """Custom exception for booking errors."""
    pass

class RoomBooking:
    """Class to manage room bookings for a vacation rental property."""
    
    def __init__(self):
        """Initialize the booking system with an empty list of bookings."""
        self.bookings = []

    def add_booking(self, guest_name, check_in_date, check_out_date):
        """
        Add a new booking to the system.

        Parameters:
        guest_name (str): Name of the guest.
        check_in_date (datetime.date): Check-in date.
        check_out_date (datetime.date): Check-out date.

        Raises:
        BookingError: If the booking dates are invalid or overlap with existing bookings.
        """
        if not isinstance(guest_name, str) or not guest_name:
            raise BookingError("Guest name must be a non-empty string.")
        
        if not isinstance(check_in_date, datetime.date) or not isinstance(check_out_date, datetime.date):
            raise BookingError("Check-in and check-out dates must be valid date objects.")
        
        if check_in_date >= check_out_date:
            raise BookingError("Check-in date must be before check-out date.")
        
        # Check for overlapping bookings
        for booking in self.bookings:
            if (check_in_date < booking['check_out'] and check_out_date > booking['check_in']):
                raise BookingError("Booking dates overlap with an existing booking.")

        # Add the new booking
        self.bookings.append({
            'guest_name': guest_name,
            'check_in': check_in_date,
            'check_out': check_out_date
        })

    def list_bookings(self):
        """List all current bookings."""
        if not self.bookings:
            print("No current bookings.")
            return
        
        for booking in self.bookings:
            print(f"Guest: {booking['guest_name']}, Check-in: {booking['check_in']}, Check-out: {booking['check_out']}")

    def remove_booking(self, guest_name):
        """
        Remove a booking by guest name.

        Parameters:
        guest_name (str): Name of the guest whose booking is to be removed.

        Raises:
        BookingError: If no booking is found for the given guest name.
        """
        for booking in self.bookings:
            if booking['guest_name'] == guest_name:
                self.bookings.remove(booking)
                print(f"Booking for {guest_name} has been removed.")
                return
        
        raise BookingError(f"No booking found for guest: {guest_name}")

def main():
    """Main function to demonstrate the RoomBooking class functionality."""
    booking_system = RoomBooking()

    try:
        # Example bookings
        booking_system.add_booking("Alice Smith", datetime.date(2023, 10, 1), datetime.date(2023, 10, 5))
        booking_system.add_booking("Bob Johnson", datetime.date(2023, 10, 6), datetime.date(2023, 10, 10))
        
        # List current bookings
        booking_system.list_bookings()

        # Attempt to add an overlapping booking
        booking_system.add_booking("Charlie Brown", datetime.date(2023, 10, 4), datetime.date(2023, 10, 7))
    except BookingError as e:
        print(f"Error: {e}")

    try:
        # Remove a booking
        booking_system.remove_booking("Alice Smith")
        booking_system.list_bookings()
    except BookingError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
