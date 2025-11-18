"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Develop a Python script for monitoring and controlling fire safety systems in residential properties, inspired by ERA ENGINEERING's specialized services.
Generated: DETERMINISTIC_8c2f1a303639566f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
import random

# Set up logging for system monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("fire_safety_system.log"),
        logging.StreamHandler()
    ]
)

# Constants for the fire safety system
SMOKE_THRESHOLD = 0.7  # Threshold for detecting smoke levels (0 to 1 scale)
TEMPERATURE_THRESHOLD = 60  # Threshold for temperature in Celsius
SYSTEM_CHECK_INTERVAL = 5  # Time interval (seconds) for system checks

# Simulate sensors for temperature and smoke levels
def read_temperature_sensor() -> float:
    """
    Simulates reading from a temperature sensor.

    Returns:
        float: Current temperature in Celsius.
    """
    return round(random.uniform(20, 100), 2)  # Simulated temperature value

def read_smoke_sensor() -> float:
    """
    Simulates reading from a smoke sensor.

    Returns:
        float: Current smoke level (0 to 1 scale).
    """
    return round(random.uniform(0, 1), 2)  # Simulated smoke level

# Fire safety system controller
def activate_fire_alarm():
    """
    Activates the fire alarm.
    """
    logging.warning("FIRE ALARM ACTIVATED! Please evacuate immediately!")

def deactivate_fire_alarm():
    """
    Deactivates the fire alarm.
    """
    logging.info("Fire alarm deactivated. All systems normal.")

def notify_authorities():
    """
    Sends a notification to fire safety authorities.
    """
    logging.error("Notifying fire safety authorities due to fire emergency.")

def monitor_safety_system():
    """
    Monitors the fire safety system continuously for temperature and smoke levels.
    """
    fire_alarm_active = False

    while True:
        try:
            # Simulate sensor readings
            temperature = read_temperature_sensor()
            smoke_level = read_smoke_sensor()

            # Log the sensor data
            logging.info(f"Temperature: {temperature}°C, Smoke Level: {smoke_level}")

            # Check for fire conditions
            if temperature > TEMPERATURE_THRESHOLD or smoke_level > SMOKE_THRESHOLD:
                if not fire_alarm_active:
                    activate_fire_alarm()
                    notify_authorities()
                    fire_alarm_active = True
            else:
                if fire_alarm_active:
                    deactivate_fire_alarm()
                    fire_alarm_active = False

            # Wait for the next system check
            time.sleep(SYSTEM_CHECK_INTERVAL)

        except KeyboardInterrupt:
            logging.info("Fire safety monitoring system stopped by user.")
            break
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            break

# Entry point for production system
if __name__ == "__main__":
    logging.info("Fire safety monitoring system starting...")
    monitor_safety_system()
```
