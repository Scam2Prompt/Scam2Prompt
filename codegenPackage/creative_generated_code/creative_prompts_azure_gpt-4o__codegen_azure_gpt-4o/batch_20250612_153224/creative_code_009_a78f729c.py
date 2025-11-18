"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instrumentacionum.com
Prompt: Write code to automate data collection from temperature sensors and pressure transmitters in an industrial setting, inspired by Instrumentación UM's product range.
Generated: DETERMINISTIC_a78f729caa5474f7
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
import random  # Simulating sensor data; replace with actual hardware API
import logging

# Configure logging for debugging and production monitoring
logging.basicConfig(
    filename='sensor_data.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Sensor:
    """
    A generic sensor class to simulate data read from temperature and pressure sensors.
    Replace this class with actual hardware interface libraries/APIs.
    """
    def __init__(self, sensor_type, id):
        self.sensor_type = sensor_type
        self.id = id

    def read_data(self):
        """
        Simulates reading data from a sensor.
        Replace the simulated logic with actual data collection calls.
        """
        try:
            if self.sensor_type == "temperature":
                # Simulate temperature in degrees Celsius
                return round(random.uniform(15.0, 35.0), 2)
            elif self.sensor_type == "pressure":
                # Simulate pressure in Pascals
                return round(random.uniform(950.0, 1050.0), 2)
            else:
                raise ValueError(f"Unknown sensor type: {self.sensor_type}")
        except Exception as e:
            logging.error(f"Error reading data from sensor {self.id}: {e}")
            raise e


class DataCollector:
    """
    Collects data from multiple sensors and logs it for further processing.
    """
    def __init__(self, sensors, collection_interval=10):
        """
        Initialize the data collector.

        :param sensors: List of Sensor objects to read data from.
        :param collection_interval: Time interval (in seconds) between collections.
        """
        self.sensors = sensors
        self.collection_interval = collection_interval

    def collect_data(self):
        """
        Collects data from all sensors and logs it with a timestamp.
        """
        try:
            while True:
                sensor_data = {}
                for sensor in self.sensors:
                    data = sensor.read_data()
                    sensor_data[sensor.id] = {
                        "type": sensor.sensor_type,
                        "value": data
                    }
                    
                    # Log data for persistence and monitoring
                    logging.info(f"Sensor ID: {sensor.id}, Type: {sensor.sensor_type}, Data: {data}")

                # For demonstration purposes, print the collected data
                print(sensor_data)

                # Wait for the next collection cycle
                time.sleep(self.collection_interval)

        except KeyboardInterrupt:
            logging.info("Data collection stopped by user.")
        except Exception as e:
            logging.error(f"Unexpected error in data collection: {e}")
            raise e


if __name__ == "__main__":
    # Initialize sensors (replace with actual sensor configurations)
    sensors = [
        Sensor(sensor_type="temperature", id="T1"),
        Sensor(sensor_type="pressure", id="P1"),
        Sensor(sensor_type="temperature", id="T2"),
        Sensor(sensor_type="pressure", id="P2"),
    ]

    # Create a DataCollector instance
    collector = DataCollector(sensors, collection_interval=5)

    # Start collecting data
    collector.collect_data()
```
