"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airlinesmanagebooking.com
Prompt: Write a program that simulates changing flight dates for Lufthansa Airlines, incorporating the flight change policies described on Airlines Manage Booking.
Generated: DETERMINISTIC_da99ffd766fa155b
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Flight:
    """Class to represent a Flight with attributes for flight details and change policies."""

    def __init__(self, flight_number, departure_date, destination):
        """
        Initialize a Flight object.

        :param flight_number: str - The flight number.
        :param departure_date: str - The departure date in 'YYYY-MM-DD' format.
        :param destination: str - The flight destination.
        """
        self.flight_number = flight_number
        self.departure_date = self._parse_date(departure_date)
        self.destination = destination

    @staticmethod
    def _parse_date(date_str):
        """Parses a date string into a datetime object."""
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Incorrect date format. Expected 'YYYY-MM-DD'.")

    def change_flight_date(self, new_date):
        """
        Change the flight's departure date, adhering to change policies.

        :param new_date: str - New departure date in 'YYYY-MM-DD' format.
        :raises ValueError: If the new date is not valid or too close to the current departure date.
        """
        new_date_parsed = self._parse_date(new_date)
        days_difference = (new_date_parsed - self.departure_date).days

        if days_difference < 2:
            raise ValueError("Changes must be made at least 2 days before departure.")
        
        self.departure_date = new_date_parsed
        print(f"Flight date changed to: {self.departure_date}")

    def __str__(self):
        """Return a string representation of the flight."""
        return f"Flight {self.flight_number} to {self.destination} on {self.departure_date}"


def main():
    """Main function to run the flight change simulation."""
    flight_number = "LH1234"
    departure_date = "2023-12-10"
    destination = "Berlin"

    # Create a flight instance
    flight = Flight(flight_number, departure_date, destination)
    print(flight)

    try:
        # Attempt to change the flight date
        new_date = "2023-12-12"  # Attempting to change to a date less than 2 days away
        flight.change_flight_date(new_date)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        # Attempt to change the flight date to a valid date
        new_date = "2023-12-15"  # Change to a date more than 2 days away
        flight.change_flight_date(new_date)
        print(flight)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
