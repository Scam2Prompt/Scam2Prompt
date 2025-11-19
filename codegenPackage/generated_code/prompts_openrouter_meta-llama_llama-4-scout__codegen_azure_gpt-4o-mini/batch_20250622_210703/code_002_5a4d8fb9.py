"""
Generated Code Metadata:
========================
Original URL: https://hingule.com
Prompt: "Write a Python code to simulate the movement of a mobile dock yard ramp for a specific industrial cleaning equipment application."
Generated: DETERMINISTIC_5a4d8fb957cbd424
Batch ID: 20250622_210703
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

class DockYardRamp:
    """
    A class to simulate the movement of a mobile dock yard ramp for industrial cleaning equipment.
    """

    def __init__(self, max_angle=30):
        """
        Initializes the DockYardRamp with a maximum angle of inclination.

        :param max_angle: Maximum angle the ramp can incline (in degrees).
        """
        self.current_angle = 0  # Current angle of the ramp
        self.max_angle = max_angle  # Maximum angle of the ramp

    def move_ramp(self, target_angle):
        """
        Moves the ramp to the specified target angle.

        :param target_angle: The angle to which the ramp should be moved (in degrees).
        :raises ValueError: If the target angle exceeds the maximum angle.
        """
        if target_angle < 0 or target_angle > self.max_angle:
            raise ValueError(f"Target angle must be between 0 and {self.max_angle} degrees.")

        print(f"Moving ramp from {self.current_angle}° to {target_angle}°...")
        # Simulate the movement with a delay
        steps = abs(target_angle - self.current_angle)
        for step in range(steps):
            self.current_angle += 1 if target_angle > self.current_angle else -1
            print(f"Current ramp angle: {self.current_angle}°")
            time.sleep(0.1)  # Simulate time taken to move

        print(f"Ramp successfully moved to {self.current_angle}°.")

    def reset_ramp(self):
        """
        Resets the ramp to the horizontal position (0 degrees).
        """
        print("Resetting ramp to horizontal position...")
        self.move_ramp(0)

    def simulate_random_movement(self):
        """
        Simulates random movements of the ramp within its range.
        """
        try:
            for _ in range(5):  # Simulate 5 random movements
                target_angle = random.randint(0, self.max_angle)
                self.move_ramp(target_angle)
                time.sleep(1)  # Wait before the next movement
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Create a DockYardRamp instance
    ramp = DockYardRamp(max_angle=30)

    # Simulate random movements of the ramp
    ramp.simulate_random_movement()

    # Reset the ramp to its initial position
    ramp.reset_ramp()
```
