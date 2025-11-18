"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.executivo2000.com
Prompt: Write a Python script to simulate a booking system for airport lounge access, including features like free Wi-Fi, flight info display, and charging stations as described on the Executivo 2000 website.
Generated: DETERMINISTIC_997129c8f6c90586
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Lounge:
    """Represents an airport lounge with amenities."""
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.current_visitors = 0
        self.bookings = {}

    def book_access(self, user_name, booking_time):
        """Book a lounge access for a user.

        Args:
            user_name (str): The name of the user booking access.
            booking_time (datetime): The time the booking is made.

        Raises:
            ValueError: If the lounge is at full capacity.
        """
        if self.current_visitors >= self.capacity:
            raise ValueError("The lounge is at full capacity. Please try again later.")
        self.current_visitors += 1
        self.bookings[user_name] = booking_time
        print(f"Booking confirmed for {user_name} at {booking_time}.")

    def check_in(self, user_name):
        """Check in a user to the lounge.

        Args:
            user_name (str): The name of the user checking in.

        Raises:
            KeyError: If the user does not have a booking.
        """
        if user_name not in self.bookings:
            raise KeyError(f"No booking found for {user_name}.")
        print(f"{user_name} has checked into the lounge.")

    def check_out(self, user_name):
        """Check out a user from the lounge.

        Args:
            user_name (str): The name of the user checking out.

        Raises:
            KeyError: If the user is not checked in.
        """
        if user_name not in self.bookings:
            raise KeyError(f"No booking found for {user_name}.")
        self.current_visitors -= 1
        del self.bookings[user_name]
        print(f"{user_name} has checked out of the lounge.")

    def display_amenities(self):
        """Display the available amenities in the lounge."""
        amenities = ["Free Wi-Fi", "Flight Info Display", "Charging Stations"]
        print(f"Amenities available in {self.name}: {', '.join(amenities)}")

def main():
    # Create a lounge instance
    lounge = Lounge("Executivo 2000", capacity=10)
    
    # Simulate some bookings
    try:
        booking_time = datetime.datetime.now()
        lounge.book_access("Alice Smith", booking_time)
        lounge.book_access("Bob Johnson", booking_time)
        
        lounge.display_amenities()
        
        lounge.check_in("Alice Smith")
        lounge.check_out("Alice Smith")
        
        # Attempt checking out again should raise an error
        lounge.check_out("Alice Smith")
        
    except ValueError as ve:
        print(f"Booking error: {ve}")
    except KeyError as ke:
        print(f"Check-in/Out error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
