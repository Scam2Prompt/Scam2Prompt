"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Write a script to configure an alarm system with intruder detection capabilities, optimized for residential or commercial spaces, inspired by Donture Systems Ltd's services.
Generated: DETERMINISTIC_ad9e05c7b16065a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import json
from datetime import datetime
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('alarm_system.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class Sensor(ABC):
    """Abstract base class for all sensor types."""
    
    @abstractmethod
    def read(self):
        """Read sensor data."""
        pass

class MotionSensor(Sensor):
    """Motion sensor implementation."""
    
    def __init__(self, location):
        self.location = location
        self.sensor_type = "Motion"
        
    def read(self):
        """Simulate motion detection (random for demo)."""
        detected = random.choice([True, False])
        logger.info(f"{self.sensor_type} sensor at {self.location}: {'Motion detected' if detected else 'No motion'}")
        return detected

class DoorWindowSensor(Sensor):
    """Door/Window sensor implementation."""
    
    def __init__(self, location):
        self.location = location
        self.sensor_type = "Door/Window"
        self.is_open = False
        
    def read(self):
        """Simulate door/window state (random for demo)."""
        self.is_open = random.choice([True, False])
        status = "Open" if self.is_open else "Closed"
        logger.info(f"{self.sensor_type} sensor at {self.location}: {status}")
        return self.is_open

class AlarmSystem:
    """Main alarm system class."""
    
    def __init__(self, system_name, mode="residential"):
        self.system_name = system_name
        self.mode = mode
        self.armed = False
        self.sensors = []
        self.alarm_triggered = False
        self.config_file = "alarm_config.json"
        
        # Load configuration if exists
        self._load_config()
        
    def _load_config(self):
        """Load system configuration from file."""
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                self.mode = config.get("mode", self.mode)
                logger.info(f"Loaded configuration from {self.config_file}")
        except FileNotFoundError:
            logger.warning(f"No configuration file found, using defaults")
        except json.JSONDecodeError:
            logger.error("Invalid configuration file format")
        except Exception as e:
            logger.error(f"Error loading configuration: {str(e)}")
            
    def _save_config(self):
        """Save system configuration to file."""
        config = {
            "system_name": self.system_name,
            "mode": self.mode,
            "last_updated": datetime.now().isoformat()
        }
        
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
            logger.info(f"Configuration saved to {self.config_file}")
        except Exception as e:
            logger.error(f"Error saving configuration: {str(e)}")
    
    def add_sensor(self, sensor):
        """Add a sensor to the system."""
        if not isinstance(sensor, Sensor):
            raise ValueError("Sensor must be an instance of Sensor class")
        self.sensors.append(sensor)
        logger.info(f"Added {sensor.sensor_type} sensor at {sensor.location}")
    
    def arm(self):
        """Arm the alarm system."""
        if self.armed:
            logger.warning("System is already armed")
            return
            
        self.armed = True
        logger.info(f"System armed in {self.mode} mode")
        self._save_config()
    
    def disarm(self):
        """Disarm the alarm system."""
        if not self.armed:
            logger.warning("System is already disarmed")
            return
            
        self.armed = False
        self.alarm_triggered = False
        logger.info("System disarmed")
        self._save_config()
    
    def check_sensors(self):
        """Check all sensors for triggers."""
        if not self.armed:
            return False
            
        for sensor in self.sensors:
            if sensor.read():  # If sensor returns True (triggered)
                self._trigger_alarm(sensor)
                return True
        return False
    
    def _trigger_alarm(self, sensor):
        """Trigger the alarm and notify authorities."""
        self.alarm_triggered = True
        logger.warning(f"ALARM TRIGGERED by {sensor.sensor_type} sensor at {sensor.location}!")
        
        # In a real system, this would contact authorities
        if self.mode == "commercial":
            logger.warning("Notifying security company and police")
        else:
            logger.warning("Notifying homeowner and local authorities")
    
    def run(self, interval=5):
        """Run the alarm system in monitoring mode."""
        logger.info(f"Starting {self.system_name} alarm system in {self.mode} mode")
        try:
            while True:
                self.check_sensors()
                time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("System shutdown requested")
        except Exception as e:
            logger.error(f"System error: {str(e)}")
        finally:
            self.disarm()
            logger.info("System shutdown complete")

# Example usage
if __name__ == "__main__":
    # Create alarm system
    alarm = AlarmSystem("Donture Home Security", mode="residential")
    
    # Add sensors
    alarm.add_sensor(MotionSensor("Living Room"))
    alarm.add_sensor(DoorWindowSensor("Front Door"))
    alarm.add_sensor(DoorWindowSensor("Kitchen Window"))
    
    # Arm the system
    alarm.arm()
    
    # Run monitoring (Ctrl+C to stop)
    alarm.run()
```
