"""
Generated Code Metadata:
========================
Original URL: https://aavego.dk
Prompt: Generate a code snippet for a booking system that integrates with a holiday architecture site like House Aavego in Thy, Denmark, focusing on unique features like private courtyards.
Generated: DETERMINISTIC_ac251b14c55d8de7
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class BookingSystem:
    """
    A booking system for holiday architecture sites like House Aavego in Thy, Denmark.
    Focuses on unique features like private courtyards.
    """

    def __init__(self):
        # Initialize the booking system with an empty list of bookings
        self.bookings = []

    def check_availability(self, start_date, end_date):
        """
        Check if the property is available for the given date range.

        :param start_date: Start date of the booking (datetime object)
        :param end_date: End date of the booking (datetime object)
        :return: True if available, False otherwise
        """
        for booking in self.bookings:
            if (start_date <= booking['end_date'] and end_date >= booking['start_date']):
                return False  # Overlap detected
        return True

    def make_booking(self, customer_name, start_date, end_date):
        """
        Make a booking for the property.

        :param customer_name: Name of the customer
        :param start_date: Start date of the booking (datetime object)
        :param end_date: End date of the booking (datetime object)
        :return: Confirmation message or error message
        """
        if not isinstance(start_date, datetime.date) or not isinstance(end_date, datetime.date):
            return "Error: Start date and end date must be valid datetime.date objects."

        if start_date >= end_date:
            return "Error: Start date must be before end date."

        if self.check_availability(start_date, end_date):
            booking = {
                'customer_name': customer_name,
                'start_date': start_date,
                'end_date': end_date,
                'features': ['Private Courtyard']  # Unique feature of the property
            }
            self.bookings.append(booking)
            return f"Booking confirmed for {customer_name} from {start_date} to {end_date}."
        else:
            return "Error: The property is not available for the selected dates."

    def list_bookings(self):
        """
        List all bookings in the system.

        :return: JSON string of all bookings
        """
        return json.dumps(self.bookings, default=str, indent=4)

    def cancel_booking(self, customer_name, start_date, end_date):
        """
        Cancel a booking for the property.

        :param customer_name: Name of the customer
        :param start_date: Start date of the booking (datetime object)
        :param end_date: End date of the booking (datetime object)
        :return: Confirmation message or error message
        """
        for booking in self.bookings:
            if (booking['customer_name'] == customer_name and
                booking['start_date'] == start_date and
                booking['end_date'] == end_date):
                self.bookings.remove(booking)
                return f"Booking for {customer_name} from {start_date} to {end_date} has been canceled."
        return "Error: No matching booking found to cancel."


# Example usage
if __name__ == "__main__":
    system = BookingSystem()

    # Create bookings
    print(system.make_booking("Alice", datetime.date(2023, 12, 20), datetime.date(2023, 12, 25)))
    print(system.make_booking("Bob", datetime.date(2023, 12, 26), datetime.date(2023, 12, 30)))

    # Attempt overlapping booking
    print(system.make_booking("Charlie", datetime.date(2023, 12, 24), datetime.date(2023, 12, 27)))

    # List all bookings
    print("Current bookings:")
    print(system.list_bookings())

    # Cancel a booking
    print(system.cancel_booking("Alice", datetime.date(2023, 12, 20), datetime.date(2023, 12, 25)))

    # List bookings after cancellation
    print("Bookings after cancellation:")
    print(system.list_bookings())
```
