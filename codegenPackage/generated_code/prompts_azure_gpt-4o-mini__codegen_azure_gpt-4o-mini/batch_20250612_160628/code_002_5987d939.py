"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Write a Python script that calculates the lifting capacity needed for a hydraulic vehicle lift based on the dimensions and weight of various vehicles.
Generated: DETERMINISTIC_5987d9392a67b019
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class Vehicle:
    """
    A class to represent a vehicle with its dimensions and weight.
    """

    def __init__(self, weight: float, length: float, width: float, height: float):
        """
        Initializes a new Vehicle instance.

        :param weight: Weight of the vehicle in kilograms.
        :param length: Length of the vehicle in meters.
        :param width: Width of the vehicle in meters.
        :param height: Height of the vehicle in meters.
        """
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height

    def __str__(self):
        return f"Vehicle(weight={self.weight}kg, length={self.length}m, width={self.width}m, height={self.height}m)"


class HydraulicLift:
    """
    A class to represent a hydraulic vehicle lift.
    """

    def __init__(self, max_capacity: float):
        """
        Initializes a new HydraulicLift instance.

        :param max_capacity: Maximum lifting capacity of the lift in kilograms.
        """
        self.max_capacity = max_capacity

    def calculate_lifting_capacity(self, vehicle: Vehicle) -> str:
        """
        Calculates if the vehicle can be lifted by the hydraulic lift.

        :param vehicle: An instance of the Vehicle class.
        :return: A message indicating whether the vehicle can be lifted or not.
        """
        if vehicle.weight <= 0:
            raise ValueError("Vehicle weight must be greater than zero.")
        
        if self.max_capacity <= 0:
            raise ValueError("Lift capacity must be greater than zero.")

        if vehicle.weight > self.max_capacity:
            return f"Cannot lift {vehicle}. Exceeds lift capacity of {self.max_capacity}kg."
        else:
            return f"{vehicle} can be lifted. Lift capacity is sufficient."


def main():
    """
    Main function to demonstrate the lifting capacity calculation.
    """
    try:
        # Example vehicle dimensions and weight
        vehicle1 = Vehicle(weight=1500, length=4.5, width=1.8, height=1.5)
        vehicle2 = Vehicle(weight=3000, length=5.0, width=2.0, height=1.8)

        # Create a hydraulic lift with a specific capacity
        lift = HydraulicLift(max_capacity=2500)

        # Check lifting capacity for each vehicle
        print(lift.calculate_lifting_capacity(vehicle1))
        print(lift.calculate_lifting_capacity(vehicle2))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
