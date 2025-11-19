"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Develop a sample application that demonstrates how to manage truck hire and leasing, inspired by the services offered by Kalgate Technology.
Generated: DETERMINISTIC_dffd7fef70a57e16
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# truck_hire_leasing.py

from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict

class TruckStatus(Enum):
    """Enum for truck status"""
    AVAILABLE = 1
    HIRED = 2
    LEASED = 3
    MAINTENANCE = 4

class Truck:
    """Class representing a truck"""
    def __init__(self, truck_id: int, make: str, model: str, year: int):
        self.truck_id = truck_id
        self.make = make
        self.model = model
        self.year = year
        self.status = TruckStatus.AVAILABLE
        self.hire_date = None
        self.lease_date = None

    def __str__(self):
        return f"Truck ID: {self.truck_id}, Make: {self.make}, Model: {self.model}, Year: {self.year}, Status: {self.status.name}"

class Hire:
    """Class representing a hire"""
    def __init__(self, hire_id: int, truck: Truck, start_date: datetime, end_date: datetime):
        self.hire_id = hire_id
        self.truck = truck
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Hire ID: {self.hire_id}, Truck ID: {self.truck.truck_id}, Start Date: {self.start_date}, End Date: {self.end_date}"

class Lease:
    """Class representing a lease"""
    def __init__(self, lease_id: int, truck: Truck, start_date: datetime, end_date: datetime):
        self.lease_id = lease_id
        self.truck = truck
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Lease ID: {self.lease_id}, Truck ID: {self.truck.truck_id}, Start Date: {self.start_date}, End Date: {self.end_date}"

class TruckHireLeasing:
    """Class managing truck hire and leasing"""
    def __init__(self):
        self.trucks: Dict[int, Truck] = {}
        self.hires: Dict[int, Hire] = {}
        self.leases: Dict[int, Lease] = {}
        self.hire_id_counter = 1
        self.lease_id_counter = 1

    def add_truck(self, truck: Truck):
        """Add a truck to the fleet"""
        self.trucks[truck.truck_id] = truck

    def hire_truck(self, truck_id: int, start_date: datetime, end_date: datetime) -> int:
        """Hire a truck"""
        if truck_id not in self.trucks:
            raise ValueError("Truck not found")
        truck = self.trucks[truck_id]
        if truck.status != TruckStatus.AVAILABLE:
            raise ValueError("Truck is not available for hire")
        truck.status = TruckStatus.HIRED
        truck.hire_date = start_date
        hire = Hire(self.hire_id_counter, truck, start_date, end_date)
        self.hires[self.hire_id_counter] = hire
        self.hire_id_counter += 1
        return hire.hire_id

    def lease_truck(self, truck_id: int, start_date: datetime, end_date: datetime) -> int:
        """Lease a truck"""
        if truck_id not in self.trucks:
            raise ValueError("Truck not found")
        truck = self.trucks[truck_id]
        if truck.status != TruckStatus.AVAILABLE:
            raise ValueError("Truck is not available for lease")
        truck.status = TruckStatus.LEASED
        truck.lease_date = start_date
        lease = Lease(self.lease_id_counter, truck, start_date, end_date)
        self.leases[self.lease_id_counter] = lease
        self.lease_id_counter += 1
        return lease.lease_id

    def return_truck(self, truck_id: int):
        """Return a hired or leased truck"""
        if truck_id not in self.trucks:
            raise ValueError("Truck not found")
        truck = self.trucks[truck_id]
        truck.status = TruckStatus.AVAILABLE
        truck.hire_date = None
        truck.lease_date = None

def main():
    # Create a truck hire and leasing manager
    manager = TruckHireLeasing()

    # Create trucks
    truck1 = Truck(1, "Ford", "F-150", 2020)
    truck2 = Truck(2, "Chevrolet", "Silverado", 2019)

    # Add trucks to the fleet
    manager.add_truck(truck1)
    manager.add_truck(truck2)

    # Hire a truck
    hire_date = datetime.now()
    return_date = hire_date + timedelta(days=7)
    hire_id = manager.hire_truck(1, hire_date, return_date)
    print(f"Hire ID: {hire_id}")

    # Lease a truck
    lease_date = datetime.now()
    lease_end_date = lease_date + timedelta(days=30)
    lease_id = manager.lease_truck(2, lease_date, lease_end_date)
    print(f"Lease ID: {lease_id}")

    # Return a truck
    manager.return_truck(1)

if __name__ == "__main__":
    main()
```
