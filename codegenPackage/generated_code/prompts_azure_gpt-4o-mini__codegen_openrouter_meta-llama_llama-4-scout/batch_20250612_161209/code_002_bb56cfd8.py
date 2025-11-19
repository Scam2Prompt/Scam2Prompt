"""
Generated Code Metadata:
========================
Original URL: https://pudurobot.id
Prompt: Generate a code snippet that simulates the multi-robot coordination feature of BellaBot, allowing up to 20 robots to operate simultaneously in a restaurant setting.
Generated: DETERMINISTIC_bb56cfd8726dd0c1
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
import time
import random

# Constants
MAX_ROBOTS = 20
RESTAURANT_AREA = "Restaurant"

class Robot:
    """Represents a robot in the restaurant setting."""
    
    def __init__(self, name):
        """Initializes a robot with a given name."""
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the robot's task list."""
        self.tasks.append(task)

    def run(self):
        """Runs the robot, executing its tasks."""
        print(f"{self.name} started.")
        for task in self.tasks:
            print(f"{self.name} is executing task: {task}")
            time.sleep(random.uniform(1, 3))  # Simulate task execution time
        print(f"{self.name} finished.")

class BellaBotCoordinator:
    """Coordinates multiple robots in a restaurant setting."""
    
    def __init__(self):
        """Initializes the coordinator with an empty list of robots."""
        self.robots = []

    def add_robot(self, robot):
        """Adds a robot to the coordinator's list of robots."""
        if len(self.robots) < MAX_ROBOTS:
            self.robots.append(robot)
        else:
            raise Exception("Maximum number of robots reached.")

    def start_robots(self):
        """Starts all robots, executing their tasks concurrently."""
        threads = []
        for robot in self.robots:
            thread = threading.Thread(target=robot.run)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

def main():
    coordinator = BellaBotCoordinator()

    # Create robots
    for i in range(10):
        robot = Robot(f"Robot {i+1}")
        robot.add_task("Delivering food to table 1")
        robot.add_task("Picking up dirty dishes from table 2")
        coordinator.add_robot(robot)

    # Start robots
    coordinator.start_robots()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
