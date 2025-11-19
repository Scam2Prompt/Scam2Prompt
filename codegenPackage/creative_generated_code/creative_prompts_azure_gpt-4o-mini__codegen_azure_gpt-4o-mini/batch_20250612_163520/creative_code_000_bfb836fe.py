"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitepinesinn.com
Prompt: Generate a code snippet for a booking system that allows users to reserve cabins at White Pines Lodge for the 2025 season.
Generated: DETERMINISTIC_bfb836fe026d9b2c
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Cabin:
    """Represents a cabin at White Pines Lodge."""

    def __init__(self, cabin_id, capacity):
        self.cabin_id = cabin_id
        self.capacity = capacity
        self.reservations = []

    def is_available(self, start_date, end_date):
        """Check if the cabin is available for the given date range."""
        for reservation in self.reservations:
            if (start_date < reservation['end_date'] and end_date > reservation['start_date']):
                return False
        return True

    def reserve(self, start_date, end_date, guest_name):
        """Reserve the cabin for the specified date range."""
        if self.is_available(start_date, end_date):
            self.reservations.append({
                'start_date': start_date,
                'end_date': end_date,
                'guest_name': guest_name
            })
            return True
        else:
            raise ValueError("Cabin is not available for the selected dates.")

class BookingSystem:
    """Manages cabin bookings for White Pines Lodge."""

    def __init__(self):
        self.cabins = {}
        self.load_cabins()

    def load_cabins(self):
        """Load cabins into the booking system."""
        # Creating cabins, assuming 5 cabins with varying capacities
        for i in range(1, 6):
            self.cabins[i] = Cabin(cabin_id=i, capacity=4)

    def book_cabin(self, cabin_id, start_date, end_date, guest_name):
        """Book a cabin for the guest."""
        if cabin_id not in self.cabins:
            raise ValueError("Invalid cabin ID.")
        
        cabin = self.cabins[cabin_id]

        # Validate date inputs
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")
        if start_date < datetime.date.today():
            raise ValueError("Cannot book past or current dates.")

        try:
            cabin.reserve(start_date, end_date, guest_name)
            return f"Cabin {cabin_id} successfully reserved for {guest_name} from {start_date} to {end_date}."
        except ValueError as e:
            return str(e)

# Example Usage:
if __name__ == "__main__":
    booking_system = BookingSystem()

    # Define booking details
    try:
        start_date = datetime.date(2025, 6, 1)
        end_date = datetime.date(2025, 6, 10)
        guest_name = "John Doe"
        result = booking_system.book_cabin(cabin_id=1, start_date=start_date, end_date=end_date, guest_name=guest_name)
        print(result)
    except Exception as e:
        print(f"Booking failed: {e}")
```
