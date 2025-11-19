"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://farmboydrone.com
Prompt: What are the best practices for integrating drone technology in agricultural settings?
Generated: DETERMINISTIC_fb3c9ebe8ea7da59
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import json
import time
from typing import List, Dict

# Configure logging for better debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Drone:
    """
    A class to represent a Drone for agricultural purposes.
    """

    def __init__(self, drone_id: str, battery_capacity: int):
        """
        Initializes a new Drone instance.

        :param drone_id: Unique identifier for the drone
        :param battery_capacity: Maximum battery capacity in percentage (0-100)
        """
        self.drone_id = drone_id
        self.battery_capacity = battery_capacity
        self.current_battery_level = battery_capacity
        self.is_flying = False

    def fly(self, duration: int) -> None:
        """
        Simulates flying the drone for a specified duration.

        :param duration: Duration of the flight in minutes
        :raises ValueError: If the duration is negative or if the battery is insufficient
        """
        if duration < 0:
            raise ValueError("Flight duration cannot be negative.")
        
        battery_consumption = duration * 10  # Assume 10% battery consumed per minute
        if battery_consumption > self.current_battery_level:
            raise RuntimeError("Insufficient battery for the requested flight duration.")
        
        logging.info(f"Drone {self.drone_id} is flying for {duration} minutes.")
        self.current_battery_level -= battery_consumption
        self.is_flying = True
        time.sleep(duration)  # Simulate flight time
        self.is_flying = False
        logging.info(f"Drone {self.drone_id} has completed its flight.")

    def land(self) -> None:
        """Simulates landing the drone."""
        if self.is_flying:
            logging.info(f"Drone {self.drone_id} is landing.")
            self.is_flying = False
        else:
            logging.warning(f"Drone {self.drone_id} is already on the ground.")

    def recharge(self) -> None:
        """Recharges the drone's battery to full capacity."""
        logging.info(f"Drone {self.drone_id} is recharging.")
        self.current_battery_level = self.battery_capacity
        logging.info(f"Drone {self.drone_id} is fully recharged.")

    def get_status(self) -> Dict[str, str]:
        """Returns the current status of the drone."""
        return {
            "drone_id": self.drone_id,
            "current_battery_level": self.current_battery_level,
            "is_flying": self.is_flying
        }


class FarmManagementSystem:
    """
    A system to manage drones in an agricultural setting.
    """

    def __init__(self):
        """Initializes the farm management system."""
        self.drones: List[Drone] = []

    def add_drone(self, drone: Drone) -> None:
        """
        Adds a new drone to the system.

        :param drone: An instance of the Drone class
        """
        self.drones.append(drone)
        logging.info(f"Drone {drone.drone_id} added to the system.")

    def perform_flight(self, drone_id: str, duration: int) -> None:
        """
        Commands a drone to perform a flight.

        :param drone_id: The ID of the drone to fly
        :param duration: Duration of the flight in minutes
        """
        drone = self._find_drone(drone_id)
        if drone:
            try:
                drone.fly(duration)
            except (ValueError, RuntimeError) as e:
                logging.error(f"Error during flight: {e}")
        else:
            logging.error(f"Drone with ID {drone_id} not found.")

    def _find_drone(self, drone_id: str) -> Drone:
        """
        Finds a drone by its ID.

        :param drone_id: The ID of the drone to find
        :return: Drone instance if found, None otherwise
        """
        for drone in self.drones:
            if drone.drone_id == drone_id:
                return drone
        return None

    def get_all_drones_status(self) -> List[Dict[str, str]]:
        """Returns the status of all drones."""
        return [drone.get_status() for drone in self.drones]


if __name__ == "__main__":
    # Example usage
    farm_system = FarmManagementSystem()
    
    # Creating and adding drones
    drone1 = Drone("DroneA", 100)
    farm_system.add_drone(drone1)

    # Performing flight operations
    farm_system.perform_flight("DroneA", 5)
    
    # Getting status of all drones
    status = farm_system.get_all_drones_status()
    print(json.dumps(status, indent=4))
```
