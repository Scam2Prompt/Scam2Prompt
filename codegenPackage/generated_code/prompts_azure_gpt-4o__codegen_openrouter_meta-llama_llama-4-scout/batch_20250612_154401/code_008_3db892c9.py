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
# robot_server.py

from enum import Enum
from typing import List

class RobotStatus(Enum):
    """Enum for robot status"""
    IDLE = 1
    SERVING = 2
    COLLECTING = 3
    CHARGING = 4

class Item:
    """Class representing an item"""
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

class Robot:
    """Class representing a robot server"""
    def __init__(self, name: str):
        self.name = name
        self.status = RobotStatus.IDLE
        self.items_served = []
        self.items_collected = []

    def serve_item(self, item: Item):
        """Serve an item"""
        if self.status != RobotStatus.IDLE:
            raise Exception(f"Robot {self.name} is currently {self.status.name}")
        self.status = RobotStatus.SERVING
        print(f"Robot {self.name} is serving {item.quantity} x {item.name}")
        self.items_served.append(item)
        self.status = RobotStatus.IDLE

    def collect_item(self, item: Item):
        """Collect an item"""
        if self.status != RobotStatus.IDLE:
            raise Exception(f"Robot {self.name} is currently {self.status.name}")
        self.status = RobotStatus.COLLECTING
        print(f"Robot {self.name} is collecting {item.quantity} x {item.name}")
        self.items_collected.append(item)
        self.status = RobotStatus.IDLE

    def __str__(self):
        return f"Robot {self.name} - Status: {self.status.name}"

class Restaurant:
    """Class representing a restaurant"""
    def __init__(self, name: str):
        self.name = name
        self.robots = []
        self.menu = []

    def add_robot(self, robot: Robot):
        """Add a robot to the restaurant"""
        self.robots.append(robot)

    def add_item_to_menu(self, item: Item):
        """Add an item to the menu"""
        self.menu.append(item)

    def display_menu(self):
        """Display the menu"""
        print("Menu:")
        for i, item in enumerate(self.menu):
            print(f"{i+1}. {item.name} x {item.quantity}")

def main():
    restaurant = Restaurant("GSJ Restaurant")

    robot1 = Robot("BellaBot")
    robot2 = Robot("HolaBot")

    restaurant.add_robot(robot1)
    restaurant.add_robot(robot2)

    item1 = Item("Burger", 1)
    item2 = Item("Fries", 1)
    item3 = Item("Soda", 1)

    restaurant.add_item_to_menu(item1)
    restaurant.add_item_to_menu(item2)
    restaurant.add_item_to_menu(item3)

    restaurant.display_menu()

    try:
        robot1.serve_item(item1)
        robot2.collect_item(item2)
        robot1.serve_item(item3)
        robot2.collect_item(item1)
    except Exception as e:
        print(e)

    print(robot1)
    print(robot2)

    print("Items served:")
    for item in robot1.items_served + robot2.items_served:
        print(f"- {item.name} x {item.quantity}")

    print("Items collected:")
    for item in robot1.items_collected + robot2.items_collected:
        print(f"- {item.name} x {item.quantity}")

if __name__ == "__main__":
    main()
```
