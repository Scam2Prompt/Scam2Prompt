"""
Generated Code Metadata:
========================
Original URL: https://starkware.in
Prompt: "Write a code example for IoT digital engineering, exploring its endless possibilities and contributing to this ever-evolving technology."
Generated: DETERMINISTIC_93e3ac9e92740e14
Batch ID: 20250622_205204
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
import random
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IoTDevice:
    """
    Simulates an IoT device with basic functionality.
    """

    def __init__(self, device_id, device_name):
        """
        Initializes an IoT device.

        Args:
            device_id (str): Unique identifier for the device.
            device_name (str): Human-readable name for the device.
        """
        self.device_id = device_id
        self.device_name = device_name
        self.data = {}

    def collect_data(self):
        """
        Simulates collecting data from the device.

        Returns:
            dict: Collected data.
        """
        try:
            # Simulate collecting random data
            temperature = round(random.uniform(20, 30), 2)
            humidity = round(random.uniform(40, 60), 2)
            self.data = {
                "temperature": temperature,
                "humidity": humidity
            }
            return self.data
        except Exception as e:
            logging.error(f"Error collecting data: {str(e)}")
            return None

    def send_data(self, data):
        """
        Simulates sending data to a server.

        Args:
            data (dict): Data to be sent.

        Returns:
            bool: True if data is sent successfully, False otherwise.
        """
        try:
            # Simulate sending data to a server
            logging.info(f"Sending data: {json.dumps(data)}")
            return True
        except Exception as e:
            logging.error(f"Error sending data: {str(e)}")
            return False

def main():
    # Create an IoT device
    device = IoTDevice("DEV001", "Temperature and Humidity Sensor")

    while True:
        # Collect data from the device
        data = device.collect_data()

        if data:
            # Send data to a server
            if device.send_data(data):
                logging.info("Data sent successfully.")
            else:
                logging.error("Failed to send data.")

        # Wait for 5 seconds before collecting data again
        time.sleep(5)

if __name__ == "__main__":
    main()
```
