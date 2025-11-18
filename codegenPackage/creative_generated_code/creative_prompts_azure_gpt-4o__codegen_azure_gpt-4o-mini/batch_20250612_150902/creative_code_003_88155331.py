"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taxltg.com
Prompt: Write code to model the movement of a KP电缆卷筒供电平车, including cable reel dynamics and collision avoidance logic.
Generated: DETERMINISTIC_88155331c540f220
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import random

class CableReel:
    """Model representing a cable reel with position and rotation."""
    
    def __init__(self, position=(0, 0), radius=1.0):
        self.position = position  # Position (x, y)
        self.radius = radius      # Radius of the cable reel
        self.angle = 0            # Current angle of the cable reel in degrees

    def rotate(self, degrees):
        """Rotate the reel by a certain degree."""
        self.angle = (self.angle + degrees) % 360

    def get_end_position(self):
        """Calculate the end position of the cable based on current angle."""
        x = self.position[0] + self.radius * math.cos(math.radians(self.angle))
        y = self.position[1] + self.radius * math.sin(math.radians(self.angle))
        return (x, y)


class Vehicle:
    """Model representing the KP电缆卷筒供电平车."""
    
    def __init__(self, position=(0, 0), speed=0.0):
        self.position = position  # Current position of the vehicle (x, y)
        self.speed = speed        # Speed of the vehicle

    def move(self, delta_time):
        """Move the vehicle based on speed and time."""
        new_x = self.position[0] + self.speed * delta_time
        self.position = (new_x, self.position[1])

    def set_speed(self, speed):
        """Set the vehicle speed."""
        if speed < 0:
            raise ValueError("Speed cannot be negative.")
        self.speed = speed


class Environment:
    """Model the environment where the vehicle operates, including collision avoidance."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []  # List of obstacles represented as rectangles

    def add_obstacle(self, x, y, width, height):
        """Add an obstacle to the environment."""
        self.obstacles.append((x, y, width, height))

    def check_collision(self, vehicle_position):
        """Check for collision with obstacles."""
        for (obstacle_x, obstacle_y, obstacle_w, obstacle_h) in self.obstacles:
            if obstacle_x <= vehicle_position[0] <= obstacle_x + obstacle_w and \
               obstacle_y <= vehicle_position[1] <= obstacle_y + obstacle_h:
                return True  # Collision detected
        return False


def main():
    """Main function to simulate the vehicle and cable reel movement."""
    try:
        # Initialize environment
        env = Environment(width=100, height=100)
        env.add_obstacle(40, 40, 10, 10)  # Add an obstacle

        # Initialize the cable reel and vehicle
        reel = CableReel(position=(5, 5), radius=2.0)
        vehicle = Vehicle(position=(0, 0), speed=1.0)

        # Simulation parameters
        simulation_time = 50  # Total time for simulation
        delta_time = 1        # Time step in seconds

        for _ in range(simulation_time):
            # Update vehicle position
            vehicle.move(delta_time)
            print(f'Vehicle Position: {vehicle.position}')

            # Check for collisions
            if env.check_collision(vehicle.position):
                print("Collision detected! Stopping the vehicle.")
                vehicle.set_speed(0)
                break

            # Rotate the cable reel
            reel.rotate(10)  # Rotate 10 degrees
            print(f'Cable Reel End Position: {reel.get_end_position()}')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')


if __name__ == "__main__":
    main()
```
