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
class HydraulicLift:
    def __init__(self, max_load_capacity, current_floor=0):
        """
        Initializes the hydraulic lift system.
        
        :param max_load_capacity: The maximum load capacity of the lift in kilograms.
        :param current_floor: The current floor the lift is on (default is 0).
        """
        self.max_load_capacity = max_load_capacity
        self.current_floor = current_floor
        self.load_weight = 0
        self.is_moving = False

    def load(self, weight):
        """
        Loads the specified weight into the lift.
        
        :param weight: The weight to load in kilograms.
        :raises ValueError: If the weight exceeds the maximum load capacity.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive value.")
        if self.load_weight + weight > self.max_load_capacity:
            raise ValueError("Exceeds maximum load capacity!")
        self.load_weight += weight
        print(f"Loaded {weight} kg. Current load: {self.load_weight} kg.")

    def unload(self):
        """
        Unloads the current load from the lift.
        """
        print(f"Unloading {self.load_weight} kg from the lift.")
        self.load_weight = 0

    def move_to_floor(self, target_floor):
        """
        Moves the lift to the specified floor if it is not already in transit.
        
        :param target_floor: The floor to move to.
        :raises ValueError: If the lift is currently moving or if the target floor is invalid.
        """
        if self.is_moving:
            raise ValueError("Lift is currently in motion. Wait for it to stop.")
        if target_floor < 0:
            raise ValueError("Invalid floor: Floor number cannot be negative.")
        
        self.is_moving = True
        print(f"Moving from floor {self.current_floor} to floor {target_floor}...")
        
        # Simulate the movement with a sleep (delay)
        import time
        time.sleep(2)  # Simulate the time taken to move between floors
        
        self.current_floor = target_floor
        self.is_moving = False
        print(f"Arrived at floor {self.current_floor}.")

    def status(self):
        """
        Prints the current status of the lift.
        """
        print(f"Current floor: {self.current_floor}, Load: {self.load_weight}/{self.max_load_capacity} kg")


# Example usage of the HydraulicLift class
if __name__ == "__main__":
    try:
        lift = HydraulicLift(max_load_capacity=1000)
        lift.load(500)
        lift.status()
        lift.move_to_floor(3)
        lift.unload()
        lift.status()
    except Exception as e:
        print(f"An error occurred: {e}")
```
