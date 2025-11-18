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

```python
import json
from typing import List, Dict, Any

class Robot:
    """Class representing a serving robot."""
    
    def __init__(self, robot_id: str, name: str, status: str = "available"):
        """Initialize a robot with an ID, name, and status."""
        self.robot_id = robot_id
        self.name = name
        self.status = status

    def update_status(self, new_status: str):
        """Update the current status of the robot."""
        valid_statuses = ["available", "busy", "charging", "maintenance"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are {valid_statuses}.")

    def to_dict(self) -> Dict[str, Any]:
        """Convert robot information to a dictionary for easy JSON serialization."""
        return {
            "robot_id": self.robot_id,
            "name": self.name,
            "status": self.status
        }


class FleetManager:
    """Class to manage a fleet of robots."""
    
    def __init__(self):
        """Initialize the fleet manager with an empty fleet."""
        self.robots: List[Robot] = []

    def add_robot(self, robot: Robot):
        """Add a new robot to the fleet."""
        self.robots.append(robot)

    def update_robot_status(self, robot_id: str, new_status: str):
        """Update the status of a robot by its ID."""
        for robot in self.robots:
            if robot.robot_id == robot_id:
                robot.update_status(new_status)
                return
        raise ValueError(f"Robot with ID {robot_id} not found.")

    def get_robot_info(self, robot_id: str) -> Dict[str, Any]:
        """Retrieve information about a specific robot."""
        for robot in self.robots:
            if robot.robot_id == robot_id:
                return robot.to_dict()
        raise ValueError(f"Robot with ID {robot_id} not found.")

    def save_fleet_to_file(self, filename: str):
        """Save the current fleet to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([robot.to_dict() for robot in self.robots], file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Error saving fleet to file: {e}")

    def load_fleet_from_file(self, filename: str):
        """Load a fleet from a JSON file."""
        try:
            with open(filename, 'r') as file:
                robots_data = json.load(file)
                self.robots = [Robot(**robot) for robot in robots_data]
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Error loading fleet from file: {e}")


# Example usage
if __name__ == "__main__":
    fleet_manager = FleetManager()

    # Add robots to the fleet
    fleet_manager.add_robot(Robot(robot_id="001", name="BellaBot"))
    fleet_manager.add_robot(Robot(robot_id="002", name="HolaBot"))

    # Update robot status
    fleet_manager.update_robot_status("001", "busy")

    # Retrieve robot information
    try:
        info = fleet_manager.get_robot_info("001")
        print("Robot Info:", info)
    except ValueError as e:
        print(e)

    # Save fleet to a file
    fleet_manager.save_fleet_to_file("fleet.json")

    # Load fleet from a file
    try:
        fleet_manager.load_fleet_from_file("fleet.json")
        print("Fleet loaded successfully.")
    except RuntimeError as e:
        print(e)
```
