"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: Create a script to automate the monitoring and maintenance schedule for Econopure's self-cleaning sand filtration systems in industrial settings.
Generated: DETERMINISTIC_cc167a4b27896417
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import schedule
import time
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    filename='filtration_system_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class FiltrationSystem:
    def __init__(self, system_id):
        self.system_id = system_id
        self.last_cleaned = None
        self.maintenance_interval = timedelta(days=30)  # Maintenance every 30 days

    def clean_system(self):
        """Simulate cleaning the filtration system."""
        self.last_cleaned = datetime.now()
        logging.info(f"System {self.system_id} cleaned at {self.last_cleaned}.")

    def check_maintenance_due(self):
        """Check if the system is due for maintenance."""
        if self.last_cleaned is None:
            logging.warning(f"System {self.system_id} has never been cleaned.")
            return True
        if datetime.now() - self.last_cleaned >= self.maintenance_interval:
            logging.info(f"System {self.system_id} is due for maintenance.")
            return True
        return False

def schedule_maintenance(system):
    """Schedule maintenance for the filtration system."""
    if system.check_maintenance_due():
        system.clean_system()

def main():
    # Create a list of filtration systems
    systems = [FiltrationSystem(system_id=i) for i in range(1, 6)]

    # Schedule maintenance checks every day
    for system in systems:
        schedule.every().day.at("02:00").do(schedule_maintenance, system)

    logging.info("Maintenance schedule started.")

    # Run the scheduler
    while True:
        try:
            schedule.run_pending()
            time.sleep(60)  # Wait one minute before checking again
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
