"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Write Python code to simulate the rental booking process for Rigid Inflatable Boats (RIBs) in Greece, incorporating options for fleet selection like "Rock 36 MIAMI" and "Rock 36 AELIA."
Generated: DETERMINISTIC_c6c9df7512a15235
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Boat:
    """Class representing a Rigid Inflatable Boat (RIB)."""
    
    def __init__(self, name, capacity, price_per_day):
        """
        Initialize a new Boat instance.

        :param name: Name of the boat
        :param capacity: Maximum number of people the boat can accommodate
        :param price_per_day: Rental price per day
        """
        self.name = name
        self.capacity = capacity
        self.price_per_day = price_per_day

    def __str__(self):
        """Return a string representation of the boat."""
        return f"{self.name} (Capacity: {self.capacity}, Price: {self.price_per_day}/day)"


class RentalBooking:
    """Class to handle the rental booking process for RIBs."""
    
    def __init__(self):
        """Initialize the rental booking system with a fleet of boats."""
        self.fleet = [
            Boat("Rock 36 MIAMI", 8, 300),
            Boat("Rock 36 AELIA", 10, 350)
        ]
        self.bookings = []

    def display_fleet(self):
        """Display the available boats in the fleet."""
        print("Available Boats:")
        for boat in self.fleet:
            print(boat)

    def book_boat(self, boat_name, start_date, end_date):
        """
        Book a boat for a specified date range.

        :param boat_name: Name of the boat to book
        :param start_date: Start date of the rental period
        :param end_date: End date of the rental period
        :raises ValueError: If the booking dates are invalid or the boat is not found
        """
        # Validate dates
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")
        
        # Check if the boat exists
        boat = next((b for b in self.fleet if b.name == boat_name), None)
        if not boat:
            raise ValueError(f"Boat '{boat_name}' not found in the fleet.")

        # Check for existing bookings
        for booking in self.bookings:
            if booking['boat'] == boat and not (end_date <= booking['start_date'] or start_date >= booking['end_date']):
                raise ValueError(f"Boat '{boat_name}' is already booked for the selected dates.")

        # Create a new booking
        self.bookings.append({
            'boat': boat,
            'start_date': start_date,
            'end_date': end_date
        })
        print(f"Successfully booked {boat_name} from {start_date} to {end_date}.")

    def calculate_total_cost(self, boat_name, start_date, end_date):
        """
        Calculate the total rental cost for a specified boat and date range.

        :param boat_name: Name of the boat
        :param start_date: Start date of the rental period
        :param end_date: End date of the rental period
        :return: Total cost of the rental
        :raises ValueError: If the boat is not found
        """
        boat = next((b for b in self.fleet if b.name == boat_name), None)
        if not boat:
            raise ValueError(f"Boat '{boat_name}' not found in the fleet.")

        rental_days = (end_date - start_date).days
        total_cost = rental_days * boat.price_per_day
        return total_cost


def main():
    """Main function to run the rental booking system."""
    rental_system = RentalBooking()
    
    # Display available boats
    rental_system.display_fleet()

    # Example booking process
    try:
        boat_name = "Rock 36 MIAMI"
        start_date = datetime.date(2023, 7, 1)
        end_date = datetime.date(2023, 7, 5)

        # Calculate total cost
        total_cost = rental_system.calculate_total_cost(boat_name, start_date, end_date)
        print(f"Total cost for renting {boat_name} from {start_date} to {end_date}: {total_cost}")

        # Book the boat
        rental_system.book_boat(boat_name, start_date, end_date)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
