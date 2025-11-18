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
from datetime import datetime, timedelta


class RoomType:
    """Enum for different types of rooms available in the hotel."""
    DOUBLE = 'Double'
    TRIPLE = 'Triple'
    QUADRUPLE = 'Quadruple'


class Booking:
    """Class to represent a hotel booking."""
    
    def __init__(self, check_in: datetime, check_out: datetime, guests: int, room_type: str):
        self.check_in = check_in
        self.check_out = check_out
        self.guests = guests
        self.room_type = room_type
        self.price_per_night = self.get_price_per_night()
        self.total_price = self.calculate_total_price()

    def get_price_per_night(self) -> float:
        """Returns the price per night based on the room type."""
        prices = {
            RoomType.DOUBLE: 100.0,
            RoomType.TRIPLE: 150.0,
            RoomType.QUADRUPLE: 200.0
        }
        return prices.get(self.room_type, 0.0)

    def calculate_total_price(self) -> float:
        """Calculates the total price for the stay."""
        number_of_nights = (self.check_out - self.check_in).days
        return self.price_per_night * number_of_nights

    def __str__(self) -> str:
        """Returns a string representation of the booking."""
        return (f'Booking from {self.check_in.date()} to {self.check_out.date()} '
                f'for {self.guests} guests in a {self.room_type} room. '
                f'Total price: ${self.total_price:.2f}')


class BookingSystem:
    """Class to manage the hotel booking system."""
    
    def __init__(self):
        self.bookings = []

    def validate_dates(self, check_in: datetime, check_out: datetime) -> None:
        """Validates that the check-in and check-out dates are correct."""
        if check_in >= check_out:
            raise ValueError("Check-out date must be after check-in date.")
        if check_in < datetime.now():
            raise ValueError("Check-in date must be in the future.")

    def book_room(self, check_in: str, check_out: str, guests: int, room_type: str) -> None:
        """Books a room based on user input."""
        try:
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
            self.validate_dates(check_in_date, check_out_date)

            booking = Booking(check_in_date, check_out_date, guests, room_type)
            self.bookings.append(booking)
            print(f'Room booked successfully: {booking}')
        except ValueError as e:
            print(f'Error: {e}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')


# Sample usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Sample user input
    booking_system.book_room('2023-12-01', '2023-12-05', 2, RoomType.DOUBLE)
    booking_system.book_room('2023-12-05', '2023-12-03', 3, RoomType.TRIPLE)  # This will raise an error
```
