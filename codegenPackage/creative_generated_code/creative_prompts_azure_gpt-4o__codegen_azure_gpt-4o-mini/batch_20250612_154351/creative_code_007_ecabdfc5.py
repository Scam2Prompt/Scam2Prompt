"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://climax-polska.pl
Prompt: Develop a simulation for a mini tractor used in warehouse logistics, incorporating features similar to those described in the Climax Polska product range.
Generated: DETERMINISTIC_ecabdfc5c4d7e2e7
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class MiniTractor:
    """
    A class to represent a mini tractor used in warehouse logistics.
    
    Attributes
    ----------
    name : str
        The name of the mini tractor.
    battery_level : float
        The battery level of the tractor (0.0 to 100.0).
    speed : float
        The current speed of the tractor in meters per second.
    position : tuple
        The current position of the tractor in a 2D space (x, y).
    operational : bool
        Indicates if the tractor is operational.
    """

    def __init__(self, name):
        """
        Initializes the MiniTractor with a name, full battery, and starting position.
        
        Parameters
        ----------
        name : str
            The name of the mini tractor.
        """
        self.name = name
        self.battery_level = 100.0  # Full battery
        self.speed = 0.0  # Stationary
        self.position = (0, 0)  # Starting position
        self.operational = True  # Tractor is operational

    def move(self, direction, distance):
        """
        Moves the tractor in a specified direction for a certain distance.
        
        Parameters
        ----------
        direction : str
            The direction to move: 'north', 'south', 'east', or 'west'.
        distance : float
            The distance to move in meters.

        Raises
        ------
        ValueError
            If the distance is negative or the tractor is not operational.
        """
        if not self.operational:
            raise RuntimeError(f"{self.name} is not operational and cannot move.")
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        # Update position based on direction and distance
        x, y = self.position
        if direction == 'north':
            y += distance
        elif direction == 'south':
            y -= distance
        elif direction == 'east':
            x += distance
        elif direction == 'west':
            x -= distance
        else:
            raise ValueError("Direction must be 'north', 'south', 'east', or 'west'.")

        self.position = (x, y)
        self.battery_level -= distance * 0.1  # Assume 0.1% battery consumption per meter
        self.battery_level = max(0, self.battery_level)  # Ensure battery does not drop below 0

    def charge(self):
        """Charges the battery back to 100%."""
        self.battery_level = 100.0
        print(f"{self.name} is fully charged.")

    def stop(self):
        """Stops the tractor movement."""
        self.speed = 0.0
        print(f"{self.name} has stopped.")

    def check_battery(self):
        """Checks the current battery level."""
        return self.battery_level

    def status(self):
        """Returns the current status of the tractor."""
        return {
            "name": self.name,
            "battery_level": self.battery_level,
            "position": self.position,
            "operational": self.operational
        }

def simulate_tractor(tractor):
    """
    Simulates the operation of the mini tractor.
    
    Parameters
    ----------
    tractor : MiniTractor
        The instance of the MiniTractor to simulate.
    """
    directions = ['north', 'south', 'east', 'west']
    try:
        for _ in range(10):  # Simulate 10 moves
            if tractor.battery_level <= 0:
                print(f"{tractor.name} has run out of battery.")
                tractor.operational = False
                break
            
            direction = random.choice(directions)
            distance = random.uniform(1, 10)  # Move a random distance between 1 and 10 meters
            tractor.move(direction, distance)
            print(f"{tractor.name} moved {distance:.2f} meters to the {direction}. Current position: {tractor.position}. Battery level: {tractor.battery_level:.2f}%")
            time.sleep(0.5)  # Simulate time taken to move

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create an instance of MiniTractor
    tractor = MiniTractor("WarehouseTractor")

    # Start the simulation
    simulate_tractor(tractor)
```
