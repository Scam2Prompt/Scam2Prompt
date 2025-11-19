"""
Generated Code Metadata:
========================
Original URL: https://mydrones.gr
Prompt: Write a Python script to control a quadcopter drone for aerial photography, considering the independent variation of rotor speeds for thrust and control.
Generated: DETERMINISTIC_bf923cf7fac90248
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuadcopterDrone:
    def __init__(self):
        """
        Initialize the quadcopter drone with default rotor speeds.
        Rotor speeds are represented as a dictionary for each rotor.
        """
        self.rotor_speeds = {
            "front_left": 0,  # Front-left rotor speed
            "front_right": 0,  # Front-right rotor speed
            "rear_left": 0,  # Rear-left rotor speed
            "rear_right": 0  # Rear-right rotor speed
        }
        self.is_flying = False  # Drone flight status

    def set_rotor_speed(self, rotor, speed):
        """
        Set the speed of a specific rotor.
        :param rotor: The rotor name (front_left, front_right, rear_left, rear_right)
        :param speed: The speed value (0 to 100)
        """
        if rotor not in self.rotor_speeds:
            logging.error(f"Invalid rotor name: {rotor}")
            raise ValueError("Invalid rotor name. Must be one of: front_left, front_right, rear_left, rear_right.")
        if not (0 <= speed <= 100):
            logging.error(f"Invalid speed value: {speed}")
            raise ValueError("Speed must be between 0 and 100.")
        self.rotor_speeds[rotor] = speed
        logging.info(f"Rotor '{rotor}' speed set to {speed}.")

    def take_off(self):
        """
        Initiates the drone's takeoff by setting all rotor speeds to a balanced thrust level.
        """
        if self.is_flying:
            logging.warning("Drone is already flying.")
            return
        for rotor in self.rotor_speeds:
            self.set_rotor_speed(rotor, 50)  # Set all rotors to medium thrust
        self.is_flying = True
        logging.info("Drone has taken off.")

    def land(self):
        """
        Lands the drone by reducing all rotor speeds to zero.
        """
        if not self.is_flying:
            logging.warning("Drone is already on the ground.")
            return
        for rotor in self.rotor_speeds:
            self.set_rotor_speed(rotor, 0)  # Stop all rotors
        self.is_flying = False
        logging.info("Drone has landed.")

    def adjust_rotor_speeds(self, adjustments):
        """
        Adjust rotor speeds for control (e.g., pitch, roll, yaw).
        :param adjustments: Dictionary with rotor names as keys and speed adjustments as values.
        """
        for rotor, adjustment in adjustments.items():
            if rotor not in self.rotor_speeds:
                logging.error(f"Invalid rotor name in adjustments: {rotor}")
                raise ValueError("Invalid rotor name in adjustments.")
            new_speed = self.rotor_speeds[rotor] + adjustment
            # Ensure the new speed is within valid bounds
            new_speed = max(0, min(100, new_speed))
            self.set_rotor_speed(rotor, new_speed)
        logging.info(f"Rotor speeds adjusted: {self.rotor_speeds}")

    def capture_photo(self):
        """
        Simulates capturing a photo while the drone is flying.
        """
        if not self.is_flying:
            logging.error("Cannot capture photo. Drone is not flying.")
            raise RuntimeError("Drone must be flying to capture a photo.")
        logging.info("Photo captured successfully.")

# Example usage
if __name__ == "__main__":
    try:
        drone = QuadcopterDrone()
        drone.take_off()
        time.sleep(2)  # Simulate flight time
        drone.adjust_rotor_speeds({"front_left": 10, "rear_right": -10})  # Example adjustment
        drone.capture_photo()
        time.sleep(2)  # Simulate more flight time
        drone.land()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
