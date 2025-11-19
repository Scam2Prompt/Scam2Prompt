"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Generate a code snippet for a hydraulic lift system that can safely transport loads between different floors in an industrial setting.
Generated: DETERMINISTIC_8242a83b83c37637
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time

class HydraulicLiftSystem:
    def __init__(self, max_load_capacity, floors):
        """
        Initialize the hydraulic lift system.

        :param max_load_capacity: Maximum load capacity of the lift in kilograms.
        :param floors: List of floor numbers the lift can access.
        """
        self.max_load_capacity = max_load_capacity
        self.floors = sorted(floors)  # Ensure floors are sorted
        self.current_floor = self.floors[0]  # Start at the lowest floor
        self.current_load = 0  # Current load in kilograms

    def load(self, weight):
        """
        Load the lift with a specified weight.

        :param weight: Weight to be loaded in kilograms.
        :raises ValueError: If the weight exceeds the maximum load capacity.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if self.current_load + weight > self.max_load_capacity:
            raise ValueError("Exceeds maximum load capacity.")
        self.current_load += weight
        print(f"Loaded {weight} kg. Current load: {self.current_load} kg.")

    def unload(self, weight):
        """
        Unload a specified weight from the lift.

        :param weight: Weight to be unloaded in kilograms.
        :raises ValueError: If the weight to unload exceeds the current load.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if weight > self.current_load:
            raise ValueError("Cannot unload more than the current load.")
        self.current_load -= weight
        print(f"Unloaded {weight} kg. Current load: {self.current_load} kg.")

    def move_to_floor(self, target_floor):
        """
        Move the lift to a specified floor.

        :param target_floor: The floor number to move to.
        :raises ValueError: If the target floor is not accessible.
        """
        if target_floor not in self.floors:
            raise ValueError(f"Floor {target_floor} is not accessible.")
        print(f"Moving from floor {self.current_floor} to floor {target_floor}...")
        time.sleep(2)  # Simulate the time taken to move between floors
        self.current_floor = target_floor
        print(f"Lift is now at floor {self.current_floor}.")

    def emergency_stop(self):
        """
        Trigger an emergency stop for the lift.
        """
        print("Emergency stop activated! Lift halted immediately.")
        # Additional safety measures can be implemented here

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the lift system with a max load capacity of 1000 kg and floors 1 to 5
        lift = HydraulicLiftSystem(max_load_capacity=1000, floors=[1, 2, 3, 4, 5])

        # Load the lift with 500 kg
        lift.load(500)

        # Move to the 3rd floor
        lift.move_to_floor(3)

        # Unload 200 kg
        lift.unload(200)

        # Move to the 5th floor
        lift.move_to_floor(5)

        # Trigger an emergency stop
        lift.emergency_stop()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
