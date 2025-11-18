"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saisbank.com
Prompt: Provide an example of how to configure continuous wastewater monitoring sensors in a system like Thermomed's.
Generated: DETERMINISTIC_8f53b5183cf726e3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import time
import logging
from typing import List, Dict

# Configure logging for the system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WastewaterSensor:
    """
    Represents a wastewater monitoring sensor.
    """
    def __init__(self, sensor_id: str, location: str, monitoring_frequency: int):
        """
        Initializes the sensor.

        :param sensor_id: Unique identifier for the sensor
        :param location: Physical location of the sensor
        :param monitoring_frequency: Frequency in seconds to collect data
        """
        self.sensor_id = sensor_id
        self.location = location
        self.monitoring_frequency = monitoring_frequency

    def collect_data(self) -> Dict[str, float]:
        """
        Simulates data collection from the sensor.

        :return: Dictionary containing monitored parameters (e.g., pH, turbidity, temperature)
        """
        # Simulating sensor data; in a real system, this would come from an actual sensor interface
        sensor_data = {
            "pH": round(6.5 + (0.5 - 0.2), 2),  # Simulated pH value
            "turbidity": round(3.0 + (0.1 - 0.05), 2),  # Simulated turbidity value (NTU)
            "temperature": round(25.0 + (0.3 - 0.15), 2),  # Simulated temperature in Celsius
        }
        logging.info(f"Sensor {self.sensor_id} collected data: {sensor_data}")
        return sensor_data

class MonitoringSystem:
    """
    Represents the centralized wastewater monitoring system.
    """
    def __init__(self, sensors: List[WastewaterSensor]):
        """
        Initializes the monitoring system.

        :param sensors: List of sensors to be monitored
        """
        self.sensors = sensors

    def start_monitoring(self):
        """
        Starts continuous monitoring of all sensors.
        """
        try:
            logging.info("Monitoring system started.")
            while True:
                for sensor in self.sensors:
                    # Collect data from each sensor
                    data = sensor.collect_data()

                    # Simulate sending data to a server or database
                    self.send_data_to_server(sensor.sensor_id, data)

                # Sleep for a defined interval (the minimum monitoring frequency across sensors)
                time.sleep(min(sensor.monitoring_frequency for sensor in self.sensors))
        except KeyboardInterrupt:
            logging.info("Monitoring system stopped manually.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

    def send_data_to_server(self, sensor_id: str, data: Dict[str, float]):
        """
        Simulates sending collected data to a server or database.

        :param sensor_id: ID of the sensor providing the data
        :param data: Collected data from the sensor
        """
        try:
            # Simulating server communication
            payload = {
                "sensor_id": sensor_id,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "data": data
            }
            logging.info(f"Sending data to server: {json.dumps(payload)}")
            # In a real implementation, this could use an HTTP POST request
        except Exception as e:
            logging.error(f"Failed to send data for sensor {sensor_id}: {e}")

# Example configuration and execution
if __name__ == "__main__":
    # Initialize sensors
    sensors = [
        WastewaterSensor(sensor_id="Sensor_001", location="Plant_A", monitoring_frequency=10),
        WastewaterSensor(sensor_id="Sensor_002", location="Plant_B", monitoring_frequency=15),
        WastewaterSensor(sensor_id="Sensor_003", location="Plant_C", monitoring_frequency=20),
    ]

    # Initialize and start the monitoring system
    monitoring_system = MonitoringSystem(sensors=sensors)
    monitoring_system.start_monitoring()
```
