"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: "Write a Python code snippet to implement a simple robotics simulation for a school project, incorporating STEAM principles, as described on the Del Sol Montessori website."
Generated: DETERMINISTIC_28f6daa0655ee01b
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class Robot:
    """
    A simple Robot class to simulate movement and sensor data.
    Incorporates STEAM principles by combining Science, Technology, Engineering, Art, and Math.
    """

    def __init__(self, name, x=0, y=0):
        """
        Initialize the robot with a name and starting position.
        :param name: Name of the robot
        :param x: Initial x-coordinate (default: 0)
        :param y: Initial y-coordinate (default: 0)
        """
        self.name = name
        self.x = x
        self.y = y
        self.angle = 0  # Angle in degrees, 0 means facing "east"

    def move_forward(self, distance):
        """
        Move the robot forward by a specified distance.
        :param distance: Distance to move forward
        """
        try:
            if distance < 0:
                raise ValueError("Distance must be a positive value.")
            # Update position based on current angle
            self.x += distance * math.cos(math.radians(self.angle))
            self.y += distance * math.sin(math.radians(self.angle))
        except ValueError as e:
            print(f"Error: {e}")

    def rotate(self, degrees):
        """
        Rotate the robot by a specified number of degrees.
        :param degrees: Degrees to rotate (positive for clockwise, negative for counterclockwise)
        """
        self.angle = (self.angle + degrees) % 360

    def get_position(self):
        """
        Get the current position of the robot.
        :return: Tuple (x, y) representing the robot's position
        """
        return round(self.x, 2), round(self.y, 2)

    def get_angle(self):
        """
        Get the current angle of the robot.
        :return: Angle in degrees
        """
        return self.angle

    def simulate_sensor(self):
        """
        Simulate a basic sensor that detects obstacles within a certain range.
        :return: Randomized sensor data (for simplicity, returns True/False)
        """
        import random
        return random.choice([True, False])  # True means obstacle detected, False means clear

# Example usage
if __name__ == "__main__":
    # Create a robot instance
    robot = Robot(name="STEAMBot")

    # Move the robot forward
    robot.move_forward(10)
    print(f"Position after moving forward: {robot.get_position()}")

    # Rotate the robot
    robot.rotate(90)
    print(f"Angle after rotation: {robot.get_angle()}")

    # Move the robot forward again
    robot.move_forward(5)
    print(f"Position after second move: {robot.get_position()}")

    # Simulate sensor data
    obstacle_detected = robot.simulate_sensor()
    print(f"Obstacle detected: {obstacle_detected}")
```
