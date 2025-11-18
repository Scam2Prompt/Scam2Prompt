"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Write Python code to simulate the rental booking process for Rigid Inflatable Boats (RIBs) in Greece, incorporating options for fleet selection like "Rock 36 MIAMI" and "Rock 36 AELIA."
Generated: DETERMINISTIC_c6c9df7512a15235
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Boat:
    """Class representing a Rigid Inflatable Boat (RIB)."""
    
    def __init__(self, name, price_per_day):
        """
        Initialize a new Boat instance.

        :param name: str - The name of the boat.
        :param price_per_day: float - The rental price per day.
        """
        self.name = name
        self.price_per_day = price_per_day

    def __str__(self):
        """Return a string representation of the boat."""
        return f"{self.name} - €{self.price_per_day}/day"


class RentalBooking:
    """Class to handle the rental booking process for RIBs."""
    
    def __init__(self):
        """Initialize the booking system with a fleet of boats."""
        self.fleet = [
            Boat("Rock 36 MIAMI", 250.0),
            Boat("Rock 36 AELIA", 300.0)
        ]
        self.bookings = []

    def display_fleet(self):
        """Display the available boats in the fleet."""
        print("Available RIBs for rental:")
        for boat in self.fleet:
            print(boat)

    def book_boat(self, boat_name, start_date, end_date):
        """
        Book a boat for a specific date range.

        :param boat_name: str - The name of the boat to rent.
        :param start_date: str - Start date in 'YYYY-MM-DD' format.
        :param end_date: str - End date in 'YYYY-MM-DD' format.
        :raises ValueError: If the booking dates are invalid.
        :raises Exception: If the boat is not found.
        """
        try:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

            if start_date >= end_date:
                raise ValueError("Start date must be before end date.")

            boat = next((b for b in self.fleet if b.name == boat_name), None)
            if not boat:
                raise Exception("Boat not found in the fleet.")

            booking = {
                'boat': boat,
                'start_date': start_date,
                'end_date': end_date,
                'total_price': boat.price_per_day * (end_date - start_date).days
            }
            self.bookings.append(booking)
            print(f"Successfully booked {boat.name} from {start_date} to {end_date}. Total price: €{booking['total_price']}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_bookings(self):
        """Display all current bookings."""
        if not self.bookings:
            print("No current bookings.")
            return

        print("Current Bookings:")
        for booking in self.bookings:
            print(f"{booking['boat'].name} booked from {booking['start_date']} to {booking['end_date']} - Total: €{booking['total_price']}")


# Example usage
if __name__ == "__main__":
    booking_system = RentalBooking()
    booking_system.display_fleet()
    
    # Example of booking a boat
    booking_system.book_boat("Rock 36 MIAMI", "2023-07-01", "2023-07-05")
    booking_system.book_boat("Rock 36 AELIA", "2023-07-03", "2023-07-07")

    # Display current bookings
    booking_system.display_bookings()
```
