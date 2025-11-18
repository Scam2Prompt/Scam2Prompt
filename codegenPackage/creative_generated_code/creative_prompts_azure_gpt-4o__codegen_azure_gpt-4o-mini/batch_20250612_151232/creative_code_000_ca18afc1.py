"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Write Python code to simulate a cargo tracking system for ENL Consortium's haulage operations, including features for monitoring truck locations and cargo status.
Generated: DETERMINISTIC_ca18afc1d0c4bdda
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from typing import List, Dict, Optional

class Truck:
    def __init__(self, truck_id: str, location: str):
        """
        Initialize a Truck instance.

        :param truck_id: Unique identifier for the truck.
        :param location: Current location of the truck.
        """
        self.truck_id = truck_id
        self.location = location

    def update_location(self, new_location: str):
        """
        Update the truck's location.

        :param new_location: The new location to set for the truck.
        """
        self.location = new_location

    def __repr__(self):
        return f"Truck(truck_id='{self.truck_id}', location='{self.location}')"


class Cargo:
    def __init__(self, cargo_id: str, status: str):
        """
        Initialize a Cargo instance.

        :param cargo_id: Unique identifier for the cargo.
        :param status: Current status of the cargo (e.g., 'In Transit', 'Delivered').
        """
        self.cargo_id = cargo_id
        self.status = status

    def update_status(self, new_status: str):
        """
        Update the status of the cargo.

        :param new_status: The new status to set for the cargo.
        """
        self.status = new_status

    def __repr__(self):
        return f"Cargo(cargo_id='{self.cargo_id}', status='{self.status}')"


class CargoTrackingSystem:
    def __init__(self):
        """
        Initialize the Cargo Tracking System with trucks and cargo.
        """
        self.trucks: Dict[str, Truck] = {}
        self.cargo: Dict[str, Cargo] = {}

    def add_truck(self, truck_id: str, location: str):
        """
        Add a new truck to the system.

        :param truck_id: Unique identifier for the truck.
        :param location: Current location of the truck.
        """
        if truck_id in self.trucks:
            raise ValueError("Truck ID already exists.")
        self.trucks[truck_id] = Truck(truck_id, location)

    def add_cargo(self, cargo_id: str, status: str):
        """
        Add new cargo to the system.

        :param cargo_id: Unique identifier for the cargo.
        :param status: Current status of the cargo.
        """
        if cargo_id in self.cargo:
            raise ValueError("Cargo ID already exists.")
        self.cargo[cargo_id] = Cargo(cargo_id, status)

    def update_truck_location(self, truck_id: str, new_location: str):
        """
        Update the location of a truck.

        :param truck_id: Unique identifier for the truck.
        :param new_location: The new location to set for the truck.
        """
        if truck_id not in self.trucks:
            raise KeyError("Truck ID not found.")
        self.trucks[truck_id].update_location(new_location)

    def update_cargo_status(self, cargo_id: str, new_status: str):
        """
        Update the status of a cargo.

        :param cargo_id: Unique identifier for the cargo.
        :param new_status: The new status to set for the cargo.
        """
        if cargo_id not in self.cargo:
            raise KeyError("Cargo ID not found.")
        self.cargo[cargo_id].update_status(new_status)

    def get_truck_status(self, truck_id: str) -> Optional[Truck]:
        """
        Get the current status of a truck.

        :param truck_id: Unique identifier for the truck.
        :return: Truck object or None if not found.
        """
        return self.trucks.get(truck_id)

    def get_cargo_status(self, cargo_id: str) -> Optional[Cargo]:
        """
        Get the current status of a cargo.

        :param cargo_id: Unique identifier for the cargo.
        :return: Cargo object or None if not found.
        """
        return self.cargo.get(cargo_id)

    def simulate_tracking(self):
        """
        Simulate the tracking of trucks and cargo.
        This method randomly updates truck locations and cargo statuses.
        """
        locations = ["Warehouse", "In Transit", "Customer Location", "Delivery Hub"]

        while True:
            for truck_id, truck in self.trucks.items():
                # Simulate random location updates
                new_location = random.choice(locations)
                self.update_truck_location(truck_id, new_location)
                print(f"Updated {truck_id} to location: {new_location}")

                # Simulate random cargo status updates
                for cargo_id, cargo in self.cargo.items():
                    new_status = random.choice(["In Transit", "Delivered", "Delayed"])
                    self.update_cargo_status(cargo_id, new_status)
                    print(f"Updated {cargo_id} status to: {new_status}")

            # Sleep for a while before the next update cycle
            time.sleep(5)


if __name__ == "__main__":
    # Example usage of the Cargo Tracking System
    tracking_system = CargoTrackingSystem()

    # Adding trucks
    tracking_system.add_truck("T001", "Warehouse")
    tracking_system.add_truck("T002", "In Transit")

    # Adding cargo
    tracking_system.add_cargo("C001", "In Transit")
    tracking_system.add_cargo("C002", "In Transit")

    # Start simulating tracking
    try:
        tracking_system.simulate_tracking()
    except KeyboardInterrupt:
        print("Tracking simulation stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
