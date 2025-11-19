"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Generate a code to implement speed governor installation for a commercial fleet in Kenya, enhancing road safety and controlling vehicle speeds.
Generated: DETERMINISTIC_af1f4b0b6f8e1096
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# speed_governor.py

import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Vehicle:
    def __init__(self, vehicle_id: str, max_speed: int):
        """
        Initialize a Vehicle object.

        Args:
        - vehicle_id (str): Unique identifier for the vehicle.
        - max_speed (int): Maximum allowed speed for the vehicle.
        """
        self.vehicle_id = vehicle_id
        self.max_speed = max_speed
        self.current_speed = 0

    def update_speed(self, speed: int):
        """
        Update the current speed of the vehicle.

        Args:
        - speed (int): New speed of the vehicle.

        Raises:
        - ValueError: If the new speed exceeds the maximum allowed speed.
        """
        if speed > self.max_speed:
            logger.warning(f"Speed limit exceeded for vehicle {self.vehicle_id}.")
            raise ValueError("Speed limit exceeded.")
        self.current_speed = speed

class SpeedGovernor:
    def __init__(self):
        """
        Initialize a SpeedGovernor object.
        """
        self.vehicles: Dict[str, Vehicle] = {}

    def add_vehicle(self, vehicle_id: str, max_speed: int):
        """
        Add a vehicle to the speed governor.

        Args:
        - vehicle_id (str): Unique identifier for the vehicle.
        - max_speed (int): Maximum allowed speed for the vehicle.
        """
        self.vehicles[vehicle_id] = Vehicle(vehicle_id, max_speed)

    def update_vehicle_speed(self, vehicle_id: str, speed: int):
        """
        Update the speed of a vehicle.

        Args:
        - vehicle_id (str): Unique identifier for the vehicle.
        - speed (int): New speed of the vehicle.

        Raises:
        - ValueError: If the vehicle is not found or the speed limit is exceeded.
        """
        if vehicle_id not in self.vehicles:
            logger.error(f"Vehicle {vehicle_id} not found.")
            raise ValueError("Vehicle not found.")
        self.vehicles[vehicle_id].update_speed(speed)

    def get_vehicle_speed(self, vehicle_id: str) -> int:
        """
        Get the current speed of a vehicle.

        Args:
        - vehicle_id (str): Unique identifier for the vehicle.

        Returns:
        - int: Current speed of the vehicle.

        Raises:
        - ValueError: If the vehicle is not found.
        """
        if vehicle_id not in self.vehicles:
            logger.error(f"Vehicle {vehicle_id} not found.")
            raise ValueError("Vehicle not found.")
        return self.vehicles[vehicle_id].current_speed

def main():
    # Create a speed governor
    governor = SpeedGovernor()

    # Add vehicles
    vehicles: List[Dict[str, int]] = [
        {"vehicle_id": "KD001", "max_speed": 80},
        {"vehicle_id": "KD002", "max_speed": 90},
    ]
    for vehicle in vehicles:
        governor.add_vehicle(vehicle["vehicle_id"], vehicle["max_speed"])

    # Update vehicle speeds
    try:
        governor.update_vehicle_speed("KD001", 70)
        governor.update_vehicle_speed("KD002", 100)  # This should raise an error
    except ValueError as e:
        logger.error(e)

    # Get vehicle speeds
    logger.info(f"Current speed of KD001: {governor.get_vehicle_speed('KD001')}")
    try:
        logger.info(f"Current speed of KD002: {governor.get_vehicle_speed('KD002')}")
    except ValueError as e:
        logger.error(e)

if __name__ == "__main__":
    main()
```
