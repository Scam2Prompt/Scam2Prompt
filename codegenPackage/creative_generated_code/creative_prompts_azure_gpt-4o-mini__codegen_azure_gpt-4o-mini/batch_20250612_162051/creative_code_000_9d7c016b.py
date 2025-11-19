"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.albertozofrea.it
Prompt: Generate a code snippet for a booking system that allows clients to schedule Shiatsu sessions based on the availability mentioned on the Alberto Zofrea website.
Generated: DETERMINISTIC_9d7c016b912373b9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ShiatsuSession:
    """Class representing a Shiatsu session."""
    
    def __init__(self, date_time):
        self.date_time = date_time
        self.is_booked = False

    def book_session(self):
        """Book the Shiatsu session."""
        if self.is_booked:
            raise ValueError("Session is already booked.")
        self.is_booked = True

    def __str__(self):
        return f"Shiatsu Session on {self.date_time.strftime('%Y-%m-%d %H:%M')} - {'Booked' if self.is_booked else 'Available'}"


class BookingSystem:
    """Class to manage Shiatsu session bookings."""
    
    def __init__(self):
        self.sessions = []

    def add_session(self, date_time):
        """Add a new Shiatsu session to the booking system."""
        if self.is_time_slot_available(date_time):
            self.sessions.append(ShiatsuSession(date_time))
        else:
            raise ValueError("A session is already scheduled at this time.")

    def is_time_slot_available(self, date_time):
        """Check if a specific time slot is available."""
        return not any(session.date_time == date_time for session in self.sessions)

    def book_session(self, date_time):
        """Book a Shiatsu session at the specified time."""
        for session in self.sessions:
            if session.date_time == date_time:
                session.book_session()
                return
        raise ValueError("No available session found at this time.")

    def list_sessions(self):
        """List all Shiatsu sessions."""
        return [str(session) for session in self.sessions]


def main():
    """Main function to demonstrate the booking system."""
    booking_system = BookingSystem()

    try:
        # Adding sessions to the booking system
        booking_system.add_session(datetime.datetime(2023, 10, 12, 10, 0))
        booking_system.add_session(datetime.datetime(2023, 10, 12, 11, 0))
        
        # Attempting to book a session
        booking_system.book_session(datetime.datetime(2023, 10, 12, 10, 0))
        
        # Listing all sessions
        for session_info in booking_system.list_sessions():
            print(session_info)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
