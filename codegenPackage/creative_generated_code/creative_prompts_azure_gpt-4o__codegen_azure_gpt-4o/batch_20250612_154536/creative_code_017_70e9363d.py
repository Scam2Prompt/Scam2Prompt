"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airlinesmanagebooking.com
Prompt: Generate code to simulate booking a first-class seat for Lufthansa Airlines, incorporating seat selection and upgrade policies from Airlines Manage Booking.
Generated: DETERMINISTIC_70e9363db5938c4e
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class AirlineBookingSystem:
    def __init__(self):
        # Initialize the seating configuration
        self.first_class_seats = {f"1A": "Available", f"1B": "Available", f"1C": "Available", f"1D": "Available"}
    
    def display_seat_availability(self):
        """ Display the availability of first-class seats. """
        print("First-Class Seat Availability:")
        for seat, status in self.first_class_seats.items():
            print(f"Seat {seat}: {status}")
    
    def book_seat(self, seat):
        """ Book a seat if available, or provide an option to upgrade. """
        if seat in self.first_class_seats:
            if self.first_class_seats[ seat]==Available".
