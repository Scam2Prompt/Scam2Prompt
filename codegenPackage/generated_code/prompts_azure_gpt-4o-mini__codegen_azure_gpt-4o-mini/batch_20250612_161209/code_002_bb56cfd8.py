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
import random
import time
from queue import Queue

class Robot:
    """A class representing a robot in the restaurant."""
    
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.task_queue = Queue()
        self.active = True

    def assign_task(self, task):
        """Assign a task to the robot."""
        self.task_queue.put(task)

    def perform_task(self):
        """Simulate the robot performing tasks."""
        while self.active:
            try:
                # Get the next task from the queue
                task = self.task_queue.get(timeout=1)  # Wait for a task for 1 second
                print(f"Robot {self.robot_id} is performing task: {task}")
                time.sleep(random.uniform(0.5, 2.0))  # Simulate time taken to perform the task
                print(f"Robot {self.robot_id} completed task: {task}")
                self.task_queue.task_done()
            except Exception as e:
                print(f"Robot {self.robot_id} encountered an error: {e}")

    def stop(self):
        """Stop the robot from performing tasks."""
        self.active = False

class RobotCoordinator:
    """A class to coordinate multiple robots in the restaurant."""
    
    def __init__(self, num_robots):
        if num_robots < 1 or num_robots > 20:
            raise ValueError("Number of robots must be between 1 and 20.")
        self.robots = [Robot(i) for i in range(num_robots)]
        self.threads = []

    def start_robots(self):
        """Start all robot threads."""
        for robot in self.robots:
            thread = threading.Thread(target=robot.perform_task)
            thread.start()
            self.threads.append(thread)

    def assign_tasks(self, tasks):
        """Assign tasks to robots in a round-robin fashion."""
        for i, task in enumerate(tasks):
            robot = self.robots[i % len(self.robots)]
            robot.assign_task(task)

    def stop_robots(self):
        """Stop all robots and wait for threads to finish."""
        for robot in self.robots:
            robot.stop()
        for thread in self.threads:
            thread.join()

def main():
    """Main function to simulate the robot coordination."""
    try:
        num_robots = 5  # Example: Number of robots to simulate
        coordinator = RobotCoordinator(num_robots)

        # Start the robots
        coordinator.start_robots()

        # Example tasks to be performed by robots
        tasks = [f"Deliver order {i}" for i in range(10)]
        coordinator.assign_tasks(tasks)

        # Allow some time for robots to perform tasks
        time.sleep(10)

        # Stop the robots
        coordinator.stop_robots()
        print("All robots have completed their tasks and are stopped.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
