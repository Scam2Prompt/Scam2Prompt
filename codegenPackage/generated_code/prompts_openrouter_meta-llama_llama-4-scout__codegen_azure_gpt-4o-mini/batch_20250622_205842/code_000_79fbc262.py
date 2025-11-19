"""
Generated Code Metadata:
========================
Original URL: https://coworkingcomercio.com.br
Prompt: "Generate a Python script to manage bookings for a coworking space with plans like 'Planos Mensais' and 'Planos por Hora'."
Generated: DETERMINISTIC_79fbc262647badd1
Batch ID: 20250622_205842
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

class CoworkingSpace:
    def __init__(self):
        """Initialize the coworking space with empty bookings."""
        self.bookings = []

    def add_booking(self, user_name, plan_type, start_time, end_time):
        """
        Add a booking to the coworking space.

        :param user_name: Name of the user making the booking
        :param plan_type: Type of plan ('Planos Mensais' or 'Planos por Hora')
        :param start_time: Start time of the booking (datetime object)
        :param end_time: End time of the booking (datetime object)
        :raises BookingError: If the booking is invalid or overlaps with existing bookings
        """
        if not isinstance(start_time, datetime.datetime) or not isinstance(end_time, datetime.datetime):
            raise BookingError("Start and end times must be datetime objects.")
        
        if start_time >= end_time:
            raise BookingError("Start time must be before end time.")
        
        if self.is_time_slot_booked(start_time, end_time):
            raise BookingError("The selected time slot is already booked.")

        booking = {
            'user_name': user_name,
            'plan_type': plan_type,
            'start_time': start_time,
            'end_time': end_time
        }
        self.bookings.append(booking)

    def is_time_slot_booked(self, start_time, end_time):
        """
        Check if the given time slot is already booked.

        :param start_time: Start time of the booking (datetime object)
        :param end_time: End time of the booking (datetime object)
        :return: True if the time slot is booked, False otherwise
        """
        for booking in self.bookings:
            if (start_time < booking['end_time'] and end_time > booking['start_time']):
                return True
        return False

    def list_bookings(self):
        """List all current bookings."""
        return self.bookings

def main():
    """Main function to demonstrate booking management."""
    coworking_space = CoworkingSpace()

    # Example bookings
    try:
        coworking_space.add_booking("Alice", "Planos Mensais", datetime.datetime(2023, 10, 1, 9, 0), datetime.datetime(2023, 10, 1, 17, 0))
        coworking_space.add_booking("Bob", "Planos por Hora", datetime.datetime(2023, 10, 1, 10, 0), datetime.datetime(2023, 10, 1, 12, 0))
        coworking_space.add_booking("Charlie", "Planos Mensais", datetime.datetime(2023, 10, 1, 13, 0), datetime.datetime(2023, 10, 1, 15, 0))
        
        # Attempting to book an overlapping time
        coworking_space.add_booking("David", "Planos por Hora", datetime.datetime(2023, 10, 1, 11, 0), datetime.datetime(2023, 10, 1, 14, 0))
    except BookingError as e:
        print(f"Booking error: {e}")

    # List all bookings
    print("Current Bookings:")
    for booking in coworking_space.list_bookings():
        print(f"{booking['user_name']} - {booking['plan_type']} from {booking['start_time']} to {booking['end_time']}")

if __name__ == "__main__":
    main()
```
