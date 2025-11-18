"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Develop a system for outsourcing drivers, including features for matching drivers to haulage needs, inspired by Kalgate Technology's driver outsourcing services.
Generated: DETERMINISTIC_a7df6dcc1d365acd
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional
import random

class Driver:
    """
    Class representing a driver in the system.
    """
    def __init__(self, driver_id: str, name: str, vehicle_type: str):
        self.driver_id = driver_id
        self.name = name
        self.vehicle_type = vehicle_type

    def __repr__(self):
        return f"Driver(id={self.driver_id}, name={self.name}, vehicle_type={self.vehicle_type})"


class HaulageNeed:
    """
    Class representing a haulage need in the system.
    """
    def __init__(self, need_id: str, cargo_type: str, required_vehicle_type: str):
        self.need_id = need_id
        self.cargo_type = cargo_type
        self.required_vehicle_type = required_vehicle_type

    def __repr__(self):
        return f"HaulageNeed(id={self.need_id}, cargo_type={self.cargo_type}, required_vehicle_type={self.required_vehicle_type})"


class DriverPool:
    """
    Class to manage a pool of drivers and match them with haulage needs.
    """
    def __init__(self):
        self.drivers: List[Driver] = []

    def add_driver(self, driver: Driver) -> None:
        """
        Adds a driver to the pool.
        """
        self.drivers.append(driver)

    def find_matching_driver(self, haulage_need: HaulageNeed) -> Optional[Driver]:
        """
        Finds a driver that matches the haulage need based on vehicle type.
        """
        for driver in self.drivers:
            if driver.vehicle_type == haulage_need.required_vehicle_type:
                return driver
        return None


class OutsourcingSystem:
    """
    Main system class to handle driver outsourcing functionalities.
    """
    def __init__(self):
        self.driver_pool = DriverPool()

    def register_driver(self, driver_id: str, name: str, vehicle_type: str) -> None:
        """
        Registers a new driver in the system.
        """
        if not driver_id or not name or not vehicle_type:
            raise ValueError("Driver ID, name, and vehicle type must be provided.")
        new_driver = Driver(driver_id, name, vehicle_type)
        self.driver_pool.add_driver(new_driver)
        print(f"Registered {new_driver}")

    def request_haulage(self, need_id: str, cargo_type: str, required_vehicle_type: str) -> Optional[Driver]:
        """
        Matches a haulage need with an available driver.
        """
        haulage_need = HaulageNeed(need_id, cargo_type, required_vehicle_type)
        matching_driver = self.driver_pool.find_matching_driver(haulage_need)
        if matching_driver:
            print(f"Matched {matching_driver} for {haulage_need}")
            return matching_driver
        else:
            print(f"No matching driver found for {haulage_need}")
            return None


# Example usage:
if __name__ == "__main__":
    try:
        system = OutsourcingSystem()
        # Register some drivers
        system.register_driver("D001", "Alice", "Truck")
        system.register_driver("D002", "Bob", "Van")

        # Request a haulage
        system.request_haulage("H001", "Furniture", "Truck")
        system.request_haulage("H002", "Groceries", "Van")
        system.request_haulage("H003", "Electronics", "Truck")
        system.request_haulage("H004", "Books", "Bicycle")  # No matching driver
    except Exception as e:
        print(f"An error occurred: {e}")
```
