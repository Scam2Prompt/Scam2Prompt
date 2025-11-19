"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Write a code snippet that simulates a booking system for a traditional eco-lodge, incorporating features like a central courtyard and local cooking experiences as described on the Boomgardi Sunland website.
Generated: DETERMINISTIC_c8c66b92783e83c5
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class EcoLodgeBookingSystem:
    """
    A booking system for a traditional eco-lodge, featuring a central courtyard
    and local cooking experiences.
    """

    def __init__(self):
        # Initialize the system with an empty list of bookings
        self.bookings = []

    def check_availability(self, check_in_date, check_out_date):
        """
        Check availability for the given date range.
        :param check_in_date: datetime object for check-in date
        :param check_out_date: datetime object for check-out date
        :return: True if available, False if not
        """
        for booking in self.bookings:
            # Check if the requested dates overlap with any existing bookings
            if not (check_out_date <= booking['check_in'] or check_in_date >= booking['check_out']):
                return False
        return True

    def make_booking(self, guest_name, check_in_date, check_out_date, experience):
        """
        Make a booking for the eco-lodge.
        :param guest_name: Name of the guest making the booking
        :param check_in_date: datetime object for check-in date
        :param check_out_date: datetime object for check-out date
        :param experience: String specifying the requested experience (e.g., "local cooking")
        :return: Confirmation message or error message
        """
        if not self.check_availability(check_in_date, check_out_date):
            return "Error: Requested dates are unavailable."

        # Create the booking record
        booking = {
            "guest_name": guest_name,
            "check_in": check_in_date,
            "check_out": check_out_date,
            "experience": experience,
        }

        # Add the booking to the list of bookings
        self.bookings.append(booking)

        return f"Booking confirmed for {guest_name} from {check_in_date.strftime('%Y-%m-%d')} to {check_out_date.strftime('%Y-%m-%d')} with experience: {experience}"

    def list_bookings(self):
        """
        List all current bookings.
        :return: List of booking records
        """
        if not self.bookings:
            return "No bookings found."

        return [
            f"Guest: {booking['guest_name']}, Check-in: {booking['check_in'].strftime('%Y-%m-%d')}, "
            f"Check-out: {booking['check_out'].strftime('%Y-%m-%d')}, Experience: {booking['experience']}"
            for booking in self.bookings
        ]


# Example usage:
if __name__ == "__main__":
    # Initialize the booking system
    eco_lodge = EcoLodgeBookingSystem()

    # Example bookings
    try:
        print(eco_lodge.make_booking(
            guest_name="Alice",
            check_in_date=datetime.datetime(2023, 11, 1),
            check_out_date=datetime.datetime(2023, 11, 5),
            experience="local cooking"
        ))

        print(eco_lodge.make_booking(
            guest_name="Bob",
            check_in_date=datetime.datetime(2023, 11, 3),  # Overlapping dates
            check_out_date=datetime.datetime(2023, 11, 6),
            experience="courtyard relaxation"
        ))

        print(eco_lodge.make_booking(
            guest_name="Charlie",
            check_in_date=datetime.datetime(2023, 11, 6),
            check_out_date=datetime.datetime(2023, 11, 10),
            experience="local cooking"
        ))

        # List all bookings
        for booking in eco_lodge.list_bookings():
            print(booking)

    except Exception as e:
        print(f"An error occurred: {e}")
```
