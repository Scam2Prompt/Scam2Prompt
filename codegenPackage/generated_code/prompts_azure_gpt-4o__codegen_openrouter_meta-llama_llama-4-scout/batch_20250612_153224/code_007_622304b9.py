"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Generate Python code to simulate the functionality of JECO's jetting and vacuum vehicles for cleaning operations.
Generated: DETERMINISTIC_622304b953d21a1d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import List

# Define an Enum for vehicle types
class VehicleType(Enum):
    JETTING = 1
    VACUUM = 2

# Abstract base class for vehicles
class Vehicle(ABC):
    def __init__(self, vehicle_type: VehicleType, capacity: float):
        """
        Initialize a vehicle with type and capacity.

        Args:
        - vehicle_type (VehicleType): Type of vehicle (JETTING or VACUUM)
        - capacity (float): Capacity of the vehicle
        """
        self.vehicle_type = vehicle_type
        self.capacity = capacity
        self.current_load = 0.0

    @abstractmethod
    def operate(self):
        pass

    def load(self, amount: float):
        """
        Load the vehicle with a certain amount.

        Args:
        - amount (float): Amount to load

        Raises:
        - ValueError: If the amount exceeds the remaining capacity
        """
        if self.current_load + amount > self.capacity:
            raise ValueError("Insufficient capacity")
        self.current_load += amount

    def unload(self, amount: float):
        """
        Unload a certain amount from the vehicle.

        Args:
        - amount (float): Amount to unload

        Raises:
        - ValueError: If the amount exceeds the current load
        """
        if amount > self.current_load:
            raise ValueError("Insufficient load")
        self.current_load -= amount


# Concrete class for jetting vehicle
class JettingVehicle(Vehicle):
    def __init__(self, capacity: float, pressure: float):
        """
        Initialize a jetting vehicle with capacity and pressure.

        Args:
        - capacity (float): Capacity of the vehicle
        - pressure (float): Pressure of the vehicle
        """
        super().__init__(VehicleType.JETTING, capacity)
        self.pressure = pressure

    def operate(self):
        """
        Operate the jetting vehicle.

        Prints a message indicating the vehicle is operating.
        """
        print(f"Jetting vehicle operating at {self.pressure} pressure")


# Concrete class for vacuum vehicle
class VacuumVehicle(Vehicle):
    def __init__(self, capacity: float, suction_power: float):
        """
        Initialize a vacuum vehicle with capacity and suction power.

        Args:
        - capacity (float): Capacity of the vehicle
        - suction_power (float): Suction power of the vehicle
        """
        super().__init__(VehicleType.VACUUM, capacity)
        self.suction_power = suction_power

    def operate(self):
        """
        Operate the vacuum vehicle.

        Prints a message indicating the vehicle is operating.
        """
        print(f"Vacuum vehicle operating at {self.suction_power} suction power")


# Fleet class to manage vehicles
class Fleet:
    def __init__(self):
        self.vehicles: List[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        """
        Add a vehicle to the fleet.

        Args:
        - vehicle (Vehicle): Vehicle to add
        """
        self.vehicles.append(vehicle)

    def operate_vehicles(self):
        """
        Operate all vehicles in the fleet.
        """
        for vehicle in self.vehicles:
            vehicle.operate()


# Example usage
def main():
    fleet = Fleet()

    jetting_vehicle = JettingVehicle(1000.0, 100.0)
    jetting_vehicle.load(500.0)
    fleet.add_vehicle(jetting_vehicle)

    vacuum_vehicle = VacuumVehicle(500.0, 50.0)
    vacuum_vehicle.load(200.0)
    fleet.add_vehicle(vacuum_vehicle)

    fleet.operate_vehicles()

    try:
        jetting_vehicle.unload(700.0)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
