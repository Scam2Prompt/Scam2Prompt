"""
Generated Code Metadata:
========================
Original URL: https://hooshmand-teb.ir
Prompt: Create a simulation script for testing a real-time health monitoring system using IoT devices, based on the features highlighted by Hooshmand Teb.
Generated: DETERMINISTIC_40286bef8e9ef6b9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HealthMonitor:
    """A class to simulate a real-time health monitoring system using IoT devices."""

    def __init__(self, device_id):
        """
        Initialize the HealthMonitor with a device ID.

        :param device_id: Unique identifier for the IoT device
        """
        self.device_id = device_id
        self.health_data = {}

    def generate_health_data(self):
        """
        Simulate the generation of health data.

        :return: A dictionary containing simulated health metrics
        """
        # Simulate health metrics
        heart_rate = random.randint(60, 100)  # Heart rate in beats per minute
        blood_pressure = (random.randint(90, 120), random.randint(60, 80))  # Systolic and diastolic
        temperature = round(random.uniform(36.0, 38.5), 1)  # Body temperature in Celsius

        # Create a health data dictionary
        self.health_data = {
            'device_id': self.device_id,
            'timestamp': datetime.now().isoformat(),
            'heart_rate': heart_rate,
            'blood_pressure': blood_pressure,
            'temperature': temperature
        }
        return self.health_data

    def send_data(self):
        """
        Simulate sending health data to a server.

        :return: JSON string of the health data
        """
        try:
            data = self.generate_health_data()
            json_data = json.dumps(data)
            logging.info(f"Sending data: {json_data}")
            # Here you would typically send the data to a server
            # For simulation, we just log it
            return json_data
        except Exception as e:
            logging.error(f"Error sending data: {e}")
            return None

def main():
    """Main function to run the health monitoring simulation."""
    device_id = "IoT-Health-Monitor-001"
    monitor = HealthMonitor(device_id)

    try:
        while True:
            monitor.send_data()
            time.sleep(5)  # Simulate a delay between data sends
    except KeyboardInterrupt:
        logging.info("Simulation stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
