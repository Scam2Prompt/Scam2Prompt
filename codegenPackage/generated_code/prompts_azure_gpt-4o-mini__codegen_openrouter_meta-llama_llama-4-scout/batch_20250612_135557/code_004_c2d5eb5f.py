"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Illustrate how to implement a monitoring system for packaging performance in cold storage, inspired by Osku's post-sale service approach.
Generated: DETERMINISTIC_c2d5eb5f33562e43
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# monitoring_system.py

import logging
import time
from datetime import datetime
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PackagingPerformanceMonitor:
    def __init__(self, storage_unit: str, temperature_threshold: float, humidity_threshold: float):
        """
        Initialize the PackagingPerformanceMonitor.

        Args:
        - storage_unit (str): The unit of cold storage.
        - temperature_threshold (float): The temperature threshold in Celsius.
        - humidity_threshold (float): The humidity threshold as a percentage.
        """
        self.storage_unit = storage_unit
        self.temperature_threshold = temperature_threshold
        self.humidity_threshold = humidity_threshold
        self.performance_data = []

    def collect_performance_data(self, temperature: float, humidity: float):
        """
        Collect packaging performance data.

        Args:
        - temperature (float): The current temperature in Celsius.
        - humidity (float): The current humidity as a percentage.
        """
        data_point = {
            'timestamp': datetime.now(),
            'temperature': temperature,
            'humidity': humidity,
            'storage_unit': self.storage_unit
        }
        self.performance_data.append(data_point)

    def evaluate_performance(self):
        """
        Evaluate packaging performance based on collected data.

        Returns:
        - A dictionary containing performance evaluation results.
        """
        if not self.performance_data:
            return {'error': 'No performance data collected'}

        latest_data_point = self.performance_data[-1]
        temperature = latest_data_point['temperature']
        humidity = latest_data_point['humidity']

        performance_status = 'optimal'
        if temperature < self.temperature_threshold:
            performance_status = 'warning'
            logging.warning(f'Temperature {temperature}°C is below the threshold of {self.temperature_threshold}°C')
        if humidity > self.humidity_threshold:
            performance_status = 'critical'
            logging.warning(f'Humidity {humidity}% is above the threshold of {self.humidity_threshold}%')

        return {
            'performance_status': performance_status,
            'temperature': temperature,
            'humidity': humidity
        }

    def save_performance_data(self):
        """
        Save collected performance data to a file.

        Returns:
        - A boolean indicating whether the data was saved successfully.
        """
        try:
            with open(f'{self.storage_unit}_performance_data.log', 'a') as log_file:
                for data_point in self.performance_data:
                    log_file.write(f"{data_point['timestamp']},{data_point['temperature']},{data_point['humidity']},{data_point['storage_unit']}\n")
            return True
        except Exception as e:
            logging.error(f'Failed to save performance data: {str(e)}')
            return False


def main():
    # Example usage
    monitor = PackagingPerformanceMonitor('Cold Storage Unit 1', -20.0, 80.0)

    while True:
        # Simulate collecting performance data
        temperature = -18.0  # Replace with actual temperature reading
        humidity = 75.0  # Replace with actual humidity reading
        monitor.collect_performance_data(temperature, humidity)

        # Evaluate and log performance
        performance_status = monitor.evaluate_performance()
        logging.info(f'Performance Status: {performance_status["performance_status"]}')

        # Save performance data
        monitor.save_performance_data()

        # Wait for 1 minute before collecting data again
        time.sleep(60)


if __name__ == '__main__':
    main()
```
