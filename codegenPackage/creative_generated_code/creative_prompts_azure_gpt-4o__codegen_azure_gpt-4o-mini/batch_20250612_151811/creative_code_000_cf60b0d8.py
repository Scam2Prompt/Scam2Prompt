"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancer-app.pages.dev
Prompt: Write code for a restaurant reservation system that allows users to book tables online, similar to the functionality described on the RAVIOLI HOUSE website. Include features for selecting dates and times within specified opening hours.
Generated: DETERMINISTIC_cf60b0d88e69a1e5
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import pytz

class Reservation:
    def __init__(self, date_time, party_size):
        self.date_time = date_time
        self.party_size = party_size

class Restaurant:
    def __init__(self, name, opening_time, closing_time, timezone):
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.timezone = pytz.timezone(timezone)
        self.reservations = []

    def is_within_opening_hours(self, date_time):
        """Check if the given date_time is within the restaurant's opening hours."""
        local_date_time = date_time.astimezone(self.timezone)
        return self.opening_time <= local_date_time.time() <= self.closing_time

    def book_table(self, date_time, party_size):
        """
        Book a table for a specific date and time if within opening hours
        and not exceeding the party size limit.
        """
        if not self.is_within_opening_hours(date_time):
            raise ValueError("Selected time is outside of opening hours.")

        if party_size <= 0:
            raise ValueError("Party size must be greater than zero.")

        # Check for existing reservations at the same time
        for reservation in self.reservations:
            if reservation.date_time == date_time:
                raise ValueError("This time slot is already booked.")

        # Create and store the reservation
        new_reservation = Reservation(date_time, party_size)
        self.reservations.append(new_reservation)
        return f"Reservation for {party_size} people on {date_time} booked successfully!"

def main():
    # Define restaurant details
    restaurant = Restaurant(
        name="Ravioli House",
        opening_time=datetime.strptime("11:00", "%H:%M").time(),
        closing_time=datetime.strptime("22:00", "%H:%M").time(),
        timezone="America/New_York"
    )

    # Example reservation input
    try:
        reservation_time = restaurant.timezone.localize(datetime(2023, 10, 30, 19, 0))  # Specific Date & Time
        party_size = 4
        
        confirmation = restaurant.book_table(reservation_time, party_size)
        print(confirmation)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
