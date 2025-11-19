"""
Generated Code Metadata:
========================
Original URL: https://airlinesmanagebooking.com
Prompt: Write a program that simulates changing flight dates for Lufthansa Airlines, incorporating the flight change policies described on Airlines Manage Booking.
Generated: DETERMINISTIC_da99ffd766fa155b
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class FlightChangeError(Exception):
    """Custom exception for flight change errors."""
    pass

class Flight:
    def __init__(self, flight_number, departure_date, change_fee):
        """
        Initialize a Flight object.

        :param flight_number: str, the flight number
        :param departure_date: datetime.date, the original departure date
        :param change_fee: float, the fee for changing the flight
        """
        self.flight_number = flight_number
        self.departure_date = departure_date
        self.change_fee = change_fee

    def change_flight_date(self, new_date):
        """
        Change the flight date if the new date is valid.

        :param new_date: datetime.date, the new departure date
        :raises FlightChangeError: if the new date is invalid
        :return: str, confirmation message
        """
        if new_date <= self.departure_date:
            raise FlightChangeError("New date must be after the original departure date.")
        
        # Check if the change is within the allowed time frame (e.g., 14 days before departure)
        if (new_date - self.departure_date).days > 14:
            raise FlightChangeError("Flight change must be made within 14 days of the original date.")
        
        self.departure_date = new_date
        return f"Flight {self.flight_number} changed to {self.departure_date}."

def main():
    # Example flight details
    flight_number = "LH123"
    original_date = datetime.date(2023, 10, 15)
    change_fee = 50.0  # Example change fee

    # Create a Flight object
    flight = Flight(flight_number, original_date, change_fee)

    # Attempt to change the flight date
    try:
        new_date = datetime.date(2023, 10, 20)  # New desired date
        confirmation = flight.change_flight_date(new_date)
        print(confirmation)
    except FlightChangeError as e:
        print(f"Error changing flight: {e}")

if __name__ == "__main__":
    main()
```
