"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pudurobot.id
Prompt: Generate a code snippet that simulates the multi-robot coordination feature of BellaBot, allowing up to 20 robots to operate simultaneously in a restaurant setting.
Generated: DETERMINISTIC_bb56cfd8726dd0c1
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
import random
import time
from typing import List

class Robot:
    """
    A class to represent a robot in the restaurant.

    Attributes:
        id (int): The unique identifier for the robot.
        location (tuple): The current location of the robot in the restaurant.
    """

    def __init__(self, robot_id: int):
        self.id = robot_id
        self.location = (0, 0)  # Start at the origin
        self.lock = threading.Lock()

    def move_to(self, new_location: tuple):
        """
        Move the robot to a new location.

        Args:
            new_location (tuple): The coordinates to move to.
        """
        with self.lock:
            print(f"Robot {self.id} moving from {self.location} to {new_location}")
            time.sleep(random.uniform(0.5, 1.5))  # Simulate movement time
            self.location = new_location
            print(f"Robot {self.id} arrived at {self.location}")

    def serve(self, order_id: int):
        """
        Simulate serving an order.

        Args:
            order_id (int): The ID of the order to be served.
        """
        with self.lock:
            print(f"Robot {self.id} serving order {order_id} at {self.location}")
            time.sleep(random.uniform(0.5, 1.5))  # Simulate serving time
            print(f"Robot {self.id} finished serving order {order_id}")

class Restaurant:
    """
    A class to represent a restaurant with multiple robots.

    Attributes:
        robots (List[Robot]): A list of robots in the restaurant.
    """

    def __init__(self):
        self.robots = [Robot(i) for i in range(20)]  # Create 20 robots

    def coordinate_robots(self, orders: List[int]):
        """
        Coordinate robots to serve orders.

        Args:
            orders (List[int]): A list of order IDs to be served.
        """
        threads = []
        for order_id in orders:
            # Randomly select a robot to serve the order
            robot = random.choice(self.robots)
            new_location = (random.randint(1, 10), random.randint(1, 10))  # Random destination
            threads.append(threading.Thread(target=self.assign_task, args=(robot, new_location, order_id)))

        # Start all threads
        for thread in threads:
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    def assign_task(self, robot: Robot, location: tuple, order_id: int):
        """
        Assign a task to a robot to move and serve an order.

        Args:
            robot (Robot): The robot assigned to the task.
            location (tuple): The destination location for the robot.
            order_id (int): The ID of the order to be served.
        """
        robot.move_to(location)
        robot.serve(order_id)

if __name__ == "__main__":
    # Simulate the restaurant operations
    restaurant = Restaurant()
    orders_to_serve = [i for i in range(30)]  # Simulate 30 orders
    restaurant.coordinate_robots(orders_to_serve)
```
