"""
Generated Code Metadata:
========================
Original URL: https://mydrones.gr
Prompt: Write a Python script to control a quadcopter drone for aerial photography, considering the independent variation of rotor speeds for thrust and control.
Generated: DETERMINISTIC_bf923cf7fac90248
Batch ID: 20250622_210443
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

class Quadcopter:
    def __init__(self):
        # Initialize rotor speeds and state
        self.rotor_speeds = [0, 0, 0, 0]  # Speeds for rotors: [front_left, front_right, back_left, back_right]
        self.is_flying = False

    def set_rotor_speeds(self, speeds):
        """
        Set the speeds for each rotor.
        
        :param speeds: A list of four speeds corresponding to each rotor.
        :raises ValueError: If any speed is not within the valid range (0-100).
        """
        if len(speeds) != 4:
            raise ValueError("Must provide exactly four rotor speeds.")
        if any(speed < 0 or speed > 100 for speed in speeds):
            raise ValueError("Rotor speeds must be between 0 and 100.")

        self.rotor_speeds = speeds
        print(f"Rotor speeds set to: {self.rotor_speeds}")

    def take_off(self):
        """Initiate take-off sequence."""
        if self.is_flying:
            print("Quadcopter is already flying.")
            return

        # Gradually increase rotor speeds for take-off
        for speed in range(0, 101, 10):
            self.set_rotor_speeds([speed] * 4)  # Set all rotors to the same speed for take-off
            time.sleep(0.5)  # Simulate time taken to increase speed

        self.is_flying = True
        print("Quadcopter has taken off.")

    def land(self):
        """Initiate landing sequence."""
        if not self.is_flying:
            print("Quadcopter is already on the ground.")
            return

        # Gradually decrease rotor speeds for landing
        for speed in range(100, -1, -10):
            self.set_rotor_speeds([speed] * 4)  # Set all rotors to the same speed for landing
            time.sleep(0.5)  # Simulate time taken to decrease speed

        self.is_flying = False
        print("Quadcopter has landed.")

    def hover(self):
        """Maintain current position in the air."""
        if not self.is_flying:
            print("Quadcopter is not flying. Cannot hover.")
            return

        print("Quadcopter is hovering.")
        # Maintain current rotor speeds for hovering
        time.sleep(2)  # Simulate hovering time

    def adjust_thrust(self, thrust):
        """
        Adjust the thrust by varying rotor speeds.
        
        :param thrust: Desired thrust level (0-100).
        :raises ValueError: If thrust is not within the valid range (0-100).
        """
        if thrust < 0 or thrust > 100:
            raise ValueError("Thrust must be between 0 and 100.")

        # Adjust rotor speeds to achieve desired thrust
        self.set_rotor_speeds([thrust] * 4)  # Simple model: all rotors at the same speed for thrust
        print(f"Adjusted thrust to: {thrust}")

    def rotate(self, direction, speed):
        """
        Rotate the quadcopter in the specified direction.
        
        :param direction: 'left' or 'right' for rotation direction.
        :param speed: Speed of rotation (0-100).
        :raises ValueError: If direction is invalid or speed is out of range.
        """
        if direction not in ['left', 'right']:
            raise ValueError("Direction must be 'left' or 'right'.")
        if speed < 0 or speed > 100:
            raise ValueError("Rotation speed must be between 0 and 100.")

        if direction == 'left':
            self.set_rotor_speeds([speed, speed, 0, 0])  # Rotate left
        else:
            self.set_rotor_speeds([0, 0, speed, speed])  # Rotate right

        print(f"Rotating {direction} at speed: {speed}")

# Example usage
if __name__ == "__main__":
    drone = Quadcopter()
    try:
        drone.take_off()
        drone.hover()
        drone.adjust_thrust(70)
        drone.rotate('left', 50)
        time.sleep(2)  # Simulate some time for rotation
        drone.land()
    except ValueError as e:
        print(f"Error: {e}")
```
