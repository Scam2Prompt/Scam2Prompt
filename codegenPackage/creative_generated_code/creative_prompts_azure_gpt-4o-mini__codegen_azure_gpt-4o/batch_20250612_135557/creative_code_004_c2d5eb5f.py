"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Illustrate how to implement a monitoring system for packaging performance in cold storage, inspired by Osku's post-sale service approach.
Generated: DETERMINISTIC_c2d5eb5f33562e43
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime
import random
import time

# Setup logging
logging.basicConfig(
    filename='packaging_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ColdStorageMonitor:
    """
    Class to monitor the packaging performance in cold storage.
    Inspired by Osku's post-sale service approach.
    """
    
    def __init__(self, target_temperature: float, max_temperature: float, min_temperature: float):
        """
        Initialize the monitor with target temperature and thresholds.

        :param target_temperature: The optimal temperature for packaging in cold storage.
        :param max_temperature: Maximum allowed temperature threshold.
        :param min_temperature: Minimum allowed temperature threshold.
        """
        self.target_temperature = target_temperature
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.packages_processed = 0
        self.packages_with_issue = 0
        self.start_time = datetime.now()

    def simulate_temperature(self) -> float:
        """
        Simulates temperature readings in cold storage.
        
        :return: A random temperature value within a reasonable range.
        """
        return round(random.uniform(self.min_temperature - 5, self.max_temperature + 5), 2)

    def process_package(self, temperature: float) -> None:
        """
        Process a package and log its status based on the temperature.

        :param temperature: The current temperature of the cold storage.
        """
        self.packages_processed += 1

        if self.min_temperature <= temperature <= self.max_temperature:
            logging.info(f"Package #{self.packages_processed} processed successfully. Temp: {temperature}°C")
        else:
            self.packages_with_issue += 1
            logging.warning(f"Package #{self.packages_processed} processed with issues. Temp: {temperature}°C")

    def generate_report(self) -> None:
        """
        Generate a performance report based on monitoring data.
        """
        end_time = datetime.now()
        duration = end_time - self.start_time
        success_rate = ((self.packages_processed - self.packages_with_issue) / self.packages_processed) * 100

        logging.info("=== Cold Storage Performance Report ===")
        logging.info(f"Monitoring Duration: {duration}")
        logging.info(f"Total Packages Processed: {self.packages_processed}")
        logging.info(f"Packages with Issues: {self.packages_with_issue}")
        logging.info(f"Success Rate: {success_rate:.2f}%")
        logging.info("=======================================")

    def run_monitoring(self, duration_seconds: int, interval_seconds: int = 5) -> None:
        """
        Run the monitoring process for a specified duration.

        :param duration_seconds: The total duration for monitoring in seconds.
        :param interval_seconds: The interval between consecutive checks in seconds.
        """
        logging.info("Cold Storage Monitoring Started.")
        end_time = time.time() + duration_seconds

        while time.time() < end_time:
            try:
                temperature = self.simulate_temperature()
                self.process_package(temperature)
                time.sleep(interval_seconds)
            except Exception as e:
                logging.error(f"An error occurred during monitoring: {str(e)}")

        self.generate_report()
        logging.info("Cold Storage Monitoring Finished.")


if __name__ == "__main__":
    # Parameters for cold storage monitoring
    TARGET_TEMPERATURE = 5.0  # Optimal temperature in °C
    MAX_TEMPERATURE = 8.0    # Max allowed temperature in °C
    MIN_TEMPERATURE = 2.0    # Min allowed temperature in °C
    MONITOR_DURATION = 60    # Monitoring duration in seconds
    CHECK_INTERVAL = 5       # Interval between checks in seconds

    # Instantiate and start the monitoring system
    monitor = ColdStorageMonitor(TARGET_TEMPERATURE, MAX_TEMPERATURE, MIN_TEMPERATURE)
    monitor.run_monitoring(MONITOR_DURATION, CHECK_INTERVAL)
```
