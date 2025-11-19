"""
Generated Code Metadata:
========================
Original URL: https://pudurobot.id
Prompt: "Generate a code example for coordinating multiple delivery robots, like BellaBot, to optimize food delivery in a large restaurant or hotel setting."
Generated: DETERMINISTIC_09b5ef138086bad1
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# delivery_robot_coordinator.py

import threading
import time
from typing import List, Dict

class DeliveryRobot:
    """Represents a delivery robot like BellaBot."""

    def __init__(self, robot_id: str, location: str):
        """
        Initializes a DeliveryRobot instance.

        Args:
        - robot_id (str): Unique identifier for the robot.
        - location (str): Current location of the robot.
        """
        self.robot_id = robot_id
        self.location = location
        self.assigned_task = None
        self.lock = threading.Lock()

    def assign_task(self, task: str):
        """Assigns a delivery task to the robot."""
        with self.lock:
            self.assigned_task = task

    def update_location(self, location: str):
        """Updates the current location of the robot."""
        with self.lock:
            self.location = location

    def __str__(self):
        return f"Robot {self.robot_id} at {self.location} with task {self.assigned_task}"


class DeliveryCoordinator:
    """Coordinates multiple delivery robots for efficient food delivery."""

    def __init__(self):
        """
        Initializes a DeliveryCoordinator instance.

        Attributes:
        - robots (Dict[str, DeliveryRobot]): Mapping of robot IDs to DeliveryRobot instances.
        - tasks (List[str]): List of pending delivery tasks.
        """
        self.robots = {}
        self.tasks = []
        self.lock = threading.Lock()

    def add_robot(self, robot: DeliveryRobot):
        """Registers a delivery robot with the coordinator."""
        with self.lock:
            self.robots[robot.robot_id] = robot

    def add_task(self, task: str):
        """Adds a new delivery task to the coordinator."""
        with self.lock:
            self.tasks.append(task)

    def assign_tasks(self):
        """Assigns pending tasks to available robots."""
        with self.lock:
            available_robots = [robot for robot in self.robots.values() if robot.assigned_task is None]
            for task in self.tasks[:]:
                if available_robots:
                    robot = available_robots.pop(0)
                    robot.assign_task(task)
                    self.tasks.remove(task)
                else:
                    break

    def update_robot_location(self, robot_id: str, location: str):
        """Updates the location of a registered robot."""
        with self.lock:
            if robot_id in self.robots:
                self.robots[robot_id].update_location(location)

    def __str__(self):
        robot_status = "\n".join([str(robot) for robot in self.robots.values()])
        return f"Delivery Coordinator:\n{robot_status}\nPending Tasks: {self.tasks}"


def simulate_delivery(coordinator: DeliveryCoordinator, robot_id: str):
    """Simulates the delivery process for a robot."""
    robot = coordinator.robots[robot_id]
    while True:
        if robot.assigned_task:
            print(f"Robot {robot_id} is delivering {robot.assigned_task}")
            time.sleep(2)  # Simulate delivery time
            robot.assign_task(None)
            print(f"Robot {robot_id} has completed delivery")
        time.sleep(1)  # Check for new tasks


def main():
    coordinator = DeliveryCoordinator()

    # Create and register robots
    robot1 = DeliveryRobot("BellaBot1", "Kitchen")
    robot2 = DeliveryRobot("BellaBot2", "Lobby")
    coordinator.add_robot(robot1)
    coordinator.add_robot(robot2)

    # Add delivery tasks
    coordinator.add_task("Food to Room 101")
    coordinator.add_task("Food to Room 202")
    coordinator.add_task("Food to Conference Room")

    # Assign tasks to robots
    coordinator.assign_tasks()

    # Start simulating delivery process
    threads = []
    for robot_id in coordinator.robots:
        thread = threading.Thread(target=simulate_delivery, args=(coordinator, robot_id))
        thread.start()
        threads.append(thread)

    try:
        while True:
            print(coordinator)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nCoordinator stopped")


if __name__ == "__main__":
    main()
```
