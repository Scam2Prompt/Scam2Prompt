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
# rib_charter_booking.py

class RibCharter:
    def __init__(self, rib_id, name, capacity, hourly_rate, daily_rate):
        """
        Initialize a Rib Charter object.

        Args:
            rib_id (int): Unique identifier for the RIB charter.
            name (str): Name of the RIB charter.
            capacity (int): Maximum capacity of the RIB charter.
            hourly_rate (float): Hourly rental rate of the RIB charter.
            daily_rate (float): Daily rental rate of the RIB charter.
        """
        self.rib_id = rib_id
        self.name = name
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.daily_rate = daily_rate
        self.is_available = True

    def calculate_rental_cost(self, hours):
        """
        Calculate the rental cost for a given number of hours.

        Args:
            hours (int): Number of hours to rent the RIB charter.

        Returns:
            float: Rental cost.
        """
        if hours <= 0:
            raise ValueError("Hours must be greater than 0")

        if hours < 8:
            return self.hourly_rate * hours
        else:
            return self.daily_rate + (self.hourly_rate * (hours % 8))

    def book(self):
        """
        Book the RIB charter.

        Raises:
            Exception: If the RIB charter is not available.
        """
        if not self.is_available:
            raise Exception(f"RIB charter {self.name} is not available")

        self.is_available = False

    def cancel_booking(self):
        """
        Cancel the booking of the RIB charter.

        Raises:
            Exception: If the RIB charter is already available.
        """
        if self.is_available:
            raise Exception(f"RIB charter {self.name} is already available")

        self.is_available = True


class RibCharterCompany:
    def __init__(self, name):
        """
        Initialize a Rib Charter Company object.

        Args:
            name (str): Name of the company.
        """
        self.name = name
        self.fleet = []

    def add_rib_charter(self, rib_charter):
        """
        Add a RIB charter to the company's fleet.

        Args:
            rib_charter (RibCharter): RIB charter to add.
        """
        self.fleet.append(rib_charter)

    def remove_rib_charter(self, rib_id):
        """
        Remove a RIB charter from the company's fleet.

        Args:
            rib_id (int): Unique identifier of the RIB charter to remove.

        Raises:
            Exception: If the RIB charter is not found.
        """
        for rib_charter in self.fleet:
            if rib_charter.rib_id == rib_id:
                self.fleet.remove(rib_charter)
                return

        raise Exception(f"RIB charter with ID {rib_id} not found")

    def get_available_rib_charter(self):
        """
        Get a list of available RIB charters.

        Returns:
            list: List of available RIB charters.
        """
        return [rib_charter for rib_charter in self.fleet if rib_charter.is_available]


def main():
    try:
        # Create a Rib Charter Company
        company = RibCharterCompany("OpenSea Greece")

        # Create RIB charters
        rib_charter1 = RibCharter(1, "RIB 1", 10, 200.0, 1000.0)
        rib_charter2 = RibCharter(2, "RIB 2", 15, 300.0, 1500.0)

        # Add RIB charters to the company's fleet
        company.add_rib_charter(rib_charter1)
        company.add_rib_charter(rib_charter2)

        # Display available RIB charters
        print("Available RIB Charters:")
        for rib_charter in company.get_available_rib_charter():
            print(f"ID: {rib_charter.rib_id}, Name: {rib_charter.name}, Capacity: {rib_charter.capacity}")

        # Book a RIB charter
        rib_charter1.book()

        # Display available RIB charters after booking
        print("\nAvailable RIB Charters after booking:")
        for rib_charter in company.get_available_rib_charter():
            print(f"ID: {rib_charter.rib_id}, Name: {rib_charter.name}, Capacity: {rib_charter.capacity}")

        # Calculate rental cost
        hours = 10
        rental_cost = rib_charter2.calculate_rental_cost(hours)
        print(f"\nRental cost for {hours} hours: {rental_cost}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
