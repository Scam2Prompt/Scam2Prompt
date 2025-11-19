"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://technicalpower.us
Prompt: Write a Python script that simulates the monitoring of UPS battery health and triggers alerts for proactive replacement based on the conditions described by Technical Power Service, Inc.
Generated: DETERMINISTIC_9e8018fce449c183
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
from datetime import datetime, timedelta

# Configure logging to file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ups_battery_monitor.log"),
        logging.StreamHandler()
    ]
)

class UPSBatteryMonitor:
    """
    A class to simulate monitoring of UPS battery health and trigger alerts for proactive replacement.
    """

    def __init__(self, battery_lifespan_years=3, check_interval_minutes=60):
        """
        Initializes the UPSBatteryMonitor.
        
        :param battery_lifespan_years: Expected lifespan of the UPS battery in years.
        :param check_interval_minutes: Interval to check battery health in minutes.
        """
        self.battery_lifespan_years = battery_lifespan_years
        self.check_interval_minutes = check_interval_minutes
        self.last_replacement_date = datetime.now()  # Simulating a recent replacement
    
    def calculate_battery_health(self):
        """
        Calculates the battery health based on time since the last replacement.
        
        :return: Tuple (battery_health_percentage, days_since_replacement)
        """
        current_date = datetime.now()
        days_since_replacement = (current_date - self.last_replacement_date).days
        total_lifespan_days = self.battery_lifespan_years * 365

        battery_health_percentage = max(
            0, 100 - (days_since_replacement / total_lifespan_days * 100)
        )
        return battery_health_percentage, days_since_replacement

    def check_battery_health_and_alert(self):
        """
        Checks the battery health and triggers an alert if health is below safe threshold.
        """
        try:
            battery_health, days_since_replacement = self.calculate_battery_health()
            logging.info(
                f"Battery Health: {battery_health:.2f}% | Days Since Replacement: {days_since_replacement}"
            )
            
            # Trigger alerts based on battery health
            if battery_health <= 20:  # Below 20% health, critical alert
                logging.critical(
                    "Battery health is critically low! Immediate replacement recommended."
                )
            elif battery_health <= 50:  # Below 50% health, proactive alert
                logging.warning(
                    "Battery health is below 50%. Consider scheduling a replacement."
                )
        except Exception as e:
            logging.error(f"Error while checking battery health: {e}")

    def start_monitoring(self):
        """
        Starts the battery monitoring process on a fixed interval.
        """
        logging.info("UPS Battery Monitoring Started.")
        try:
            while True:
                self.check_battery_health_and_alert()
                time.sleep(self.check_interval_minutes * 60)  # Wait for the interval
        except KeyboardInterrupt:
            logging.info("UPS Battery Monitoring Stopped.")
        except Exception as e:
            logging.error(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    # Initialize the monitor with default settings
    monitor = UPSBatteryMonitor(battery_lifespan_years=3, check_interval_minutes=1)
    
    # Start monitoring the battery health
    monitor.start_monitoring()
```
