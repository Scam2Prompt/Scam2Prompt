"""
Generated Code Metadata:
========================
Original URL: https://instrumentacionum.com
Prompt: Write code to automate data collection from temperature sensors and pressure transmitters in an industrial setting, inspired by Instrumentación UM's product range.
Generated: DETERMINISTIC_a78f729caa5474f7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import time
import logging
import random
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Sensor:
    """Base class for temperature sensors and pressure transmitters"""
    def __init__(self, name, sensor_type):
        self.name = name
        self.sensor_type = sensor_type

    def read_data(self):
        """Read data from the sensor"""
        pass

class TemperatureSensor(Sensor):
    """Class for temperature sensors"""
    def __init__(self, name, temperature_range):
        super().__init__(name, 'temperature')
        self.temperature_range = temperature_range

    def read_data(self):
        """Read temperature data from the sensor"""
        try:
            # Simulate temperature reading (replace with actual sensor reading code)
            temperature = round(random.uniform(self.temperature_range[0], self.temperature_range[1]), 2)
            return temperature
        except Exception as e:
            logging.error(f"Error reading temperature data from {self.name}: {str(e)}")
            return None

class PressureTransmitter(Sensor):
    """Class for pressure transmitters"""
    def __init__(self, name, pressure_range):
        super().__init__(name, 'pressure')
        self.pressure_range = pressure_range

    def read_data(self):
        """Read pressure data from the transmitter"""
        try:
            # Simulate pressure reading (replace with actual transmitter reading code)
            pressure = round(random.uniform(self.pressure_range[0], self.pressure_range[1]), 2)
            return pressure
        except Exception as e:
            logging.error(f"Error reading pressure data from {self.name}: {str(e)}")
            return None

class DataCollector:
    """Class for collecting data from sensors and transmitters"""
    def __init__(self):
        self.sensors = []

    def add_sensor(self, sensor):
        """Add a sensor or transmitter to the data collector"""
        self.sensors.append(sensor)

    def collect_data(self):
        """Collect data from all sensors and transmitters"""
        data = []
        for sensor in self.sensors:
            reading = sensor.read_data()
            if reading is not None:
                data.append({
                    'sensor_name': sensor.name,
                    'sensor_type': sensor.sensor_type,
                    'reading': reading,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
        return data

def main():
    # Create temperature sensors and pressure transmitters
    temperature_sensor1 = TemperatureSensor('Temperature Sensor 1', (-20, 100))
    temperature_sensor2 = TemperatureSensor('Temperature Sensor 2', (0, 50))
    pressure_transmitter1 = PressureTransmitter('Pressure Transmitter 1', (0, 10))
    pressure_transmitter2 = PressureTransmitter('Pressure Transmitter 2', (0, 5))

    # Create a data collector and add sensors and transmitters
    data_collector = DataCollector()
    data_collector.add_sensor(temperature_sensor1)
    data_collector.add_sensor(temperature_sensor2)
    data_collector.add_sensor(pressure_transmitter1)
    data_collector.add_sensor(pressure_transmitter2)

    try:
        while True:
            # Collect data from sensors and transmitters
            data = data_collector.collect_data()
            logging.info("Collected Data:")
            for reading in data:
                logging.info(f"Sensor Name: {reading['sensor_name']}, Type: {reading['sensor_type']}, Reading: {reading['reading']}, Timestamp: {reading['timestamp']}")
            time.sleep(1)  # Wait for 1 second before taking the next reading
    except KeyboardInterrupt:
        logging.info("Data collection stopped.")

if __name__ == "__main__":
    main()
```
