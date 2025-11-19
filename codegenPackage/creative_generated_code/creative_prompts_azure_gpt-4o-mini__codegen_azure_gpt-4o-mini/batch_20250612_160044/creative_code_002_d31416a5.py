"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Create a Python script that manages tennis court bookings, ensuring optimal usage of facilities like those at TC Harsewinkel.
Generated: DETERMINISTIC_d31416a5297de891
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Court:
    """Class representing a Tennis Court."""
    
    def __init__(self, court_number):
        """Initializes a court with a specific number."""
        self.court_number = court_number
        self.bookings = []

    def is_available(self, start_time, end_time):
        """Check if the court is available for the given time slot."""
        for booking in self.bookings:
            if (start_time < booking['end_time'] and end_time > booking['start_time']):
                return False
        return True

    def book(self, start_time, end_time, user):
        """Book the court for the specified time slot."""
        if not self.is_available(start_time, end_time):
            raise Exception("Court is not available for the requested time.")
        
        booking = {
            'user': user,
            'start_time': start_time,
            'end_time': end_time
        }
        self.bookings.append(booking)
        return booking

    def get_bookings(self):
        """Return a list of all bookings for the court."""
        return self.bookings


class CourtManager:
    """Class to manage multiple tennis courts."""
    
    def __init__(self):
        """Initializes the CourtManager with no courts."""
        self.courts = {}

    def add_court(self, court_number):
        """Add a new court to the manager."""
        if court_number in self.courts:
            raise Exception("Court already exists.")
        self.courts[court_number] = Court(court_number)

    def book_court(self, court_number, start_time, end_time, user):
        """Book a specific court for the user."""
        if court_number not in self.courts:
            raise Exception("Court not found.")
        
        court = self.courts[court_number]
        return court.book(start_time, end_time, user)

    def get_court_bookings(self, court_number):
        """Get all bookings for a specific court."""
        if court_number not in self.courts:
            raise Exception("Court not found.")
        
        return self.courts[court_number].get_bookings()

    
def main():
    """Main function to demonstrate court booking."""
    court_manager = CourtManager()
    
    # Adding courts to the manager
    court_manager.add_court(1)
    court_manager.add_court(2)

    # Define some time slots for booking
    user = "John Doe"
    start_time = datetime.datetime(2023, 10, 1, 10, 0)  # 1st Oct 2023, 10:00 AM
    end_time = datetime.datetime(2023, 10, 1, 11, 0)    # 1st Oct 2023, 11:00 AM

    # Attempt to book a court
    try:
        booking = court_manager.book_court(1, start_time, end_time, user)
        print(f"Booking successful: {booking}")
    except Exception as e:
        print(f"Booking failed: {e}")

    # Retrieve court bookings
    try:
        bookings = court_manager.get_court_bookings(1)
        print(f"Current bookings for Court 1: {bookings}")
    except Exception as e:
        print(f"Error retrieving bookings: {e}")

if __name__ == "__main__":
    main()
```
