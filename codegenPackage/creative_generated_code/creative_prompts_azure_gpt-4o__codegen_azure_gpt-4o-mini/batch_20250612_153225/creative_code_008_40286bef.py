"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Create a simulation script for testing a real-time health monitoring system using IoT devices, based on the features highlighted by Hooshmand Teb.
Generated: DETERMINISTIC_40286bef8e9ef6b9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HealthMonitor:
    """
    A class to represent a health monitoring system that simulates real-time data from IoT devices.
    """

    def __init__(self, device_id):
        """
        Initialize the health monitor with a unique device ID.

        :param device_id: Unique identifier for the IoT device
        """
        self.device_id = device_id
        self.health_data = {}

    def generate_health_data(self):
        """
        Simulate health data generation by the IoT device.
        
        :return: A dictionary containing simulated health metrics
        """
        # Simulating health metrics
        heart_rate = random.randint(60, 100)  # Heart rate in BPM
        blood_pressure = (random.randint(90, 120), random.randint(60, 80))  # Systolic and diastolic
        temperature = round(random.uniform(36.0, 38.5), 2)  # Body temperature in Celsius

        # Create a dictionary to hold health metrics
        self.health_data = {
            'timestamp': datetime.now().isoformat(),
            'device_id': self.device_id,
            'heart_rate': heart_rate,
            'blood_pressure': blood_pressure,
            'temperature': temperature,
        }
        return self.health_data

    def send_data(self):
        """
        Simulate sending health data to a remote server.
        
        This function generates health data and simulates a network transmission.
        """
        data = self.generate_health_data()
        try:
            # Simulate sending data (In production, this would involve actual network code)
            logging.info("Sending data: %s", json.dumps(data))
            # Simulate potential network failure
            if random.random() < 0.1:  # 10% chance of failure
                raise ConnectionError("Simulated network failure.")
            logging.info("Data sent successfully.")
        except ConnectionError as e:
            logging.error("Failed to send data: %s", e)

    def run(self):
        """
        Continuously run the health monitor, simulating data transmission at regular intervals.
        """
        logging.info("Starting health monitoring on device %s", self.device_id)
        while True:
            self.send_data()
            time.sleep(5)  # Wait for 5 seconds before sending new data

if __name__ == "__main__":
    try:
        # Create an instance of HealthMonitor with a unique device ID
        monitor = HealthMonitor(device_id="IoT_Device_001")
        monitor.run()
    except KeyboardInterrupt:
        logging.info("Health monitoring stopped by user.")
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
```
