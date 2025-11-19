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
import time
import random

# Constants
MAX_ROBOTS = 20
RESTAURANT_SECTIONS = ['Kitchen', 'Dining Area', 'Reception', 'Storage']

# Robot class to simulate BellaBot functionality
class BellaBot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.current_task = None
        self.current_location = 'Docking Station'

    def assign_task(self, task, location):
        """
        Assign a new task to the robot.
        :param task: The name of the task to perform.
        :param location: The location to execute the task.
        """
        self.current_task = task
        self.current_location = location

    def execute_task(self):
        """
        Simulate task execution by the robot.
        """
        if self.current_task:
            print(f"Robot {self.robot_id} is executing '{self.current_task}' at {self.current_location}.")
            time.sleep(random.uniform(1, 3))  # Simulate variable task duration
            print(f"Robot {self.robot_id} completed '{self.current_task}' at {self.current_location}.")
            self.current_task = None
            self.current_location = 'Docking Station'
        else:
            print(f"Robot {self.robot_id} is idle at {self.current_location}.")

# Function to simulate robot coordination
def simulate_robot_operations():
    """
    Simulates the coordination of multiple BellaBot robots in a restaurant setting.
    """
    robots = [BellaBot(robot_id=i + 1) for i in range(MAX_ROBOTS)]

    def robot_worker(robot):
        """
        Worker thread for each robot to simulate its operation.
        """
        while True:
            if random.random() > 0.2:  # 80% chance to assign a new task
                task = random.choice(['Serve Food', 'Collect Plates', 'Guide Customer', 'Deliver Supplies'])
                location = random.choice(RESTAURANT_SECTIONS)
                robot.assign_task(task, location)
                robot.execute_task()
            else:
                robot.execute_task()
            time.sleep(random.uniform(0.5, 2))  # Simulate idle time

    # Create and start threads for each robot
    threads = []
    for robot in robots:
        t = threading.Thread(target=robot_worker, args=(robot,))
        t.daemon = True  # Ensure threads exit when main program exits
        threads.append(t)
        t.start()

    # Allow the simulation to run for a fixed duration
    try:
        time.sleep(30)  # Run simulation for 30 seconds
    except KeyboardInterrupt:
        print("Simulation interrupted by user.")

# Main entry point
if __name__ == "__main__":
    print("Starting multi-robot coordination simulation...")
    simulate_robot_operations()
    print("Simulation ended.")
```

This Python script simulates up to 20 BellaBot robots coordinating tasks in a restaurant setting, using threads for parallel operations. It follows clean coding practices, is well-documented, and includes error handling for interruptions.
