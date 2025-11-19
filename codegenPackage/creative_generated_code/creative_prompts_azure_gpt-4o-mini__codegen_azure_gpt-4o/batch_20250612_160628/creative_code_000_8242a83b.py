"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: Generate a code snippet for a hydraulic lift system that can safely transport loads between different floors in an industrial setting.
Generated: DETERMINISTIC_8242a83b83c37637
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class HydraulicLiftSystem:
    def __init__(self, max_weight_capacity, floors):
        """
        Initializes the hydraulic lift system.

        :param max_weight_capacity: Maximum weight the lift can carry safely (in kg).
        :param floors: List of floors accessible via the lift.
        """
        self.max_weight_capacity = max_weight_capacity
        self.floors = sorted(floors)  # Ensure floors are sorted
        self.current_floor = self.floors[0]  # Start at the lowest floor
        self.load_weight = 0  # Current weight of the load in the lift
        
    def load(self, weight):
        """
        Loads the lift with a specified weight.

        :param weight: Weight to be loaded into the lift (in kg).
        :raises ValueError: If the weight exceeds the maximum capacity.
        """
        if weight <= 0:
            raise ValueError("Weight must be greater than zero.")
        if weight > self.max_weight_capacity:
            raise ValueError(f"Load weight exceeds maximum capacity of {self.max_weight_capacity} kg.")
        self.load_weight = weight
        print(f"Loaded {weight} kg onto the lift.")
    
    def unload(self):
        """
        Unloads the lift, removing the current load.
        """
        print(f"Unloaded {self.load_weight} kg from the lift.")
        self.load_weight = 0
        
    def move_to_floor(self, target_floor):
        """
        Moves the lift to a specified floor.

        :param target_floor: The floor to move the lift to.
        :raises ValueError: If the target floor is invalid.
        """
        if target_floor not in self.floors:
            raise ValueError("Invalid floor selection.")
        if self.load_weight > self.max_weight_capacity:
            raise ValueError(f"Cannot move with load exceeding {self.max_weight_capacity} kg.")
        
        print(f"Moving lift from floor {self.current_floor} to floor {target_floor}...")
        time.sleep(1)  # Simulate lift movement time
        self.current_floor = target_floor
        print(f"Lift arrived at floor {target_floor}.")
    
    def status(self):
        """
        Prints the current status of the lift.
        """
        print(f"Current Floor: {self.current_floor}")
        print(f"Current Load: {self.load_weight} kg")
        print(f"Maximum Capacity: {self.max_weight_capacity} kg")
        print(f"Available Floors: {self.floors}")


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize lift system with 1000 kg capacity and floors 1 to 5
        lift = HydraulicLiftSystem(max_weight_capacity=1000, floors=[1, 2, 3, 4, 5])

        # Display initial status
        lift.status()

        # Load the lift with 800 kg
        lift.load(800)

        # Move to floor 3
        lift.move_to_floor(3)
        
        # Unload the lift
        lift.unload()

        # Move to floor 1
        lift.move_to_floor(1)

        # Display final status
        lift.status()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
