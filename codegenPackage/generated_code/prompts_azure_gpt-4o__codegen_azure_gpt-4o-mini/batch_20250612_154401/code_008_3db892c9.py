"""
Generated Code Metadata:
========================
Original URL: https://gsj-technology.com
Prompt: Create a simulation of a robot serving and collecting items in a restaurant, inspired by the functionalities of BellaBot and HolaBot described on the GSJ website.
Generated: DETERMINISTIC_3db892c9d285450b
Batch ID: 20250612_154401
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
from enum import Enum

class Item(Enum):
    FOOD = "Food"
    DRINK = "Drink"
    DESSERT = "Dessert"

class RobotState(Enum):
    IDLE = "Idle"
    SERVING = "Serving"
    COLLECTING = "Collecting"

class Robot:
    def __init__(self, name):
        """Initialize the robot with a name and set its initial state."""
        self.name = name
        self.state = RobotState.IDLE
        self.items_served = []
        self.items_collected = []

    def serve_item(self, item):
        """Simulate serving an item to a customer."""
        if self.state != RobotState.IDLE:
            raise RuntimeError(f"{self.name} is busy and cannot serve items.")
        
        self.state = RobotState.SERVING
        print(f"{self.name} is serving {item.value}.")
        time.sleep(random.uniform(1, 3))  # Simulate time taken to serve
        self.items_served.append(item)
        print(f"{self.name} has served {item.value}.")
        self.state = RobotState.IDLE

    def collect_item(self, item):
        """Simulate collecting an item from a customer."""
        if self.state != RobotState.IDLE:
            raise RuntimeError(f"{self.name} is busy and cannot collect items.")
        
        self.state = RobotState.COLLECTING
        print(f"{self.name} is collecting {item.value}.")
        time.sleep(random.uniform(1, 3))  # Simulate time taken to collect
        self.items_collected.append(item)
        print(f"{self.name} has collected {item.value}.")
        self.state = RobotState.IDLE

    def report_status(self):
        """Report the current status of the robot."""
        print(f"{self.name} Status:")
        print(f"  State: {self.state.value}")
        print(f"  Items Served: {[item.value for item in self.items_served]}")
        print(f"  Items Collected: {[item.value for item in self.items_collected]}")

def main():
    """Main function to simulate the robot's operation in a restaurant."""
    robot = Robot("BellaBot")

    try:
        # Simulate serving and collecting items
        robot.serve_item(Item.FOOD)
        robot.collect_item(Item.DRINK)
        robot.serve_item(Item.DESSERT)
        robot.collect_item(Item.FOOD)
        
        # Report the robot's status
        robot.report_status()
        
    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
