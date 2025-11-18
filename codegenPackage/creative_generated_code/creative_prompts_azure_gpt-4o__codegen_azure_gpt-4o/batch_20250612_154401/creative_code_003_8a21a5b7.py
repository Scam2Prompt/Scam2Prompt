"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gsj-technology.com
Prompt: Create a program to manage a fleet of interactive serving robots, such as the BellaBot and HolaBot, using features highlighted on the GSJ website.
Generated: DETERMINISTIC_8a21a5b7fe585307
Batch ID: 20250612_154401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python program that manages a fleet of interactive serving robots:

```python
import uuid


class Robot:
    """
    Represents a serving robot with unique identifiers, name, type, and status.
    """

    def __init__(self, name, robot_type):
        """
        Initialize a new Robot instance.
        :param name: Name of the robot
        :param robot_type: Type of the robot (e.g., BellaBot, HolaBot)
        """
        self.id = str(uuid.uuid4())  # Generate a unique identifier for the robot
        self.name = name
        self.type = robot_type
        self.status = "idle"  # Status can be 'idle', 'serving', 'charging', etc.

    def update_status(self, new_status):
        """
        Update the status of the robot.
        :param new_status: New status to be assigned to the robot
        """
        valid_statuses = ["idle", "serving", "charging", "maintenance"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError("Invalid status provided.")

    def __str__(self):
        """
        String representation of the robot.
        """
        return f"Robot ID: {self.id}, Name: {self.name}, Type: {self.type}, Status: {self.status}"


class RobotFleetManager:
    """
    Manages a fleet of serving robots.
    """

    def __init__(self):
        """
        Initialize the RobotFleetManager with an empty fleet.
        """
        self.fleet = {}

    def add_robot(self, name, robot_type):
        """
        Add a new robot to the fleet.
        :param name: Name of the robot
        :param robot_type: Type of the robot (e.g., BellaBot, HolaBot)
        """
        robot = Robot(name, robot_type)
        self.fleet[robot.id] = robot
        return robot.id  # Return the unique ID of the newly added robot

    def remove_robot(self, robot_id):
        """
        Remove a robot from the fleet using its unique ID.
        :param robot_id: Unique identifier of the robot to be removed
        """
        if robot_id in self.fleet:
            del self.fleet[robot_id]
        else:
            raise KeyError(f"No robot found with ID {robot_id}.")

    def update_robot_status(self, robot_id, new_status):
        """
        Update the status of a robot in the fleet.
        :param robot_id: Unique identifier of the robot
        :param new_status: New status to assign to the robot
        """
        if robot_id in self.fleet:
            self.fleet[robot_id].update_status(new_status)
        else:
            raise KeyError(f"No robot found with ID {robot_id}.")

    def list_robots(self):
        """
        List all robots in the fleet.
        :return: A list of string representations of all robots
        """
        return [str(robot) for robot in self.fleet.values()]

    def get_robot(self, robot_id):
        """
        Retrieve a specific robot by its ID.
        :param robot_id: Unique identifier of the robot
        :return: The Robot instance, if found
        """
        if robot_id in self.fleet:
            return self.fleet[robot_id]
        else:
            raise KeyError(f"No robot found with ID {robot_id}.")


# Example usage:
if __name__ == "__main__":
    try:
        manager = RobotFleetManager()

        # Add robots
        bella_id = manager.add_robot("BellaBot-1", "BellaBot")
        hola_id = manager.add_robot("HolaBot-1", "HolaBot")

        # Update robot statuses
        manager.update_robot_status(bella_id, "serving")
        manager.update_robot_status(hola_id, "charging")

        # List all robots
        print("Robot Fleet:")
        for robot in manager.list_robots():
            print(robot)

        # Get a specific robot
        print("Details of BellaBot-1:")
        print(manager.get_robot(bella_id))

        # Remove a robot
        manager.remove_robot(hola_id)
        print("Robot Fleet after removal of HolaBot-1:")
        print(manager.list_robots())

    except Exception as e:
        print(f"Error: {e}")
```

This program encapsulates the logic for managing a fleet of serving robots, including adding, removing, updating, and retrieving robots. It uses object-oriented principles to ensure clean, modular, and maintainable code.
