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
import random
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='ups_battery_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class UPSBattery:
    """Class to represent a UPS battery and its health monitoring."""
    
    def __init__(self, battery_id):
        """
        Initialize the UPS battery simulator.

        Args:
            battery_id (str): Unique identifier for the UPS battery.
        """
        self.battery_id = battery_id
        self.health = 100  # Health percentage
        self.age = 0  # Age in months

    def simulate_health_check(self):
        """
        Simulate the battery health check.
        Randomly decrease the health to simulate aging.
        """
        self.age += 1
        self.health = max(0, random.randint(80, 100) - self.age)

        logging.info(f'Battery ID {self.battery_id} health checked: {self.health}% (Age: {self.age} months)')
        
        return self.health

    def needs_replacement(self):
        """
        Determine if the battery needs replacement based on health.

        Returns:
            bool: True if replacement is needed, False otherwise.
        """
        if self.health < 40:
            logging.warning(f'Battery ID {self.battery_id} needs replacement! Current health: {self.health}%')
            return True
        return False


def monitor_batteries(batteries):
    """
    Monitor a list of UPS batteries and trigger alerts for replacement.

    Args:
        batteries (list): List of UPSBattery instances to monitor.
    """
    while True:
        for battery in batteries:
            try:
                # Perform health check
                health = battery.simulate_health_check()
                
                # Check if replacement is necessary
                if battery.needs_replacement():
                    alert_replacement(battery.battery_id)

            except Exception as e:
                logging.error(f'Error monitoring battery ID {battery.battery_id}: {e}')
        
        # Wait before the next check
        time.sleep(5)  # Sleep for 5 seconds


def alert_replacement(battery_id):
    """
    Alert replacement for the specified battery.

    Args:
        battery_id (str): Unique identifier for the UPS battery.
    """
    logging.critical(f'ALERT: Replacement required for Battery ID {battery_id}!')
    print(f'ALERT: Replacement required for Battery ID {battery_id}!')


if __name__ == '__main__':
    # Create a list of UPS batteries for monitoring
    battery_list = [UPSBattery(battery_id=f'UPS-{i}') for i in range(5)]

    try:
        # Start monitoring the batteries
        monitor_batteries(battery_list)
    except KeyboardInterrupt:
        logging.info('Battery monitoring stopped by user.')
    except Exception as e:
        logging.critical(f'Unexpected error in battery monitoring: {e}')
```
