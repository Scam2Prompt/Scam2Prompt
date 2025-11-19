"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saltydazeusvi.com
Prompt: Generate a code snippet for a booking system that allows users to reserve a boat charter from Salty Daze Charters in Coral Bay, St. John.
Generated: DETERMINISTIC_ddc97c1895b57238
Batch ID: 20250612_163117
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

class BoatCharter:
    def __init__(self, name: str, capacity: int, base_price: float):
        """
        Initialize a BoatCharter instance.

        Args:
            name (str): Name of the boat charter.
            capacity (int): Maximum number of guests allowed.
            base_price (float): Price per hour for renting the boat.
        """
        self.name = name
        self.capacity = capacity
        self.base_price = base_price
        self.bookings = []  # Store all bookings for this charter

    def book(self, start_time: datetime, end_time: datetime, guests: int) -> Optional[str]:
        """
        Book the boat charter for a specified time and number of guests.

        Args:
            start_time (datetime): Start time for the booking.
            end_time (datetime): End time for the booking.
            guests (int): Number of guests for the booking.

        Returns:
            Optional[str]: Confirmation of booking or error message.
        """
        if guests > self.capacity:
            return "Error: Number of guests exceeds boat capacity."

        for booking in self.bookings:
            if (start_time < booking['end_time'] and end_time > booking['start_time']):
                return "Error: The boat is already booked for the selected time."

        # Add the booking if no conflicts
        self.bookings.append({
            'start_time': start_time,
            'end_time': end_time,
            'guests': guests
        })
        return "Booking confirmed!"

    def calculate_total_price(self, start_time: datetime, end_time: datetime) -> float:
        """
        Calculate the total price for a booking.

        Args:
            start_time (datetime): Start time for the booking.
            end_time (datetime): End time for the booking.

        Returns:
            float: Total price for the booking.
        """
        duration = (end_time - start_time).total_seconds() / 3600  # Convert seconds to hours
        return max(duration, 0) * self.base_price  # Ensure duration is not negative


# Example usage of the BoatCharter class
if __name__ == "__main__":
    # Create an instance of BoatCharter
    salty_daze_charter = BoatCharter(name="Salty Daze", capacity=6, base_price=150.00)

    # Define booking times
    start_time = datetime(2023, 10, 15, 10, 0)  # October 15, 2023, 10:00 AM
    end_time = datetime(2023, 10, 15, 14, 0)    # October 15, 2023, 2:00 PM
    guests = 4

    # Attempt to book the charter
    booking_confirmation = salty_daze_charter.book(start_time, end_time, guests)
    print(booking_confirmation)

    # Calculate total price for the booking
    total_price = salty_daze_charter.calculate_total_price(start_time, end_time)
    print(f"Total price for the booking: ${total_price:.2f}")
```
