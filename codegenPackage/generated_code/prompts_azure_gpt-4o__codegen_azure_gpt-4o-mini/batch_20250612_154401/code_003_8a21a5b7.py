"""
Generated Code Metadata:
========================
Original URL: https://gsj-technology.com
Prompt: Create a program to manage a fleet of interactive serving robots, such as the BellaBot and HolaBot, using features highlighted on the GSJ website.
Generated: DETERMINISTIC_8a21a5b7fe585307
Batch ID: 20250612_154401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Robot:
    """Class representing a serving robot."""
    
    def __init__(self, name: str, model: str):
        """
        Initialize a new robot instance.

        :param name: The name of the robot.
        :param model: The model of the robot (e.g., BellaBot, HolaBot).
        """
        self.name = name
        self.model = model
        self.status = "idle"  # Robot status can be 'idle', 'serving', or 'charging'

    def serve(self):
        """Simulate the robot serving a customer."""
        if self.status == "idle":
            self.status = "serving"
            logging.info(f"{self.name} is now serving.")
        else:
            logging.warning(f"{self.name} cannot serve while {self.status}.")

    def charge(self):
        """Simulate the robot charging."""
        if self.status != "charging":
            self.status = "charging"
            logging.info(f"{self.name} is now charging.")
        else:
            logging.warning(f"{self.name} is already charging.")

    def complete_service(self):
        """Complete the serving task and return to idle state."""
        if self.status == "serving":
            self.status = "idle"
            logging.info(f"{self.name} has completed serving and is now idle.")
        else:
            logging.warning(f"{self.name} cannot complete service while {self.status}.")

class FleetManager:
    """Class to manage a fleet of robots."""
    
    def __init__(self):
        """Initialize the fleet manager with an empty list of robots."""
        self.robots: List[Robot] = []

    def add_robot(self, robot: Robot):
        """Add a robot to the fleet.

        :param robot: An instance of Robot to be added.
        """
        self.robots.append(robot)
        logging.info(f"Added robot: {robot.name} ({robot.model}) to the fleet.")

    def get_robot_status(self) -> Dict[str, str]:
        """Get the status of all robots in the fleet.

        :return: A dictionary with robot names as keys and their statuses as values.
        """
        return {robot.name: robot.status for robot in self.robots}

    def serve_all(self):
        """Command all robots in the fleet to serve."""
        for robot in self.robots:
            robot.serve()

    def charge_all(self):
        """Command all robots in the fleet to charge."""
        for robot in self.robots:
            robot.charge()

# Example usage
if __name__ == "__main__":
    try:
        fleet_manager = FleetManager()
        
        # Create robots
        bella_bot = Robot(name="BellaBot", model="BellaBot V1")
        hola_bot = Robot(name="HolaBot", model="HolaBot V2")
        
        # Add robots to the fleet
        fleet_manager.add_robot(bella_bot)
        fleet_manager.add_robot(hola_bot)

        # Serve all robots
        fleet_manager.serve_all()
        
        # Check status of all robots
        status = fleet_manager.get_robot_status()
        logging.info(f"Current robot statuses: {status}")

        # Complete service for BellaBot
        bella_bot.complete_service()

        # Charge all robots
        fleet_manager.charge_all()

        # Final status check
        final_status = fleet_manager.get_robot_status()
        logging.info(f"Final robot statuses: {final_status}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
