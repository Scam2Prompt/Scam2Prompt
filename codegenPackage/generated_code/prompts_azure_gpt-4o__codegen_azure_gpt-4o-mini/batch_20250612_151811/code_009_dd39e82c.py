"""
Generated Code Metadata:
========================
Original URL: https://superstep.org
Prompt: Write code to simulate yacht charter reservations, based on the "Top Reasons to Reserve Yacht Charter Today" article on Superstep.org.
Generated: DETERMINISTIC_dd39e82c092c8334
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Yacht:
    """Class representing a yacht available for charter."""
    
    def __init__(self, name, capacity, price_per_day):
        """
        Initialize a new yacht instance.

        :param name: Name of the yacht
        :param capacity: Maximum number of guests the yacht can accommodate
        :param price_per_day: Daily rental price of the yacht
        """
        self.name = name
        self.capacity = capacity
        self.price_per_day = price_per_day
        self.reservations = []

    def is_available(self, start_date, end_date):
        """
        Check if the yacht is available for the given date range.

        :param start_date: Start date of the reservation
        :param end_date: End date of the reservation
        :return: True if available, False otherwise
        """
        for reservation in self.reservations:
            if (start_date < reservation['end_date'] and end_date > reservation['start_date']):
                return False
        return True

    def reserve(self, start_date, end_date, customer_name):
        """
        Reserve the yacht for a given date range.

        :param start_date: Start date of the reservation
        :param end_date: End date of the reservation
        :param customer_name: Name of the customer making the reservation
        :raises ValueError: If the yacht is not available or dates are invalid
        """
        if not self.is_available(start_date, end_date):
            raise ValueError("Yacht is not available for the selected dates.")
        if start_date >= end_date:
            raise ValueError("End date must be after start date.")
        
        self.reservations.append({
            'customer_name': customer_name,
            'start_date': start_date,
            'end_date': end_date
        })

    def get_reservations(self):
        """Return a list of current reservations."""
        return self.reservations


class YachtCharterService:
    """Service to manage yacht charters."""

    def __init__(self):
        """Initialize the yacht charter service with available yachts."""
        self.yachts = []

    def add_yacht(self, yacht):
        """
        Add a yacht to the charter service.

        :param yacht: Yacht instance to be added
        """
        self.yachts.append(yacht)

    def find_available_yachts(self, start_date, end_date):
        """
        Find all available yachts for the given date range.

        :param start_date: Start date of the reservation
        :param end_date: End date of the reservation
        :return: List of available yachts
        """
        available_yachts = []
        for yacht in self.yachts:
            if yacht.is_available(start_date, end_date):
                available_yachts.append(yacht)
        return available_yachts

    def reserve_yacht(self, yacht_name, start_date, end_date, customer_name):
        """
        Reserve a yacht by name for a given date range.

        :param yacht_name: Name of the yacht to reserve
        :param start_date: Start date of the reservation
        :param end_date: End date of the reservation
        :param customer_name: Name of the customer making the reservation
        :raises ValueError: If the yacht is not found or reservation fails
        """
        yacht = next((y for y in self.yachts if y.name == yacht_name), None)
        if yacht is None:
            raise ValueError("Yacht not found.")
        yacht.reserve(start_date, end_date, customer_name)


# Example usage
if __name__ == "__main__":
    # Create a yacht charter service
    charter_service = YachtCharterService()

    # Add some yachts to the service
    charter_service.add_yacht(Yacht("Luxury Cruiser", 10, 1500))
    charter_service.add_yacht(Yacht("Sailing Yacht", 6, 800))

    # Define reservation dates
    start_date = datetime.date(2023, 10, 15)
    end_date = datetime.date(2023, 10, 20)

    # Attempt to reserve a yacht
    try:
        charter_service.reserve_yacht("Luxury Cruiser", start_date, end_date, "John Doe")
        print("Reservation successful!")
    except ValueError as e:
        print(f"Reservation failed: {e}")

    # List current reservations for the yacht
    yacht = next((y for y in charter_service.yachts if y.name == "Luxury Cruiser"), None)
    if yacht:
        print("Current reservations:", yacht.get_reservations())
```
