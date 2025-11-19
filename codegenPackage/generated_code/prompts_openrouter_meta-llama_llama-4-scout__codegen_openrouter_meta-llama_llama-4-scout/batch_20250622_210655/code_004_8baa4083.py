"""
Generated Code Metadata:
========================
Original URL: https://farmboydrone.com
Prompt: How can drones be used for tasks such as crop spraying, planting, and soil analysis in farming?
Generated: DETERMINISTIC_8baa40833526da47
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
from typing import List, Dict

class Drone:
    def __init__(self, drone_id: str, drone_model: str):
        """
        Initialize a Drone object.

        Args:
        - drone_id (str): Unique identifier for the drone.
        - drone_model (str): Model of the drone.
        """
        self.drone_id = drone_id
        self.drone_model = drone_model
        self.tasks: List[str] = []

    def assign_task(self, task: str):
        """
        Assign a task to the drone.

        Args:
        - task (str): Task to be assigned (e.g., crop spraying, planting, soil analysis).
        """
        self.tasks.append(task)

    def __str__(self):
        return f"Drone {self.drone_id} ({self.drone_model}) - Tasks: {self.tasks}"


class Farm:
    def __init__(self, farm_name: str, farm_size: float):
        """
        Initialize a Farm object.

        Args:
        - farm_name (str): Name of the farm.
        - farm_size (float): Size of the farm in acres.
        """
        self.farm_name = farm_name
        self.farm_size = farm_size
        self.drones: Dict[str, Drone] = {}
        self.tasks: Dict[str, List[str]] = {"crop spraying": [], "planting": [], "soil analysis": []}

    def add_drone(self, drone: Drone):
        """
        Add a drone to the farm.

        Args:
        - drone (Drone): Drone object to be added.
        """
        self.drones[drone.drone_id] = drone

    def assign_drone_task(self, drone_id: str, task: str):
        """
        Assign a task to a drone.

        Args:
        - drone_id (str): ID of the drone.
        - task (str): Task to be assigned.

        Raises:
        - ValueError: If the drone does not exist or the task is invalid.
        """
        if drone_id not in self.drones:
            raise ValueError("Drone does not exist")
        if task not in self.tasks:
            raise ValueError("Invalid task")

        self.drones[drone_id].assign_task(task)
        self.tasks[task].append(drone_id)

    def __str__(self):
        farm_info = f"Farm {self.farm_name} ({self.farm_size} acres)\n"
        drone_info = "\n".join([str(drone) for drone in self.drones.values()])
        task_info = "\nTasks:\n" + "\n".join([f"{task}: {drones}" for task, drones in self.tasks.items()])
        return farm_info + drone_info + task_info


def main():
    try:
        # Create a farm
        farm = Farm("Green Farm", 100.0)

        # Create drones
        drone1 = Drone("D1", "DroneX")
        drone2 = Drone("D2", "DroneY")

        # Add drones to the farm
        farm.add_drone(drone1)
        farm.add_drone(drone2)

        # Assign tasks to drones
        farm.assign_drone_task("D1", "crop spraying")
        farm.assign_drone_task("D2", "planting")
        farm.assign_drone_task("D1", "soil analysis")

        # Print farm information
        print(farm)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
