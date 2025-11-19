"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Can you provide a code snippet for a booking system that allows users to schedule text-based counselling sessions, inspired by the features of Text Counselling Online?
Generated: DETERMINISTIC_cca11cc5bcc73277
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class Counsellor:
    """Represents a counsellor with their details and availability."""

    def __init__(self, id: int, name: str, email: str):
        """
        Initializes a Counsellor object.

        Args:
        id (int): Unique identifier for the counsellor.
        name (str): Name of the counsellor.
        email (str): Email address of the counsellor.
        """
        self.id = id
        self.name = name
        self.email = email
        self.availability = []  # List of available time slots

    def add_availability(self, date: str, start_time: str, end_time: str):
        """
        Adds a time slot to the counsellor's availability.

        Args:
        date (str): Date of the time slot (YYYY-MM-DD).
        start_time (str): Start time of the time slot (HH:MM).
        end_time (str): End time of the time slot (HH:MM).
        """
        self.availability.append({
            'date': date,
            'start_time': start_time,
            'end_time': end_time
        })

class User:
    """Represents a user with their details and bookings."""

    def __init__(self, id: int, name: str, email: str):
        """
        Initializes a User object.

        Args:
        id (int): Unique identifier for the user.
        name (str): Name of the user.
        email (str): Email address of the user.
        """
        self.id = id
        self.name = name
        self.email = email
        self.bookings = []  # List of booked sessions

    def book_session(self, counsellor: Counsellor, date: str, start_time: str):
        """
        Books a counselling session with a counsellor.

        Args:
        counsellor (Counsellor): Counsellor object.
        date (str): Date of the session (YYYY-MM-DD).
        start_time (str): Start time of the session (HH:MM).
        """
        for time_slot in counsellor.availability:
            if time_slot['date'] == date and time_slot['start_time'] == start_time:
                self.bookings.append({
                    'counsellor_id': counsellor.id,
                    'date': date,
                    'start_time': start_time
                })
                print(f"Session booked with {counsellor.name} on {date} at {start_time}.")
                return
        print("Sorry, this time slot is not available.")

class BookingSystem:
    """Manages counsellors, users, and bookings."""

    def __init__(self):
        self.counsellors: Dict[int, Counsellor] = {}  # Dictionary of counsellors
        self.users: Dict[int, User] = {}  # Dictionary of users

    def add_counsellor(self, counsellor: Counsellor):
        """
        Adds a counsellor to the system.

        Args:
        counsellor (Counsellor): Counsellor object.
        """
        self.counsellors[counsellor.id] = counsellor

    def add_user(self, user: User):
        """
        Adds a user to the system.

        Args:
        user (User): User object.
        """
        self.users[user.id] = user

    def display_counsellors(self):
        """Displays all counsellors and their availability."""
        for counsellor in self.counsellors.values():
            print(f"Counsellor: {counsellor.name}")
            for time_slot in counsellor.availability:
                print(f"  - {time_slot['date']} at {time_slot['start_time']} - {time_slot['end_time']}")

def main():
    booking_system = BookingSystem()

    # Create counsellors
    counsellor1 = Counsellor(1, "John Doe", "john@example.com")
    counsellor1.add_availability("2024-09-20", "10:00", "11:00")
    counsellor1.add_availability("2024-09-21", "14:00", "15:00")

    counsellor2 = Counsellor(2, "Jane Smith", "jane@example.com")
    counsellor2.add_availability("2024-09-20", "12:00", "13:00")

    # Add counsellors to the system
    booking_system.add_counsellor(counsellor1)
    booking_system.add_counsellor(counsellor2)

    # Create users
    user1 = User(1, "User1", "user1@example.com")
    user2 = User(2, "User2", "user2@example.com")

    # Add users to the system
    booking_system.add_user(user1)
    booking_system.add_user(user2)

    # Display counsellors and their availability
    print("Counsellors and Availability:")
    booking_system.display_counsellors()

    # Book sessions
    user1.book_session(counsellor1, "2024-09-20", "10:00")
    user2.book_session(counsellor2, "2024-09-20", "12:00")
    user1.book_session(counsellor1, "2024-09-20", "11:00")  # Should fail

if __name__ == "__main__":
    main()
```
