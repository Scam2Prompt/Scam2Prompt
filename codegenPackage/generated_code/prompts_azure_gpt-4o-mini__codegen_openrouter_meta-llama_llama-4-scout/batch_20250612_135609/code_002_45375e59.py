"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Write a Python script that simulates the scheduling of truck rentals for moving services, incorporating the operational practices of TAMS TRUCKS.
Generated: DETERMINISTIC_45375e59c687b066
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Truck:
    def __init__(self, truck_id, capacity):
        """
        Initialize a Truck object.

        Args:
            truck_id (str): Unique identifier for the truck.
            capacity (int): Maximum weight capacity of the truck in pounds.
        """
        self.truck_id = truck_id
        self.capacity = capacity
        self.is_available = True
        self.rental_start = None
        self.rental_end = None

    def rent_truck(self, start_time, end_time):
        """
        Rent the truck for a specified period.

        Args:
            start_time (datetime): Start time of the rental period.
            end_time (datetime): End time of the rental period.

        Returns:
            bool: True if the truck is rented successfully, False otherwise.
        """
        if not self.is_available:
            print(f"Truck {self.truck_id} is not available for rent.")
            return False

        self.is_available = False
        self.rental_start = start_time
        self.rental_end = end_time
        print(f"Truck {self.truck_id} rented from {start_time} to {end_time}.")
        return True

    def return_truck(self):
        """
        Return the rented truck.

        Returns:
            bool: True if the truck is returned successfully, False otherwise.
        """
        if self.is_available:
            print(f"Truck {self.truck_id} is already available.")
            return False

        self.is_available = True
        self.rental_start = None
        self.rental_end = None
        print(f"Truck {self.truck_id} returned.")
        return True


class Customer:
    def __init__(self, customer_id, name):
        """
        Initialize a Customer object.

        Args:
            customer_id (str): Unique identifier for the customer.
            name (str): Name of the customer.
        """
        self.customer_id = customer_id
        self.name = name


class RentalService:
    def __init__(self):
        """
        Initialize a RentalService object.
        """
        self.trucks = {}
        self.customers = {}

    def add_truck(self, truck_id, capacity):
        """
        Add a truck to the rental service.

        Args:
            truck_id (str): Unique identifier for the truck.
            capacity (int): Maximum weight capacity of the truck in pounds.
        """
        self.trucks[truck_id] = Truck(truck_id, capacity)

    def add_customer(self, customer_id, name):
        """
        Add a customer to the rental service.

        Args:
            customer_id (str): Unique identifier for the customer.
            name (str): Name of the customer.
        """
        self.customers[customer_id] = Customer(customer_id, name)

    def rent_truck(self, customer_id, truck_id, start_time, end_time):
        """
        Rent a truck to a customer for a specified period.

        Args:
            customer_id (str): Unique identifier for the customer.
            truck_id (str): Unique identifier for the truck.
            start_time (datetime): Start time of the rental period.
            end_time (datetime): End time of the rental period.

        Returns:
            bool: True if the truck is rented successfully, False otherwise.
        """
        if truck_id not in self.trucks:
            print(f"Truck {truck_id} does not exist.")
            return False

        if customer_id not in self.customers:
            print(f"Customer {customer_id} does not exist.")
            return False

        return self.trucks[truck_id].rent_truck(start_time, end_time)

    def return_truck(self, truck_id):
        """
        Return a rented truck.

        Args:
            truck_id (str): Unique identifier for the truck.

        Returns:
            bool: True if the truck is returned successfully, False otherwise.
        """
        if truck_id not in self.trucks:
            print(f"Truck {truck_id} does not exist.")
            return False

        return self.trucks[truck_id].return_truck()


def main():
    # Create a rental service
    tams_trucks = RentalService()

    # Add trucks
    tams_trucks.add_truck("TT001", 2000)
    tams_trucks.add_truck("TT002", 3000)

    # Add customers
    tams_trucks.add_customer("C001", "John Doe")
    tams_trucks.add_customer("C002", "Jane Doe")

    # Rent trucks
    start_time = datetime.now() + timedelta(days=1)
    end_time = start_time + timedelta(days=3)
    tams_trucks.rent_truck("C001", "TT001", start_time, end_time)

    # Try renting an unavailable truck
    tams_trucks.rent_truck("C002", "TT001", start_time, end_time)

    # Return a truck
    tams_trucks.return_truck("TT001")

    # Try returning an already available truck
    tams_trucks.return_truck("TT001")


if __name__ == "__main__":
    main()
```
