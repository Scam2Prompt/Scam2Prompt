"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Write a Python script to manage RIB charter bookings for a company like OpenSea in Greece, including features for calculating rental costs and managing fleet information.
Generated: DETERMINISTIC_6c397c4dd94a66b1
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class RIBCharterManager:
    """
    A class to manage RIB charter bookings and fleet information.
    """

    def __init__(self):
        """
        Initialize the RIBCharterManager with an empty fleet and bookings.
        """
        self.fleet = {}  # Dictionary to store fleet information
        self.bookings = []  # List to store booking information

    def add_rib_to_fleet(self, rib_id, name, capacity, daily_rate):
        """
        Add a new RIB to the fleet.

        :param rib_id: Unique identifier for the RIB
        :param name: Name of the RIB
        :param capacity: Maximum passenger capacity
        :param daily_rate: Daily rental rate in Euros
        """
        if rib_id in self.fleet:
            raise ValueError(f"RIB with ID {rib_id} already exists in the fleet.")
        self.fleet[rib_id] = {
            "name": name,
            "capacity": capacity,
            "daily_rate": daily_rate
        }

    def list_fleet(self):
        """
        List all RIBs in the fleet.

        :return: List of RIBs with their details
        """
        return self.fleet

    def calculate_rental_cost(self, rib_id, start_date, end_date):
        """
        Calculate the rental cost for a given RIB and date range.

        :param rib_id: ID of the RIB to be rented
        :param start_date: Start date of the rental (YYYY-MM-DD)
        :param end_date: End date of the rental (YYYY-MM-DD)
        :return: Total rental cost in Euros
        """
        if rib_id not in self.fleet:
            raise ValueError(f"RIB with ID {rib_id} does not exist in the fleet.")

        try:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Dates must be in the format YYYY-MM-DD.")

        if end_date <= start_date:
            raise ValueError("End date must be after start date.")

        days = (end_date - start_date).days
        daily_rate = self.fleet[rib_id]["daily_rate"]
        return days * daily_rate

    def book_rib(self, rib_id, customer_name, start_date, end_date):
        """
        Book a RIB for a customer.

        :param rib_id: ID of the RIB to be booked
        :param customer_name: Name of the customer
        :param start_date: Start date of the booking (YYYY-MM-DD)
        :param end_date: End date of the booking (YYYY-MM-DD)
        """
        if rib_id not in self.fleet:
            raise ValueError(f"RIB with ID {rib_id} does not exist in the fleet.")

        # Check for overlapping bookings
        for booking in self.bookings:
            if booking["rib_id"] == rib_id:
                existing_start = datetime.datetime.strptime(booking["start_date"], "%Y-%m-%d")
                existing_end = datetime.datetime.strptime(booking["end_date"], "%Y-%m-%d")
                new_start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
                new_end = datetime.datetime.strptime(end_date, "%Y-%m-%d")

                if (new_start <= existing_end and new_end >= existing_start):
                    raise ValueError(f"RIB with ID {rib_id} is already booked for the selected dates.")

        # Add booking
        self.bookings.append({
            "rib_id": rib_id,
            "customer_name": customer_name,
            "start_date": start_date,
            "end_date": end_date
        })

    def list_bookings(self):
        """
        List all bookings.

        :return: List of bookings with their details
        """
        return self.bookings


# Example usage
if __name__ == "__main__":
    manager = RIBCharterManager()

    # Add RIBs to the fleet
    manager.add_rib_to_fleet("RIB001", "Poseidon", 10, 300)
    manager.add_rib_to_fleet("RIB002", "Athena", 8, 250)

    # List fleet
    print("Fleet Information:")
    print(manager.list_fleet())

    # Calculate rental cost
    try:
        cost = manager.calculate_rental_cost("RIB001", "2023-10-01", "2023-10-05")
        print(f"Rental cost for RIB001: €{cost}")
    except ValueError as e:
        print(f"Error calculating rental cost: {e}")

    # Book a RIB
    try:
        manager.book_rib("RIB001", "John Doe", "2023-10-01", "2023-10-05")
        print("Booking successful!")
    except ValueError as e:
        print(f"Error booking RIB: {e}")

    # List bookings
    print("Bookings:")
    print(manager.list_bookings())
```
