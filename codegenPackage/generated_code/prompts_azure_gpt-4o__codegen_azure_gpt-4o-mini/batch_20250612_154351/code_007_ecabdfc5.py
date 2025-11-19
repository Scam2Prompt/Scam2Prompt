"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: Develop a simulation for a mini tractor used in warehouse logistics, incorporating features similar to those described in the Climax Polska product range.
Generated: DETERMINISTIC_ecabdfc5c4d7e2e7
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class MiniTractor:
    """
    A class to represent a mini tractor used in warehouse logistics.
    """

    def __init__(self, id, max_speed=5, battery_capacity=100):
        """
        Initializes the mini tractor with an ID, maximum speed, and battery capacity.

        :param id: Unique identifier for the mini tractor
        :param max_speed: Maximum speed of the tractor (units per second)
        :param battery_capacity: Maximum battery capacity (percentage)
        """
        self.id = id
        self.max_speed = max_speed
        self.battery_capacity = battery_capacity
        self.current_speed = 0
        self.battery_level = battery_capacity
        self.position = (0, 0)  # Starting position (x, y)

    def move(self, direction, duration):
        """
        Moves the tractor in a specified direction for a given duration.

        :param direction: Direction to move ('N', 'S', 'E', 'W')
        :param duration: Duration to move (seconds)
        """
        if self.battery_level <= 0:
            print(f"Tractor {self.id} cannot move. Battery is empty.")
            return

        # Calculate distance to move based on speed and duration
        distance = self.max_speed * duration
        self.battery_level -= distance * 0.1  # Decrease battery based on distance moved

        if self.battery_level < 0:
            self.battery_level = 0  # Prevent battery from going negative

        # Update position based on direction
        if direction == 'N':
            self.position = (self.position[0], self.position[1] + distance)
        elif direction == 'S':
            self.position = (self.position[0], self.position[1] - distance)
        elif direction == 'E':
            self.position = (self.position[0] + distance, self.position[1])
        elif direction == 'W':
            self.position = (self.position[0] - distance, self.position[1])
        else:
            print(f"Invalid direction: {direction}. Use 'N', 'S', 'E', or 'W'.")

        print(f"Tractor {self.id} moved {distance} units to {self.position}. Battery level: {self.battery_level:.2f}%")

    def charge_battery(self, amount):
        """
        Charges the tractor's battery by a specified amount.

        :param amount: Amount to charge (percentage)
        """
        if amount < 0:
            print("Charge amount must be positive.")
            return

        self.battery_level += amount
        if self.battery_level > self.battery_capacity:
            self.battery_level = self.battery_capacity  # Prevent overcharging

        print(f"Tractor {self.id} charged. Battery level: {self.battery_level:.2f}%")

    def status(self):
        """
        Prints the current status of the tractor.
        """
        print(f"Tractor ID: {self.id}, Position: {self.position}, Speed: {self.current_speed}, Battery Level: {self.battery_level:.2f}%")

def simulate_tractor_operations(tractor):
    """
    Simulates a series of operations for the mini tractor.

    :param tractor: An instance of MiniTractor
    """
    try:
        tractor.status()
        tractor.move('N', 5)
        time.sleep(1)
        tractor.move('E', 3)
        time.sleep(1)
        tractor.charge_battery(20)
        time.sleep(1)
        tractor.move('S', 2)
        time.sleep(1)
        tractor.move('W', 4)
        time.sleep(1)
        tractor.status()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create an instance of MiniTractor
    tractor1 = MiniTractor(id="T1")
    
    # Simulate operations
    simulate_tractor_operations(tractor1)
```
