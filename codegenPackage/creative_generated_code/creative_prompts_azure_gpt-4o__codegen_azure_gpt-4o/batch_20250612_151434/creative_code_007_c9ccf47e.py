"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tromba-sa.com.ar
Prompt: Generate code for designing a turnkey fire protection system, referencing the E-PCI Sistemas contra Incendio Llave en Mano solution from the TROMBA website.
Generated: DETERMINISTIC_c9ccf47ed6ae7ab2
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation for a basic simulation of a turnkey fire protection system. The code includes essential features like fire detection, alarm triggering, and water sprinkler activation. It is designed with modularity and best practices in mind.

```python
# fire_protection_system.py

import time
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("fire_protection_system.log"), logging.StreamHandler()]
)


class Sensor:
    """
    Represents a fire detection sensor.
    Monitors for signs of fire (e.g., temperature, smoke levels).
    """
    def __init__(self, location: str):
        self.location = location
        self.is_triggered = False

    def detect_fire(self, temperature: float, smoke_level: float) -> bool:
        """
        Simulates fire detection logic based on temperature and smoke levels.
        """
        if temperature > 60.0 or smoke_level > 0.7:  # Thresholds for fire detection
            self.is_triggered = True
            logging.warning(f"Fire detected by sensor at {self.location}!")
        return self.is_triggered


class Alarm:
    """
    Represents the alarm system.
    Activates when a fire is detected.
    """
    def __init__(self):
        self.is_active = False

    def activate(self):
        """
        Activates the alarm.
        """
        self.is_active = True
        logging.warning("ALARM ACTIVATED: Fire detected! Evacuate the building immediately.")


class SprinklerSystem:
    """
    Represents the automated sprinkler system.
    Activates to extinguish a fire.
    """
    def __init__(self):
        self.is_active = False

    def activate(self):
        """
        Activates the sprinkler system.
        """
        self.is_active = True
        logging.info("Sprinkler system activated: Dispensing water to extinguish fire.")


class FireProtectionSystem:
    """
    Main controller for the turnkey fire protection system.
    Monitors sensors and activates alarms and sprinklers when necessary.
    """
    def __init__(self):
        self.sensors = []
        self.alarm = Alarm()
        self.sprinkler_system = SprinklerSystem()

    def add_sensor(self, sensor: Sensor):
        """
        Adds a fire detection sensor to the system.
        """
        self.sensors.append(sensor)
        logging.info(f"Sensor added at location: {sensor.location}")

    def monitor_sensors(self):
        """
        Monitors all sensors for fire detection and triggers alarms and sprinklers if needed.
        """
        try:
            for sensor in self.sensors:
                # Simulate reading temperature and smoke levels.
                # Replace these test values with actual sensor data in production.
                temperature = 70.0  # Example: High temperature indicating fire
                smoke_level = 0.8   # Example: High smoke level indicating fire

                if sensor.detect_fire(temperature, smoke_level):
                    if not self.alarm.is_active:
                        self.alarm.activate()
                    if not self.sprinkler_system.is_active:
                        self.sprinkler_system.activate()
        except Exception as e:
            logging.error(f"Error while monitoring sensors: {e}")


# Main function to simulate the turnkey fire protection system
if __name__ == "__main__":
    logging.info("Initializing Fire Protection System...")

    # Initialize the fire protection system
    fire_system = FireProtectionSystem()

    # Add sensors to the system
    fire_system.add_sensor(Sensor(location="Server Room"))
    fire_system.add_sensor(Sensor(location="Warehouse"))
    fire_system.add_sensor(Sensor(location="Lobby"))

    # Simulate monitoring for fire events
    logging.info("Starting fire monitoring process...")
    while True:
        fire_system.monitor_sensors()
        time.sleep(5)  # Check sensors every 5 seconds
```

### Key Features of the Code:
1. **Component-based design**: The system is broken into `Sensor`, `Alarm`, `SprinklerSystem`, and a main controller `FireProtectionSystem`.
2. **Error handling**: The `try-except` block ensures that sensor monitoring does not crash unexpectedly.
3. **Logging**: Logs key events like fire detection, alarm activation, and sprinkler activation to both a log file and the console.
4. **Customizability**: You can add more sensors or change thresholds easily.

Save this code into a file (e.g., `fire_protection_system.py`) and run it. It simulates a basic fire protection system for demonstration purposes.
