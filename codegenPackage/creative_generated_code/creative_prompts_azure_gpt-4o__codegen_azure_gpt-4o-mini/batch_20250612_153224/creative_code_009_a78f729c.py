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
import random
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Sensor:
    """
    Base class for a sensor.
    """
    def read_value(self) -> float:
        """
        Read the sensor value.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

class TemperatureSensor(Sensor):
    """
    Class representing a temperature sensor.
    """
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
    
    def read_value(self) -> float:
        """
        Simulate reading a temperature value.
        Returns a random float between -20 and 50 degrees Celsius.
        """
        return round(random.uniform(-20.0, 50.0), 2)

class PressureTransmitter(Sensor):
    """
    Class representing a pressure transmitter.
    """
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id

    def read_value(self) -> float:
        """
        Simulate reading a pressure value.
        Returns a random float between 0 and 300 PSI.
        """
        return round(random.uniform(0.0, 300.0), 2)

class DataCollector:
    """
    Class for collecting data from sensors.
    """
    def __init__(self, sensors: List[Sensor]):
        self.sensors = sensors

    def collect_data(self) -> Dict[str, float]:
        """
        Collect data from all sensors.
        
        Returns:
            A dictionary with sensor IDs as keys and their respective values as values.
        """
        data = {}
        for sensor in self.sensors:
            try:
                value = sensor.read_value()
                data[sensor.sensor_id] = value
                logging.info(f"Collected data from {sensor.sensor_id}: {value}")
            except Exception as e:
                logging.error(f"Error reading from sensor {sensor.sensor_id}: {e}")
        return data

def main():
    """
    Main function to execute data collection.
    """
    # Initialize sensors
    sensors = [
        TemperatureSensor('TempSensor_1'),
        TemperatureSensor('TempSensor_2'),
        PressureTransmitter('PressureTransmitter_1'),
        PressureTransmitter('PressureTransmitter_2'),
    ]

    # Create a data collector instance
    data_collector = DataCollector(sensors)

    # Loop for continuous data collection
    try:
        while True:
            # Collect data from sensors
            collected_data = data_collector.collect_data()
            # Process the collected data (e.g., save to a database, send to a server, etc.)
            # Here we just log it
            logging.info(f"Collected data: {collected_data}")
            # Wait for a specified interval before the next collection
            time.sleep(10)  # Adjust the sleep time as necessary
    except KeyboardInterrupt:
        logging.info("Data collection terminated by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
