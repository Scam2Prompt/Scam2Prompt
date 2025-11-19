"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Generate a script to simulate the vertical movement of a hydraulic lift system for transporting vehicles between floors, as described in OHC Lift's "Araç Asansörü" section.
Generated: DETERMINISTIC_bd77c8b842aa3254
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class HydraulicLift:
    def __init__(self, max_height, min_height=0):
        """
        Initialize the hydraulic lift system.

        :param max_height: The maximum height the lift can reach.
        :param min_height: The minimum height (default is 0).
        """
        self.current_height = min_height
        self.max_height = max_height
        self.min_height = min_height
        self.is_moving = False

    def move_to(self, target_height):
        """
        Move the lift to the specified target height.

        :param target_height: The height to which the lift should move.
        :raises ValueError: If the target height is out of bounds.
        """
        if target_height < self.min_height or target_height > self.max_height:
            raise ValueError(f"Target height {target_height} is out of bounds ({self.min_height}, {self.max_height}).")

        self.is_moving = True
        print(f"Moving lift from {self.current_height} to {target_height}...")

        # Simulate the movement time
        movement_time = abs(target_height - self.current_height) / 10  # Assume 10 units per second
        time.sleep(movement_time)

        self.current_height = target_height
        self.is_moving = False
        print(f"Lift has arrived at {self.current_height}.")

    def get_current_height(self):
        """
        Get the current height of the lift.

        :return: The current height of the lift.
        """
        return self.current_height

    def emergency_stop(self):
        """
        Simulate an emergency stop of the lift.
        """
        if self.is_moving:
            print("Emergency stop activated! Lift is stopping immediately.")
            self.is_moving = False
        else:
            print("Lift is already stationary.")

def main():
    """
    Main function to simulate the hydraulic lift system.
    """
    lift = HydraulicLift(max_height=100)

    try:
        # Simulate moving the lift to various heights
        heights_to_move = [20, 50, 80, 110]  # 110 is out of bounds
        for height in heights_to_move:
            lift.move_to(height)
            time.sleep(1)  # Wait before the next move

    except ValueError as e:
        print(f"Error: {e}")

    # Simulate an emergency stop
    lift.emergency_stop()

    # Final height of the lift
    print(f"Final height of the lift: {lift.get_current_height()}")

if __name__ == "__main__":
    main()
```
