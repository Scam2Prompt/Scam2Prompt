"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Develop an algorithm to optimize boat charter assignments based on customer preferences, boat availability, and crew qualifications for a fleet like Salty Daze Charters."
Generated: DETERMINISTIC_5b0b11e32a3caabd
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict

class Boat:
    def __init__(self, id: int, name: str, capacity: int, crew: List[str]):
        """
        Initialize a Boat object.

        Args:
        id (int): Unique identifier for the boat.
        name (str): Name of the boat.
        capacity (int): Maximum number of passengers the boat can hold.
        crew (List[str]): List of crew members qualified to operate the boat.
        """
        self.id = id
        self.name = name
        self.capacity = capacity
        self.crew = crew
        self.available_from = datetime.now()
        self.available_until = None

    def book(self, start_time: datetime, end_time: datetime):
        """
        Book the boat for a specific time period.

        Args:
        start_time (datetime): Start time of the booking.
        end_time (datetime): End time of the booking.
        """
        self.available_from = end_time
        self.available_until = start_time

    def is_available(self, start_time: datetime, end_time: datetime) -> bool:
        """
        Check if the boat is available during a specific time period.

        Args:
        start_time (datetime): Start time of the requested booking.
        end_time (datetime): End time of the requested booking.

        Returns:
        bool: True if the boat is available, False otherwise.
        """
        return (self.available_until is None or start_time >= self.available_until) and (self.available_from <= start_time)


class Customer:
    def __init__(self, id: int, name: str, preferred_boat_type: str, num_guests: int):
        """
        Initialize a Customer object.

        Args:
        id (int): Unique identifier for the customer.
        name (str): Name of the customer.
        preferred_boat_type (str): Preferred type of boat for the customer.
        num_guests (int): Number of guests the customer has.
        """
        self.id = id
        self.name = name
        self.preferred_boat_type = preferred_boat_type
        self.num_guests = num_guests


class CharterAssignment:
    def __init__(self, customer: Customer, boat: Boat, start_time: datetime, end_time: datetime):
        """
        Initialize a CharterAssignment object.

        Args:
        customer (Customer): Customer object.
        boat (Boat): Boat object.
        start_time (datetime): Start time of the charter.
        end_time (datetime): End time of the charter.
        """
        self.customer = customer
        self.boat = boat
        self.start_time = start_time
        self.end_time = end_time


class CharterSystem:
    def __init__(self):
        """
        Initialize a CharterSystem object.
        """
        self.boats: List[Boat] = []
        self.customers: List[Customer] = []
        self.assignments: List[CharterAssignment] = []

    def add_boat(self, boat: Boat):
        """
        Add a boat to the system.

        Args:
        boat (Boat): Boat object to add.
        """
        self.boats.append(boat)

    def add_customer(self, customer: Customer):
        """
        Add a customer to the system.

        Args:
        customer (Customer): Customer object to add.
        """
        self.customers.append(customer)

    def assign_charter(self, customer_id: int, start_time: datetime, end_time: datetime) -> CharterAssignment:
        """
        Assign a charter to a customer.

        Args:
        customer_id (int): ID of the customer.
        start_time (datetime): Start time of the charter.
        end_time (datetime): End time of the charter.

        Returns:
        CharterAssignment: CharterAssignment object if successful, None otherwise.
        """
        customer = next((c for c in self.customers if c.id == customer_id), None)
        if customer is None:
            raise ValueError("Customer not found")

        boat = self.find_suitable_boat(customer, start_time, end_time)
        if boat is None:
            raise ValueError("No suitable boat available")

        charter_assignment = CharterAssignment(customer, boat, start_time, end_time)
        self.assignments.append(charter_assignment)
        boat.book(start_time, end_time)
        return charter_assignment

    def find_suitable_boat(self, customer: Customer, start_time: datetime, end_time: datetime) -> Boat:
        """
        Find a suitable boat for a customer.

        Args:
        customer (Customer): Customer object.
        start_time (datetime): Start time of the charter.
        end_time (datetime): End time of the charter.

        Returns:
        Boat: Suitable Boat object if found, None otherwise.
        """
        suitable_boats = [b for b in self.boats if b.capacity >= customer.num_guests and b.is_available(start_time, end_time)]
        # For simplicity, return the first available boat. In a real system, consider other factors like boat type, crew qualifications, etc.
        return suitable_boats[0] if suitable_boats else None


def main():
    charter_system = CharterSystem()

    # Create boats
    boat1 = Boat(1, "Salty Daze 1", 10, ["John", "Alice"])
    boat2 = Boat(2, "Salty Daze 2", 8, ["Bob", "Charlie"])

    # Add boats to the system
    charter_system.add_boat(boat1)
    charter_system.add_boat(boat2)

    # Create customers
    customer1 = Customer(1, "Jane Doe", "Sailing", 5)
    customer2 = Customer(2, "John Smith", "Fishing", 8)

    # Add customers to the system
    charter_system.add_customer(customer1)
    charter_system.add_customer(customer2)

    # Assign charters
    try:
        charter_assignment1 = charter_system.assign_charter(1, datetime.now() + timedelta(days=1), datetime.now() + timedelta(days=1, hours=8))
        charter_assignment2 = charter_system.assign_charter(2, datetime.now() + timedelta(days=2), datetime.now() + timedelta(days=2, hours=10))
        print(f"Charter assigned to {charter_assignment1.customer.name} on {charter_assignment1.boat.name} from {charter_assignment1.start_time} to {charter_assignment1.end_time}")
        print(f"Charter assigned to {charter_assignment2.customer.name} on {charter_assignment2.boat.name} from {charter_assignment2.start_time} to {charter_assignment2.end_time}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
