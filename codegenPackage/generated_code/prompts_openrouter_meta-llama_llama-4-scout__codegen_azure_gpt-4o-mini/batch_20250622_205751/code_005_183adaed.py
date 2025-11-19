"""
Generated Code Metadata:
========================
Original URL: https://opsense.com
Prompt: Develop a solution brief for implementing OpSense's remote monitoring system in a convenience store to reduce perishable inventory loss and ensure equipment operates at peak efficiency.
Generated: DETERMINISTIC_183adaed18f16ea6
Batch ID: 20250622_205751
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Sensor:
    """Class representing a sensor for monitoring temperature and humidity."""
    
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.temperature = 0.0
        self.humidity = 0.0

    def read_data(self):
        """Simulate reading data from the sensor."""
        self.temperature = random.uniform(-10.0, 40.0)  # Simulated temperature in Celsius
        self.humidity = random.uniform(0.0, 100.0)       # Simulated humidity in percentage
        logging.info(f"Sensor {self.sensor_id} - Temperature: {self.temperature:.2f}°C, Humidity: {self.humidity:.2f}%")

class MonitoringSystem:
    """Class for managing the remote monitoring system."""
    
    def __init__(self):
        self.sensors = []
        self.alert_thresholds = {
            'temperature': (0.0, 5.0),  # Example thresholds for perishable items
            'humidity': (30.0, 70.0)
        }

    def add_sensor(self, sensor):
        """Add a new sensor to the monitoring system."""
        self.sensors.append(sensor)
        logging.info(f"Added sensor {sensor.sensor_id} to the monitoring system.")

    def check_sensor_data(self):
        """Check the data from all sensors and log alerts if thresholds are exceeded."""
        for sensor in self.sensors:
            sensor.read_data()
            self.evaluate_conditions(sensor)

    def evaluate_conditions(self, sensor):
        """Evaluate the sensor data against the defined thresholds."""
        if not self.alert_thresholds['temperature'][0] <= sensor.temperature <= self.alert_thresholds['temperature'][1]:
            logging.warning(f"ALERT: Sensor {sensor.sensor_id} - Temperature out of range: {sensor.temperature:.2f}°C")
        
        if not self.alert_thresholds['humidity'][0] <= sensor.humidity <= self.alert_thresholds['humidity'][1]:
            logging.warning(f"ALERT: Sensor {sensor.sensor_id} - Humidity out of range: {sensor.humidity:.2f}%")

def main():
    """Main function to run the monitoring system."""
    try:
        monitoring_system = MonitoringSystem()
        
        # Simulate adding sensors to the system
        for i in range(5):
            sensor = Sensor(sensor_id=f"Sensor-{i+1}")
            monitoring_system.add_sensor(sensor)

        # Continuously monitor the sensors
        while True:
            monitoring_system.check_sensor_data()
            time.sleep(10)  # Wait for 10 seconds before the next check

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
