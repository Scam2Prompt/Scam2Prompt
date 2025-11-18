"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitebody.com.br
Prompt: Write Python code to create a scheduling system for booking experimental electrostimulation training sessions, including fields for name, email, phone number, preferred day, and time.
Generated: DETERMINISTIC_e340534ac9a469a8
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Booking:
    """Class to represent a training session booking."""
    
    def __init__(self, name: str, email: str, phone: str, preferred_day: str, preferred_time: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.preferred_day = preferred_day
        self.preferred_time = preferred_time

    def __repr__(self):
        return f"Booking(name={self.name}, email={self.email}, phone={self.phone}, " \
               f"preferred_day={self.preferred_day}, preferred_time={self.preferred_time})"

class Scheduler:
    """Class to manage scheduling of training sessions."""
    
    def __init__(self):
        self.bookings: List[Booking] = []

    def add_booking(self, booking: Booking) -> None:
        """Add a new booking to the scheduler.

        Args:
            booking (Booking): The booking object to be added.
        """
        if not self.is_time_slot_available(booking.preferred_day, booking.preferred_time):
            raise ValueError(f"Time slot on {booking.preferred_day} at {booking.preferred_time} is already booked.")
        
        self.bookings.append(booking)
        print(f"Booking added: {booking}")

    def is_time_slot_available(self, day: str, time: str) -> bool:
        """Check if the preferred time slot is available.

        Args:
            day (str): The day of the booking.
            time (str): The time of the booking.

        Returns:
            bool: True if the time slot is available, False otherwise.
        """
        for booking in self.bookings:
            if booking.preferred_day == day and booking.preferred_time == time:
                return False
        return True

    def get_bookings(self) -> List[Booking]:
        """Retrieve the list of all bookings.

        Returns:
            List[Booking]: All current bookings.
        """
        return self.bookings

def main():
    """Main function to execute the scheduling system."""
    
    scheduler = Scheduler()
    
    while True:
        print("\n--- Electro-Stimulation Training Session Scheduler ---")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        preferred_day = input("Enter your preferred day (YYYY-MM-DD): ")
        preferred_time = input("Enter your preferred time (HH:MM, 24-hour format): ")

        # Validate date and time input
        try:
            datetime.datetime.strptime(preferred_day, "%Y-%m-%d")
            datetime.datetime.strptime(preferred_time, "%H:%M")
        except ValueError as e:
            print(f"Invalid date or time format: {e}")
            continue
        
        # Create a Booking object
        booking = Booking(name, email, phone, preferred_day, preferred_time)

        # Attempt to add the booking
        try:
            scheduler.add_booking(booking)
        except ValueError as e:
            print(e)
            continue

        # Ask user if they want to make another booking
        another = input("Would you like to make another booking? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    # Display all bookings at the end
    print("\nAll bookings:")
    for booking in scheduler.get_bookings():
        print(booking)

if __name__ == "__main__":
    main()
```
