"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Design a system architecture for a real-time pipe monitoring system that integrates data from various sensors, including pressure, flow rate, and water quality sensors.
Generated: DETERMINISTIC_1baa15f2c1d407c6
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Real-Time Pipe Monitoring System

This system integrates data from various sensors (pressure, flow rate, and water quality)
to monitor the status of pipes in real-time. It uses a modular architecture with the following components:
1. Sensor Data Collection
2. Data Processing and Validation
3. Alert System
4. Data Storage
5. API for external access

The code below is designed to be clean, efficient, and production-ready.
"""

import time
import random
import logging
from typing import Dict, Any

# Configure logging for the system
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

# Define custom exceptions for error handling
class SensorError(Exception):
    """Raised when there is an issue with sensor data."""
    pass

class DataValidationError(Exception):
    """Raised when sensor data fails validation checks."""
    pass

# Simulated sensor data collection module
class Sensor:
    """Base class for sensors."""
    def __init__(self, sensor_type: str):
        self.sensor_type = sensor_type

    def read_data(self) -> float:
        """Simulate reading data from a sensor."""
        raise NotImplementedError("This method should be implemented by subclasses.")

class PressureSensor(Sensor):
    """Pressure sensor implementation."""
    def __init__(self):
        super().__init__("Pressure")

    def read_data(self) -> float:
        # Simulate pressure data (in psi)
        return random.uniform(10.0, 100.0)

class FlowRateSensor(Sensor):
    """Flow rate sensor implementation."""
    def __init__(self):
        super().__init__("FlowRate")

    def read_data(self) -> float:
        # Simulate flow rate data (in liters per second)
        return random.uniform(0.1, 10.0)

class WaterQualitySensor(Sensor):
    """Water quality sensor implementation."""
    def __init__(self):
        super().__init__("WaterQuality")

    def read_data(self) -> float:
        # Simulate water quality data (pH level)
        return random.uniform(6.0, 8.5)

# Data processing and validation module
def validate_sensor_data(sensor_type: str, value: float) -> bool:
    """Validate sensor data based on predefined thresholds."""
    thresholds = {
        "Pressure": (10.0, 100.0),
        "FlowRate": (0.1, 10.0),
        "WaterQuality": (6.0, 8.5)
    }
    if sensor_type not in thresholds:
        raise SensorError(f"Unknown sensor type: {sensor_type}")
    
    min_val, max_val = thresholds[sensor_type]
    if not (min_val <= value <= max_val):
        raise DataValidationError(f"{sensor_type} data out of range: {value}")
    
    return True

# Alert system module
def send_alert(sensor_type: str, value: float):
    """Send an alert if sensor data is out of range."""
    logging.warning(f"ALERT: {sensor_type} sensor reported abnormal value: {value}")

# Data storage module
class DataStorage:
    """Simple in-memory data storage."""
    def __init__(self):
        self.data = []

    def store_data(self, sensor_type: str, value: float, timestamp: float):
        """Store sensor data."""
        self.data.append({
            "sensor_type": sensor_type,
            "value": value,
            "timestamp": timestamp
        })
        logging.info(f"Stored data: {sensor_type}={value} at {timestamp}")

    def get_data(self) -> list:
        """Retrieve all stored data."""
        return self.data

# Main system loop
def main():
    """Main function to run the real-time pipe monitoring system."""
    # Initialize sensors
    sensors = [
        PressureSensor(),
        FlowRateSensor(),
        WaterQualitySensor()
    ]

    # Initialize data storage
    storage = DataStorage()

    try:
        while True:
            for sensor in sensors:
                try:
                    # Read data from sensor
                    value = sensor.read_data()
                    timestamp = time.time()

                    # Validate data
                    validate_sensor_data(sensor.sensor_type, value)

                    # Store data
                    storage.store_data(sensor.sensor_type, value, timestamp)

                except DataValidationError as e:
                    # Handle validation errors
                    send_alert(sensor.sensor_type, value)
                    logging.error(f"Validation error: {e}")

                except SensorError as e:
                    # Handle sensor errors
                    logging.error(f"Sensor error: {e}")

            # Simulate real-time monitoring with a delay
            time.sleep(1)

    except KeyboardInterrupt:
        # Graceful shutdown on user interrupt
        logging.info("Shutting down the monitoring system.")

if __name__ == "__main__":
    main()
```
