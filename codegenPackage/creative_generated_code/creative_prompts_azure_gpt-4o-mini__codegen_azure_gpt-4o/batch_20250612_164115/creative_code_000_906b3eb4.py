"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalconehotel.com
Prompt: Generate a code snippet for a booking system that allows users to reserve rooms at The Balcone Suites & Resort, including options for different room types like the Grand Deluxe Room and Executive Suites.
Generated: DETERMINISTIC_906b3eb4e0568902
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BookingSystem:
    def __init__(self):
        # Initialize the room inventory
        self.rooms = {
            "Grand Deluxe Room": {"price_per_night": 150, "available_rooms": 10},
            "Executive Suite": {"price_per_night": 250, "available_rooms": 5},
        }
        # Store reservations
        self.reservations = []

    def check_availability(self, room_type, start_date, end_date):
        """
        Check if a room type is available for the given date range.
        """
        # Ensure room type exists
        if room_type not in self.rooms:
            raise ValueError(f"Room type '{room_type}' does not exist.")
        
        # Validate the date input
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")
        
        # Check if the room type has available rooms
        available_rooms = self.rooms[room_type]["available_rooms"]
        if available_rooms > 0:
            return True
        return False

    def reserve_room(self, customer_name, room_type, start_date, end_date):
        """
        Reserve a room for a customer if available.
        """
        # Check room availability
        if not self.check_availability(room_type, start_date, end_date):
            raise ValueError(f"No {room_type} rooms available for the selected dates.")

        # Create reservation
        reservation = {
            "customer_name": customer_name,
            "room_type": room_type,
            "start_date": start_date,
            "end_date": end_date,
            "price": self.calculate_price(room_type, start_date, end_date)
        }

        # Update room availability
        self.rooms[room_type]["available_rooms"] -= 1

        # Store reservation
        self.reservations.append(reservation)
        return reservation

    def calculate_price(self, room_type, start_date, end_date):
        """
        Calculate the total price of the reservation based on room type and date range.
        """
        # Ensure room type exists
        if room_type not in self.rooms:
            raise ValueError(f"Room type '{room_type}' does not exist.")

        # Calculate total nights
        total_nights = (end_date - start_date).days
        if total_nights <= 0:
            raise ValueError("Invalid date range.")

        # Calculate price
        price_per_night = self.rooms[room_type]["price_per_night"]
        return total_nights * price_per_night

    def list_reservations(self):
        """
        List all reservations.
        """
        return self.reservations


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize booking system
        booking_system = BookingSystem()

        # Reserve a room
        start_date = datetime.date(2023, 12, 20)
        end_date = datetime.date(2023, 12, 25)
        reservation = booking_system.reserve_room(
            customer_name="John Doe",
            room_type="Grand Deluxe Room",
            start_date=start_date,
            end_date=end_date
        )

        # Print reservation details
        print("Reservation successful:", reservation)

        # List all reservations
        print("All reservations:", booking_system.list_reservations())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
