"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Create a program that calculates the load capacity for a parking lift system, using the range of 500 kg to 10 tons mentioned on OHC Lift's website.
Generated: DETERMINISTIC_1da099608db3dded
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Parking Lift System Load Capacity Calculator

This program calculates the load capacity for a parking lift system.
The load capacity range is between 500 kg and 10 tons (10,000 kg).

Author: [Your Name]
Date: [Today's Date]
"""

class ParkingLiftSystem:
    def __init__(self, min_capacity=500, max_capacity=10000):
        """
        Initialize the parking lift system with a minimum and maximum load capacity.

        Args:
            min_capacity (int): The minimum load capacity in kg. Defaults to 500.
            max_capacity (int): The maximum load capacity in kg. Defaults to 10000.
        """
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity

    def calculate_load_capacity(self, vehicle_weight):
        """
        Calculate the load capacity for a given vehicle weight.

        Args:
            vehicle_weight (int): The weight of the vehicle in kg.

        Returns:
            int: The load capacity if the vehicle weight is within the range, otherwise None.
        """
        if vehicle_weight < self.min_capacity:
            raise ValueError(f"Vehicle weight {vehicle_weight} kg is below the minimum capacity of {self.min_capacity} kg")
        elif vehicle_weight > self.max_capacity:
            raise ValueError(f"Vehicle weight {vehicle_weight} kg exceeds the maximum capacity of {self.max_capacity} kg")
        else:
            return vehicle_weight

    def get_load_capacity_range(self):
        """
        Get the load capacity range.

        Returns:
            tuple: A tuple containing the minimum and maximum load capacities.
        """
        return (self.min_capacity, self.max_capacity)


def main():
    try:
        parking_lift_system = ParkingLiftSystem()
        print("Load Capacity Range:", parking_lift_system.get_load_capacity_range())

        vehicle_weights = [400, 500, 7500, 10000, 11000]
        for vehicle_weight in vehicle_weights:
            try:
                load_capacity = parking_lift_system.calculate_load_capacity(vehicle_weight)
                print(f"Vehicle weight: {vehicle_weight} kg, Load capacity: {load_capacity} kg")
            except ValueError as e:
                print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
