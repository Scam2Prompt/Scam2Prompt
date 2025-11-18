"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Write code for a hotel booking system that allows users to select check-in and check-out dates, number of guests, and room types (e.g., double, triple, quadruple) with pricing options similar to Hostal Koltin Suchitoto.
Generated: DETERMINISTIC_b1a14ead7dd9e1bf
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class HotelBookingSystem:
    def __init__(self):
        # Initialize rooms and their pricing
        self.rooms = {
            "Double": {"price_per_night": 50, "capacity": 2},
            "Triple": {"price_per_night": 75, "capacity": 3},
            "Quadruple": {"price_per_night": 100, "capacity": 4}
        }
        self.bookings = []  # Store active bookings

    def is_date_valid(self, check_in, check_out):
        """
        Validates that check-in and check-out dates are correct.
        - check_in must be before check_out.
        - Dates must not be in the past.
        """
        today = datetime.date.today()
        if check_in >= check_out:
            return False, "Check-in date must be before the check-out date."
        if check_in < today or check_out < today:
            return False, "Dates must not be in the past."
        return True, "Dates are valid."

    def calculate_price(self, check_in, check_out, room_type):
        """
        Calculate total price based on room type and number of nights.
        """
        if room_type not in self.rooms:
            raise ValueError(f"Invalid room type '{room_type}'. Available types: {list(self.rooms.keys())}")
        
        nights = (check_out - check_in).days
        price_per_night = self.rooms[room_type]["price_per_night"]
        return nights * price_per_night

    def book_room(self, check_in, check_out, number_of_guests, room_type):
        """
        Book a room based on user input and return booking details.
        """
        # Validate room type
        if room_type not in self.rooms:
            raise ValueError(f"Invalid room type '{room_type}'. Available types: {list(self.rooms.keys())}")
        
        # Validate guest capacity
        if number_of_guests > self.rooms[room_type]["capacity"]:
            raise ValueError(f"The selected room type '{room_type}' can accommodate a maximum of {self.rooms[room_type]['capacity']} guests.")
        
        # Validate dates
        valid_dates, message = self.is_date_valid(check_in, check_out)
        if not valid_dates:
            raise ValueError(message)
        
        # Calculate total price
        total_price = self.calculate_price(check_in, check_out, room_type)

        # Save booking
        booking = {
            "check_in": check_in,
            "check_out": check_out,
            "number_of_guests": number_of_guests,
            "room_type": room_type,
            "total_price": total_price
        }
        self.bookings.append(booking)
        return booking
    
    def view_bookings(self):
        """
        Returns all active bookings.
        """
        return self.bookings

# Example usage
if __name__ == "__main__":
    # Create a booking system instance
    hotel = HotelBookingSystem()

    try:
        # Input dates and details
        check_in_date = datetime.date(2023, 12, 20)
        check_out_date = datetime.date(2023, 12, 25)
        guests = 3
        room_type_selected = "Triple"

        # Attempt to book a room
        booking_info = hotel.book_room(check_in_date, check_out_date, guests, room_type_selected)
        print("Booking successful!")
        print("Booking details:", booking_info)

        # View all bookings
        print("\nAll Current Bookings:")
        for booking in hotel.view_bookings():
            print(booking)
    
    except ValueError as e:
        print("Error:", e)
```
