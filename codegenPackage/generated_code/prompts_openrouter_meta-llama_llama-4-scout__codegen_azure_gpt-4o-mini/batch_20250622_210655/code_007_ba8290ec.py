"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: "Recommend a suitable programming language and libraries for developing a data logging system for a metering skid in the oil and gas industry."
Generated: DETERMINISTIC_ba8290ec1bd18a49
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import logging
import json
import time
import random
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='data_logging_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MeteringSkid:
    """
    A class to represent a metering skid in the oil and gas industry.
    It simulates data logging for various parameters.
    """

    def __init__(self, skid_id):
        """
        Initializes the metering skid with a unique identifier.

        :param skid_id: Unique identifier for the metering skid
        """
        self.skid_id = skid_id
        self.data_log = []

    def read_sensor_data(self):
        """
        Simulates reading data from sensors. In a real application, this would interface with actual hardware.

        :return: A dictionary containing simulated sensor data
        """
        return {
            'temperature': round(random.uniform(20.0, 100.0), 2),  # Simulated temperature in Celsius
            'pressure': round(random.uniform(1.0, 10.0), 2),      # Simulated pressure in bar
            'flow_rate': round(random.uniform(0.0, 100.0), 2)     # Simulated flow rate in m³/h
        }

    def log_data(self):
        """
        Logs the sensor data to the data log and a log file.
        """
        try:
            sensor_data = self.read_sensor_data()
            timestamp = datetime.now().isoformat()
            log_entry = {
                'timestamp': timestamp,
                'skid_id': self.skid_id,
                **sensor_data
            }
            self.data_log.append(log_entry)
            logging.info(f"Logged data: {log_entry}")
        except Exception as e:
            logging.error(f"Error logging data: {e}")

    def save_log_to_file(self, filename='data_log.json'):
        """
        Saves the logged data to a JSON file.

        :param filename: The name of the file to save the log data
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.data_log, json_file, indent=4)
            logging.info(f"Data log saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving log to file: {e}")

def main():
    """
    Main function to run the data logging system.
    """
    metering_skid = MeteringSkid(skid_id='SKID-001')

    try:
        while True:
            metering_skid.log_data()
            time.sleep(5)  # Log data every 5 seconds
    except KeyboardInterrupt:
        logging.info("Data logging stopped by user.")
        metering_skid.save_log_to_file()

if __name__ == "__main__":
    main()
```
