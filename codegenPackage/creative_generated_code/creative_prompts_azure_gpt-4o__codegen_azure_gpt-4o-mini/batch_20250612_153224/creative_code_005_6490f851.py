"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Develop a Python program to manage bookings for a music studio, such as the one managed by Sophia Loisirs & Vie, including features for scheduling and availability checks.
Generated: DETERMINISTIC_6490f85178326306
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BookingError(Exception):
    """Custom exception for booking-related errors."""
    pass

class StudioBooking:
    """A class to manage bookings for a music studio."""
    
    def __init__(self):
        """
        Initialize the StudioBooking class with an empty bookings list.
        """
        self.bookings = []

    def schedule_booking(self, start_time, end_time, client_name):
        """
        Schedule a booking for the studio.

        Args:
            start_time (datetime): The start time of the booking.
            end_time (datetime): The end time of the booking.
            client_name (str): The name of the client booking the studio.

        Raises:
            BookingError: If the booking times are invalid or overlap with existing bookings.
        """
        
        if not isinstance(start_time, datetime.datetime) or not isinstance(end_time, datetime.datetime):
            raise BookingError("Start time and end time must be datetime objects.")
        
        if start_time >= end_time:
            raise BookingError("Start time must be before end time.")
        
        if self.check_availability(start_time, end_time):
            self.bookings.append({
                'client_name': client_name,
                'start_time': start_time,
                'end_time': end_time
            })
        else:
            raise BookingError("The studio is already booked for this time.")

    def check_availability(self, start_time, end_time):
        """
        Check if the studio is available for the given time slot.

        Args:
            start_time (datetime): The start time of the desired booking.
            end_time (datetime): The end time of the desired booking.

        Returns:
            bool: True if available, False otherwise.
        """
        
        for booking in self.bookings:
            if (start_time < booking['end_time'] and end_time > booking['start_time']):
                return False
        return True

    def list_bookings(self):
        """
        List all current bookings in the studio.

        Returns:
            list: A list of all bookings with details.
        """
        return self.bookings

# Example Usage
if __name__ == "__main__":
    studio = StudioBooking()
    
    try:
        # Schedule a booking
        studio.schedule_booking(datetime.datetime(2023, 10, 10, 10, 0), 
                                datetime.datetime(2023, 10, 10, 12, 0), 
                                "Client A")
        
        # Check availability for another booking
        studio.schedule_booking(datetime.datetime(2023, 10, 10, 12, 30), 
                                datetime.datetime(2023, 10, 10, 13, 30), 
                                "Client B")

        # Attempting to overlap with existing booking
        studio.schedule_booking(datetime.datetime(2023, 10, 10, 11, 0), 
                                datetime.datetime(2023, 10, 10, 12, 30), 
                                "Client C")  # This will raise BookingError

    except BookingError as e:
        print(f"Booking Error: {e}")

    # List all bookings
    print("Current Bookings:")
    for booking in studio.list_bookings():
        print(f"{booking['client_name']} - {booking['start_time']} to {booking['end_time']}")
```
