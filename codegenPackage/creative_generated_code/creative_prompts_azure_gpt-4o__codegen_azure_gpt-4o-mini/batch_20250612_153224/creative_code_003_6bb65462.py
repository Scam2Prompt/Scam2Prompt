"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instrumentacionum.com
Prompt: Create a telemetry system using Python that collects data from inductive position sensors and pressure transmitters, similar to the solutions provided by Instrumentación UM.
Generated: DETERMINISTIC_6bb65462469ba846
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging
from typing import Dict, Any

# Configure logging for monitoring the telemetry system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

class Sensor:
    """Base class for Sensors."""
    def read(self) -> float:
        """Reads data from the sensor. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")

class InductivePositionSensor(Sensor):
    """Inductive Position Sensor class that simulates position readings."""
    def __init__(self, id: str):
        self.id = id
    
    def read(self) -> float:
        """Read a simulated position value."""
        # Simulate reading a position value between 0 and 100
        position = random.uniform(0, 100)
        logging.info(f"Position Sensor {self.id} reading: {position:.2f}")
        return position
    
class PressureTransmitter(Sensor):
    """Pressure Transmitter class that simulates pressure readings."""
    def __init__(self, id: str):
        self.id = id
    
    def read(self) -> float:
        """Read a simulated pressure value."""
        # Simulate reading a pressure value between 0 and 150
        pressure = random.uniform(0, 150)
        logging.info(f"Pressure Transmitter {self.id} reading: {pressure:.2f}")
        return pressure

class TelemetrySystem:
    """Telemetry System for collecting and processing sensor data."""
    def __init__(self):
        self.sensors: Dict[str, Sensor] = {}
    
    def add_sensor(self, sensor: Sensor):
        """Add a sensor to the telemetry system."""
        self.sensors[sensor.id] = sensor
    
    def collect_data(self) -> Dict[str, Any]:
        """Collect data from all sensors and return the readings."""
        data = {}
        for sensor_id, sensor in self.sensors.items():
            try:
                data[sensor_id] = sensor.read()
            except Exception as e:
                logging.error(f"Error reading sensor {sensor_id}: {e}")
                data[sensor_id] = None  # Store None if reading fails
        return data

    def process_data(self, data: Dict[str, Any]) -> None:
        """Process the collected data."""
        for sensor_id, value in data.items():
            if value is not None:
                logging.info(f"Processed data for {sensor_id}: {value}")
            else:
                logging.warning(f"No data to process for {sensor_id}.")

def main():
    """Main function to run the telemetry system."""
    telemetry_system = TelemetrySystem()
    
    # Create and add sensors
    position_sensor = InductivePositionSensor(id="pos_sensor_1")
    pressure_sensor = PressureTransmitter(id="pressure_sensor_1")
    
    telemetry_system.add_sensor(position_sensor)
    telemetry_system.add_sensor(pressure_sensor)

    try:
        while True:
            # Collect and process sensor data
            sensor_data = telemetry_system.collect_data()
            telemetry_system.process_data(sensor_data)
            time.sleep(2)  # Sleep for 2 seconds before the next read
    except KeyboardInterrupt:
        logging.info("Telemetry system stopped by user.")
    except Exception as e:
        logging.critical(f"Telemetry system encountered an unexpected error: {e}")

if __name__ == "__main__":
    main()
```
