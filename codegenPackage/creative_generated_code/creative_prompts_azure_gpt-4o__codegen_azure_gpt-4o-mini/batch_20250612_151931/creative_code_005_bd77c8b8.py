"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: Generate a script to simulate the vertical movement of a hydraulic lift system for transporting vehicles between floors, as described in OHC Lift's "Araç Asansörü" section.
Generated: DETERMINISTIC_bd77c8b842aa3254
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class HydraulicLift:
    def __init__(self, max_height: int, min_height: int = 0):
        """
        Initialize the hydraulic lift system.

        :param max_height: Maximum height the lift can reach in meters.
        :param min_height: Minimum height the lift can go (default is ground level).
        """
        self.current_height = min_height
        self.max_height = max_height
        self.min_height = min_height
        self.is_moving = False

    def move_up(self, distance: int):
        """
        Move the lift up by a specified distance.

        :param distance: Distance to move up in meters. Must be positive.
        :raises ValueError: If the distance is negative or if it exceeds max height.
        """
        if distance < 0:
            raise ValueError("Distance must be a positive number.")
        if self.current_height + distance > self.max_height:
            raise ValueError("Cannot move up beyond maximum height.")
        
        self.is_moving = True
        print(f"Moving up {distance} meters...")
        time.sleep(random.uniform(1, 3))  # Simulate time taken to move
        self.current_height += distance
        print(f"Lift reached height: {self.current_height} meters.")
        self.is_moving = False

    def move_down(self, distance: int):
        """
        Move the lift down by a specified distance.

        :param distance: Distance to move down in meters. Must be positive.
        :raises ValueError: If the distance is negative or if it goes below min height.
        """
        if distance < 0:
            raise ValueError("Distance must be a positive number.")
        if self.current_height - distance < self.min_height:
            raise ValueError("Cannot move down below minimum height.")

        self.is_moving = True
        print(f"Moving down {distance} meters...")
        time.sleep(random.uniform(1, 3))  # Simulate time taken to move
        self.current_height -= distance
        print(f"Lift reached height: {self.current_height} meters.")
        self.is_moving = False

    def get_current_height(self) -> int:
        """
        Get the current height of the lift.

        :return: The current height of the lift in meters.
        """
        return self.current_height

def main():
    """
    Main function to simulate the hydraulic lift.
    """
    # Initialize the lift with a maximum height of 10 meters
    lift = HydraulicLift(max_height=10)

    try:
        lift.move_up(5)  # Move up to 5 meters
        lift.move_down(3)  # Move down to 2 meters
        lift.move_up(8)  # Attempt to move up beyond max height (should raise an error)
    except ValueError as e:
        print(f"Error: {e}")

    print(f"Final height of the lift: {lift.get_current_height()} meters.")

if __name__ == "__main__":
    main()
```
