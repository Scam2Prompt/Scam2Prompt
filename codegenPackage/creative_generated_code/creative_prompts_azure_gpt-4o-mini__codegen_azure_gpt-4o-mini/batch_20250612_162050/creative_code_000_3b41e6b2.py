"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baturjeeptour.my.id
Prompt: Generate a code snippet for a booking system that allows users to select a Jeep tour in Bali, including options for sunrise and sunset tours at Mount Batur.
Generated: DETERMINISTIC_3b41e6b2204cf7db
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Optional

class Tour:
    """Class representing a Jeep tour."""
    
    def __init__(self, name: str, duration: int, price: float):
        """Initialize a tour with name, duration, and price."""
        self.name = name
        self.duration = duration  # in hours
        self.price = price  # in USD

class Booking:
    """Class to handle bookings for tours."""
    
    def __init__(self):
        """Initialize an empty booking system."""
        self.tours: List[Tour] = []
        self.bookings: List[str] = []  # Store booking details as strings
    
    def add_tour(self, tour: Tour):
        """Add a tour to the booking system."""
        if isinstance(tour, Tour):
            self.tours.append(tour)
        else:
            raise ValueError("Invalid tour object")
    
    def list_tours(self) -> List[str]:
        """List available tours."""
        return [f"{tour.name} - Duration: {tour.duration} hours - Price: ${tour.price}" for tour in self.tours]
    
    def book_tour(self, tour_name: str, user_name: str) -> str:
        """Book a tour for a user."""
        for tour in self.tours:
            if tour.name == tour_name:
                booking_detail = f"Booking: {user_name} has booked the {tour.name} tour."
                self.bookings.append(booking_detail)
                return booking_detail
        raise ValueError("Tour not found")

def main():
    """Main function to set up the booking system."""
    # Create an instance of Booking
    booking_system = Booking()
    
    # Define available tours
    sunrise_tour = Tour("Sunrise Jeep Tour at Mount Batur", duration=4, price=100)
    sunset_tour = Tour("Sunset Jeep Tour at Mount Batur", duration=4, price=100)
    
    # Add tours to the booking system
    booking_system.add_tour(sunrise_tour)
    booking_system.add_tour(sunset_tour)
    
    # List available tours
    print("Available Tours:")
    for tour in booking_system.list_tours():
        print(tour)
    
    # Sample booking process
    try:
        user_name = "Alice"
        print(booking_system.book_tour("Sunrise Jeep Tour at Mount Batur", user_name))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
