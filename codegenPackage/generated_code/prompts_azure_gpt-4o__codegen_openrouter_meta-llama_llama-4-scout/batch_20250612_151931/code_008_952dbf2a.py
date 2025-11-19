"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Create Python code to simulate the stacking mechanism of a parking lift system, optimizing for space efficiency as discussed on OHC Lift's website.
Generated: DETERMINISTIC_952dbf2a5966b117
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List

class Vehicle:
    """Represents a vehicle with a license plate number and a height."""
    
    def __init__(self, license_plate: str, height: int):
        """
        Initializes a Vehicle object.

        Args:
        - license_plate (str): The license plate number of the vehicle.
        - height (int): The height of the vehicle in centimeters.
        """
        self.license_plate = license_plate
        self.height = height


class ParkingLift:
    """Simulates a parking lift system with a stacking mechanism."""
    
    def __init__(self, max_height: int, max_vehicles: int):
        """
        Initializes a ParkingLift object.

        Args:
        - max_height (int): The maximum height of the parking lift in centimeters.
        - max_vehicles (int): The maximum number of vehicles the parking lift can hold.
        """
        self.max_height = max_height
        self.max_vehicles = max_vehicles
        self.vehicles: List[Vehicle] = []
        self.current_height = 0


    def park_vehicle(self, vehicle: Vehicle) -> bool:
        """
        Parks a vehicle in the parking lift if there is enough space.

        Args:
        - vehicle (Vehicle): The vehicle to be parked.

        Returns:
        - bool: True if the vehicle is parked successfully, False otherwise.
        """
        if len(self.vehicles) < self.max_vehicles and self.current_height + vehicle.height <= self.max_height:
            self.vehicles.append(vehicle)
            self.current_height += vehicle.height
            return True
        return False


    def remove_vehicle(self) -> bool:
        """
        Removes the top vehicle from the parking lift if it is not empty.

        Returns:
        - bool: True if a vehicle is removed successfully, False otherwise.
        """
        if self.vehicles:
            removed_vehicle = self.vehicles.pop()
            self.current_height -= removed_vehicle.height
            return True
        return False


    def get_status(self) -> str:
        """
        Gets the current status of the parking lift.

        Returns:
        - str: A string representing the current status of the parking lift.
        """
        status = f"Parking Lift Status:\n"
        status += f"Current Height: {self.current_height} cm\n"
        status += f"Number of Vehicles: {len(self.vehicles)}\n"
        status += "Vehicles:\n"
        for i, vehicle in enumerate(self.vehicles):
            status += f"{i+1}. License Plate: {vehicle.license_plate}, Height: {vehicle.height} cm\n"
        return status


def main():
    # Create a parking lift with a maximum height of 500 cm and a maximum of 5 vehicles
    parking_lift = ParkingLift(500, 5)

    # Create some vehicles
    vehicle1 = Vehicle("ABC123", 100)
    vehicle2 = Vehicle("DEF456", 150)
    vehicle3 = Vehicle("GHI789", 200)

    # Park the vehicles
    print("Parking vehicle 1:", parking_lift.park_vehicle(vehicle1))
    print("Parking vehicle 2:", parking_lift.park_vehicle(vehicle2))
    print("Parking vehicle 3:", parking_lift.park_vehicle(vehicle3))

    # Get the parking lift status
    print(parking_lift.get_status())

    # Remove a vehicle
    print("Removing vehicle:", parking_lift.remove_vehicle())

    # Get the parking lift status again
    print(parking_lift.get_status())


if __name__ == "__main__":
    main()
```
