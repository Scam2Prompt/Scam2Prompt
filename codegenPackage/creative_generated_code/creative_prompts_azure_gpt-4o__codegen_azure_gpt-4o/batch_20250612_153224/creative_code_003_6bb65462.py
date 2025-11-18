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

# Configure logging for the telemetry system
logging.basicConfig(
    filename='telemetry_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Sensor:
    """
    Base class for sensors. Defines the interface for all sensor types.
    """
    def __init__(self, sensor_id, sensor_type):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type

    def read_data(self):
        """
        This method should be overridden by subclasses to provide sensor-specific data reading logic.
        """
        raise NotImplementedError("Subclasses must implement this method.")

class InductivePositionSensor(Sensor):
    """
    Represents an inductive position sensor that measures position data.
    """
    def __init__(self, sensor_id):
        super().__init__(sensor_id, 'InductivePositionSensor')

    def read_data(self):
        # Simulate reading position data from the sensor
        try:
            position = round(random.uniform(0, 100), 2)  # Simulated position value in mm
            return position
        except Exception as e:
            logging.error(f"Error reading data from sensor {self.sensor_id}: {e}")
            return None

class PressureTransmitter(Sensor):
    """
    Represents a pressure transmitter that measures pressure data.
    """
    def __init__(self, sensor_id):
        super().__init__(sensor_id, 'PressureTransmitter')

    def read_data(self):
        # Simulate reading pressure data from the sensor
        try:
            pressure = round(random.uniform(0, 200), 2)  # Simulated pressure value in bar
            return pressure
        except Exception as e:
            logging.error(f"Error reading data from sensor {self.sensor_id}: {e}")
            return None

class TelemetrySystem:
    """
    Telemetry system for collecting data from sensors and logging it for monitoring purposes.
    """
    def __init__(self):
        self.sensors = []

    def add_sensor(self, sensor):
        """
        Adds a sensor to the telemetry system.
        :param sensor: Instance of a Sensor subclass.
        """
        if isinstance(sensor, Sensor):
            self.sensors.append(sensor)
            logging.info(f"Added sensor {sensor.sensor_id} ({sensor.sensor_type}) to the system.")
        else:
            logging.error("Invalid sensor type. Sensor must be an instance of the Sensor class or its subclasses.")

    def collect_data(self):
        """
        Collects data from all sensors and logs it.
        """
        if not self.sensors:
            logging.warning("No sensors in the system to collect data from.")
            return

        for sensor in self.sensors:
            data = sensor.read_data()
            if data is not None:
                logging.info(f"Sensor {sensor.sensor_id} ({sensor.sensor_type}) - Data: {data}")
            else:
                logging.warning(f"Failed to retrieve data from sensor {sensor.sensor_id} ({sensor.sensor_type}).")

    def run(self, interval):
        """
        Runs the telemetry system to continuously collect data at specified intervals.
        :param interval: Time in seconds between data collection cycles.
        """
        try:
            while True:
                logging.info("Starting data collection cycle.")
                self.collect_data()
                logging.info(f"Data collection cycle complete. Sleeping for {interval} seconds.")
                time.sleep(interval)
        except KeyboardInterrupt:
            logging.info("Telemetry system stopped by user.")
        except Exception as e:
            logging.error(f"Error occurred during telemetry system operation: {e}")

# Instantiate the telemetry system
telemetry_system = TelemetrySystem()

# Add sensors to the system
telemetry_system.add_sensor(InductivePositionSensor("IPS001"))
telemetry_system.add_sensor(PressureTransmitter("PT001"))

# Run the telemetry system (collect data every 5 seconds)
if __name__ == "__main__":
    telemetry_system.run(interval=5)
```
