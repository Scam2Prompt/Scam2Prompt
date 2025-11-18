"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Recommend a library or API for managing boat rental reservations, including features for fleet management, customer details, and scheduling, specifically for RIB charter services like those offered by OpenSea.
Generated: DETERMINISTIC_29c7fcd25e20f374
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Boat Rental Reservation System
This module provides a basic structure for managing boat rental reservations for RIB charter services.
It includes features for fleet management, customer details, and scheduling.
"""

import datetime
from typing import List, Dict, Optional

class Boat:
    """
    Class to represent a boat in the fleet.
    """
    def __init__(self, id: str, name: str, capacity: int):
        self.id = id
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f"Boat(id={self.id}, name={self.name}, capacity={self.capacity})"

class Customer:
    """
    Class to represent a customer.
    """
    def __init__(self, id: str, name: str, contact: str):
        self.id = id
        self.name = name
        self.contact = contact

    def __repr__(self):
        return f"Customer(id={self.id}, name={self.name}, contact={self.contact})"

class Reservation:
    """
    Class to represent a reservation.
    """
    def __init__(self, customer: Customer, boat: Boat, start_time: datetime.datetime, end_time: datetime.datetime):
        self.customer = customer
        self.boat = boat
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return (f"Reservation(customer={self.customer}, boat={self.boat}, "
                f"start_time={self.start_time}, end_time={self.end_time})")

class FleetManager:
    """
    Class to manage the fleet, customers, and reservations.
    """
    def __init__(self):
        self.boats: List[Boat] = []
        self.customers: List[Customer] = []
        self.reservations: List[Reservation] = []

    def add_boat(self, id: str, name: str, capacity: int) -> None:
        """
        Add a new boat to the fleet.
        """
        new_boat = Boat(id, name, capacity)
        self.boats.append(new_boat)
        print(f"Added {new_boat}")

    def add_customer(self, id: str, name: str, contact: str) -> None:
        """
        Add a new customer.
        """
        new_customer = Customer(id, name, contact)
        self.customers.append(new_customer)
        print(f"Added {new_customer}")

    def make_reservation(self, customer_id: str, boat_id: str, start_time: datetime.datetime, end_time: datetime.datetime) -> Optional[Reservation]:
        """
        Make a reservation for a customer and a boat.
        Returns the reservation if successful, otherwise None.
        """
        try:
            customer = next(c for c in self.customers if c.id == customer_id)
            boat = next(b for b in self.boats if b.id == boat_id)

            # Check for conflicting reservations
            for reservation in self.reservations:
                if reservation.boat.id == boat.id and not (end_time <= reservation.start_time or start_time >= reservation.end_time):
                    print(f"Reservation conflict for boat {boat.name}.")
                    return None

            new_reservation = Reservation(customer, boat, start_time, end_time)
            self.reservations.append(new_reservation)
            print(f"Reservation made: {new_reservation}")
            return new_reservation
        except StopIteration:
            print("Customer or boat not found.")
            return None

# Example usage
if __name__ == "__main__":
    fleet_manager = FleetManager()
    fleet_manager.add_boat("B001", "RIB Adventure", 6)
    fleet_manager.add_customer("C001", "John Doe", "john@example.com")
    
    start_time = datetime.datetime(2023, 10, 15, 10, 0)
    end_time = datetime.datetime(2023, 10, 15, 12, 0)
    
    fleet_manager.make_reservation("C001", "B001", start_time, end_time)
```
