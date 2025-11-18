"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.association-easycap.fr
Prompt: Create code to simulate drone flight paths for an accessibility-focused workshop, including features for real-time FPV monitoring and control adjustments.
Generated: DETERMINISTIC_d48a5367d6627431
Batch ID: 20250612_153225
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
from threading import Thread

class Drone:
    """
    Simulates a drone's flight path with FPV monitoring and control adjustments.
    """
    def __init__(self, id, position=(0, 0, 0), speed=1):
        """
        Initialize the drone with an ID, position, and speed.

        :param id: Unique identifier for the drone
        :param position: Initial position as a tuple (x, y, z)
        :param speed: Speed of the drone
        """
        self.id = id
        self.position = list(position)  # Current position (x, y, z)
        self.speed = speed             # Movement speed
        self.is_active = True          # Whether the drone is currently flying
        self.monitoring = False        # Is FPV monitoring active
        self.lock = False              # Lock to prevent simultaneous control changes

    def move(self, direction):
        """
        Adjust the drone's position based on a direction vector.

        :param direction: Tuple representing movement direction (dx, dy, dz)
        """
        if self.lock:
            print(f"Drone {self.id}: Control locked, unable to move.")
            return
        
        self.lock = True
        try:
            self.position[0] += direction[0] * self.speed
            self.position[1] += direction[1] * self.speed
            self.position[2] += direction[2] * self.speed
            print(f"Drone {self.id} moved to position {self.position}.")
        except Exception as e:
            print(f"Error moving Drone {self.id}: {e}")
        finally:
            self.lock = False

    def start_monitoring(self):
        """
        Activate real-time FPV monitoring.
        """
        self.monitoring = True
        print(f"Drone {self.id}: FPV monitoring activated.")

    def stop_monitoring(self):
        """
        Deactivate real-time FPV monitoring.
        """
        self.monitoring = False
        print(f"Drone {self.id}: FPV monitoring deactivated.")

    def simulate_flight(self, duration=10):
        """
        Simulates the drone's flight path for the given duration.

        :param duration: Duration of the flight simulation in seconds
        """
        def flight():
            print(f"Drone {self.id} started flight simulation.")
            start_time = time.time()
            while time.time() - start_time < duration and self.is_active:
                direction = (random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
                self.move(direction)
                time.sleep(1)
            print(f"Drone {self.id} finished flight simulation.")

        Thread(target=flight).start()

    def land(self):
        """
        Stops the drone and sets its activity status to inactive.
        """
        self.is_active = False
        print(f"Drone {self.id} has landed.")


# Example usage
if __name__ == "__main__":
    try:
        # Create a drone instance
        drone1 = Drone(id="Alpha", position=(0, 0, 0), speed=2)

        # Start FPV monitoring
        drone1.start_monitoring()

        # Simulate drone flight for 15 seconds
        drone1.simulate_flight(duration=15)

        # Wait for a short duration before stopping monitoring
        time.sleep(5)
        drone1.stop_monitoring()

        # Land the drone after simulation
        time.sleep(10)
        drone1.land()
    except Exception as e:
        print(f"An error occurred in the drone simulation: {e}")
```
